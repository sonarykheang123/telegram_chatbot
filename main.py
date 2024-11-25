import json

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes


# Replace with your bot token
TOKEN = "8048524018:AAEbepb_WF4_SNf9n0h03UKLldhV6f_Xqxo"

# Load questions and answers from a JSON file
def load_qa_data(filename):
    with open(filename, encoding="utf-8") as file:
        data = json.load(file)
    return data["questions_and_answers"]

# Load data from qa.json file
qa_data = load_qa_data("qa.json")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hello! Welcome to the Python, CSS, and HTML Helper Bot.💞\n"
        "You can ask me questions about programming topics, and I’ll do my best to help.\n"
        "Type /help to see a list of commands and topics I can assist with!"
    )

# Help command to show detailed instructions and examples
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🤖 *Help Guide* 🤖\n\n"
        "I’m here to answer your questions about programming topics including Python, CSS, and HTML.\n\n"
        "*Commands*\n"
        "/start - Start a conversation with me\n"
        "/help - View this help message\n\n"

        "*How to Ask Questions*\n"



        "- 'What is Python?'\n"
        "- 'What is a CSS selector?'\n"
        "- 'Explain HTML attributes'\n\n"
        "Just type a question, and I’ll do my best to provide an answer! 😊"
    )
# Function to find the answer or provide a default response with a link
def find_answer(user_question):
    user_question = user_question.lower()
    for qa in qa_data:
        if qa["question"].lower() in user_question:
            return qa["answer"]
    return (
        "I’m not sure about that. Try asking another question! You can learn more about programming here:\n"
        "[Learn programming](https://www.w3schools.com)"
    )

# Function to handle user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = find_answer(user_message)
    await update.message.reply_text(response, parse_mode="Markdown")

# Main function to set up the bot and handlers
def main():

    application = ApplicationBuilder().token(TOKEN).build()


    application.add_handler(CommandHandler("start", start))

    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    application.run_polling()
    
if __name__ == '__main__':
    main()
