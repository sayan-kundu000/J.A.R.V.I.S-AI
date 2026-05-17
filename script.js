// Global Chart.js defaults for JARVIS theme
Chart.defaults.color = '#dfedf5';
Chart.defaults.font.family = 'Outfit';

async function fetchStats() {
    // Quantum Simulation
    fetch('http://10.44.193.18:5000/api/quantum').then(r=>r.json()).then(data => {
        if(data.status === 'SUCCESS'){
            document.getElementById('q-status').innerText = `Active (Qubits: ${data.qubits_used})`;
            document.getElementById('q-output').innerText = ` |${data.bitstring_measured}> = ${data.integer_value}`;
        }
    }).catch(e => console.log("Quantum API not ready yet"));

    // System Stats
    fetch('http://10.44.193.18:5000/api/system').then(r=>r.json()).then(data => {
        document.getElementById('sys-os').innerText = data.info.os;
        document.getElementById('sys-cpu').innerText = data.cpu + '%';
        document.getElementById('sys-mem').innerText = data.memory.percent + '% (' + data.memory.used_gb + 'GB)';
        document.getElementById('sys-bat').innerText = data.battery.percent + '% (' + data.battery.status + ')';
        document.getElementById('sys-temp').innerText = data.temperature_c + '°C';
    }).catch(e => console.log(e));

    // Sports Live
    fetch('http://10.44.193.18:5000/api/events/sports').then(r=>r.json()).then(data => {
        const container = document.getElementById('sports-container');
        container.innerHTML = `
            <div class="sports-card">
                <strong>🏏 ${data.cricket.match} <span class="highlight">(${data.cricket.status})</span></strong><br>
                Score: ${data.cricket.score}<br>
                <small>${data.cricket.details}</small>
            </div>
            <div class="sports-card">
                <strong>⚽ ${data.football.match} <span class="highlight">(${data.football.status})</span></strong><br>
                Score: ${data.football.score}<br>
                <small>${data.football.details}</small>
            </div>
        `;
    }).catch(e => console.log(e));

    // Init all visual charts
    initWeatherChart();
    initStocksChart();
    initGoldChart();
    initMovieChart();
    initCountryCharts();
}

async function initWeatherChart() {
    try {
        const res = await fetch('http://10.44.193.18:5000/api/events/weather').then(r=>r.json());
        if(res.error) return;

        // Ensure we only take up to 15 days for the UI
        const labels = res.days.map(d => d.substring(5, 10)); // Just month-day
        const maxT = res.max_temps;
        const minT = res.min_temps;
        const humidity = res.humidity;
        const precip = res.precipitation;

        const ctx = document.getElementById('weatherChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Max Temp (°C)',
                        data: maxT,
                        borderColor: '#ff3366',
                        backgroundColor: 'rgba(255, 51, 102, 0.1)',
                        tension: 0.3,
                        yAxisID: 'y'
                    },
                    {
                        label: 'Min Temp (°C)',
                        data: minT,
                        borderColor: '#00f3ff',
                        backgroundColor: 'rgba(0, 243, 255, 0.1)',
                        tension: 0.3,
                        yAxisID: 'y'
                    },
                    {
                        label: 'Humidity (%)',
                        data: humidity,
                        type: 'bar',
                        backgroundColor: 'rgba(138, 43, 226, 0.4)',
                        yAxisID: 'y1'
                    },
                    {
                        label: 'Precip (mm)',
                        data: precip,
                        type: 'bar',
                        backgroundColor: 'rgba(50, 205, 50, 0.5)',
                        yAxisID: 'y1'
                    }
                ]
            },
            options: { 
                responsive: true, 
                maintainAspectRatio: false,
                scales: {
                    y: { type: 'linear', position: 'left', title: {display:true, text:'Temp °C'} },
                    y1: { type: 'linear', position: 'right', title: {display:true, text:'% / mm'}, grid: {drawOnChartArea: false} }
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            afterLabel: function(context) {
                                // Add weather condition text to tooltip
                                const index = context.dataIndex;
                                return 'Condition: ' + res.conditions[index];
                            }
                        }
                    }
                }
            }
        });
    } catch(e) { console.error(e); }
}

