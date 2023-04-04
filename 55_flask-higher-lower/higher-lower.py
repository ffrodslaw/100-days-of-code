from flask import Flask
import random

app = Flask(__name__)

number = random.randint(1, 9)
print(number)

@app.route("/")
def start():
    return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/l378khQxt68syiWJy/giphy-downsized-large.gif' width=300>"


@app.route("/<guess>")
def check(guess):
    guess = int(guess)
    if guess == number:
        return "<h1><b>You are right!</b></h1>" \
               "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTU5ZDcxZGFlOWFmMjliZDY5YjAzZDI2YWQ1ZWQ0ZjA4MzI2MWYxMCZjdD1n/QyK8gRzGW2fV6qo8Hm/giphy.gif' width=300>"
    elif guess < number:
        return "<h1><b>Too low, try again!</b></h1>" \
               "<img src='https://media.giphy.com/media/3o7TKHVU0xsgGDCyPu/giphy.gif' width=300>"
    elif guess > number:
        return "<h1><b>Too high, try again!</b></h1>" \
               "<img src='https://media.giphy.com/media/ScBC8WQ7JUjS1EGhgi/giphy.gif' width=300>"


if __name__ == "__main__":
    app.run(debug=True)