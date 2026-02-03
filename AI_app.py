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

# Load audio system JavaScript with proper initialization
audio_js_path = Path(__file__).parent / "assets" / "audio.js"
with open(audio_js_path) as f:
    audio_js_content = f.read()
    st.components.v1.html(f"""
        <script>
        {audio_js_content}
        // Force initialization on load
        setTimeout(() => {{
            if (typeof setupAudioListeners === 'function') {{
                setupAudioListeners();
            }}
        }}, 500);
        </script>
    """, height=0, scrolling=False)

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Initialize audio mute state
if 'audio_muted' not in st.session_state:
    st.session_state.audio_muted = False

# Sidebar for Portal History
with st.sidebar:
    st.markdown("""
        <h2 style='
            text-align: center;
            color: #00ff41;
            font-family: "Bungee", cursive;
            font-size: 1.5rem;
            text-shadow: 0 0 10px rgba(0, 255, 65, 0.8);
            margin-bottom: 20px;
        '>
            <i class="fas fa-history" style='margin-right: 10px;'></i>
            PORTAL HISTORY
        </h2>
    """, unsafe_allow_html=True)

    # Audio control button
    audio_icon = "🔇" if st.session_state.audio_muted else "🔊"
    audio_text = "Unmute Portal Audio" if st.session_state.audio_muted else "Mute Portal Audio"

    if st.button(f"{audio_icon} {audio_text}", use_container_width=True, key="audio_toggle"):
        st.session_state.audio_muted = not st.session_state.audio_muted
        st.components.v1.html("""
            <script>
                if (window.togglePortalAudio) {
                    window.togglePortalAudio();
                }
            </script>
        """, height=0)
        st.rerun()

    st.markdown("<hr style='border: 1px solid rgba(0, 255, 65, 0.3); margin: 20px 0;'>", unsafe_allow_html=True)

    if st.session_state.chat_history:
        if st.button("🗑️ Clear All Dimensions", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

        st.markdown("<hr style='border: 1px solid rgba(0, 255, 65, 0.3); margin: 20px 0;'>", unsafe_allow_html=True)

        # Display history in reverse order (newest first)
        for idx, entry in enumerate(reversed(st.session_state.chat_history)):
            with st.expander(f"🌀 Query #{len(st.session_state.chat_history) - idx}"):
                st.markdown(f"""
                    <div style='
                        background: rgba(0, 0, 0, 0.3);
                        padding: 10px;
                        border-radius: 8px;
                        margin-bottom: 10px;
                    '>
                        <p style='
                            color: #00d9ff;
                            font-family: "Courier New", monospace;
                            font-size: 0.85rem;
                            margin: 0;
                        '>
                            <strong style='color: #00ff41;'>Q:</strong> {entry['question']}
                        </p>
                    </div>
                    <div style='
                        background: rgba(0, 0, 0, 0.3);
                        padding: 10px;
                        border-radius: 8px;
                        margin-bottom: 10px;
                    '>
                        <p style='
                            color: #ff00de;
                            font-family: "Courier New", monospace;
                            font-size: 0.8rem;
                            margin: 0;
                        '>
                            <strong style='color: #00d9ff;'>Target:</strong> {entry['character']}
                        </p>
                    </div>
                    <div style='
                        background: rgba(0, 255, 65, 0.05);
                        padding: 10px;
                        border-radius: 8px;
                        border-left: 3px solid #00ff41;
                    '>
                        <p style='
                            color: #00d9ff;
                            font-family: "Courier New", monospace;
                            font-size: 0.85rem;
                            line-height: 1.6;
                            margin: 0;
                        '>
                            <strong style='color: #00ff41;'>A:</strong> {entry['response']}
                        </p>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style='
                text-align: center;
                padding: 30px 20px;
                background: rgba(0, 0, 0, 0.3);
                border-radius: 10px;
                border: 2px dashed rgba(0, 255, 65, 0.3);
            '>
                <p style='
                    color: #00d9ff;
                    font-family: "Press Start 2P", monospace;
                    font-size: 0.7rem;
                    line-height: 1.8;
                '>
                    No portal jumps yet...<br>
                    Start asking questions!
                </p>
            </div>
        """, unsafe_allow_html=True)

# Floating Sidebar Toggle Button
st.components.v1.html("""
    <div class="sidebar-toggle" id="sidebarToggle" title="Toggle Portal History">
        <i class="fas fa-bars"></i>
    </div>
    <script>
        function toggleSidebar() {
            try {
                // Try multiple methods to find and toggle sidebar
                const sidebar = parent.document.querySelector('[data-testid="stSidebar"]');
                if (!sidebar) return;

                // Method 1: Click collapse button
                const collapseBtn = parent.document.querySelector('[data-testid="collapsedControl"]');
                if (collapseBtn) {
                    collapseBtn.click();
                    return;
                }

                // Method 2: Toggle aria-expanded
                const isExpanded = sidebar.getAttribute('aria-expanded') === 'true';
                sidebar.setAttribute('aria-expanded', !isExpanded);

                // Method 3: Toggle CSS
                if (isExpanded) {
                    sidebar.style.marginLeft = '-21rem';
                } else {
                    sidebar.style.marginLeft = '0';
                }
            } catch (e) {
                console.log('Sidebar toggle error:', e);
            }
        }

        // Setup click handler
        const toggleBtn = document.getElementById('sidebarToggle');
        if (toggleBtn) {
            toggleBtn.addEventListener('click', toggleSidebar);
        }

        // Auto-hide toggle button when sidebar is visible
        function checkSidebarVisibility() {
            try {
                const sidebar = parent.document.querySelector('[data-testid="stSidebar"]');
                const toggleBtn = document.getElementById('sidebarToggle');
                if (sidebar && toggleBtn) {
                    const isExpanded = sidebar.getAttribute('aria-expanded') === 'true';
                    toggleBtn.style.display = isExpanded ? 'none' : 'flex';
                }
            } catch (e) {
                // Ignore errors
            }
        }

        setInterval(checkSidebarVisibility, 200);
    </script>
""", height=50, scrolling=False)

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
    )

    # Show custom character input if "Andere..." is selected
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
    final_character = custom_character if character_choice == "Andere..." and custom_character.strip() else character_choice

    st.markdown("<br>", unsafe_allow_html=True)

    generate_button = form.form_submit_button(label="🚀 ACTIVATE PORTAL 🚀")

    if generate_button:
        if question.strip():  # Only proceed if question is not empty
            # Check if custom character is needed but not provided
            if character_choice == "Andere..." and not custom_character.strip():
                st.warning("⚠️ Please describe your custom character before activating the portal!")
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
        else:
            st.warning("⚠️ Please enter a question before activating the portal!")

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
