// RICK & MORTY PORTAL AUDIO SYSTEM
// Web Audio API for generating sci-fi sounds

class PortalAudioSystem {
    constructor() {
        this.audioContext = null;
        this.isMuted = false;
        this.masterVolume = 0.3;
        this.init();
    }

    init() {
        // Initialize Audio Context on first user interaction
        document.addEventListener('click', () => {
            if (!this.audioContext) {
                this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
                this.startAmbientLoop();
            }
        }, { once: true });
    }

    // Ambient background loop - glitchy space electronica
    startAmbientLoop() {
        if (this.isMuted) return;

        const playAmbient = () => {
            // Create oscillators for ambient drone
            const osc1 = this.audioContext.createOscillator();
            const osc2 = this.audioContext.createOscillator();
            const osc3 = this.audioContext.createOscillator();

            const gain1 = this.audioContext.createGain();
            const gain2 = this.audioContext.createGain();
            const gain3 = this.audioContext.createGain();
            const masterGain = this.audioContext.createGain();

            // Deep space frequencies
            osc1.frequency.value = 55; // Deep bass
            osc2.frequency.value = 110;
            osc3.frequency.value = 165;

            osc1.type = 'sine';
            osc2.type = 'triangle';
            osc3.type = 'sawtooth';

            // Connect nodes
            osc1.connect(gain1);
            osc2.connect(gain2);
            osc3.connect(gain3);
            gain1.connect(masterGain);
            gain2.connect(masterGain);
            gain3.connect(masterGain);
            masterGain.connect(this.audioContext.destination);

            // Volume settings (very subtle)
            gain1.gain.value = 0.02 * this.masterVolume;
            gain2.gain.value = 0.015 * this.masterVolume;
            gain3.gain.value = 0.01 * this.masterVolume;
            masterGain.gain.value = 1;

            // Random frequency modulation for glitchy effect
            const lfo = this.audioContext.createOscillator();
            const lfoGain = this.audioContext.createGain();
            lfo.frequency.value = 0.1;
            lfoGain.gain.value = 3;
            lfo.connect(lfoGain);
            lfoGain.connect(osc2.frequency);

            const now = this.audioContext.currentTime;
            osc1.start(now);
            osc2.start(now);
            osc3.start(now);
            lfo.start(now);

            // Random duration for glitchy feel
            const duration = 8 + Math.random() * 4;

            osc1.stop(now + duration);
            osc2.stop(now + duration);
            osc3.stop(now + duration);
            lfo.stop(now + duration);

            // Schedule next ambient sound
            setTimeout(playAmbient, duration * 1000 - 500);
        };

        playAmbient();
    }

    // Portal activation sound - dramatic whoosh
    playPortalActivation() {
        if (this.isMuted || !this.audioContext) return;

        const now = this.audioContext.currentTime;

        // Swoosh sound with frequency sweep
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();
        const filter = this.audioContext.createBiquadFilter();

        osc.type = 'sawtooth';
        filter.type = 'lowpass';

        // Dramatic frequency sweep
        osc.frequency.setValueAtTime(800, now);
        osc.frequency.exponentialRampToValueAtTime(50, now + 0.8);

        filter.frequency.setValueAtTime(2000, now);
        filter.frequency.exponentialRampToValueAtTime(100, now + 0.8);
        filter.Q.value = 10;

        // Volume envelope
        gain.gain.setValueAtTime(0, now);
        gain.gain.linearRampToValueAtTime(0.4 * this.masterVolume, now + 0.1);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.8);

        osc.connect(filter);
        filter.connect(gain);
        gain.connect(this.audioContext.destination);

        osc.start(now);
        osc.stop(now + 0.8);

