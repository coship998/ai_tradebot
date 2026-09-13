import os, json
from groq import Groq

def get_ai_analysis(symbol, data, news):
    try:
        # Load API Key from environment
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        
        # Format news headlines for the LLM
        news_text = "\n".join([f"- {n['headline']}" for n in news]) if news else "No major news updates."
        
        # The heavily engineered prompt
        prompt = f"""
        Analyze {symbol} as a professional quant analyst. Return ONLY valid JSON.
        Price: {data['price']}, RSI: {data['rsi']}, MACD: {data['macd']}
        Volume: {data['volume']} (Avg: {data['avg_volume']})
        Bollinger Bands: Upper {data['bb_upper']}, Lower {data['bb_lower']}
        Recent News Headlines: {news_text}
        
        Format exactly like this JSON schema:
        {{
            "decision": "BUY", // or SELL or HOLD
            "tech_analysis": "Provide a detailed 2-sentence explanation of what the RSI, Volume, and Bollinger bands indicate.",
            "news_analysis": "Provide a detailed 2-sentence explanation of how the recent news headlines impact the stock's sentiment.",
            "catalyst": "Short 3-5 word phrase of the main driver"
        }}
        """
        
        # Execute the call forcing JSON output
        res = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
            temperature=0.2
        )
        
        return json.loads(res.choices[0].message.content)

    except Exception as e:
        print("AI Error:", e)
        # Safe fallback if API fails
        return {
            "decision": "HOLD", 
            "tech_analysis": "AI engine temporarily offline. Awaiting connection.", 
            "news_analysis": "Could not process fundamental news sentiment.", 
            "catalyst": "System Offline"
        }