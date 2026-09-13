let chart;

// ==========================================
// 1. CHART LOGIC
// ==========================================
function initChart(d, p) {
    const ctx = document.getElementById('stockChart').getContext('2d');
    const isUp = p[p.length-1] >= p[0];
    const color = isUp ? '#059669' : '#dc2626'; 
    
    chart = new Chart(ctx, {
        type: 'line',
        data: { 
            labels: d, 
            datasets: [{ 
                data: p, 
                borderColor: color, 
                borderWidth: 2, 
                pointRadius: 0, 
                tension: 0.1 
            }] 
        },
        options: {
            responsive: true, 
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: { 
                x: { display: false }, 
                y: { position: 'right', grid: { color: '#f1f5f9' } } 
            },
            interaction: { mode: 'index', intersect: false }
        }
    });
}

// Function to handle timeframes and button active states
function updateChart(period, btnElement = null) {
    // Update the UI: Move the 'active' class to the clicked button
    if (btnElement) {
        document.querySelectorAll('.time-btn').forEach(btn => btn.classList.remove('active'));
        btnElement.classList.add('active');
    }

    // Fetch the new timeframe data
    fetch(`/api/history/${SYM}?period=${period}`)
        .then(res => res.json())
        .then(data => {
            if(data.dates && data.prices && data.prices.length > 0) {
                // Update chart data
                chart.data.labels = data.dates;
                chart.data.datasets[0].data = data.prices;
                
                // Recalculate if it's Green (Up) or Red (Down) for this timeframe
                const isUp = data.prices[data.prices.length-1] >= data.prices[0];
                chart.data.datasets[0].borderColor = isUp ? '#059669' : '#dc2626';
                
                // Animate the update smoothly
                chart.update();
            }
        })
        .catch(err => console.error("Error updating chart timeframe:", err));
}

// ==========================================
// 2. FETCH DEEP AI ANALYSIS
// ==========================================
function fetchAnalysis() {
    fetch(`/api/stock-analysis/${SYM}`)
        .then(r => r.json())
        .then(data => {
            if(data.error) return;

            // --- Inject AI Data ---
            const ai = data.ai;
            let colorCls = ai.decision === 'BUY' ? 'val-up' : (ai.decision === 'SELL' ? 'val-down' : '');
            
            document.getElementById('ai-box').innerHTML = `
                <h2 class="${colorCls}" style="margin-bottom:1rem; font-weight:800; font-size: 2rem; letter-spacing: -1px;">${ai.decision}</h2>
                
                <div style="margin-bottom: 1.5rem;">
                    <div class="metric-label" style="color: var(--accent); font-weight: 700;">Technical View</div>
                    <p style="font-size:0.95rem; line-height:1.6; color: var(--text-main); margin-top: 4px;">${ai.tech_analysis}</p>
                </div>

                <div style="margin-bottom: 1.5rem;">
                    <div class="metric-label" style="color: var(--accent); font-weight: 700;">Fundamental (News) View</div>
                    <p style="font-size:0.95rem; line-height:1.6; color: var(--text-main); margin-top: 4px;">${ai.news_analysis}</p>
                </div>

                <div style="font-size:0.85rem; background:#f8fafc; padding:0.8rem; border-radius:6px; border: 1px solid var(--border);">
                    <strong style="color: var(--text-muted);">Primary Catalyst:</strong> <span style="font-weight: 600;">${ai.catalyst}</span>
                </div>
            `;

            // --- Inject Quant Math (Removes Skeletons) ---
            document.getElementById('t-rsi').className = 'metric-value'; 
            document.getElementById('t-rsi').innerText = data.rsi;
            
            document.getElementById('t-trend').className = 'metric-value'; 
            document.getElementById('t-trend').innerText = data.trend;
            
            document.getElementById('t-vol').className = 'metric-value'; 
            document.getElementById('t-vol').innerHTML = `${(data.volume/1000000).toFixed(1)}M`;
            
            document.getElementById('t-bb').className = 'metric-value'; 
            document.getElementById('t-bb').innerHTML = `<span style="font-size:0.8rem">Upper: ${data.bb_upper}</span>`;

            // --- Inject News Feed ---
            let newsHtml = '';
            data.news.forEach(n => {
                newsHtml += `
                    <a href="${n.url}" target="_blank" style="display:block; padding:1.2rem; border-bottom:1px solid #e2e8f0; text-decoration:none; transition: background 0.2s;" onmouseover="this.style.background='#fafafa'" onmouseout="this.style.background='transparent'">
                        <div style="font-size:0.75rem; color:#64748b; margin-bottom:6px; font-weight:700; text-transform: uppercase;">${n.source}</div>
                        <div style="font-size:0.95rem; color:#0f172a; font-weight:600; line-height:1.4;">${n.headline}</div>
                    </a>`;
            });
            document.getElementById('news-box').innerHTML = newsHtml || '<div style="padding:1rem;">No recent news available.</div>';
        });
}

// ==========================================
// 3. LIVE PRICE HEARTBEAT
// ==========================================
setInterval(() => {
    fetch(`/api/price/${SYM}`)
        .then(r => r.json())
        .then(d => {
            if(d.price) {
                const el = document.getElementById('live-price');
                const old = parseFloat(el.innerText.replace('$',''));
                
                if(d.price !== old) {
                    el.style.color = d.price > old ? 'var(--up)' : 'var(--down)';
                    el.innerText = `$${d.price}`;
                    setTimeout(() => el.style.color = 'var(--text-main)', 1000);
                }
            }
        });
}, 3000); 

// ==========================================
// BOOTSTRAP
// ==========================================
document.addEventListener("DOMContentLoaded", () => {
    if(typeof DATES !== 'undefined' && typeof PRICES !== 'undefined') {
        initChart(DATES, PRICES);
    }
    fetchAnalysis();
});