from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    return f"<h1>Hello world! {random.randint(1, 10)}</h1>"

if __name__ == "__main__":
    app.run(debug=True)