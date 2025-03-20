from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TOKEN")

   # ottenuto su BotFather

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Ciao, sono Gnagneo. Che bbuo'?") # quando scrivi start risponde così

async def risposta_automatica (update: Update, context: CallbackContext) -> None:
    messaggio = update.message.text.lower()

    if "ciao" in messaggio:
        await update.message.reply_text("Cià")
    elif "come stai" in messaggio:
        await update.message.reply_text("Che te ne fotte?")
    elif "grazie" in messaggio:
        await update.message.reply_text("Ao cazz")
    elif "teresa" in messaggio:
        await update.message.reply_text("Ma tu che ne sai di quello che sento io? Teresa con me brillava!")
    
    else:
        await update.message.reply_text("Nn aggio capito. Che bbuò?")

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start)) # dice al bot che quando qualcuno scrive /start deve eseguire la funzione start
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, risposta_automatica))  # Filters.text = ascolta i messaggi di testo, ~Filters.command = ignora i comandi (/comandi)
    print('bot in esecuzione...')
    app.run_polling() # controlla nuovi messaggi
    
if __name__ == '__main__':
    main()
