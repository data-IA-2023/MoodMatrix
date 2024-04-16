import streamlit as st
from datetime import datetime

def main():
    st.title("Chatbot")

    
    logo_path = r"E:\MoodMatrix\1681038242chatgpt-logo-png.png"

    # Display smaller version of logo image
    st.image(logo_path, caption='', width=150)

    # Custom styling
    st.markdown(
        """
        <style>
        .chat-container {
            display: flex;
            flex-direction: column;
            padding: 10px;
        }
        .user-message {
            align-self: flex-end;
            max-width: 70%;
            background-color: #dcf8c6;
            border-radius: 10px;
            padding: 10px;
            margin: 5px;
        }
        .bot-message {
            align-self: flex-start;
            max-width: 70%;
            background-color: #ffffff;
            border-radius: 10px;
            padding: 10px;
            margin: 5px;
        }
        .timestamp {
            font-size: 12px;
            color: #888888;
            margin-top: 5px;
        }
        .feelings {
            font-style: italic;
            color: #888888;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    chat_history = []

    user_input = st.text_input("You:", key="user_input")

    if st.button("Send"):
        if user_input:
            feelings = get_feelings(user_input)  # Get feelings associated with user input
            chat_history.append({"user": user_input, "feelings": feelings, "time": datetime.now().strftime("%H:%M"), "sender": "user"})
            bot_response = get_bot_response(user_input)
            bot_feelings = get_feelings(bot_response)  # Get feelings associated with bot response
            chat_history.append({"user": bot_response, "feelings": bot_feelings, "time": datetime.now().strftime("%H:%M"), "sender": "bot"})

    if st.button("Refresh"):
        chat_history.clear()

    for message in chat_history:
        if message['sender'] == 'user':
            st.markdown(
                f'<div class="chat-container"><div class="user-message">{message["user"]}'
                f'<div class="feelings">{message["feelings"]}</div>'
                f'<div class="timestamp">{message["time"]}</div></div></div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="chat-container"><div class="bot-message">{message["user"]}'
                f'<div class="feelings">{message["feelings"]}</div>'
                f'<div class="timestamp">{message["time"]}</div></div></div>',
                unsafe_allow_html=True
            )

def get_bot_response(message):
    
    return f"Bot received: {message}"

def get_feelings(text):
    # This function should analyze the text and return associated feelings
    # Replace this with your actual implementation
    return "Happy"

if __name__ == "__main__":
    main()
