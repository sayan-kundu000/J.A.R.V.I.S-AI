import os
import shutil
import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def build_mobile_bundle():
    print("Generating JARVIS Mobile App Bundle for Android...")
    
    ip_addr = get_local_ip()
    target_dir = "jarvis_mobile_dist"
    
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.makedirs(target_dir)
    
    # 1. Copy and patch index.html
    with open("templates/index.html", "r", encoding="utf-8") as f:
        html = f.read()
        
    # Remove Jinja syntax for a standalone Android Webview
    html = html.replace("{{ url_for('static', filename='style.css') }}", "style.css")
    html = html.replace("{{ url_for('static', filename='script.js') }}", "script.js")
    
    with open(f"{target_dir}/index.html", "w", encoding="utf-8") as f:
        f.write(html)
        
    # 2. Copy and patch style.css
    shutil.copy("static/style.css", f"{target_dir}/style.css")
    
    # 3. Copy and patch script.js
    with open("static/script.js", "r", encoding="utf-8") as f:
        js = f.read()
        
    # Reroute fetch('/api/...') -> fetch('http://<PC_IP>:5000/api/...')
    # Use regex or simple string replacement
    # We will search for all fetch('/api
    js = js.replace("fetch('/api", f"fetch('http://{ip_addr}:5000/api")
    
    with open(f"{target_dir}/script.js", "w", encoding="utf-8") as f:
        f.write(js)
        
    print(f"[SUCCESS] Mobile bundle created inside ./{target_dir}")
    print(f"[SUCCESS] Android App logic will point to your JARVIS server at: http://{ip_addr}:5000")
    print("--------------------------------------------------")
    print("Next Steps for Android (Capacitor):")
    print(f"1. Run: npx cap init jarvis com.jarvis.os --web-dir {target_dir}")
    print(f"2. Run: npm install @capacitor/android")
    print(f"3. Run: npx cap add android")
    print(f"4. Run: npx cap open android")
    print("This will open Android Studio automatically to compile your phone APK.")

if __name__ == '__main__':
    build_mobile_bundle()
