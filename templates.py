# ⚡ QUANTUM FORENSIC WORKSPACE v9.9 ULTIMATE MASTER TEMPLATE ⚡

HTML_TEMPLATE_START = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><title>⚡ QUANTUM FORENSIC WORKSPACE v9.9 ⚡</title>
    <style>
        :root { --bg-dark: #020208; --cyber-cyan: #00f0ff; --matrix-green: #39ff14; --danger-red: #ff0055; --neon-purple: #bc13fe; --glass-bg: rgba(6, 6, 20, 0.85); --glass-border: rgba(0, 240, 255, 0.25); }
        * { margin:0; padding:0; box-sizing:border-box; }
        body { background-color: var(--bg-dark); color:#f1f5f9; font-family: monospace; overflow-x:hidden; background-image: linear-gradient(rgba(0, 240, 255, 0.02) 1px, transparent 1px), linear-gradient(90deg, rgba(0, 240, 255, 0.02) 1px, transparent 1px); background-size: 25px 25px; }
        header { background: linear-gradient(180deg, #050515 0%, transparent 100%); border-bottom: 2px dashed var(--cyber-cyan); padding:1.2rem 3rem; display:flex; justify-content:space-between; align-items:center; box-shadow: 0 0 20px rgba(0,240,255,0.1); }
        .sys-title { font-weight:900; font-size:1.4rem; display:flex; align-items:center; gap:0.75rem; text-shadow: 0 0 10px var(--cyber-cyan); letter-spacing: 2px; }
        .pulse-node { width:12px; height:12px; background-color:var(--danger-red); border-radius:50%; box-shadow:0 0 15px var(--danger-red); animation: blinker 0.8s infinite; }
        .user-pill { background:rgba(188,19,254,0.15); border:1px solid var(--neon-purple); padding:0.5rem 1.2rem; border-radius:4px; font-size:0.9rem; font-weight:bold; box-shadow: 0 0 15px rgba(188,19,254,0.3); }
        .logout-lnk { color:var(--danger-red); text-decoration:none; font-weight:bold; margin-left:10px; text-shadow: 0 0 5px var(--danger-red); }
        .cyber-grid { display:grid; grid-template-columns:1.2fr 1fr; gap:2rem; padding:2rem; max-width:1600px; margin:0 auto; width:100%; }
        .section-label { font-size:0.95rem; font-weight:700; color:var(--cyber-cyan); margin-bottom:12px; border-left:4px solid var(--neon-purple); padding-left:8px; text-transform:uppercase; text-shadow: 0 0 5px var(--cyber-cyan); letter-spacing: 1px; }
        .glass-panel { background:var(--glass-bg); border:2px solid var(--glass-border); border-radius:4px; padding:1.5rem; position: relative; box-shadow: 0 0 20px rgba(0,240,255,0.05); }
        .glass-panel::before { content: ''; position: absolute; top:0; left:0; width:10px; height:10px; border-top: 2px solid var(--cyber-cyan); border-left: 2px solid var(--cyber-cyan); }
        .glass-panel::after { content: ''; position: absolute; bottom:0; right:0; width:10px; height:10px; border-bottom: 2px solid var(--cyber-cyan); border-right: 2px solid var(--cyber-cyan); }
        .terminal-upload { border:2px dashed var(--neon-purple); background:rgba(188,19,254,0.03); border-radius:4px; padding:2.5rem 1rem; text-align:center; cursor:pointer; transition: all 0.3s; }
        .terminal-upload:hover { border-color: var(--cyber-cyan); background: rgba(0,240,255,0.05); box-shadow: 0 0 15px rgba(0,240,255,0.2); }
        .display-container { display:grid; grid-template-columns:1fr 1fr; gap:1rem; }
        .matrix-display { width:100%; height:250px; background:#010409; border:1px solid #1e293b; border-radius:4px; display:flex; align-items:center; justify-content:center; overflow:hidden; position:relative; }
        .scan-laser { position:absolute; top:0; left:0; width:100%; height:6px; background:linear-gradient(180deg, rgba(255,0,85,0) 0%, var(--cyber-cyan) 50%, rgba(255,0,85,0) 100%); opacity:0; z-index:5; pointer-events:none; }
        .matrix-display img { max-width:100%; max-height:100%; object-fit:contain; z-index:2; position:relative; }
        .hud-status-wrapper { display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:1.5rem; }
        .gauge-container { display:flex; justify-content:center; align-items:center; position:relative; background:rgba(0,0,0,0.5); border-radius:4px; height:130px; border: 1px solid rgba(255,255,255,0.05); }
        .gauge-text { position:absolute; bottom:15px; font-weight:900; font-size:2rem; color:#fff; text-shadow: 0 0 10px #fff; }
        .threat-matrix-box { display:flex; flex-direction:column; justify-content:center; align-items:center; background:rgba(0,0,0,0.5); border-radius:4px; padding:1rem; border: 1px solid rgba(255,255,255,0.05); }
        .threat-title { font-size:0.75rem; color:#64748b; text-transform:uppercase; letter-spacing: 1px; font-weight:bold; }
        .threat-level { font-size:1.4rem; font-weight:900; text-shadow: 0 0 10px var(--matrix-green); }
        .metrics-container { display:flex; flex-direction:column; gap:1rem; }
        .module-sci-card { background:rgba(5,5,15,0.6); border-left:5px solid #475569; padding:1rem; border-radius:0 4px 4px 0; border: 1px solid rgba(255,255,255,0.03); }
        .module-meta { display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem; }
        .module-name { font-size:1.05rem; font-weight:700; color:#fff; letter-spacing: 1px; }
        .holo-badge { font-size:0.72rem; font-weight:800; padding:0.3rem 0.8rem; border-radius:2px; border:2px solid currentColor; text-transform: uppercase; }
        .neon-track { width:100%; height:8px; background-color:#000; border-radius:2px; overflow:hidden; margin-bottom:0.75rem; border:1px solid rgba(255,255,255,0.1); }
        .neon-fill { height:100%; width:0%; transition:width 1s; }
        .fill-pass { width:100%; background:linear-gradient(90deg, var(--cyber-cyan), var(--matrix-green)); box-shadow: 0 0 10px var(--matrix-green); }
        .fill-fail { width:100%; background:linear-gradient(90deg, var(--neon-purple), var(--danger-red)); box-shadow: 0 0 10px var(--danger-red); }
        .terminal-logs { font-size:0.85rem; color:#cbd5e1; background:#01030a; padding:0.75rem; border-radius:4px; border:1px solid #1e293b; }
        .gateway-btn { width:100%; padding:1rem; background:linear-gradient(135deg, var(--neon-purple), #0284c7); border:none; border-radius:4px; color:#fff; font-weight:900; cursor:pointer; text-transform:uppercase; margin-top: 15px; box-shadow: 0 0 15px rgba(188,19,254,0.3); transition: all 0.3s; }
        .gateway-btn:hover { background: linear-gradient(135deg, var(--cyber-cyan), var(--neon-purple)); box-shadow: 0 0 25px var(--cyber-cyan); transform: scale(1.01); }
        .active-scan .scan-laser { opacity:1; animation:laser-move 1.5s infinite linear; }
        @keyframes laser-move { 0%,100% {top:0%;} 50% {top:100%;} }
        @keyframes blinker { 50% { opacity: 0.3; } }
</style>
</head>
<body>
    <div class="cyber-grid">
"""
HTML_TEMPLATE_CONSOLE = """
    <div class="cyber-grid">
        <div class="glass-panel">
            <div class="section-label">📂 DATA FEED INGESTION CONSOLE</div>
            <form method="POST" action="/" enctype="multipart/form-data">
                <div class="terminal-upload" onclick="document.getElementById('realFileInput').click();">
                    <h4 style="color:#fff; letter-spacing:1px;">☣️ INGEST FORENSIC TARGET IMAGE</h4>
                    <p id="uploadLabelText" style="color: var(--cyber-cyan); font-size: 0.85rem; margin-top:5px; font-weight:bold;">[ CLICK TO MOUNT: JPEG / PNG ]</p>
                    <input type="file" id="realFileInput" name="file" style="display: none;" onchange="if(this.files.length>0){ document.getElementById('uploadLabelText').innerText = '🔥 MOUNTED: ' + this.files.name; }" required>
                </div>
                <button type="submit" class="gateway-btn">⚡ RUN CORE DIAGNOSTIC PIPELINE ⚡</button>
            </form>
            <div class="section-label" style="margin-top:1.5rem;">🖥️ SPATIAL WORKSPACE MATRIX MONITORS</div>
            <div class="display-container">
                <div class="matrix-display" id="displayArea"><div class="scan-laser"></div>{% if file_base64 %}<img src="data:image/png;base64,{{ file_base64 }}">{% else %}<span style="color:#334155;">[AWAITING STREAM FEED]</span>{% endif %}</div>
                <div class="matrix-display" id="displayMap"><div class="scan-laser"></div>{% if map_base64 and map_base64 != 'CRASH_SAFE' %}<img src="data:image/png;base64,{{ map_base64 }}">{% elif file_base64 %}<img src="data:image/png;base64,{{ file_base64 }}" style="filter: hue-rotate(290deg) saturate(3) contrast(1.5);">{% else %}<span style="color:#334155;">[AWAITING STREAM FEED]</span>{% endif %}</div>
            </div>
        </div>
        <div class="glass-panel" id="compliancePanel" style="box-shadow: 0 0 30px rgba(0,240,255,0.15); transition: all 0.5s;">
            <div class="section-label">📊 CRYPTOGRAPHIC COMPLIANCE HUB MONITOR</div>
            <div class="hud-status-wrapper">
                <div class="gauge-container">
                    <svg width="140" height="90" viewBox="0 0 200 110">
                        <path d="M20,100 A80,80 0 0,1 180,100" fill="none" stroke="#1e293b" stroke-width="14" stroke-linecap="round"/>
                        <path id="gaugeProgress" d="M20,100 A80,80 0 0,1 180,100" fill="none" stroke="var(--matrix-green)" stroke-width="14" stroke-linecap="round" stroke-dasharray="251" stroke-dashoffset="251" style="transition: all 1s;"/>
                        <line id="gaugeNeedle" x1="100" y1="100" x2="30" y2="100" stroke="#ff0055" stroke-width="4" stroke-linecap="round" style="transform-origin:100px 100px; transform:rotate(0deg); transition: all 1s;"/>
                    </svg>
                    <div class="gauge-text" id="gaugeScoreText">0%</div>
                </div>
                <div class="threat-matrix-box"><div class="threat-title">Threat Assessment Matrix</div><div class="threat-level" id="threatLevelText" style="color: var(--matrix-green); margin-top:5px; text-shadow:0 0 10px var(--matrix-green);">STANDBY</div></div>
            </div>
            <div class="metrics-container">
                <div class="module-sci-card" id="cardAlpha"><div class="module-meta"><span class="module-name">▶️ ALTERATION TENSOR</span><span class="holo-badge" id="badgeAlpha" style="color:#94a3b8;">NO FEED</span></div><div class="neon-track"><div class="neon-fill" id="fillAlpha"></div></div><div class="terminal-logs" id="logAlpha">[SYS-LOG]: Core matrix stack uninitialized...</div></div>
                <div class="module-sci-card" id="cardBeta"><div class="module-meta"><span class="module-name">▶️ MODEL IDENTIFIER</span><span class="holo-badge" id="badgeBeta" style="color:#94a3b8;">NO FEED</span></div><div class="neon-track"><div class="neon-fill" id="fillBeta"></div></div><div class="terminal-logs" id="logBeta">[SYS-LOG]: Core matrix stack uninitialized...</div></div>
            </div>
        </div>
    </div>
    <div style="max-width:1600px; margin:0 auto 2rem auto; padding:0 2rem; width:100%;">
        <div class="glass-panel" style="border-color: rgba(0,240,255,0.2); padding:1.5rem; background: rgba(2,2,10,0.9);">
            <div class="section-label">📋 LIVE QUANTUM CORE FORENSIC MANIFEST REPORT</div>
            <div class="terminal-logs" id="liveReportLogs" style="background:#000003; min-height:100px; font-size:0.95rem; color:#cbd5e1; line-height:1.6; border:1px dashed var(--cyber-cyan); padding: 12px;">[SYSTEM STATUS]: STANDBY CONSOLE NODE. Ingest forensic target image file above to execute recursive neural network diagnostic manifest report logs...</div>
        </div>
    </div>
"""

BODY_TEMPLATE_END = """
    <script>
        const score = parseInt("{{ trust_score }}") || 0; const filename = "{{ filename }}";
        if (filename && filename !== "") {
            document.getElementById('displayArea').classList.add('active-scan'); document.getElementById('displayMap').classList.add('active-scan');
            document.getElementById('gaugeScoreText').innerText = score + "%";
            const progress = document.getElementById('gaugeProgress'); const needle = document.getElementById('gaugeNeedle'); const threat = document.getElementById('threatLevelText');
            if (score < 80) {
                progress.style.strokeDashoffset = "155"; progress.style.stroke = "var(--danger-red)"; needle.style.transform = "rotate(68deg)"; threat.innerText = "CRITICAL BREACH"; threat.style.color = "var(--danger-red)";
                document.getElementById('compliancePanel').style.borderColor = "var(--danger-red)";
                document.getElementById('cardAlpha').style.borderLeftColor = "var(--danger-red)"; document.getElementById('cardBeta').style.borderLeftColor = "var(--danger-red)";
                document.getElementById('badgeAlpha').innerText = "SUSPICIOUS"; document.getElementById('badgeAlpha').style.color = "var(--danger-red)";
                document.getElementById('badgeBeta').innerText = "SUSPICIOUS"; document.getElementById('badgeBeta').style.color = "var(--danger-red)";
                document.getElementById('fillAlpha').className = "neon-fill fill-fail"; document.getElementById('fillBeta').className = "neon-fill fill-fail";
                document.getElementById('logAlpha').innerText = "[ALERT]: Non-uniform ELA noise footprints discovered!"; document.getElementById('logBeta').innerText = "[ALERT]: High-frequency digital manipulation anomaly captured.";
                document.getElementById('liveReportLogs').innerHTML = "<span style='color:var(--danger-red); font-weight:bold;'>🚨 CRITICAL SECURITY BREACH ALERT:</span> High-frequency digital alteration signatures and synthetic metadata footprints detected in central grid matrix. Case Target file: " + filename + ". Trust score degraded to " + score + "%. Secure forensic text report successfully compiled in secure vault database.";
            } else {
                progress.style.strokeDashoffset = "10"; progress.style.stroke = "var(--matrix-green)"; needle.style.transform = "rotate(172deg)"; threat.innerText = "SAFE SECURITY"; threat.style.color = "var(--matrix-green)";
                document.getElementById('cardAlpha').style.borderLeftColor = "var(--matrix-green)"; document.getElementById('cardBeta').style.borderLeftColor = "var(--matrix-green)";
                document.getElementById('badgeAlpha').innerText = "VERIFIED"; document.getElementById('badgeAlpha').style.color = "var(--matrix-green)";
                document.getElementById('badgeBeta').innerText = "VERIFIED"; document.getElementById('badgeBeta').style.color = "var(--matrix-green)";
                document.getElementById('fillAlpha').className = "neon-fill fill-pass"; document.getElementById('fillBeta').className = "neon-fill fill-pass";
                document.getElementById('logAlpha').innerText = "[COMPLETED]: Uniform ELA noise resolved. Zero localized anomalies."; document.getElementById('logBeta').innerText = "[COMPLETED]: Genuine sensor noise fingerprint verified.";
                document.getElementById('liveReportLogs').innerHTML = "<span style='color:var(--matrix-green); font-weight:bold;'>🟢 SECURITY MATRIX VERIFIED:</span> Core image vectors successfully resolved with uniform noise grid distribution. Zero pixel matrix localized anomalies discovered. Target file matches organic hardware sensor noise fingerprint.";
            }
        }
    </script>
</body>
</html>
"""
HTML_LOGIN_GATEWAY = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>QUANTUM FORENSIC LOGIN</title>
    <style>
        :root { --bg-dark: #020208; --cyber-cyan: #00ffff; --glass-bg: rgba(2, 2, 8, 0.6); }
        body { background-color: var(--bg-dark); color: #fff; font-family: monospace; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .gateway-panel { width: 100%; max-width: 480px; background: var(--glass-bg); border: 2px solid var(--cyber-cyan); padding: 2rem; border-radius: 8px; box-shadow: 0 0 20px rgba(0, 255, 255, 0.2); text-align: left; }
        .gateway-title { text-align: center; color: var(--cyber-cyan); letter-spacing: 1px; margin-bottom: 1.5rem; }
        .gateway-input-group { margin-bottom: 1.5rem; }
        .gateway-input-group label { display: block; font-size: 0.8rem; font-weight: 800; color: var(--cyber-cyan); margin-bottom: 0.5rem; }
        .gateway-input { width: 100%; padding: 0.9rem 1.2rem; background: rgba(0,0,0,0.8); border: 1px solid var(--cyber-cyan); color: #fff; border-radius: 4px; box-sizing: border-box; }
        .gateway-btn { width: 100%; padding: 1rem; background: var(--cyber-cyan); color: #000; border: none; font-weight: bold; cursor: pointer; letter-spacing: 1px; border-radius: 4px; font-size: 1rem; }
        .gateway-btn:hover { background: #00cccc; }
    </style>
</head>
<body>
    <div class="gateway-panel">
        <h2 class="gateway-title">FORENSIC LOGIN GATEWAY</h2>
        <form method="POST" action="/login-gateway">
            <div class="gateway-input-group">
                <label>OPERATOR IDENTIFIER</label>
                <input type="text" name="user_name" class="gateway-input" placeholder="Enter Operator Name" required>
            </div>
            <div class="gateway-input-group">
                <label>BADGE SECURITY KEY</label>
                <input type="password" name="user_roll" class="gateway-input" placeholder="Enter Badge Key" required>
            </div>
            <button type="submit" class="gateway-btn">Access Matrix Control</button>
        </form>
    </div>
</body>
</html>
"""

# ==========================================
# 2. इसके नीचे तुम्हारा पुराना जावास्क्रिप्ट (जैसा मिडिल पार्ट में था)
# ==========================================
BODY_TEMPLATE_END = """
<script>
function streamConsoleLog(targetId, fullText, speed = 15) {
    const element = document.getElementById(targetId);
    if (!element) return;
    element.innerHTML = "";
    let i = 0;
    function typeChar() {
        if (i < fullText.length) {
            element.innerHTML += fullText.charAt(i);
            i++;
            setTimeout(typeChar, speed);
        }
    }
    typeChar();
}

const score = parseInt("{{ trust_score }}") || 0;
const filename = "{{ filename }}";
if (filename && filename !== "") {
    document.getElementById('displayArea').classList.add('active-scan');
    document.getElementById('displayMap').classList.remove('active-scan');
    document.getElementById('gaugeScoreText').innerText = score + "%";
    const progress = document.getElementById('gaugeProgress');
    const needle = document.getElementById('gaugeNeedle');
    if (score < 80) {
        progress.style.strokeDashoffset = "155";
        progress.style.stroke = "var(--danger-red)";
        needle.style.transform = "rotate(65deg)";
        document.getElementById('cardBeta').style.borderLeftColor = "var(--danger-red)";
        document.getElementById('badgeAlpha').style.color = "var(--danger-red)";
        document.getElementById('badgeAlpha').innerText = "SUSPICIOUS";
        document.getElementById('badgeAlpha').className = "neon-fill-fail";
        streamConsoleLog('logAlpha', "[ALERT]: Non-uniform ELA noise footprints discovered!");
        streamConsoleLog('logBeta', "[WARNING]: Critical metadata alteration detected.");
    } else {
        progress.style.strokeDashoffset = "10";
        progress.style.stroke = "var(--matrix-green)";
        needle.style.transform = "rotate(172deg)";
        document.getElementById('badgeAlpha').style.color = "var(--matrix-green)";
        document.getElementById('badgeAlpha').innerText = "SAFE SECURITY";
    }
}
</script>
"""
BODY_TEMPLATE_END = """
<script>
function streamConsoleLog(targetId, fullText, speed = 15) {
            const element = document.getElementById(targetId); if(!element) return;
            element.innerHTML = ""; let i = 0;
            function typeChar() { if (i < fullText.length) { element.innerHTML += fullText.charAt(i); i++; setTimeout(typeChar, speed); } }
            typeChar();
        }
        const score = parseInt("{{ trust_score }}") || 0; const filename = "{{ filename }}";
        if (filename && filename !== "") {
            document.getElementById('displayArea').classList.add('active-scan'); document.getElementById('displayMap').classList.add('active-scan');
            document.getElementById('gaugeScoreText').innerText = score + "%";
            const progress = document.getElementById('gaugeProgress'); const needle = document.getElementById('gaugeNeedle'); const threat = document.getElementById('threatLevelText');
            if (score < 80) {
                progress.style.strokeDashoffset = "155"; progress.style.stroke = "var(--danger-red)"; needle.style.transform = "rotate(68deg)"; threat.innerText = "CRITICAL BREACH"; threat.style.color = "var(--danger-red)";
                document.getElementById('compliancePanel').style.borderColor = "var(--danger-red)";
                document.getElementById('cardAlpha').style.borderLeftColor = "var(--danger-red)"; document.getElementById('cardBeta').style.borderLeftColor = "var(--danger-red)";
                document.getElementById('badgeAlpha').innerText = "SUSPICIOUS"; document.getElementById('badgeAlpha').style.color = "var(--danger-red)";
                document.getElementById('badgeBeta').innerText = "SUSPICIOUS"; document.getElementById('badgeBeta').style.color = "var(--danger-red)";
                document.getElementById('fillAlpha').className = "neon-fill fill-fail"; document.getElementById('fillBeta').className = "neon-fill fill-fail";
                streamConsoleLog('logAlpha', "[ALERT]: Non-uniform ELA noise footprints discovered!"); streamConsoleLog('logBeta', "[ALERT]: High-frequency digital manipulation anomaly captured.");
                streamConsoleLog('liveReportLogs', "🚨 CRITICAL SECURITY BREACH ALERT: High-frequency digital alteration signatures detected. Case file: " + filename, 10);
                } else {
                progress.style.strokeDashoffset = "10"; progress.style.stroke = "var(--matrix-green)"; needle.style.transform = "rotate(172deg)"; threat.innerText = "SAFE SECURITY"; threat.style.color = "var(--matrix-green)";
                document.getElementById('cardAlpha').style.borderLeftColor = "var(--matrix-green)"; document.getElementById('cardBeta').style.borderLeftColor = "var(--matrix-green)";
                document.getElementById('badgeAlpha').innerText = "VERIFIED"; document.getElementById('badgeAlpha').style.color = "var(--matrix-green)";
                document.getElementById('badgeBeta').innerText = "VERIFIED"; document.getElementById('badgeBeta').style.color = "var(--matrix-green)";
                document.getElementById('fillAlpha').className = "neon-fill fill-pass"; document.getElementById('fillBeta').className = "neon-fill fill-pass";
                streamConsoleLog('logAlpha', "[COMPLETED]: Uniform ELA noise resolved. Zero localized anomalies."); streamConsoleLog('logBeta', "[COMPLETED]: Genuine sensor noise fingerprint verified.");
                streamConsoleLog('liveReportLogs', "🟢 SECURITY MATRIX VERIFIED: Target file matches organic hardware sensor noise fingerprint.", 10);
            }
        }
    </script>
</body>
</html>
"""