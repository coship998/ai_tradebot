# ⚡ AI Market Intelligence Workspace

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![LLM](https://img.shields.io/badge/AI-Llama--3.1--8B-orange.svg)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

An institutional-grade, zero-scroll financial terminal that bridges the gap between raw market data and high-speed AI reasoning. This workspace provides real-time quantitative metrics, fundamental news sentiment, and algorithmic trade synthesis in a professional desktop-first environment.

---

## 🖥️ Terminal Interface

> *The UI implements a strict "Bloomberg-style" aesthetic, utilizing monospace typography for numeric precision and a zero-scroll 100vh CSS Grid architecture.*

---

## 🚀 Key Features

### 1. **Algorithmic Synthesis (Llama-3.1)**

The "Brain" of the terminal. Utilizing the **Groq API**, the backend forces Llama-3.1 to perform structured reasoning.

Unlike standard chatbots, this system parses technical and fundamental data into a strict JSON schema to provide:

* **Two-Part Reasoning:** Separate paragraphs for Quantitative (Technical) and Fundamental (News) analysis
* **Buy/Hold/Sell Verdicts:** High-contrast visual signals based on vector analysis of recent market catalysts

---

### 2. **Quantitative Engine**

Custom-built indicators processed via **Pandas** and **yfinance**:

* **Relative Strength (RSI):** 14-period momentum oscillator
* **Volatility Bands:** Bollinger Bands using standard deviation
* **Trend Analysis:** SMA-50 crossover detection
* **Volume Analysis:** Real-time liquidity tracking

---

### 3. **Interactive Visualizations**

* **Dynamic Timeframes:** `1W`, `1M`, `3M`, `6M`, `1Y`, `5Y`
* **Asynchronous UX:** Independent API calls (Chart, AI, News)
* **Live Price Heartbeat:** 3-second polling with UI updates

---

## 🛠️ Tech Stack

| Layer        | Technology                       |
| ------------ | -------------------------------- |
| Backend      | Python / Flask                   |
| Data Science | Pandas / NumPy / yfinance        |
| AI / LLM     | Groq (Llama-3.1-8B-Instant)      |
| Frontend     | HTML5 / CSS3 / JavaScript (ES6+) |
| Visuals      | Chart.js                         |
| News API     | Finnhub                          |

---

## 📂 Project Structure

```text
AI-MARKET-WORKSPACE/
├── app.py
├── services/
│   ├── ai_service.py
│   ├── analysis_service.py
│   ├── indicator_service.py
│   ├── market_service.py
│   ├── news_service.py
│   └── stock_service.py
├── static/
│   ├── css/style.css
│   └── js/stock.js
├── templates/
│   ├── index.html
│   └── stock.html
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-market-workspace.git
cd ai-market-workspace
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

**Activate:**

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Environment Variables

Create a `.env` file in the root:

```env
GROQ_API_KEY=your_groq_api_key_here
FINNHUB_API_KEY=your_finnhub_api_key_here
```

---

### 5. Run the Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## 📈 Roadmap

* [ ] Portfolio Tracking (SQLite integration)
* [ ] WebSockets for real-time streaming
* [ ] Macro-economic AI analysis
* [ ] Strategy backtesting engine

---

## 🎓 Author

**Yashvanth G**
CSE Student, Lovely Professional University (LPU)

* LinkedIn
* Portfolio

---

## ⚠️ Disclaimer

This project is for educational and portfolio purposes only.
Financial markets involve significant risk. Always consult a certified financial advisor before making investment decisions.
