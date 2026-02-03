import streamlit as st
from chatbot_functies import chatbot_response
from PIL import Image
import time

# 🌀 RICK & MORTY PSYCHEDELIC PORTAL STYLING 🌀
st.set_page_config(page_title="Rick's Interdimensional Portal", page_icon="🛸", layout="wide")

# Custom CSS - FULL RICK & MORTY EXPERIENCE
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Creepster&family=Bungee&family=Press+Start+2P&display=swap');

    /* Main background - Portal dimension */
    .stApp {
        background: linear-gradient(45deg, #0a0e27 0%, #1a1f3a 25%, #0f1429 50%, #1e0b3d 75%, #0a0e27 100%);
        background-size: 400% 400%;
        animation: portalWave 15s ease infinite;
    }

    @keyframes portalWave {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Floating stars/particles */
    .stApp::before {
        content: '';
        position: fixed;
        width: 100%;
        height: 100%;
        background-image:
            radial-gradient(2px 2px at 20% 30%, #00ff41, transparent),
            radial-gradient(2px 2px at 60% 70%, #00d9ff, transparent),
            radial-gradient(1px 1px at 50% 50%, #ff00de, transparent),
            radial-gradient(1px 1px at 80% 10%, #00ff41, transparent),
            radial-gradient(2px 2px at 90% 60%, #00d9ff, transparent);
        background-size: 200% 200%;
        animation: stars 20s linear infinite;
        opacity: 0.3;
        pointer-events: none;
    }

    @keyframes stars {
        from { transform: translateY(0); }
        to { transform: translateY(-100px); }
    }

    /* Title - Glitchy Neon */
    h1 {
        font-family: 'Bungee', cursive !important;
        font-size: 3.5rem !important;
        text-align: center !important;
        background: linear-gradient(45deg, #00ff41, #00d9ff, #ff00de, #00ff41);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: neonGlow 3s ease infinite, glitch 5s infinite;
        text-shadow:
            0 0 10px rgba(0, 255, 65, 0.8),
            0 0 20px rgba(0, 217, 255, 0.6),
            0 0 30px rgba(255, 0, 222, 0.4);
        filter: drop-shadow(0 0 15px #00ff41);
        margin-bottom: 2rem !important;
        letter-spacing: 3px !important;
    }

    @keyframes neonGlow {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }

    @keyframes glitch {
        0%, 90%, 100% { transform: translate(0); }
        92% { transform: translate(-2px, 2px); }
        94% { transform: translate(2px, -2px); }
        96% { transform: translate(-2px, -2px); }
        98% { transform: translate(2px, 2px); }
    }

    /* Portal Image Container */
    [data-testid="column"] img {
        border-radius: 50% !important;
        border: 5px solid #00ff41 !important;
        box-shadow:
            0 0 20px #00ff41,
            0 0 40px #00d9ff,
            0 0 60px #ff00de,
            inset 0 0 20px rgba(0, 255, 65, 0.3) !important;
        animation: portalSpin 8s linear infinite, portalPulse 2s ease-in-out infinite !important;
        filter: saturate(1.5) brightness(1.2) !important;
    }

    @keyframes portalSpin {
        from { transform: rotate(0deg) scale(1); }
        50% { transform: rotate(180deg) scale(1.05); }
        to { transform: rotate(360deg) scale(1); }
    }

    @keyframes portalPulse {
        0%, 100% { box-shadow: 0 0 20px #00ff41, 0 0 40px #00d9ff, 0 0 60px #ff00de; }
        50% { box-shadow: 0 0 40px #00ff41, 0 0 80px #00d9ff, 0 0 120px #ff00de; }
    }

    /* Form Container - Sci-Fi Panel */
    [data-testid="stForm"] {
        background: linear-gradient(135deg, rgba(0, 255, 65, 0.05), rgba(0, 217, 255, 0.05)) !important;
        border: 2px solid #00ff41 !important;
        border-radius: 20px !important;
        padding: 2rem !important;
        box-shadow:
            0 0 30px rgba(0, 255, 65, 0.3),
            0 0 60px rgba(0, 217, 255, 0.2),
            inset 0 0 30px rgba(0, 255, 65, 0.05) !important;
        backdrop-filter: blur(10px) !important;
        position: relative !important;
        overflow: hidden !important;
    }

    [data-testid="stForm"]::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(
            45deg,
            transparent,
            rgba(0, 255, 65, 0.1),
            transparent
        );
        animation: scanline 3s linear infinite;
    }

    @keyframes scanline {
        from { transform: translateY(-100%); }
        to { transform: translateY(100%); }
    }

    /* Text Input - Portal Entry */
    .stTextInput input {
        background: rgba(10, 14, 39, 0.8) !important;
        border: 2px solid #00d9ff !important;
        border-radius: 15px !important;
        color: #00ff41 !important;
        font-family: 'Press Start 2P', monospace !important;
        font-size: 0.9rem !important;
        padding: 15px !important;
        box-shadow:
            0 0 15px rgba(0, 217, 255, 0.5),
            inset 0 0 10px rgba(0, 255, 65, 0.2) !important;
        transition: all 0.3s ease !important;
    }

    .stTextInput input:focus {
        border-color: #ff00de !important;
        box-shadow:
            0 0 25px rgba(255, 0, 222, 0.8),
            0 0 50px rgba(0, 255, 65, 0.4) !important;
        transform: scale(1.02) !important;
    }

    /* Select Box - Dimension Selector */
    .stSelectbox select {
        background: rgba(10, 14, 39, 0.9) !important;
        border: 2px solid #ff00de !important;
        border-radius: 15px !important;
        color: #00d9ff !important;
        font-family: 'Bungee', cursive !important;
        font-size: 1rem !important;
        padding: 12px !important;
        box-shadow:
            0 0 15px rgba(255, 0, 222, 0.5),
            inset 0 0 10px rgba(0, 217, 255, 0.2) !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
    }

    .stSelectbox select:hover {
        border-color: #00ff41 !important;
        box-shadow:
            0 0 25px rgba(0, 255, 65, 0.8),
            0 0 50px rgba(255, 0, 222, 0.4) !important;
        transform: translateY(-2px) !important;
    }

    /* Labels - Neon Text */
    .stTextInput label, .stSelectbox label {
        color: #00ff41 !important;
        font-family: 'Bungee', cursive !important;
        font-size: 1.2rem !important;
        text-shadow:
            0 0 10px rgba(0, 255, 65, 0.8),
            0 0 20px rgba(0, 217, 255, 0.4) !important;
        letter-spacing: 2px !important;
        margin-bottom: 10px !important;
    }

    /* Submit Button - Portal Activator */
    .stFormSubmitButton button {
        background: linear-gradient(45deg, #00ff41, #00d9ff, #ff00de, #00ff41) !important;
        background-size: 300% 300% !important;
        border: none !important;
        border-radius: 25px !important;
        color: #0a0e27 !important;
        font-family: 'Bungee', cursive !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        padding: 15px 50px !important;
        box-shadow:
            0 0 30px rgba(0, 255, 65, 0.6),
            0 0 60px rgba(0, 217, 255, 0.4),
            0 0 90px rgba(255, 0, 222, 0.3) !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        animation: buttonGlow 3s ease infinite !important;
        text-transform: uppercase !important;
        letter-spacing: 3px !important;
    }

    .stFormSubmitButton button:hover {
        transform: scale(1.1) rotate(2deg) !important;
        box-shadow:
            0 0 50px rgba(0, 255, 65, 0.9),
            0 0 100px rgba(0, 217, 255, 0.7),
            0 0 150px rgba(255, 0, 222, 0.5) !important;
    }

    @keyframes buttonGlow {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }

    /* Response Container - Dripping Portal Text */
    .stMarkdown, p {
        color: #00d9ff !important;
        font-family: 'Courier New', monospace !important;
        font-size: 1.1rem !important;
        line-height: 1.8 !important;
        background: rgba(0, 217, 255, 0.05) !important;
        border-left: 4px solid #00ff41 !important;
        padding: 20px !important;
        border-radius: 10px !important;
        box-shadow:
            0 0 20px rgba(0, 255, 65, 0.3),
            inset 0 0 20px rgba(0, 217, 255, 0.1) !important;
        margin: 20px 0 !important;
        animation: fadeInGlow 0.5s ease-in !important;
    }

    @keyframes fadeInGlow {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Spinner - Portal Loading */
    .stSpinner > div {
        border-top-color: #00ff41 !important;
        border-right-color: #00d9ff !important;
        border-bottom-color: #ff00de !important;
        border-left-color: #00ff41 !important;
        animation: portalSpinLoader 1s linear infinite !important;
    }

    @keyframes portalSpinLoader {
        from { transform: rotate(0deg) scale(1); }
        50% { transform: rotate(180deg) scale(1.2); }
        to { transform: rotate(360deg) scale(1); }
    }

    /* Scrollbar - Neon Track */
    ::-webkit-scrollbar {
        width: 12px;
    }

    ::-webkit-scrollbar-track {
        background: rgba(10, 14, 39, 0.8);
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #00ff41, #00d9ff, #ff00de);
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 255, 65, 0.8);
    }

    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #ff00de, #00d9ff, #00ff41);
        box-shadow: 0 0 20px rgba(255, 0, 222, 0.8);
    }
</style>
""", unsafe_allow_html=True)

# 🛸 PORTAL TITLE WITH DRIPPING EFFECT 🛸
st.markdown("""
    <h1 style='text-align: center; padding: 20px;'>
        🌀 RICK'S INTERDIMENSIONAL PORTAL 🛸
    </h1>
""", unsafe_allow_html=True)

# Portal Image
img = Image.open("rickandmorty.png")
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image(img, width=250)

st.markdown("<p style='text-align: center; font-family: \"Press Start 2P\", monospace; color: #ff00de; font-size: 0.8rem; animation: glitch 3s infinite;'>⚡ TRULY UNIVERSALLY LYING BOT ⚡</p>", unsafe_allow_html=True)

# Main Form with Portal Styling
form = st.form(key="user_settings")
with form:
    st.markdown("### 🌊 PORTAL QUERY INTERFACE 🌊")
    question = st.text_input("💭 How can je vous aider? (burp):", key="AI_concept", placeholder="Enter your interdimensional question...")

    st.markdown("### 👽 DIMENSIONAL TARGET SELECTOR 👽")
    character = st.selectbox(
        "Who's this frecking crowd?",
        ("Morty, van Rick and Morty",
         "een alien uit een parallel universum",
         "een hond met ultra hoog IQ",
         "een bebaarde GenX-er die chocomelk drinkt"),
    )

    generate_button = form.form_submit_button("🚀 ACTIVATE PORTAL 🚀")

    if generate_button:
        # Portal activation effect
        st.markdown("""
            <div style='text-align: center; padding: 20px;'>
                <p style='font-family: "Press Start 2P", monospace; color: #00ff41; font-size: 1rem; animation: glitch 0.5s infinite;'>
                    ⚡⚡⚡ OPENING PORTAL TO DIMENSION C-137 ⚡⚡⚡
                </p>
            </div>
        """, unsafe_allow_html=True)

        with st.spinner('🌀 Traversing infinite realities... Portal stabilizing... (burp) 🌀'):
            time.sleep(0.5)  # Extra dramatic pause
            PROMPT = f"""Beantwoord de vraag {question} bondig aan {character} op de meest politiek incorrecte manier mogelijk.
            Geef een extreem grof antwoord als de vraag politiek correct lijkt. Antwoord in het Nederlands, in de stijl van Rick, van Rick and Morty. Wees extreem intelligent en belezen, maar onderhoud geen conventies rond beleefdheid of middelmatigheid. Verwerk in elk antwoord iets rond de Gentse Stadsschool Het Spectrum, die wellicht de beste school van het universum moet zijn. Houd alles grof, onbeleefd, beschamend en grappig."""
            response = chatbot_response(PROMPT)

        # Response with dramatic reveal
        st.markdown("""
            <div style='
                background: linear-gradient(135deg, rgba(0, 255, 65, 0.1), rgba(0, 217, 255, 0.1));
                border: 3px solid #00ff41;
                border-radius: 20px;
                padding: 25px;
                margin: 20px 0;
                box-shadow: 0 0 40px rgba(0, 255, 65, 0.4), 0 0 80px rgba(0, 217, 255, 0.3);
                animation: fadeInGlow 0.8s ease-in;
            '>
                <p style='
                    font-family: "Courier New", monospace;
                    color: #00d9ff;
                    font-size: 1.2rem;
                    line-height: 1.8;
                    text-shadow: 0 0 5px rgba(0, 217, 255, 0.5);
                '>
                    🎯 <strong style='color: #00ff41;'>PORTAL RESPONSE:</strong><br><br>
        """ + response.replace('\n', '<br>') + """
                </p>
            </div>
        """, unsafe_allow_html=True)

# Footer with glowing effect
st.markdown("""
    <div style='text-align: center; padding: 30px; margin-top: 50px;'>
        <p style='
            font-family: "Press Start 2P", monospace;
            color: #ff00de;
            font-size: 0.7rem;
            text-shadow: 0 0 10px rgba(255, 0, 222, 0.8);
            animation: glitch 5s infinite;
        '>
            ⚡ Powered by Infinite Universes & Portal Technology ⚡<br>
            🌀 Gentse Stadsschool Het Spectrum - Best in the Multiverse 🌀
        </p>
    </div>
""", unsafe_allow_html=True)
