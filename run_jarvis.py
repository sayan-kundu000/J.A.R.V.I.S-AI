import subprocess
import os
import sys

def main():
    print("--- JARVIS OS BOOT LOADER ---")
    
    # Path to the virtual environment python
    venv_python = os.path.join("venv", "Scripts", "python.exe")
    
    if not os.path.exists(venv_python):
        print("[!] Warning: Virtual environment not found at ./venv/Scripts/python.exe")
        venv_python = "python"
    
    print(f"[*] Booting JARVIS systems using: {venv_python}")
    
    try:
        # 1. Start the Flask server in the background
        server_process = subprocess.Popen(
            [venv_python, "-u", "app.py"],
            stdout=sys.stdout,
            stderr=sys.stderr,
            universal_newlines=True
        )
        
        # 2. Wait for the server to initialize
        print("[*] Waiting for core logic to stabilize...")
        import time
        time.sleep(3)
        
        # 3. Launch Chrome in App Mode
        url = "http://127.0.0.1:5000"
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        chrome_path_x86 = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        
        launched = False
        if os.path.exists(chrome_path):
            print(f"[*] Launching JARVIS Interface in Chrome App Mode...")
            subprocess.Popen([chrome_path, f"--app={url}"])
            launched = True
        elif os.path.exists(chrome_path_x86):
            print(f"[*] Launching JARVIS Interface in Chrome App Mode (x86)...")
            subprocess.Popen([chrome_path_x86, f"--app={url}"])
            launched = True
        
        if not launched:
            print("[!] Chrome not found at standard paths. Falling back to default browser.")
            import webbrowser
            webbrowser.open(url)
            
        print("[OK] JARVIS is now online and active.")
        
        # 4. Wait for the server to exit
        server_process.wait()
        
    except KeyboardInterrupt:
        print("\n[*] JARVIS OS: Powering down...")
        if 'server_process' in locals():
            server_process.terminate()
    except Exception as e:
        print(f"[!] Critical Error during boot: {e}")

if __name__ == "__main__":
    main()