async function initStocksChart() {
    try {
        const res = await fetch('http://10.44.193.18:5000/api/finance/stocks').then(r=>r.json());
        const labels = Object.keys(res);
        const selling = labels.map(k => res[k].selling_price);
        const predicted = labels.map(k => res[k].predicted_5yr);

        const ctx = document.getElementById('stocksChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Current Selling Price ($)',
                        data: selling,
                        backgroundColor: '#0066ff'
                    },
                    {
                        label: 'Predicted 5-Yr Price ($) via Regression',
                        data: predicted,
                        backgroundColor: '#00f3ff'
                    }
                ]
            },
            options: { responsive: true, maintainAspectRatio: false }
        });
    } catch(e) {}
}

async function initGoldChart() {
    try {
        const res = await fetch('http://10.44.193.18:5000/api/finance/gold').then(r=>r.json());
        
        const combined = [...res.increasing, ...res.decreasing].slice(0, 15);
        const labels = combined.map(i => i.state);
        const rates = combined.map(i => i.rate);
        const changes = combined.map(i => i.change);
        
        const ctx = document.getElementById('goldChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Gold Rate 24k (INR / gm)',
                    data: rates,
                    borderColor: '#ffd700',
                    backgroundColor: 'rgba(255, 215, 0, 0.1)',
                    fill: true,
                    yAxisID: 'y'
                }, {
                    label: 'Market Trend Change',
                    data: changes,
                    type: 'bar',
                    backgroundColor: changes.map(c => c > 0 ? '#00f3ff' : '#ff3366'),
                    yAxisID: 'y1'
                }]
            },
            options: { 
                responsive: true, 
                maintainAspectRatio: false,
                scales: {
                    y: { type: 'linear', position: 'left' },
                    y1: { type: 'linear', position: 'right', grid: {drawOnChartArea: false} }
                }
            }
        });
    } catch(e) {}
}

async function initMovieChart() {
    try {
        const res = await fetch('http://10.44.193.18:5000/api/events/boxoffice').then(r=>r.json());
        const labels = res.map(m => m.name);
        const globalGross = res.map(m => m.worldwide_millions);
        const indiaGross = res.map(m => m.india_millions);

        const ctx = document.getElementById('movieChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Worldwide Collection (Millions $)',
                        data: globalGross,
                        backgroundColor: '#8a2be2'
                    },
                    {
                        label: 'India Collection (Millions $)',
                        data: indiaGross,
                        backgroundColor: '#ff1493'
                    }
                ]
            },
            options: { responsive: true, maintainAspectRatio: false }
        });
    } catch(e) {}
}

async function initCountryCharts() {
    try {
        const res = await fetch('http://10.44.193.18:5000/api/country/ranks').then(r=>r.json());
        
        const labels = res.map(c => c.country);
        const gdp = res.map(c => c.gdp_billions);
        const pop = res.map(c => c.population_millions);
        const aqi = res.map(c => c.pollution_aqi);

        // Chart 1: GDP vs Pop
        const ctxGdp = document.getElementById('countryGdpPopChart').getContext('2d');
        new Chart(ctxGdp, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'GDP (Billions $)',
                        data: gdp,
                        backgroundColor: '#00f3ff',
                        yAxisID: 'y'
                    },
                    {
                        label: 'Population (Millions)',
                        data: pop,
                        type: 'line',
                        borderColor: '#ff1493',
                        backgroundColor: '#ff1493',
                        yAxisID: 'y1'
                    }
                ]
            },
            options: { 
                responsive: true, 
                maintainAspectRatio: false,
                scales: {
                    y: { type: 'linear', position: 'left', title: {display: true, text: 'GDP ($Bn)'} },
                    y1: { type: 'linear', position: 'right', title: {display: true, text: 'Pop (Mils)'}, grid: {drawOnChartArea: false} }
                }
            }
        });

        // Chart 2: AQI
        const ctxAqi = document.getElementById('countryPollutionChart').getContext('2d');
        new Chart(ctxAqi, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Pollution Index (AQI)',
                    data: aqi,
                    borderColor: '#ffd700',
                    backgroundColor: 'rgba(255, 215, 0, 0.2)',
                    fill: true,
                    tension: 0.3
                }]
            },
            options: { responsive: true, maintainAspectRatio: false }
        });

    } catch(e) {}
}

