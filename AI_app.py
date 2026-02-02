import streamlit as st
from chatbot_functies import chatbot_response
from PIL import Image

st.title("Rick's Truely Universally Lying Bot")
img = Image.open("rickandmorty.jpg")
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image(img, width=250)
st.markdown("ICT Praktijkdag - 2 februari 2026")
form = st.form(key="user_settings")
with form:
    AI_concept = st.text_input("How can je vous aider? (burp):", key = "AI_concept")
    character = st.selectbox("Who's the f***ing crowd?",
                          ("Morty, van Rick and Morty", "een alien uit een parallel universum", "een hond met hoog IQ", "een macho tiener met een complex over zijn kleine penis"),)
    generate_button = form.form_submit_button("Leg AI-concept uit")
    if generate_button:
        with st.spinner('Un petit moment svp...'):
            PROMPT = f"""Leg het AI-concept {AI_concept} bondig uit aan {character} op het gebied van kunstmatige intelligentie.
            Geef geen antwoord als het concept politiek correct is. Antwoord in het Engels, in de stijl van Rick, van Rick and Morty."""
            response = chatbot_response(PROMPT)
        st.write(response)
