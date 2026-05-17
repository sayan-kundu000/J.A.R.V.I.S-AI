class JarvisVoice {
    constructor() {
        this.synth = window.speechSynthesis;
        this.recognition = null;
        this.voice = null;
        this.isListening = false;
        this.voiceEnabled = true;

        if ('webkitSpeechRecognition' in window) {
            this.recognition = new webkitSpeechRecognition();
            this.recognition.continuous = false;
            this.recognition.interimResults = false;
            this.recognition.lang = 'en-GB';
        }

        // Try to find a good JARVIS-like voice
        this.loadVoices();
        if (this.synth.onvoiceschanged !== undefined) {
            this.synth.onvoiceschanged = () => this.loadVoices();
        }
    }

    loadVoices() {
        const voices = this.synth.getVoices();
        // Look for British Male voices
        this.voice = voices.find(v => v.name.includes('Google UK English Male') || 
                                     v.name.includes('Microsoft George') ||
                                     (v.lang === 'en-GB' && v.name.includes('Male')));
        
        // Fallback to any en-GB voice
        if (!this.voice) {
            this.voice = voices.find(v => v.lang === 'en-GB');
        }
    }

    speak(text) {
        if (!this.voiceEnabled) return;
        
        // Cancel any ongoing speech
        this.synth.cancel();

        const utterance = new SpeechSynthesisUtterance(text);
        if (this.voice) {
            utterance.voice = this.voice;
        }
        utterance.pitch = 0.9; // Slightly deeper
        utterance.rate = 1.0;  // Measured pace
        utterance.volume = 1.0;

        this.synth.speak(utterance);
    }

    startListening(onResult, onEnd) {
        if (!this.recognition) {
            console.error("Speech recognition not supported.");
            return;
        }

        this.isListening = true;
        this.recognition.start();

        this.recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            if (onResult) onResult(transcript);
        };

        this.recognition.onend = () => {
            this.isListening = false;
            if (onEnd) onEnd();
        };

        this.recognition.onerror = (event) => {
            console.error("Speech recognition error:", event.error);
            this.isListening = false;
            if (onEnd) onEnd();
        };
    }

    stopListening() {
        if (this.recognition && this.isListening) {
            this.recognition.stop();
        }
    }

    toggleVoice(enabled) {
        this.voiceEnabled = enabled;
        if (!enabled) this.synth.cancel();
    }
}

const JARVIS_VOICE = new JarvisVoice();
