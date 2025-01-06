# FAQ com IA da Investe Legal

![captura1](https://github.com/user-attachments/assets/1c74659e-3cff-48ec-86f0-2d719839257e)

Este projeto consiste em um **FAQ com IA** para a empresa fictícia de investimentos. O objetivo foi criar um protótipo funcional com menos de 100 linhas de código, utilizando a API da OpenAI e a ferramenta **Assistant** (Beta). O FAQ oferece respostas consistentes e restritas ao conteúdo de um documento específico, mesmo que o usuário reformule a pergunta ou altere o contexto.

## Visão Geral

- **OpenAI API**: Utiliza a API da OpenAI para processar linguagem natural e retornar respostas relevantes.  
- **Assistant (Beta)**: A base do modelo de IA foi construída com o Assistant, explorando suas capacidades de contextualização e geração de respostas.  
- **Streamlit**: O front-end foi implementado em Streamlit, fornecendo uma interface de chat simples e prática para interação.  

## Características Principais

1. **Respostas Consistentes**  
   - O sistema mantém o contexto de perguntas anteriores, garantindo maior coerência nas respostas.  
2. **Escopo Restrito**  
   - Perguntas fora do escopo do documento recebem respostas educadas, explicando que o sistema não pode fornecer tais informações.  
3. **Protótipo Simples**  
   - Um código compacto e funcional, ideal para aprendizado e demonstração de soluções com IA.  

## Limitações

- **Versão Beta**: Por ser baseado em uma tecnologia em desenvolvimento, o Assistant pode apresentar limitações no desempenho.  
- **Atraso no Retorno**: As chamadas à API podem ocasionalmente resultar em um pequeno atraso nas respostas.  
- **Prompt Básico**: O conjunto de instruções utilizado no modelo é simples, podendo ser expandido para casos mais complexos.

## Documento Base

O documento **"Base_Empresa.docx"**, que contém as informações utilizadas para o FAQ, também está disponível neste repositório. Ele é a principal fonte de dados para as respostas fornecidas pelo sistema.  

