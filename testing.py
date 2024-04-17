'''from flask import Flask, render_template, request
from datetime import datetime


from main1 import text_analyse_et_generation, get_df_bd_monitoring, get_df_bd_historique


app = Flask(__name__)

chat_history = []

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        user_input = request.form['user_input']
        if user_input:
            bot_response = generate_bot_response(user_input)
            chat_history.append({"user": user_input, "response": bot_response, "time": datetime.now().strftime("%H:%M")})
    return render_template('index.html', chat_history=chat_history)

@app.route('/refresh', methods=['GET', 'POST'])
def refresh():
    chat_history.clear()
    return render_template('index.html', chat_history=chat_history)

def generate_bot_response(user_input):
    try:
        analysis_result = text_analyse_et_generation(user_input, 1, datetime.now())  # Assuming idConversation = 1
        bot_response = analysis_result['resultat']
    except Exception as e:
        bot_response = f"Sorry, I couldn't process your request. Error: {e}"
    return bot_response

if __name__ == "__main__":
    app.run(debug=True)'''

from flask import Flask, render_template, request
import datetime

# Import your functions from main1.py
from main1 import text_analyse_et_generation, get_df_bd_monitoring, get_df_bd_historique

app = Flask(__name__)

# Initialize an empty list for chat history
chat_history = []

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        user_input = request.form['user_input']
        if user_input:
            # Call the text analysis and generation function
            idConversation = len(chat_history) + 1  # Generate a unique conversation ID
            dateHistorique = datetime.datetime.now()
            result = text_analyse_et_generation(user_input, idConversation, dateHistorique)
            bot_response = result['resultat']
            bot_emotion = result['sentiment']
            bot_emoticon = result['emoticon']
            
            # Append user input and bot response to chat history
            chat_history.append({"user": user_input, "emotion": bot_emotion, "emoticon": bot_emoticon, "sender": "user"})
            chat_history.append({"user": bot_response, "emotion": bot_emotion, "emoticon": bot_emoticon, "sender": "bot"})
            
    return render_template('index.html', chat_history=chat_history)

@app.route('/refresh', methods=['GET', 'POST'])
def refresh():
    chat_history.clear()  # Clear the chat history
    return render_template('index.html', chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