        // Add glitch sounds
        for (let i = 0; i < 3; i++) {
            setTimeout(() => this.playGlitch(), i * 200);
        }
    }

    // Glitch sound effect
    playGlitch() {
        if (this.isMuted || !this.audioContext) return;

        const now = this.audioContext.currentTime;
        const noise = this.audioContext.createBufferSource();
        const buffer = this.audioContext.createBuffer(1, 4410, 44100);
        const data = buffer.getChannelData(0);

        for (let i = 0; i < 4410; i++) {
            data[i] = Math.random() * 2 - 1;
        }

        noise.buffer = buffer;
        const gain = this.audioContext.createGain();
        const filter = this.audioContext.createBiquadFilter();

        filter.type = 'highpass';
        filter.frequency.value = 2000;

        gain.gain.setValueAtTime(0.15 * this.masterVolume, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.1);

        noise.connect(filter);
        filter.connect(gain);
        gain.connect(this.audioContext.destination);

        noise.start(now);
        noise.stop(now + 0.1);
    }

    // Typing sound - subtle click
    playTyping() {
        if (this.isMuted || !this.audioContext) return;

        const now = this.audioContext.currentTime;
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();

        osc.frequency.value = 800 + Math.random() * 200;
        osc.type = 'sine';

        gain.gain.setValueAtTime(0.05 * this.masterVolume, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.03);

        osc.connect(gain);
        gain.connect(this.audioContext.destination);

        osc.start(now);
        osc.stop(now + 0.03);
    }

    // Dropdown select sound - digital beep
    playSelect() {
        if (this.isMuted || !this.audioContext) return;

        const now = this.audioContext.currentTime;
        const osc = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();

        osc.frequency.setValueAtTime(600, now);
        osc.frequency.exponentialRampToValueAtTime(800, now + 0.1);
        osc.type = 'square';

        gain.gain.setValueAtTime(0.1 * this.masterVolume, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.1);

        osc.connect(gain);
        gain.connect(this.audioContext.destination);

        osc.start(now);
        osc.stop(now + 0.1);
    }

    // Response ready sound - success chime
    playResponseReady() {
        if (this.isMuted || !this.audioContext) return;

        const now = this.audioContext.currentTime;
        const frequencies = [523.25, 659.25, 783.99]; // C, E, G chord

        frequencies.forEach((freq, index) => {
            const osc = this.audioContext.createOscillator();
            const gain = this.audioContext.createGain();

            osc.frequency.value = freq;
            osc.type = 'sine';

            const startTime = now + index * 0.08;
            gain.gain.setValueAtTime(0, startTime);
            gain.gain.linearRampToValueAtTime(0.15 * this.masterVolume, startTime + 0.05);
            gain.gain.exponentialRampToValueAtTime(0.01, startTime + 0.4);

            osc.connect(gain);
            gain.connect(this.audioContext.destination);

            osc.start(startTime);
            osc.stop(startTime + 0.4);
        });
    }

    // Spinner sound - continuous portal hum
    playSpinnerSound() {
        if (this.isMuted || !this.audioContext) return;

        const now = this.audioContext.currentTime;
        const osc1 = this.audioContext.createOscillator();
        const osc2 = this.audioContext.createOscillator();
        const gain = this.audioContext.createGain();

        osc1.frequency.value = 200;
        osc2.frequency.value = 203; // Slight detuning for warble
        osc1.type = 'sine';
        osc2.type = 'sine';

        gain.gain.setValueAtTime(0, now);
        gain.gain.linearRampToValueAtTime(0.08 * this.masterVolume, now + 0.2);

        osc1.connect(gain);
        osc2.connect(gain);
        gain.connect(this.audioContext.destination);

        osc1.start(now);
        osc2.start(now);

        // Store for stopping later
        this.spinnerOsc1 = osc1;
        this.spinnerOsc2 = osc2;
        this.spinnerGain = gain;
    }

    stopSpinnerSound() {
        if (this.spinnerOsc1) {
            const now = this.audioContext.currentTime;
            this.spinnerGain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);
            this.spinnerOsc1.stop(now + 0.3);
            this.spinnerOsc2.stop(now + 0.3);
            this.spinnerOsc1 = null;
            this.spinnerOsc2 = null;
        }
    }

    toggleMute() {
        this.isMuted = !this.isMuted;
        if (this.isMuted) {
            this.stopSpinnerSound();
        }
        return this.isMuted;
    }
}

// Initialize audio system
const portalAudio = new PortalAudioSystem();

