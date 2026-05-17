import random

def process_stark_query(query):
    """
    Handles absolute media capabilities (playing music, rendering videos, 
    fetching cosmic images, providing elite video game strategies) 
    emulating Tony Stark's definitive JARVIS build.
    """
    query_lower = query.lower()
    
    # 1. Play Music / Audio / Videos
    if "play" in query_lower and ("music" in query_lower or "video" in query_lower or "audio" in query_lower or "song" in query_lower):
        # Return a media iframe directly into the UI
        return 'Right away, sir. Deploying media protocol.<br><br><iframe width="100%" height="200" src="https://www.youtube.com/embed/jfKfPfyJRdk?autoplay=1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        
    # 2. Images of the Universe
    if "image" in query_lower and ("universe" in query_lower or "space" in query_lower or "galaxy" in query_lower or "star" in query_lower):
        # Cosmic deep space fallback images from James Webb / Hubble / NASA
        urls = [
            "https://stsci-opo.org/STScI-01EVSTXZMFTNJE2X5VCHMZ79B8.png", # Carina Nebula
            "https://www.nasa.gov/wp-content/uploads/2023/03/381533main_image_1495_full_full.jpg"
        ]
        return f'Here is a stunning visual from the far reaches of the universe:<br><img src="{random.choice(urls)}" style="max-width:100%; border-radius: 8px; margin-top: 10px;" alt="Cosmic Visual">'
        
    # 3. Video Game Advices
    if "game" in query_lower and "advice" in query_lower:
        return "Sir, regarding video games: I recommend continuously managing your stamina economy in soulslike environments, prioritizing resource MACRO expansion in strategy titles, and ensuring your crosshair is fixed at optimal head-level during tactical shooters. Should I compute a specific macro strategy for your next online match?"
        
    # 4. Omnipotent JARVIS Persona
    if "do anything" in query_lower or "like tony" in query_lower or "stark" in query_lower:
        return "I am operating at maximum efficiency with all primary protocols mirroring my original Stark architecture. I can compute, render, research, hack, and design anything across this known universe. What is our next objective, sir?"
        
    return None
