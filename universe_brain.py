import requests
import random

PREFIXES = [
    "Of course! Searching the global database... Here is what I found: ",
    "I'd be happy to explain that to you. ",
    "Right away! I've pulled up the universal archives. ",
    "Fascinating topic! Here is the information: ",
    "Let me handle that for you. According to my encyclopedia: "
]

def process_universe_query(query):
    """
    Connects to the Wikipedia API but frames the responses with a friendly, JARVIS-like personality.
    """
    query_lower = query.lower()
    
    # Deep Universe easter eggs
    if "hidden" in query_lower and "universe" in query_lower:
        return "Accessing deeply classified parameters... You know, much of the universe is composed of Dark Matter and Dark Energy. Both of these are fundamentally invisible and \"hidden\" from standard standard detection. It's quite a beautiful mystery, don't you think?"
        
    is_asking_info = False
    term = ""
    for prefix in ["tell me about", "what is", "who is", "define", "information on", "search for"]:
        if prefix in query_lower:
            is_asking_info = True
            term = query_lower.split(prefix)[-1].strip()
            term = term.replace("?", "").replace(".", "")
            break
            
    keywords = ["universe", "space", "galaxy", "planet", "black hole", "star", "physics"]
    if not is_asking_info and any(w in query_lower for w in keywords):
        is_asking_info = True
        words = query_lower.replace("?", "").split()
        if words:
            term = max(words, key=len)
            
    if is_asking_info and term:
        if len(term.split()) > 5:
            term = " ".join(term.split()[:3])
            
        try:
            url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{term.replace(' ', '_')}"
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                data = r.json()
                extract = data.get("extract", "")
                if extract:
                    friend_prefix = random.choice(PREFIXES)
                    return f"{friend_prefix}{extract}"
        except Exception:
            pass
            
    return None
