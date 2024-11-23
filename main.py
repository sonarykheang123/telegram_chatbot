import json
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes


# Replace with your bot token
TOKEN = "8048524018:AAEbepb_WF4_SNf9n0h03UKLldhV6f_Xqxo"

# Example API URL for StackExchange (you can replace with any other API)
API_URL = "https://api.stackexchange.com/2.3/search/advanced"
# Store questions and responses in a JSON format (you could store this in a file or database in a real-world scenario)
qa_data = {

    "what is python": (

        "Python is a versatile programming language used for web development, data science, AI, and more.\n\n"

        "More: Visit [Python Official Docs](https://docs.python.org/3/)"
    ),
    "what is html": (

    "HTML (HyperText Markup Language) structures web content.\n\n"
    
    "More: Visit [HTML Reference](https://developer.mozilla.org/en-US/docs/Web/HTML)"
    ),
    "what is css": (

    
     "CSS (Cascading Style Sheets) styles HTML elements.\n\n"

     "More: Visit [CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS)"
    ),
        "thank you" :"Your welcome!🤍😊 ",
        "adding css to html": "You can add CSS to HTML by using the `<style>` tag or linking to an external `.css` file.",
        "creating a link in html": "In HTML, you create links using the `<a>` tag: `<a href='https://example.com'>Click Here</a>`.",
        "changing text color in css": "In CSS, you can change the text color using the `color` property: `color: red;`.",
        "understanding html tags": "HTML tags are used to define elements in an HTML document. Tags like `<div>`, `<p>`, and `<h1>` are examples of HTML tags.",
        "making a div in html": "In HTML, you create a `<div>` by using the `<div>` tag: `<div>Content here</div>`.",
        "centering a div in css": "To center a div in CSS, you can use `margin: auto` with a defined width, or use flexbox. Example:\n```css\n.container {\n  display: flex;\n  justify-content: center;\n}\n```",
        "changing background color in css": "To change the background color in CSS, you can use the `background-color` property. Example: `background-color: lightblue;`.",
        "creating a button in html": "In HTML, you create a button using the `<button>` tag: `<button>Click Me</button>`.",
        "adding an image in html": "You can add an image in HTML using the `<img>` tag: `<img src='image.jpg' alt='description'>`.",
        "explaining html class": "In HTML, a class is used to group elements and apply the same styles to them. Example: `<div class='myClass'>Content</div>`.",
        "explaining html id": "In HTML, an ID is a unique identifier for an element. Example: `<div id='uniqueId'>Content</div>`.",
        
        "using javascript in html": "To use JavaScript in HTML, you can include it using the `<script>` tag: `<script>console.log('Hello World');</script>`.",
        
        "installing python": "To install Python, visit [python.org](https://www.python.org/downloads/) and download the appropriate version for your operating system.",
        "creating a function in python": "In Python, you can create a function using the `def` keyword. Example:\n```python\ndef greet(name):\n    return f'Hello, {name}!'\n```",
        "using loops in python": "In Python, you can use a `for` loop or `while` loop. Example of a `for` loop:\n```python\nfor i in range(5):\n    print(i)\n```",
        "understanding variables in python": "In Python, variables are used to store data. Example:\n```python\nx = 10\nname = 'Alice'\n```",
        "taking user input in python": "In Python, you can take user input using the `input()` function. Example:\n```python\nname = input('Enter your name: ')\n```",
        "creating a dictionary in python": "In Python, dictionaries are created using curly braces `{}`. Example:\n```python\nmy_dict = {'name': 'Alice', 'age': 25}\n```",
        "handling exceptions in python": "In Python, exceptions can be handled using `try` and `except` blocks. Example:\n```python\ntry:\n    x = 10 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero!')\n```",
        "importing modules in python": "In Python, you can import a module using the `import` keyword. Example:\n```python\nimport math\nprint(math.sqrt(16))\n```",
        "explaining lists in python": "In Python, a list is an ordered collection of items. Example:\n```python\nmy_list = [1, 2, 3, 4]\n```",
        "using loops in css": "CSS does not natively support loops, but you can use CSS pre-processors like Sass or Less to create loops.",
        "using flexbox in css": "Flexbox is a CSS layout model that allows easy alignment of items. Example:\n```css\n.container {\n  display: flex;\n  justify-content: center;\n}\n```",
        "creating a table in html": "In HTML, you can create a table using the `<table>`, `<tr>`, `<th>`, and `<td>` tags. Example:\n```html\n<table>\n  <tr>\n    <th>Name</th>\n    <th>Age</th>\n  </tr>\n  <tr>\n    <td>Alice</td>\n    <td>25</td>\n  </tr>\n</table>\n```",
        "creating a form in html": "In HTML, you can create a form using the `<form>` tag. Example:\n```html\n<form action='/submit' method='POST'>\n  <input type='text' name='name'>\n  <input type='submit' value='Submit'>\n</form>\n```",
        "creating a select dropdown in html": "In HTML, you can create a dropdown using the `<select>` and `<option>` tags. Example:\n```html\n<select>\n  <option value='option1'>Option 1</option>\n  <option value='option2'>Option 2</option>\n</select>\n```",
        "using css grid": "CSS Grid is a powerful layout system. Example:\n```css\n.container {\n  display: grid;\n  grid-template-columns: repeat(3, 1fr);\n}\n```",
        "explaining css selectors": "A CSS selector is a pattern used to select elements in a document. Examples include element selectors like `div`, class selectors like `.class`, and ID selectors like `#id`.",
        "making text bold in html": "In HTML, you can make text bold using the `<b>` or `<strong>` tag. Example: `<strong>This is bold text</strong>`.",
        "making text italic in html": "In HTML, you can make text italic using the `<i>` or `<em>` tag. Example: `<em>This is italic text</em>`.",
        "adding comments in html": "In HTML, comments are added using `<!--` and `-->`. Example: `<!-- This is a comment -->`.",
        "adding comments in css": "In CSS, comments are added using `/*` and `*/`. Example: `/* This is a comment */`.",
        "using python libraries": "In Python, you can use libraries by importing them with the `import` keyword. Example:\n```python\nimport numpy as np\n```",
        "performing arithmetic in python": "In Python, you can perform arithmetic operations using operators like `+`, `-`, `*`, and `/`. Example:\n```python\nresult = 10 + 5\n```",
        "using while loops in python": "In Python, a `while` loop is used to repeat code as long as a condition is true. Example:\n```python\nwhile x < 10:\n    print(x)\n    x += 1\n```"
        # Python Topics
        "set" "A set is an unordered collection of unique elements in Python. Example: `my_set = {1, 2, 3}`.",
        "f-string": "An f-string is a way to format strings in Python, introduced in version 3.6. Example: `name = 'Alice'; print(f'Hello, {name}')`.",
        "file handling": "File handling in Python allows you to read from and write to files. Example:\n```python\nwith open('file.txt', 'r') as file:\n    content = file.read()\n```",
        "map": "The `map()` function applies a given function to each item of an iterable (like a list) and returns a list of the results. Example: `map(lambda x: x ** 2, [1, 2, 3])`.",
        "filter": "The `filter()` function filters elements from an iterable based on a condition. Example: `filter(lambda x: x > 2, [1, 2, 3])`.",
        "reduce": "The `reduce()` function from the `functools` module applies a function cumulatively to the items of an iterable. Example: `reduce(lambda x, y: x + y, [1, 2, 3])`.",
        "zip": "The `zip()` function pairs elements from multiple iterables into tuples. Example: `zip([1, 2], ['a', 'b'])` results in `[(1, 'a'), (2, 'b')]`.",
        "enumerate": "The `enumerate()` function adds a counter to an iterable and returns it as an enumerate object. Example: `enumerate(['a', 'b', 'c'])`.",
        "iterator": "An iterator is an object that allows you to traverse through all the elements of a collection (like a list). Example: `iter([1, 2, 3])`.",
        "generator": "A generator is a special type of iterator that yields items one at a time using the `yield` keyword. Example:\n```python\ndef my_gen():\n    yield 1\n    yield 2\n```",
        
        "loop": "A loop is a programming construct that repeats a block of code multiple times. In Python, common loops are 'for' and 'while' loops.",
        "function": "A function is a block of code designed to perform a particular task. In Python, you define functions using the 'def' keyword.",
        "variable": "A variable is used to store data in a program. In Python, variables don't require explicit declaration of type. Example: `x = 10`.",
        "list": "A list is an ordered collection of items in Python. Example: `my_list = [1, 2, 3, 4]`.",
        "dictionary": "A dictionary is a collection of key-value pairs. Example: `my_dict = {'name': 'Alice', 'age': 25}`.",
        "if statement": "An if statement is used to execute a block of code only if a specified condition is true. Example: `if x > 10: print('Greater')`.",
        "while loop": "A while loop repeatedly executes a block of code as long as a condition is true. Example:\n```python\nwhile x < 10:\n    print(x)\n    x += 1\n```",
        "for loop": "A for loop iterates over a sequence (like a list or a range) and executes a block of code for each item. Example:\n```python\nfor i in range(5):\n    print(i)\n```",
        "class": "A class in Python is a blueprint for creating objects. It allows you to define properties and methods that belong to the object.",
        "object": "An object is an instance of a class. It represents a specific entity in your program with its own data and behaviors.",
        "import": "In Python, you can import code from other files or libraries using the 'import' keyword. Example: `import math`.",
        
        # CSS Topics
        "html": "HTML (HyperText Markup Language) is the standard language used to create web pages. It structures the content of the page.",
        "css": "CSS (Cascading Style Sheets) is used to style the appearance of a webpage. It defines the look and feel of HTML elements.",
        "selectors": "CSS selectors are used to select HTML elements to apply styles to them. Examples: `.class`, `#id`, and `div` are CSS selectors.",
        "box model": "The CSS box model represents the structure of an element on the page. It includes margins, borders, padding, and the content itself.",
        "margin": "The margin property in CSS defines the space outside the element's border. Example: `margin: 10px;`.",
        "padding": "The padding property in CSS defines the space between the element's content and its border. Example: `padding: 10px;`.",
        "background-color": "The background-color property in CSS sets the background color of an element. Example: `background-color: lightblue;`.",
        "flexbox": "Flexbox is a layout model in CSS that allows easy alignment of items within a container. Example: `display: flex;`.",
        "grid": "CSS Grid is a powerful layout system that provides a two-dimensional grid for aligning items. Example: `display: grid; grid-template-columns: 1fr 1fr;`.",
        "media queries": "Media queries in CSS allow you to apply styles based on different device characteristics, like screen width. Example: `@media (max-width: 600px) { ... }`.",
        "positioning": "CSS positioning allows you to control the position of an element on the page. Values: `static`, `relative`, `absolute`, and `fixed`.",
        "display": "The `display` property in CSS defines how an element is displayed. Common values include `block`, `inline`, and `flex`.",
        "inline-block": "The `inline-block` value for the `display` property combines features of both `inline` and `block`. The element can sit inline but also accepts width and height properties.",
        "overflow": "The `overflow` property controls what happens when content overflows its container. Values: `visible`, `hidden`, `scroll`, and `auto`.",
        "float": "The `float` property allows elements to be positioned to the left or right of their container. It’s commonly used for layouts, but Flexbox is now preferred for this purpose.",
        "clear": "The `clear` property specifies whether an element should be moved below floating elements. Example: `clear: both;`.",
        "text-align": "The `text-align` property in CSS defines the horizontal alignment of text within an element. Example: `text-align: center;`.",
        "font-size": "The `font-size` property defines the size of the text. Example: `font-size: 16px;`.",
        "line-height": "The `line-height` property in CSS controls the vertical space between lines of text. Example: `line-height: 1.5;`.",
        "font-weight": "The `font-weight` property defines the thickness of the font. Example: `font-weight: bold;`.",
        "font-family": "The `font-family` property sets the font style of text. Example: `font-family: 'Arial', sans-serif;`.",
        "text-decoration": "The `text-decoration` property is used to set decoration on text like underline, overline, or line-through. Example: `text-decoration: underline;`.",
        "letter-spacing": "The `letter-spacing` property controls the space between characters in text. Example: `letter-spacing: 2px;`.",
        "word-spacing": "The `word-spacing` property controls the space between words. Example: `word-spacing: 5px;`.",
        "box-shadow": "The `box-shadow` property in CSS adds a shadow effect to an element. Example: `box-shadow: 2px 2px 5px grey;`.",
        
        # HTML Topics
        "html tags": "HTML tags define elements on a web page. Common tags include `<div>`, `<p>`, `<a>`, and `<h1>`.",
        "forms": "HTML forms are used to collect user input. Example:\n```html\n<form action='/submit' method='POST'>\n  <input type='text' name='name'>\n  <input type='submit' value='Submit'>\n</form>\n```",
        "images": "In HTML, you can add images using the `<img>` tag. Example: `<img src='image.jpg' alt='Description'>`.",
        "links": "To create a hyperlink in HTML, use the `<a>` tag. Example: `<a href='https://example.com'>Click Here</a>`.",
        "tables": "HTML tables are created using the `<table>`, `<tr>`, `<th>`, and `<td>` tags. Example:\n```html\n<table>\n  <tr>\n    <th>Name</th>\n    <th>Age</th>\n  </tr>\n  <tr>\n    <td>Alice</td>\n    <td>25</td>\n  </tr>\n</table>\n```",
        "div": "The `<div>` tag is a block-level element used to group other elements for styling or layout purposes. Example: `<div>Content</div>`.",
        "span": "The `<span>` tag is an inline element used to group parts of text or other inline elements for styling. Example: `<span>Text</span>`.",
        "header": "The `<header>` tag represents the introductory content of a page or section. It's commonly used to wrap navigation or logo elements.",
        "footer": "The `<footer>` tag represents the footer section of a page or section. It's often used for copyright or contact information.",
        "lists": "HTML supports ordered (`<ol>`) and unordered (`<ul>`) lists. Example:\n```html\n<ul>\n  <li>Item 1</li>\n  <li>Item 2</li>\n</ul>\n```",
        
        # Combined Topics (CSS + HTML)
        "responsive web design": "Responsive web design ensures that web pages look good on all devices. This is achieved through flexible grids and media queries.",
        "modern css": "Modern CSS includes the use of Flexbox and Grid for layouts, CSS variables for reuse, and the `clamp()` function for responsive design.",
        "progressive web apps (PWA)": "PWAs combine the best of web and mobile apps. They are fast, reliable, and can work offline. You can enhance a website to become a PWA by adding a service worker.",
        "web components": "Web Components allow you to create custom elements that can be used in HTML like native elements. This is achieved using the `<custom-element>` tag and JavaScript.",
        "cross-browser compatibility": "Cross-browser compatibility ensures that a website works across different web browsers. Techniques include using feature queries, fallbacks, and prefixes for CSS properties.",
        "data attributes": "Data attributes are used to store extra information on HTML elements. They are prefixed with `data-`. Example: `<div data-id='123'>`.",
        "parallax scrolling": "Parallax scrolling is a scrolling technique where background content moves at a different speed than the foreground content, creating a sense of depth.",
        "lazy loading": "Lazy loading is a technique that defers loading non-essential resources (like images) until they are needed, improving page load speed.",
        "content management system (CMS)": "A CMS is a software application used to create, manage, and modify digital content. Examples include WordPress, Drupal, and Joomla.",
        "web security": "Web security refers to protecting websites from malicious attacks like cross-site scripting (XSS), SQL injection, and cross-site request forgery (CSRF). Common practices include using HTTPS, sanitizing input, and setting up firewalls.",
        "server-side rendering (SSR)": "SSR is a technique where the server generates the HTML content and sends it to the browser, which can improve SEO and performance.",
        "client-side rendering (CSR)": "CSR is a technique where the browser renders the web page content. Popular JavaScript frameworks like React and Angular use CSR to create dynamic web pages."
        "responsive design" "Responsive design is about making web pages look good on all devices. You can achieve this using CSS media queries.",
        "semantic html": "Semantic HTML refers to using HTML tags that convey meaning about the content, like `<article>`, `<section>`, and `<header>`, instead of generic tags like `<div>`.",
        "seo": "SEO (Search Engine Optimization) involves optimizing web pages so they rank better in search engines. Good practices include using proper headings, meta tags, and alt attributes for images."
}

# Function to get an answer from Stack Exchange API based on user query

def get_api_answer(query):
    params = {
        'order': 'desc',
        'sort': 'relevance',
        'q': query,
        'site': 'stackoverflow'
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
        "Hello! Welcome to the Python, CSS, and HTML Helper Bot.💞\n"
        "You can ask me questions about programming topics, and I’ll do my best to help💛.  "
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

        "- 'What is Python?'\n"
        "- 'filter'\n"
        "- 'function'\n\n"
        "- 'What is CSS?'\n"
        "- 'HTML?'\n"
        "- 'selectors?'\n\n"
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
