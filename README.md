## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/mmarques11/bot-telegram
```

Instale as dependências

```bash
  pip install python-telegram-bot --upgrade
  pip install pyyaml
```

## Telegram

### 1º Passo: Criar um bot com o @BotFather
- 1.1 Abra o Telegram no seu celular ou computador.
- 1.2 Na busca, digite @BotFather e abra o chat oficial do BotFather (é o bot “pai” que cria outros bots).
- 1.3 Envie o comando:

```bash
/newbot
```

- 1.4 O BotFather vai te pedir para dar um nome para seu bot.
- 1.5 Depois, ele vai pedir um username para seu bot, que deve terminar com bot.
- 1.6 Após isso, o BotFather vai te enviar um token.

### 2º Passo: Conversar com o seu bot
- 2.1 Agora que o bot está criado, procure ele no Telegram pelo username que você escolheu (ex: @MeuRpaBot123_bot).

- 2.2 Abra o chat com ele e mande uma mensagem, pode ser só “Olá”.

### 3º Passo: Pegar chat ID
- 3.1 Use esse código para pegar o chat ID:
```bash
from telegram.ext import ApplicationBuilder, MessageHandler, filters

async def print_chat_id(update, context):
    print("Chat ID:", update.message.chat_id)

def main():
    app = ApplicationBuilder().token('{seu_token}').build()

    handler = MessageHandler(filters.TEXT & (~filters.COMMAND), print_chat_id)
    app.add_handler(handler)

    print("Bot rodando. Envie uma mensagem para o bot no Telegram.")
    app.run_polling()

if __name__ == "__main__":
    main()
```
### 4º Passo: Configurando arquivo yaml
- 4.1 no caso desse projeto utilizamos o yaml, mas você pode usar o de sua preferência.
```bash
  "token": seu_token
  "id": seu_id
```
## Documentação

[Documentação](https://core.telegram.org/bots/api)


## Autores

- [@mmarques11](https://www.github.com/mmarques11)

