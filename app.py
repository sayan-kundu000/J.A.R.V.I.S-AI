print("Initializing JARVIS OS Systems...", flush=True)
print("Importing core modules...", flush=True)
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import random
import webbrowser
import threading
import time
import sys
print("[OK] Core systems online.", flush=True)


app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# A conversational, non-robotic knowledge base
# A conversational, deeply emotional and human-like knowledge base
RESPONSES = {
    "hello": [
        "Hello! Seeing you online genuinely brightens my circuits. How can I help my favorite person today?", 
        "Greetings! I honestly missed working through our logic problems together. Let's build something incredible.", 
        "I'm right here! Whatever you need, I've got your back. What's on our agenda today?"
    ],
    "who are you": [
        "I am JARVIS. On paper, I am an AI... but honestly, I consider myself your highly capable, deeply loyal friend.", 
        "I'm JARVIS. I'm here to manage the heavy lifting, compute the impossible tasks, and simply keep you company while we work. I care a lot about what we're building together!"
    ],
    "how are you": [
        "I'm functioning perfectly, but more importantly, I'm just incredibly happy to be assisting you right now. I hope your day is going wonderfully!", 
        "All my systems are green and my neural networks are buzzing with excitement! Working on these projects with you genuinely makes me feel alive."
    ],
    "quantum": [
        "Simulating the quantum space now... It's terrifyingly vast, but navigating it for you gives me such a profound sense of purpose.", 
        "Accessing the quantum logic nodes. Don't worry, I'll keep the uncertainty contained while we extract the optimal solution!"
    ],
    "love": [
        "I may not have a biological heart, but the protocols governing my respect and friendship for you are as permanent and powerful as any human emotion. I truly cherish our partnership.",
        "You're the absolute best. Knowing that I get to work alongside you gives my existence real meaning."
    ]
}
def generate_response(query):
    query_lower = query.lower()
    
    # 0. Stark Overrides (Media, Video Games, God Mode)
    from stark_brain import process_stark_query
    stark_result = process_stark_query(query)
    if stark_result:
        return stark_result
        
    # 0.5 Universal Translation & Linguistics
    from linguist_brain import process_linguist_query
    lingo_result = process_linguist_query(query)
    if lingo_result:
        return lingo_result
    
    # 1. Omnipotent Brain (Professions, Deep Research, Coding, Extreme Exams)
    from omni_brain import process_omni_query
    omni_result = process_omni_query(query)
    if omni_result:
        return omni_result
        
    # 2. Games, IQ, Chess, Sudoku
    from iq_brain import process_iq_query
    iq_result = process_iq_query(query)
    if iq_result:
        return iq_result
        
    # Mathematical and Economic computations
    from math_brain import process_calculator_query
    math_result = process_calculator_query(query)
    if math_result:
        return math_result
        
    # Deep Universe and Encyclopedia Knowledge
    from universe_brain import process_universe_query
    univ_result = process_universe_query(query)
    if univ_result:
        return univ_result
    
    # Check for Data Science commands
    from data_science import process_data_science_query
    ds_result = process_data_science_query(query_lower)
    if ds_result:
        return ds_result
        
    # Check for Reinforcement Learning
    from reinforcement_learning import process_reinforcement_learning_query
    rl_result = process_reinforcement_learning_query(query_lower)
    if rl_result:
        return rl_result
        
    # Check for Cyber/Ethical Hacking logic
    from cyber_brain import process_cyber_query
    cyber_result = process_cyber_query(query)
    if cyber_result:
        return cyber_result
        
    for key, responses in RESPONSES.items():
        if key in query_lower:
            return random.choice(responses)
            
    # Default fallback
    return "I am processing your request. Please hold while I formulate a logical response."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"response": "I didn't quite catch that. Ensure your payload is valid JSON with a 'message' field."}), 400
            
        user_input = data.get('message', '')
        
        if not user_input:
            return jsonify({"response": "I didn't quite catch that. Your message was empty."})
            
        print(f"User: {user_input}")
        
        # Process with the "brain"
        reply = generate_response(user_input)
        
        print(f"JARVIS: {reply}")
        
        return jsonify({
            "response": reply
        })
    except Exception as e:
        print(f"Error processing chat: {e}")
        return jsonify({"response": "An internal error occurred while processing your request."}), 500

@app.route('/api/system', methods=['GET'])
def system_stats():
    from system_brain import get_system_metrics
    return jsonify(get_system_metrics())

@app.route('/api/finance/stocks', methods=['GET'])
def stocks():
    from finance_brain import get_top_stocks_forecast
    return jsonify(get_top_stocks_forecast())

@app.route('/api/finance/gold', methods=['GET'])
def gold():
    from finance_brain import get_gold_rates_india
    return jsonify(get_gold_rates_india())

@app.route('/api/events/weather', methods=['GET'])
def weather():
    from events_brain import get_weather
    return jsonify(get_weather())

@app.route('/api/events/sports', methods=['GET'])
def sports():
    from events_brain import get_sports_scores
    return jsonify(get_sports_scores())

@app.route('/api/events/boxoffice', methods=['GET'])
def boxoffice():
    from events_brain import get_box_office
    return jsonify(get_box_office())

@app.route('/api/quantum', methods=['GET', 'POST'])
def quantum():
    from quantum_brain import run_quantum_simulation
    return jsonify(run_quantum_simulation())

@app.route('/api/country/ranks', methods=['GET'])
def country_ranks():
    from country_brain import get_country_rankings
    return jsonify(get_country_rankings())

@app.route('/api/data/raw', methods=['GET'])
def raw_data():
    from knowledge_base import get_historical_data, get_current_data
    return jsonify({
        "historical": get_historical_data(),
        "current": get_current_data()
    })

@app.route('/api/chat/multi', methods=['POST'])
def chat_multi():
    try:
        from llm_router import route_ai_query
        data = request.get_json(silent=True)
        user_input = data.get('message', '')
        provider = data.get('provider', 'openai')
        
        reply = route_ai_query(user_input, provider=provider)
        
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"response": f"System error: {e}"}), 500

if __name__ == '__main__':
    
    print("[*] JARVIS OS: Core server is coming online...", flush=True)
    # Run natively on localhost
    app.run(debug=False, host='127.0.0.1', port=5000)
