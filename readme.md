# GoodWe ChargeGrid Assistant


# EV Challenge 2026 — GoodWe

## Sobre o Projeto

O GoodWe ChargeGrid Assistant é um chatbot operacional desenvolvido para o EV Challenge 2026, com foco na gestão inteligente de eletropostos comerciais.

A solução busca auxiliar gestores e operadores na supervisão das operações de carregamento, faturamento, monitoramento de equipamentos, controle de potência e suporte técnico básico.


# Problema

Com o crescimento da mobilidade elétrica, os eletropostos comerciais enfrentam desafios relacionados à:

* Gestão simultânea de múltiplos carregadores
* Controle de potência disponível
* Registro de sessões de carregamento
* Faturamento baseado em consumo energético
* Monitoramento de falhas
* Comunicação operacional


# Solução Proposta

O chatbot GoodWe ChargeGrid Assistant atua como uma interface inteligente para apoio operacional, permitindo consultas rápidas e contextualizadas sobre o sistema ChargeGrid.

Principais funcionalidades:

* Consulta de status dos carregadores
* Consulta de consumo energético
* Apoio ao faturamento
* Identificação de falhas
* Recomendações operacionais
* Suporte técnico básico
* Orquestração de potência


# Persona Principal

**Gestor/Operador Comercial de Eletroposto**

Responsável pela operação diária dos carregadores, acompanhamento de faturamento e tomada de decisões relacionadas ao funcionamento da infraestrutura de carregamento.


# Tecnologias Utilizadas

## Modelo de IA

Gemini

Motivos da escolha:

* Boa compreensão de linguagem natural
* Facilidade de integração
* Boa capacidade de seguir instruções
* Disponibilidade para desenvolvimento acadêmico

## Linguagem

* Python

## Ambiente de Desenvolvimento

* Google Colab


# Funcionamento

1. O usuário envia uma pergunta.
2. O system prompt define o contexto operacional.
3. O modelo interpreta a solicitação.
4. O histórico da conversa é utilizado para manter contexto.
5. O chatbot gera uma resposta dentro do escopo definido.
6. A resposta é apresentada ao usuário.



# Configuração

## Dependências

Instalação:

```bash
pip install google-generativeai
```


## Variáveis de Ambiente

É necessário configurar uma chave de acesso à API utilizada.

Exemplo:

```python
API_KEY = "SUA_CHAVE"
```

Nenhuma chave deve ser armazenada diretamente no repositório.



# Exemplos de Uso

### Consulta de Status

Pergunta:

```text
Qual o status do carregador CG-01?
```

Resposta:

```text
Não possuo acesso aos dados em tempo real. Informe os dados atualizados do sistema para consulta.
```


### Consulta de Faturamento

Pergunta:

```text
Quanto foi faturado ontem?
```

Resposta:

```text
É necessário fornecer os registros de consumo e a tarifa aplicada para calcular o faturamento.
```



### Falha Técnica

Pergunta:

```text
O carregador não está iniciando.
```

Resposta:

```text
Verifique conexão elétrica, comunicação com o sistema e status de manutenção. Caso o problema persista, recomenda-se abertura de chamado técnico.
```


# Testes

Os resultados dos testes realizados estão documentados no arquivo:

```text
resultados_testes.md
```



# Melhorias Futuras

* Integração com banco de dados operacional
* Integração com APIs da infraestrutura ChargeGrid
* Implementação de RAG
* Dashboards operacionais
* Relatórios automáticos



# Vídeo de Demonstração

Link do vídeo:

```text
Inserir link do YouTube aqui
```
