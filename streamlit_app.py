import streamlit as st

st.title("🎈 PM2.5 Chatbot App")


# Display the user input 
if user_input := st.text_input("You: ", placeholder="Type your message here..."): 
    st.write(f"User Input: {user_input}")