function setupNavigation() {
    const btn1 = document.getElementById('btn-panel1');
    const btn2 = document.getElementById('btn-panel2');
    const p1 = document.getElementById('panel-1');
    const p2 = document.getElementById('panel-2');

    btn1.addEventListener('click', () => {
        btn1.classList.add('active');
        btn2.classList.remove('active');
        p1.classList.add('active-panel');
        p2.classList.remove('active-panel');
    });

    btn2.addEventListener('click', () => {
        btn2.classList.add('active');
        btn1.classList.remove('active');
        p2.classList.add('active-panel');
        p1.classList.remove('active-panel');
    });
}

// Start visualizations
window.onload = () => {
    setupNavigation();
    fetchStats();
    
    // Poll fast-changing values every 10 seconds
    setInterval(() => {
        fetch('http://10.44.193.18:5000/api/system').then(r=>r.json()).then(data => {
            document.getElementById('sys-cpu').innerText = data.cpu + '%';
            document.getElementById('sys-mem').innerText = data.memory.percent + '% (' + data.memory.used_gb + 'GB)';
        });
        fetch('http://10.44.193.18:5000/api/quantum').then(r=>r.json()).then(data => {
            if(data.status === 'SUCCESS'){
                document.getElementById('q-output').innerText = ` |${data.bitstring_measured}> = ${data.integer_value}`;
            }
        });
    }, 10000);
    
    // Setup Chat Handlers
    document.getElementById('chat-send').addEventListener('click', sendChat);
    document.getElementById('chat-input').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') sendChat();
    });
};

async function sendChat() {
    const input = document.getElementById('chat-input');
    const msg = input.value.trim();
    if (!msg) return;
    
    appendMessage(msg, 'user');
    input.value = '';
    
    try {
        const response = await fetch('http://10.44.193.18:5000/api/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({message: msg})
        });
        const data = await response.json();
        // Delay slightly for dramatic text effect
        setTimeout(() => {
            appendMessage(data.response, 'jarvis');
            speakText(data.response);
        }, 400);
    } catch(e) {
        appendMessage("Error communicating with JARVIS cores.", 'jarvis');
        speakText("Error communicating with JARVIS cores.");
    }
}

function speakText(htmlString) {
    if (!('speechSynthesis' in window)) return;
    
    // Strip out any HTML elements (like iframes or images) before speaking!
    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = htmlString;
    const cleanText = tempDiv.textContent || tempDiv.innerText || "";
    
    // Stop any currently playing speech to prevent overlap
    window.speechSynthesis.cancel();
    
    const utterance = new SpeechSynthesisUtterance(cleanText);
    const voices = window.speechSynthesis.getVoices();
    // Try to find a nice British or clean English voice
    const jarvisVoice = voices.find(v => v.name.includes('Great Britain') || v.lang === 'en-GB' || v.name.includes('Google UK English Male'));
    
    if (jarvisVoice) {
        utterance.voice = jarvisVoice;
    }
    
    utterance.pitch = 0.9; // Smooth deep tone
    utterance.rate = 1.0;
    
    window.speechSynthesis.speak(utterance);
}

function appendMessage(text, sender) {
    const box = document.getElementById('chat-box');
    const div = document.createElement('div');
    div.className = 'message ' + sender;
    div.innerHTML = text; // Uses innerHTML to render iframe / images safely for this demo!
    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
}
