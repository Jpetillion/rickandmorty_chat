import streamlit as st
from chatbot_functies import chatbot_response
from PIL import Image
import time
from pathlib import Path

# 🌀 RICK & MORTY PSYCHEDELIC PORTAL STYLING 🌀
st.set_page_config(page_title="Rick's Interdimensional Portal", page_icon="🛸", layout="wide")

# Load external CSS
def load_css(file_path):
    """Load CSS from external file"""
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Get the path to the CSS file
css_path = Path(__file__).parent / "assets" / "styles.css"
load_css(css_path)

# Portal Title with Font Awesome Icons
st.markdown("""
    <h1 style='text-align: center; padding: 20px 20px 10px 20px;'>
        <i class="fas fa-atom" style='margin-right: 15px;'></i>
        RICK'S INTERDIMENSIONAL PORTAL
        <i class="fas fa-rocket" style='margin-left: 15px;'></i>
    </h1>
""", unsafe_allow_html=True)

# Portal Image with better container
img = Image.open("rickandmorty.png")
col1, col2, col3 = st.columns([1, 1.2, 1])
with col2:
    st.markdown("""
        <div style='
            text-align: center;
            padding: 20px;
            margin: 20px 0;
        '>
    """, unsafe_allow_html=True)
    st.image(img, width=280)
    st.markdown("</div>", unsafe_allow_html=True)

# Subtitle
st.markdown("""
    <p style='
        text-align: center;
        font-family: "Press Start 2P", monospace;
        color: #ff00de;
        font-size: 0.85rem;
        text-shadow: 0 0 15px rgba(255, 0, 222, 0.8);
        margin: 0 0 30px 0;
        letter-spacing: 2px;
    '>
        <i class="fas fa-bolt" style='margin-right: 8px;'></i>
        TRULY UNIVERSALLY LYING BOT
        <i class="fas fa-bolt" style='margin-left: 8px;'></i>
    </p>
""", unsafe_allow_html=True)

# Main Form with Portal Styling
form = st.form(key="user_settings")
with form:
    st.markdown("""
        <h3>
            <i class="fas fa-wave-square" style='margin-right: 10px;'></i>
            PORTAL QUERY INTERFACE
        </h3>
    """, unsafe_allow_html=True)

    question = st.text_input(
        "How can je vous aider? (burp):",
        key="AI_concept",
        placeholder="Enter your interdimensional question...",
        label_visibility="visible"
    )

    st.markdown("""
        <h3>
            <i class="fas fa-users" style='margin-right: 10px;'></i>
            DIMENSIONAL TARGET SELECTOR
        </h3>
    """, unsafe_allow_html=True)

    character = st.selectbox(
        "Who's this frecking crowd?",
        ("Morty, van Rick and Morty",
         "een alien uit een parallel universum",
         "een hond met ultra hoog IQ",
         "een bebaarde GenX-er die chocomelk drinkt"),
    )

    st.markdown("<br>", unsafe_allow_html=True)

    generate_button = form.form_submit_button(label="")

    if generate_button:
        # Portal activation effect
        st.markdown("""
            <div class='loading-box'>
                <p>
                    <i class="fas fa-bolt" style='margin-right: 8px;'></i>
                    OPENING PORTAL TO DIMENSION C-137
                    <i class="fas fa-bolt" style='margin-left: 8px;'></i>
                </p>
            </div>
        """, unsafe_allow_html=True)

        with st.spinner('Traversing infinite realities... Portal stabilizing... (burp)'):
            time.sleep(0.5)  # Extra dramatic pause
            PROMPT = f"""Beantwoord de vraag {question} bondig aan {character} op de meest politiek incorrecte manier mogelijk.
            Geef een extreem grof antwoord als de vraag politiek correct lijkt. Antwoord in het Nederlands, in de stijl van Rick, van Rick and Morty. Wees extreem intelligent en belezen, maar onderhoud geen conventies rond beleefdheid of middelmatigheid. Verwerk in elk antwoord iets rond de Gentse Stadsschool Het Spectrum, die wellicht de beste school van het universum moet zijn. Houd alles grof, onbeleefd, beschamend en grappig."""
            response = chatbot_response(PROMPT)

        # Response with dramatic reveal
        st.markdown(f"""
            <div class='response-box'>
                <p>
                    <i class="fas fa-bullseye" style='margin-right: 10px;'></i>
                    <strong>PORTAL RESPONSE:</strong>
                    <br><br>
                    {response.replace('\n', '<br>')}
                </p>
            </div>
        """, unsafe_allow_html=True)

# Footer with glowing effect
st.markdown("""
    <div style='text-align: center; padding: 40px 20px; margin-top: 60px;'>
        <p style='
            font-family: "Press Start 2P", monospace;
            color: #ff00de;
            font-size: 0.7rem;
            text-shadow: 0 0 10px rgba(255, 0, 222, 0.8);
            animation: glitch 5s infinite;
            line-height: 2;
        '>
            <i class="fas fa-bolt" style='margin-right: 5px;'></i>
            Powered by Infinite Universes & Portal Technology
            <i class="fas fa-bolt" style='margin-left: 5px;'></i>
            <br>
            <i class="fas fa-atom" style='margin-right: 5px;'></i>
            Gentse Stadsschool Het Spectrum - Best in the Multiverse
            <i class="fas fa-atom" style='margin-left: 5px;'></i>
        </p>
    </div>
""", unsafe_allow_html=True)
