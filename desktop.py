import os
import threading
import time
import subprocess
from app import app

def start_server():
    """
    Spawns the JARVIS Flask API server in the background 
    on 127.0.0.1 (local interface) to act as the internal logic brain.
    """
    # use_reloader=False is critically required for threading
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)

if __name__ == '__main__':
    print("Booting JARVIS Core Neural Networks...")
    
    # 1. Start backend OS Brain in a separate background daemon thread
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()
    
    # Allow the core logic 1.5 seconds to fully initialize the Flask ports
    time.sleep(1.5)
    
    # 2. Render the Frontend inside a native Windows Desktop GUI
    # We utilize Native Chromium App Mode to bypass webview compilation gridlocks.
    # This renders a completely frameless, native-looking desktop executable window.
    url = "http://127.0.0.1:5000/"
    
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    ]
    
    launched = False
    for path in chrome_paths:
        if os.path.exists(path):
            print(f"Injecting into native UI container using {path}")
            subprocess.Popen([path, f"--app={url}"])
            launched = True
            break
            
    # Fallback to standard web browser if App-Mode targets fail
    if not launched:
        print("Fallback: Launching via default protocol.")
        import webbrowser
        webbrowser.open(url)
        
    print("JARVIS is now online and active on your Desktop.")
    
    # Keep main thread alive so the python script doesn't exit immediately 
    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        print("Shutting down JARVIS.")