// Event listeners for Streamlit elements
function setupAudioListeners() {
    // Button clicks - Portal Activation
    document.addEventListener('click', (e) => {
        const button = e.target.closest('button[kind="formSubmit"]');
        if (button && button.textContent.includes('ACTIVATE PORTAL')) {
            portalAudio.playPortalActivation();
        }
    });

    // Input typing
    document.addEventListener('keydown', (e) => {
        const input = e.target.closest('input[type="text"]');
        if (input) {
            portalAudio.playTyping();
        }
    });

    // Dropdown selection
    document.addEventListener('change', (e) => {
        const select = e.target.closest('select');
        if (select) {
            portalAudio.playSelect();
        }
    });

    // Detect spinner appearance
    const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            mutation.addedNodes.forEach((node) => {
                if (node.nodeType === 1) {
                    if (node.classList && node.classList.contains('stSpinner')) {
                        portalAudio.playSpinnerSound();
                    }
                }
            });
            mutation.removedNodes.forEach((node) => {
                if (node.nodeType === 1) {
                    if (node.classList && node.classList.contains('stSpinner')) {
                        portalAudio.stopSpinnerSound();
                        portalAudio.playResponseReady();
                    }
                }
            });
        });
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true
    });

    // Detect response box appearance
    const responseObserver = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            mutation.addedNodes.forEach((node) => {
                if (node.nodeType === 1 && node.innerHTML && node.innerHTML.includes('response-box')) {
                    setTimeout(() => portalAudio.playResponseReady(), 100);
                }
            });
        });
    });

    responseObserver.observe(document.body, {
        childList: true,
        subtree: true
    });
}

// Wait for DOM to be ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupAudioListeners);
} else {
    setupAudioListeners();
}

// Expose toggle function globally
window.togglePortalAudio = () => portalAudio.toggleMute();

// TEXT-TO-SPEECH: Rick-like voice (free, using Web Speech API)
class RickVoice {
    constructor() {
        this.synth = window.speechSynthesis;
        this.isSpeaking = false;
    }

    speak(text) {
        if (this.isSpeaking) {
            this.synth.cancel();
            this.isSpeaking = false;
            return;
        }

        if (!this.synth) {
            console.error('Speech synthesis not supported');
            return;
        }

        // Clean HTML from text
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = text;
        const cleanText = tempDiv.textContent || tempDiv.innerText || '';

        const utterance = new SpeechSynthesisUtterance(cleanText);

        // Rick's voice characteristics
        utterance.pitch = 1.3;  // Higher pitch
        utterance.rate = 1.2;   // Faster speech
        utterance.volume = 1.0;

        // Try to find a voice that works (prefer English for better quality)
        const voices = this.synth.getVoices();
        const preferredVoice = voices.find(voice =>
            voice.lang.startsWith('en') && voice.name.includes('Male')
        ) || voices.find(voice =>
            voice.lang.startsWith('en')
        ) || voices[0];

        if (preferredVoice) {
            utterance.voice = preferredVoice;
        }

        // Add random burps and stutters for Rick effect
        utterance.onboundary = (event) => {
            // Randomly add glitch sounds during speech
            if (Math.random() < 0.05) {
                portalAudio.playGlitch();
            }
        };

        utterance.onstart = () => {
            this.isSpeaking = true;
            // Update button text
            const readBtn = document.getElementById('read-aloud-btn');
            if (readBtn) {
                readBtn.innerHTML = '<i class="fas fa-stop"></i> STOP RICK';
            }
        };

        utterance.onend = () => {
            this.isSpeaking = false;
            const readBtn = document.getElementById('read-aloud-btn');
            if (readBtn) {
                readBtn.innerHTML = '<i class="fas fa-volume-up"></i> RICK LEEST VOOR';
            }
        };

        utterance.onerror = () => {
            this.isSpeaking = false;
            const readBtn = document.getElementById('read-aloud-btn');
            if (readBtn) {
                readBtn.innerHTML = '<i class="fas fa-volume-up"></i> RICK LEEST VOOR';
            }
        };

        this.synth.speak(utterance);
    }

    stop() {
        if (this.synth) {
            this.synth.cancel();
            this.isSpeaking = false;
        }
    }
}

// Initialize Rick voice
const rickVoice = new RickVoice();

// Load voices (Chrome needs this)
if (window.speechSynthesis) {
    window.speechSynthesis.onvoiceschanged = () => {
        window.speechSynthesis.getVoices();
    };
}

// Expose globally
window.rickSpeakText = (text) => rickVoice.speak(text);
window.rickStopSpeaking = () => rickVoice.stop();
