import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# 1. Carrega as variáveis de ambiente locais (caso use arquivo .env no computador)
load_dotenv()

print("=== Inicializando o Sistema (Versão Gemini) ===")

# 2. Configuração Segura da API Key (Padrão de mercado para servidores e IDEs)
# Procura primeiro pela variável padrão do sistema ou o que foi definido no ambiente
chave_gemini = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')

if not chave_gemini:
    print("❌ ERRO: Variável de ambiente GEMINI_API_KEY não encontrada.")
    print("Certifique-se de configurar a chave nas variáveis do sistema ou em um arquivo .env")
else:
    os.environ["GOOGLE_API_KEY"] = chave_gemini
    print("✓ Google API Key injetada com sucesso!")

# 3. Garante a leitura do arquivo externo de System Prompt
caminho_prompt = "system-prompt.txt"
if not os.path.exists(caminho_prompt):
    # Backup de segurança caso o arquivo não seja encontrado na pasta
    prompt_padrao = """# System Prompt — GoodWe ChargeGrid Assistant
Você é o GoodWe ChargeGrid Assistant, especializado em eletropostos comerciais.
Sempre responda usando a estrutura: Status atual, Causa provável, Ação recomendada e Próximo passo."""
    with open(caminho_prompt, "w", encoding="utf-8") as f:
        f.write(prompt_padrao)

# 4. Inicializa o modelo Gemini via LangChain
try:
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.0)
    print("✓ Modelo Gemini pronto para uso!\n")
except Exception as e:
    print(f"❌ Erro ao conectar com o Gemini: {e}")

# 5. Classe do Chatbot com histórico de conversas (Memória)
class ChargeGridBot:
    def __init__(self):
        with open(caminho_prompt, "r", encoding="utf-8") as f:
            self.system_prompt = f.read()
        self.historico = [SystemMessage(content=self.system_prompt)]

    def enviar_mensagem(self, texto_usuario):
        self.historico.append(HumanMessage(content=texto_usuario))
        resposta = llm.invoke(self.historico)
        self.historico.append(AIMessage(content=resposta.content))
        return resposta.content

# 6. Execução do Chat via Terminal
if __name__ == "__main__":
    bot = ChargeGridBot()
    print("=== GoodWe ChargeGrid Assistant Ativo ===")
    print("Digite suas perguntas abaixo. Para encerrar, digite 'sair'.\n")

    while True:
        entrada = input("Operador/Gestor: ")
        if entrada.lower() == 'sair':
            print("Sessão encerrada.")
            break
        if entrada.strip() == "":
            continue
            
        resposta_ia = bot.enviar_mensagem(entrada)
        print(f"\nAssistant:\n{resposta_ia}")
        print("-" * 50)
