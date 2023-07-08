import os
import time
import openai
from pyrogram import Client, filters
from termcolor import colored
from dotenv import load_dotenv

load_dotenv('.env')

openai.api_key = os.getenv("OPENAI_API_KEY")

# API TELEGRAM
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv('BOT_TOKEN')

app = Client("@nome-seu-bot", bot_token=bot_token, api_id=api_id, api_hash=api_hash)

with app:
    me = app.get_me()

# Para manter um histórico de mensagens
conversas = {}

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Olá {message.from_user.first_name}, seja bem-vindo ao nosso bot! Você pode começar a conversar agora.")

@app.on_message(filters.text & filters.private)
def reply(client, message):
    # Pega a conversa atual baseado no chat_id
    historico = conversas.get(message.chat.id, "")

    # Atualiza o histórico da conversa com a mensagem mais recente
    historico += f" \nUsuário: {message.text}"
    
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=historico + "\nIA:",
      max_tokens=150,
      temperature=0.4,
      top_p=1
    )

    # Atualiza o histórico com a resposta da IA
    resposta = response.choices[0].text.strip()
    historico += f" \nIA: {resposta}"

    # Guarda o histórico atualizado
    conversas[message.chat.id] = historico

    # Imprime a conversa recente
    print(colored(f"\nUsuário: {message.from_user.id} Mensagem: {message.text}", "red"))
    print(colored(f"\nIA: {resposta}", "green"))
    print(colored(f"\n\n{conversas}", "blue"))

    if "não entendi" in resposta.lower():
        resposta += "\n\nPor favor, poderia reformular a pergunta?"

    message.reply_text(resposta)

print(colored(f'Rodando - {me.first_name}', 'green'))
app.run()
