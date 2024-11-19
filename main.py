import json
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Replace with your bot token
TOKEN = "8048524018:AAEbepb_WF4_SNf9n0h03UKLldhV6f_Xqxo"

# Example API URL for StackExchange (you can replace with any other API)
API_URL = "https://api.chatgpt.com/c/673c3fe2-0cb4-800c-b5ed-42d468480105"

# Store questions and responses in a JSON format (you could store this in a file or database in a real-world scenario)
qa_data = {
    "what is python": (
        "1. **What is Python?**\n"
        "Python is a versatile programming language used for web development, data science, AI, and more.\n\n"
        "2. **Variables:**\n"
        "Variables store data. Example:\n`x = 5`\n\n"
        "3. **Functions:**\n"
        "Functions are blocks of reusable code. Example:\n"
        "```python\n"
        "def greet(name):\n"
        "    return f'Hello, {name}!'\n"
        "```\n\n"
        "4. **Loops:**\n"
        "For repetitive tasks, use loops. Example:\n"
        "```python\n"
        "for i in range(5):\n"
        "    print(i)\n"
        "```\n\n"
        "More: Visit [Python Official Docs](https://docs.python.org/3/)"
    ),
    "what is html": (
        "1. **What is HTML?**\n"
        "HTML (HyperText Markup Language) structures web content.\n\n"
        "2. Basic Tags:\n"
        "- `<html>`: Root of the document\n"
        "- `<head>`: Metadata container\n"
        "- `<body>`: Main content\n"
        "- `<h1>` to `<h6>`: Headings\n"
        "- `<p>`: Paragraph\n\n"
        "3. **Example:**\n"
        "```html\n"
        "<!DOCTYPE html>\n"
        "<html>\n"
        "  <head>\n"
        "    <title>My Page</title>\n"
        "  </head>\n"
        "  <body>\n"
        "    <h1>Welcome to My Page</h1>\n"
        "    <p>This is a paragraph.</p>\n"
        "  </body>\n"
        "</html>\n"
        "```\n\n"
        "More: Visit [HTML Reference](https://developer.mozilla.org/en-US/docs/Web/HTML)"
    ),
    "what is css": (
        "1. What is CSS?\n"
        "CSS (Cascading Style Sheets) styles HTML elements.\n\n"
        "2. Selectors:\n"
        "- `element {}`: Targets all elements\n"
        "- `.class {}`: Targets elements with a class\n"
        "- `#id {}`: Targets an element with an ID\n\n"
        "3. Properties:\n"
        "- `color`: Text color\n"
        "- `background-color`: Background color\n"
        "- `font-size`: Size of text\n\n"
        "4. Example:\n"
        "```css\n"
        "body {\n"
        "    background-color: lightblue;\n"
        "    color: black;\n"
        "}\n"
        "h1 {\n"
        "    color: darkblue;\n"
        "    font-size: 2em;\n"
        "}\n"
        "```\n\n"
        "More: Visit [CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS)"
    ),
    "how to add css to html": "You can add CSS to HTML by using the `<style>` tag or linking to an external `.css` file.",
    "how to create a link in html": "In HTML, you create links using the `<a>` tag: `<a href='https://example.com'>Click Here</a>`.",
    "how to change text color in css": "In CSS, you can change the text color using the `color` property: `color: red;`.",
    "what are html tags": "HTML tags are used to define elements in an HTML document. Tags like `<div>`, `<p>`, and `<h1>` are examples of HTML tags.",
    "how to make a div in html": "In HTML, you create a `<div>` by using the `<div>` tag: `<div>Content here</div>`.",
    "how to center a div in css": "To center a div in CSS, you can use `margin: auto` with a defined width, or use flexbox. Example:\n```css\n.container {\n  display: flex;\n  justify-content: center;\n}\n```",
    "how to change background color in css": "To change the background color in CSS, you can use the `background-color` property. Example: `background-color: lightblue;`.",
    "how to create a button in html": "In HTML, you create a button using the `<button>` tag: `<button>Click Me</button>`.",
    "how to add an image in html": "You can add an image in HTML using the `<img>` tag: `<img src='image.jpg' alt='description'>`.",
    "what is a class in html": "In HTML, a class is used to group elements and apply the same styles to them. Example: `<div class='myClass'>Content</div>`.",
    "what is an id in html": "In HTML, an ID is a unique identifier for an element. Example: `<div id='uniqueId'>Content</div>`.",
    "how to use javascript in html": "To use JavaScript in HTML, you can include it using the `<script>` tag: `<script>console.log('Hello World');</script>`.",
    "what is python": "Python is a high-level programming language known for its readability and versatility. It is used for web development, data analysis, AI, and more.",
    "how to install python": "To install Python, visit [python.org](https://www.python.org/downloads/) and download the appropriate version for your operating system.",
    "how to create a function in python": "In Python, you can create a function using the `def` keyword. Example:\n```python\ndef greet(name):\n    return f'Hello, {name}!'\n```",
    "how to use a loop in python": "In Python, you can use a `for` loop or `while` loop. Example of a `for` loop:\n```python\nfor i in range(5):\n    print(i)\n```",
    "what are variables in python": "In Python, variables are used to store data. Example:\n```python\nx = 10\nname = 'Alice'\n```",
    "how to take user input in python": "In Python, you can take user input using the `input()` function. Example:\n```python\nname = input('Enter your name: ')\n```",
    "how to create a dictionary in python": "In Python, dictionaries are created using curly braces `{}`. Example:\n```python\nmy_dict = {'name': 'Alice', 'age': 25}\n```",
    "how to handle exceptions in python": "In Python, exceptions can be handled using `try` and `except` blocks. Example:\n```python\ntry:\n    x = 10 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero!')\n```",
    "how to import a module in python": "In Python, you can import a module using the `import` keyword. Example:\n```python\nimport math\nprint(math.sqrt(16))\n```",
    "what is a list in python": "In Python, a list is an ordered collection of items. Example:\n```python\nmy_list = [1, 2, 3, 4]\n```",
    "how to create a loop in css": "In CSS, loops are not natively supported, but you can use CSS pre-processors like Sass or Less to create loops.",
    "how to use flexbox in css": "Flexbox is a CSS layout model that allows easy alignment of items. Example:\n```css\n.container {\n  display: flex;\n  justify-content: center;\n}\n```",
    "how to create a table in html": "In HTML, you can create a table using the `<table>`, `<tr>`, `<th>`, and `<td>` tags. Example:\n```html\n<table>\n  <tr>\n    <th>Name</th>\n    <th>Age</th>\n  </tr>\n  <tr>\n    <td>Alice</td>\n    <td>25</td>\n  </tr>\n</table>\n```",
    "how to create a form in html": "In HTML, you can create a form using the `<form>` tag. Example:\n```html\n<form action='/submit' method='POST'>\n  <input type='text' name='name'>\n  <input type='submit' value='Submit'>\n</form>\n```",
    "how to create a select dropdown in html": "In HTML, you can create a dropdown using the `<select>` and `<option>` tags. Example:\n```html\n<select>\n  <option value='option1'>Option 1</option>\n  <option value='option2'>Option 2</option>\n</select>\n```",
    "how to use css grid": "CSS Grid is a powerful layout system. Example:\n```css\n.container {\n  display: grid;\n  grid-template-columns: repeat(3, 1fr);\n}\n```",
    "what is a css selector": "A CSS selector is a pattern used to select elements in a document. Examples include element selectors like `div`, class selectors like `.class`, and ID selectors like `#id`.",
    "how to make text bold in html": "In HTML, you can make text bold using the `<b>` or `<strong>` tag. Example: `<strong>This is bold text</strong>`.",
    "how to make text italic in html": "In HTML, you can make text italic using the `<i>` or `<em>` tag. Example: `<em>This is italic text</em>`.",
    "how to add comments in html": "In HTML, comments are added using `<!--` and `-->`. Example: `<!-- This is a comment -->`.",
    "how to add comments in css": "In CSS, comments are added using `/*` and `*/`. Example: `/* This is a comment */`.",
    "how to use python libraries": "In Python, you can use libraries by importing them with the `import` keyword. Example:\n```python\nimport numpy as np\n```",
    "how to perform arithmetic in python": "In Python, you can perform arithmetic operations using operators like `+`, `-`, `*`, and `/`. Example:\n```python\nresult = 10 + 5\n```",
    "how to use a while loop in python": "In Python, a `while` loop is used to repeat code as long as a condition is true. Example:\n```python\nwhile x < 10:\n    print(x)\n    x += 1\n```"
}



