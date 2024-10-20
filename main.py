import os
import openai
from pyrogram import Client, filters
from termcolor import colored
from dotenv import load_dotenv

load_dotenv('.env')

# API OPEN_AI
openai.api_key = os.getenv("OPENAI_API_KEY")

# API TELEGRAM
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv('BOT_TOKEN')

app = Client("meu_bot", bot_token=bot_token, api_id=api_id, api_hash=api_hash)

# Para manter um histórico de mensagens
conversas = {}

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(f"Olá {message.from_user.first_name}, seja bem-vindo ao nosso bot! Você pode começar a conversar agora.")

@app.on_message(filters.text & filters.private)
async def reply(client, message):
    chat_id = message.chat.id
    historico = conversas.get(chat_id, "")

    historico += f"\nUsuário: {message.text}"
    
    try:
        response = openai.Completion.create(
            engine="gpt-4o-mini",
            prompt=historico + "\nIA:",
            max_tokens=150,
            temperature=0.4,
            top_p=1
        )
    except Exception as e:
        await message.reply_text("Ocorreu um erro ao processar sua mensagem. Por favor, tente novamente mais tarde.")
        print(colored(f"Erro ao chamar API OpenAI (detalhes): {e}", "red"))
        return

    if response and hasattr(response, 'choices') and len(response.choices) > 0:
        resposta = response.choices[0].text.strip()
        historico += f"\nIA: {resposta}"

        # Limita o histórico a um número máximo de caracteres para evitar problemas de performance
        if len(historico) > 1000:
            historico = historico[-1000:]

        conversas[chat_id] = historico

        print(colored(f"\n\nUsuário: {message.from_user.id} Mensagem: {message.text}", "red"))
        print(colored(f"\n\nIA: {resposta}", "green"))
        print(colored(f"\n\nHistórico: {conversas}", "blue"))

        if "não entendi" in resposta.lower():
            resposta += "\n\nPor favor, poderia reformular a pergunta?"

        await message.reply_text(resposta)
    else:
        await message.reply_text("Não foi possível gerar uma resposta no momento. Por favor, tente novamente mais tarde.")

if __name__ == '__main__':
    try:
        print(colored(f'Rodando - {app.name}', 'green'))
        app.run()
    except Exception as e:
        print(colored(f"Erro ao iniciar o bot: {e}", "red"))
