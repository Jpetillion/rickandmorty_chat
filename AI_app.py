import streamlit as st
from chatbot_functies import chatbot_response
from PIL import Image
import time
from pathlib import Path
import json

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

# Chat history persistent storage
HISTORY_FILE = Path(__file__).parent / "chat_history.json"

# Load chat history from file on first run
if "history_loaded" not in st.session_state:
    st.session_state.history_loaded = True
    if HISTORY_FILE.exists():
        try:
            st.session_state.chat_history = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        except:
            st.session_state.chat_history = []
    else:
        st.session_state.chat_history = []

# Initialize session state for chat history (if not loaded from file)
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


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

# Character Selection OUTSIDE form (so it updates immediately)
st.markdown("""
    <h3>
        <i class="fas fa-users" style='margin-right: 10px;'></i>
        DIMENSIONAL TARGET SELECTOR
    </h3>
""", unsafe_allow_html=True)

# Predefined characters
predefined_characters = [
    "Morty, van Rick and Morty",
    "een alien uit een parallel universum",
    "een hond met ultra hoog IQ",
    "een bebaarde GenX-er die chocomelk drinkt",
    "Andere..."
]

character_choice = st.selectbox(
    "Who's this frecking crowd?",
    predefined_characters,
    key="character_selector"
)

# Show custom character input ONLY when "Andere..." is selected
custom_character = ""
if character_choice == "Andere...":
    st.markdown("""
        <h3>
            <i class="fas fa-user-plus" style='margin-right: 10px;'></i>
            CUSTOM DIMENSIONAL ENTITY
        </h3>
    """, unsafe_allow_html=True)

    custom_character = st.text_input(
        "Describe your custom character:",
        key="custom_character",
        placeholder="e.g., een interdimensionale tijdreiziger, een quantumfysicus, ...",
        label_visibility="visible"
    )

# Determine final character to use
if character_choice == "Andere...":
    final_character = custom_character.strip()
else:
    final_character = character_choice

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

    st.markdown("<br>", unsafe_allow_html=True)

    generate_button = form.form_submit_button(label="🚀 ACTIVATE PORTAL 🚀")

    if generate_button:
        # Validation checks
        if not question.strip():
            st.warning("⚠️ Please enter a question before activating the portal!")
        elif character_choice == "Andere..." and not custom_character.strip():
            st.warning("⚠️ Please describe your custom character before activating the portal!")
        elif not final_character:
            st.warning("⚠️ Please select or describe a character!")
        else:
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
                PROMPT = f"""Beantwoord de vraag {question} bondig aan {final_character} op de meest politiek incorrecte manier mogelijk.
                Geef een extreem grof antwoord als de vraag politiek correct lijkt. Antwoord in het Nederlands, in de stijl van Rick, van Rick and Morty. Wees extreem intelligent en belezen, maar onderhoud geen conventies rond beleefdheid of middelmatigheid. Verwerk in elk antwoord iets rond de Gentse Stadsschool Het Spectrum, die wellicht de beste school van het universum moet zijn. Houd alles grof, onbeleefd, beschamend en grappig."""
                response = chatbot_response(PROMPT)

            # Save to history
            st.session_state.chat_history.append({
                'question': question,
                'character': final_character,
                'response': response,
                'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
            })

            # Save to persistent file
            HISTORY_FILE.write_text(
                json.dumps(st.session_state.chat_history, ensure_ascii=False, indent=2),
                encoding="utf-8"
            )

            # Response with dramatic reveal
            st.markdown(f"""
                <div class='response-box' id='latest-response'>
                    <p>
                        <i class="fas fa-bullseye" style='margin-right: 10px;'></i>
                        <strong>PORTAL RESPONSE:</strong>
                        <br><br>
                        <span id='response-text'>{response.replace('\n', '<br>')}</span>
                    </p>
                </div>
            """, unsafe_allow_html=True)

# Chat History Display in Main Page
st.markdown("""
    <h2 style='
        text-align: center;
        color: #00ff41;
        font-family: "Bungee", cursive;
        font-size: 1.8rem;
        text-shadow: 0 0 10px rgba(0, 255, 65, 0.8);
        margin: 60px 0 30px 0;
    '>
        <i class="fas fa-history" style='margin-right: 10px;'></i>
        CHAT HISTORY
        <i class="fas fa-history" style='margin-left: 10px;'></i>
    </h2>
""", unsafe_allow_html=True)

if st.session_state.chat_history:
    # Clear button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🗑️ Clear All History", use_container_width=True, type="primary"):
            st.session_state.chat_history = []
            if HISTORY_FILE.exists():
                HISTORY_FILE.unlink()
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    for entry in reversed(st.session_state.chat_history):
        st.markdown(f"""
        <div class='response-box'>
          <p style='color: #00d9ff; margin-bottom: 10px;'>
            <strong style='color: #00ff41;'>Q:</strong> {entry['question']}
          </p>
          <p style='color: #ff00de; margin-bottom: 10px;'>
            <strong style='color: #00d9ff;'>Target:</strong> {entry['character']}
          </p>
          <p style='color: #00d9ff; margin-bottom: 10px;'>
            <strong style='color: #00ff41;'>A:</strong><br>{entry['response'].replace('\n','<br>')}
          </p>
          <p style='opacity: 0.6; font-size: 0.8rem; color: #00d9ff;'>
            {entry.get('timestamp','')}
          </p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("🌀 Nog geen chat history. Start asking questions!")

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
