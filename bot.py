import wikipedia
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set the language for Wikipedia (default: English)
wikipedia.set_lang("en")

BOT_TOKEN = os.getenv("BOT_TOKEN")   # Replace with your token

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I'm your WikiBot 🤖\n"
        "Use /wiki <query> to search Wikipedia.\n"
        "Send /help for assistance."
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "*Help Menu*\n"
        "/start - Welcome message\n"
        "/wiki <search term> - Get Wikipedia summary\n"
        "Type anything else and I'll echo it back!",
        parse_mode='Markdown'
    )

# /wiki command
async def wiki_search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /wiki <search term>")
        return

    query = " ".join(context.args)
    try:
        summary = wikipedia.summary(query, sentences=3)
        await update.message.reply_text(f"📖 *{query}*\n\n{summary}", parse_mode='Markdown')
    except wikipedia.exceptions.DisambiguationError as e:
        await update.message.reply_text(
            f"That term is ambiguous. Try one of these:\n• " + "\n• ".join(e.options[:5])
        )
    except wikipedia.exceptions.PageError:
        await update.message.reply_text("No Wikipedia page found for your query.")
    except Exception as e:
        await update.message.reply_text(f"An unexpected error occurred:\n{str(e)}")

# Fallback for non-command messages
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'You said: {update.message.text}')

# Main function
def main():
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("ERROR: Please set your Telegram BOT_TOKEN.")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("wiki", wiki_search))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