# Function to get an answer from Stack Exchange API based on user query
def get_api_answer(query):
    params = {
        'order': 'desc',
        'sort': 'relevance',
        'q': query,
        'site': 'ChatGPT'
    }
    response = requests.get(API_URL, params=params)
    data = response.json()

    # Check if the API returned any results
    if data['items']:
        return f"Here's a helpful answer:\n{data['items'][0]['title']}\nLink: {data['items'][0]['link']}"
    else:
        return "Sorry, I couldn't find any relevant answers."

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hello! Welcome to the Python, CSS, and HTML Helper Bot.\n"
        "You can ask me questions about programming topics, and I’ll do my best to help. "
        "Type /help to see a list of commands and topics I can assist with!"
    )

# Help command to show detailed instructions and examples
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🤖 *Help Guide* 🤖\n\n"
        "I’m here to answer your questions about programming topics including Python, CSS, and HTML. "
        "Here’s how you can interact with me:\n\n"
        "*Commands*\n"
        "/start - Start a conversation with me\n"
        "/help - View this help message\n\n"
        "*How to Ask Questions*\n"
        "Simply type your question or topic! Here are some examples:\n\n"
        "📌 *Python*\n"
        "- 'What is Python?'\n"
        "- 'How do I install Python?'\n"
        "- 'How to create a function in Python?'\n\n"
        "📌 *CSS*\n"
        "- 'What is CSS?'\n"
        "- 'How to add CSS to HTML?'\n"
        "- 'What are CSS selectors?'\n\n"
        "📌 *HTML*\n"
        "- 'What is HTML?'\n"
        "- 'How to create a link in HTML?'\n"
        "- 'What are HTML tags?'\n\n"
        "Just type a question about Python, CSS, or HTML, and I’ll do my best to provide an answer! If I don’t know an answer, I’ll let you know. 😊"
    )

# Message handler for responding to specific questions
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text.lower()  # Convert text to lowercase for matching

    # Check if the question exists in the predefined QA data
    if user_text in qa_data:
        response = qa_data[user_text]
    else:
        # If no direct answer, query the API (e.g., Stack Exchange)
        response = get_api_answer(user_text)

    # Send the response to the user
    await update.message.reply_text(response)

# Set up the bot and handlers
def main():
    # Set up the bot with the token
    application = ApplicationBuilder().token(TOKEN).build()

    # Add handlers for commands and messages
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
