from flask import Flask
app = Flask(__name__)

print(__name__)


def make_bold(function):
    def wrapper():
        text = function()
        return f"<b>{text}</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        text = function()
        return f"<em>{text}</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        text = function()
        return f"<u>{text}</u>"
    return wrapper

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p>This is a paragraph</p>" \
           "<img src='https://media2.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif?cid=ecf05e47xl10fzm0c2hpmqfocktxi5zaiue3vnz7z60m9kto&rid=giphy.gif&ct=g' width=200>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye!"


@app.route("/<name>")
def greet(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)

### Exercise

# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        result = function(args[0], args[1], args[2])
        print(f"You called {function.__name__}({args})\nIt returned: {result}")
    return wrapper


# Use the decorator 👇

@logging_decorator
def a_function(a, b, c):
    return a + b + c

a_function(1,2,3)