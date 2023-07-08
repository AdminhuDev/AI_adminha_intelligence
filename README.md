# 🤖 Meu Bot de IA

Este é um bot de Telegram que utiliza a IA da OpenAI para responder às perguntas dos usuários. Ele foi projetado para fornecer respostas de maneira natural e eficaz.

## 💡 Como Funciona

O bot recebe uma mensagem de um usuário, anexa essa mensagem a um histórico de mensagens e, em seguida, usa o modelo de linguagem da OpenAI para gerar uma resposta. As mensagens são enviadas e recebidas através da API do Telegram, usando a biblioteca Pyrogram para facilitar a interação com a API.

## 🚀 Começando

Para rodar o bot, você precisa seguir as seguintes etapas:

### 📦 Instalação

1. Clone este repositório para sua máquina local usando `https://github.com/AdminhuDev/Adminha_Intelligence.git`
2. Instale as dependências do projeto utilizando o pip:

```bash
pip install pyrogram termcolor openai python-dotenv
```

# 🕹️ Configuração
Crie um arquivo config.env na raiz do projeto.
Adicione as seguintes variáveis ao config.env (substitua os valores pelos seus próprios):

```bash
OPENAI_API_KEY=your_openai_key
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
```

### ⚠️ Importante: Nunca divulgue as chaves e tokens. Certifique-se de adicionar config.env ao seu .gitignore.

# 🎲 Rodando o bot
Agora você pode rodar o bot:
```bash
python3 main.py
```

# 🧪 Testes
Para testar o bot, envie uma mensagem para o nome de usuário do bot no Telegram após rodar o script.

# 🛠️ Tecnologias Utilizadas
Python

Pyrogram

OpenAI

python-dotenv

# ✍️ Autor
Adminhu -

# 📚 Licença
Este projeto está sob a licença MIT - veja o arquivo LICENSE.md para mais detalhes.