import openai
import streamlit as st
import time
import re
from dotenv import load_dotenv, find_dotenv

######################
# Esqueleto do modelo
######################

_ = load_dotenv(find_dotenv())
client = openai.Client()

# ID do assistant
ASSISTANT_ID = "Coloque o ID do seu Assistant"

# Como ja criei e configurei o Assistant so forneci o ID dele, deixei comentandado para nao criar novamente, abaixo o codigo de criação:
########################################################################
# vector_store = client.beta.vector_stores.create(name = 'FAQ_Invest')
# files = ['Base_Empresa.docx']
# file_stream = [open(f, 'rb') for f in files]

# file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
#     vector_store_id=vector_store.id,
#    files= file_stream)
########################################################################


 # Cria um chat com usuario, envia a pergunta e executa com instruçoes gerais
def resposta_faq(user_input: str) -> str:

    thread = client.beta.threads.create()

    client.beta.threads.messages.create(
        thread_id=thread.id,
        role='user',
        content=user_input
    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=ASSISTANT_ID,
        instructions="""
Você é um assistente administrativo da empresa Investe Legal.  
- Você tem acesso a um documento anexo (via file_search) que fala sobre contas, investimentos, prazos, etc.  
- Sempre que a pergunta tiver algo sobre a empresa ou sobre o conteúdo do documento, procure a resposta no arquivo.  
- Se o usuário perguntar algo que não está no documento ou que é claramente fora do escopo da empresa (por ex.: “Quantos paises tem na America do Sul?”), você deve dizer:  
  "Desculpe, não posso responder a essa parte pois não está no documento."  
- Se o usuário misturar perguntas (parte no escopo, parte fora), responda apenas a parte sobre o documento e avise que não pode responder a parte fora do documento.  
- Seja educado e ligeiramente informal, podendo usar algumas expressões amigáveis, mas sempre mantenha a precisão.
- Quando o usuário agradecer, responda de forma breve e simpática, afirmando apenas que estamos sempre à disposição para ajudá-lo no que for possível sobre a Invest Legal, sem adicionar qualquer outra informação.
""".strip(),
        temperature=0.2
    )

    try:
        run = client.beta.threads.runs.wait(run.id)
    except AttributeError:
        time.sleep(4)

    # Verifica a ultima mensagem do 'assistant'
    messages_page = client.beta.threads.messages.list(thread_id=thread.id)
    all_messages = messages_page.data


    assistant_msgs = [m for m in all_messages if m.role == "assistant"]
    if not assistant_msgs:
        return "Desculpa, não consigo responder essa pergunta, porfavor entrar em contato (00) 000000000."

    last_msg = assistant_msgs[-1]

   # Estrutura o texto final e remove marcaçoes da resposta do assistant
    text_blocks = []
    for block in last_msg.content:
        if block.type == "text":
            text_blocks.append(block.text.value)

    final_text = "\n".join(text_blocks)

    # Tira as anotações do tipo 【...】 usando regex
    final_text = re.sub(r"【.*?】", "", final_text)

    return final_text

####################################################################
# Layout do Chat (titulo, historico de mensagens e input do usuario)
####################################################################

st.title("FAQ da Investe Legal 💼📊")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Digite sua pergunta..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    resposta_assistente = resposta_faq(prompt)

    with st.chat_message("assistant"):
        st.markdown(resposta_assistente)

    st.session_state["messages"].append({"role": "assistant", "content": resposta_assistente})
