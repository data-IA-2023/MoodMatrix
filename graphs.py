from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


feelings_to_emoji = {
    "Happy": "😊",
    "Sad": "😔",
    "Angry": "😡",
    "Excited": "😃",
    "Surprised": "😮",
    "Neutral": "😐",
}

chat_history = []

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        user_input = request.form['user_input']
        if user_input:
            feelings = get_feelings(user_input)
            emoji = feelings_to_emoji.get(feelings, "")
            chat_history.append({"user": user_input, "feelings": feelings, "emoji": emoji, "time": datetime.now().strftime("%H:%M"), "sender": "user"})
            bot_response = get_bot_response(user_input)
            bot_feelings = get_feelings(bot_response)
            bot_emoji = feelings_to_emoji.get(bot_feelings, "")
            chat_history.append({"user": bot_response, "feelings": bot_feelings, "emoji": bot_emoji, "time": datetime.now().strftime("%H:%M"), "sender": "bot"})
    return render_template('index.html', chat_history=chat_history)

@app.route('/refresh', methods=['GET', 'POST'])
def refresh():
    chat_history.clear()
    return render_template('index.html', chat_history=chat_history)

def get_bot_response(message):
    return f"Bot received: {message}"
    
def get_feelings(text):
    text_lower = text.lower()
    if any(keyword in text_lower for keyword in ["happy", "joy", "excited", "good"]):
        return "Happy"
    elif any(keyword in text_lower for keyword in ["sad", "cry", "unhappy", "depressed"]):
        return "Sad"
    elif any(keyword in text_lower for keyword in ["angry", "mad", "frustrated", "upset"]):
        return "Angry"
    elif any(keyword in text_lower for keyword in ["surprised", "shocked", "amazed"]):
        return "Surprised"
    else:
        return "Neutral"

if __name__ == "__main__":
    app.run(debug=True)