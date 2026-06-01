# GoodWe ChargeGrid Assistant — Sprint 2

[cite_start]O **GoodWe ChargeGrid Assistant** é um chatbot operacional inteligente, dotado de memória conversacional ativa, desenvolvido especificamente para a gestão de eletropostos comerciais no contexto do **EV Challenge 2026**[cite: 40, 55]. [cite_start]A solução funciona como uma interface técnica em tempo real para auxiliar gestores e operadores na tomada de decisões, monitoramento de carga e suporte operacional[cite: 41, 57].

---

##  Tecnologias e Comparativo de Modelos

[cite_start]Para esta etapa, a inteligência do chatbot foi estruturada utilizando a biblioteca **LangChain** integrada à API do **Google Gemini**[cite: 59]. Abaixo encontra-se o comparativo técnico que justifica a seleção do modelo para o ambiente de produção:

| Critério | Google Gemini 1.5 Flash (Escolhido) | OpenAI GPT-4o (Avaliado) |
| :--- | :--- | :--- |
| **Custo** | Gratuito (Cota de Estudante/Dev) | Pago (US$ 2.50 / 1M tokens) |
| **Latência de Resposta** | Ultra-baixa (~0.8s) | Média (~2.0s) |
| **Janela de Contexto** | 1 Milhão de tokens | 128k tokens |
| **Gargalo Identificado** | Nenhum na cota acadêmica padrão | Erros de Quota Excedida (`RateLimitError`) |

###  Justificativa: Cenário Comercial vs. Condominial
[cite_start]Optou-se estritamente pelo desenvolvimento voltado ao ambiente **Comercial (ChargeGrid Intelligence)** devido à sua complexidade técnica e de negócios consideravelmente superior ao ambiente residencial[cite: 41]:
1. [cite_start]**Alta Criticidade Energética:** Eletropostos comerciais trabalham com múltiplos carregadores rápidos DC (alta potência), tornando indispensável o balanceamento de carga e a orquestração de potência para evitar multas contratuais por pico de demanda com a concessionária[cite: 44, 49].
2. [cite_start]**Complexidade de Faturamento:** Diferente do ambiente residencial (onde o custo é fixo ou rateado), o cenário comercial exige faturamento baseado em consumo energético dinâmico (kWh), aplicação de tarifas configuradas e geração de relatórios financeiros para auditoria[cite: 43, 49, 50].
3. [cite_start]**Logística e Suporte Físico:** A indisponibilidade de um carregador comercial gera prejuízo financeiro imediato ao estabelecimento[cite: 14]. [cite_start]Por isso, o sistema exige políticas estritas de triagem de falhas e regras matemáticas claras para a escalada de suporte técnico humano[cite: 44, 48].

---

##  Arquitetura e Funcionamento do Código (`app.py`)

O arquivo principal `app.py` foi modularizado utilizando as melhores práticas de Engenharia de Prompts e Engenharia de Software:

1. [cite_start]**Gestão de Contexto de Segurança:** Utiliza a biblioteca `python-dotenv` e o método `os.getenv` para injetar a API Key diretamente da memória do ambiente (cumprindo a exigência de não expor credenciais em código público)[cite: 63].
2. [cite_start]**Ciclo de Vida da Mensagem:** O fluxo operacional segue rigorosamente a arquitetura planejada no fluxograma do sistema[cite: 55, 60]:
   * [cite_start]Entrada do operador ➔ Validação com o Histórico de Memória ➔ Injeção do `system-prompt.txt` ➔ Processamento pela LLM (Gemini) ➔ Resposta Estruturada[cite: 49, 61, 62].
3. **Memória Conversacional Ativa:** Implementada nativamente através dos componentes `SystemMessage`, `HumanMessage` e `AIMessage` do LangChain. [cite_start]Isso garante que o chatbot se lembre das interações passadas do operador dentro da mesma sessão, permitindo diagnósticos continuados[cite: 61].

---

##  Regras de Negócio e Escalada Humana

[cite_start]O comportamento do chatbot é ditado pelo arquivo `system-prompt.txt`, que restringe as respostas ao escopo do eletroposto comercial[cite: 40, 53]. 

 **Política Crítica de Escalada Humana:**
[cite_start]O assistente foi programado para recomendar **imediatamente a abertura de um chamado técnico para suporte presencial físico** nas seguintes condições operacionais quantificáveis[cite: 44, 48]:
* [cite_start]Após **2 tentativas consecutivas** de reinício de sessão sem sucesso por parte do operador[cite: 44].
* [cite_start]Se os logs de telemetria acusarem uma **sobrecarga de potência acima de 15%** da capacidade nominal do eletroposto[cite: 44].
* Se o status do carregador apontar falhas críticas irreversíveis por software (como "Erro de Isolamento Interno").

---

##  Arquitetura de Arquivos da Entrega

O repositório está organizado da seguinte forma:
* 📄 `app.py`: Código-fonte do chatbot com memória ativa e integração com o Gemini.
* [cite_start]📄 `system-prompt.txt`: Prompt de sistema com a persona, escopo comercial e regras de escalada técnica[cite: 40].
* 📄 `test-cases.txt`: Planejamento detalhado dos 7 cenários de teste operacionais.
* [cite_start]📄 `resultados_testes.md`: Relatório com as saídas reais geradas pela IA, incluindo validações de segurança contra jailbreak e fora de escopo[cite: 16].
* [cite_start] `fluxograma.jpg`: Diagrama visual detalhando o fluxo de dados, intenções e tratamento de falhas do sistema.

---

##  Como Executar o Projeto

1. Instale as dependências através do gerenciador de pacotes:
   ```bash
   pip install langchain-google-genai python-dotenv
