from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

# Data: Jokes & Quotes
JOKES = [
    "Programmer ka favorite hangout spot? - Foo Bar!",
    "Developer 0 se count kyu karte hain? - Kyunki 1 pehle hi reserve ho chuka hota hai!",
    "Code me bug nahi hai, ye toh bas ek undocumented feature hai!",
    "Real programmers don't comment their code. If it was hard to write, it should be hard to understand!"
]

QUOTES = [
    {"quote": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
    {"quote": "Code is like humor. When you have to explain it, it’s bad.", "author": "Cory House"},
    {"quote": "Make it work, make it right, make it fast.", "author": "Kent Beck"}
]

# Home Route
@app.route('/')
def home():
    return jsonify({
        "status": "Online",
        "endpoints": {
            "joke": "/api/joke",
            "quote": "/api/quote",
            "dice": "/api/roll"
        }
    })

# Endpoint 1: Random Joke
@app.route('/api/joke', methods=['GET'])
def get_joke():
    return jsonify({
        "success": True,
        "joke": random.choice(JOKES)
    })

# Endpoint 2: Random Quote
@app.route('/api/quote', methods=['GET'])
def get_quote():
    data = random.choice(QUOTES)
    return jsonify({
        "success": True,
        "quote": data["quote"],
        "author": data["author"]
    })

# Endpoint 3: Virtual Dice Roller (1 to 6)
@app.route('/api/roll', methods=['GET'])
def roll_dice():
    return jsonify({
        "success": True,
        "number": random.randint(1, 6)
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
