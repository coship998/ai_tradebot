def get_rule_decision(data):
    """
    Rule-based stock decision engine
    """

    score = 0
    reasons = []

    rsi = data.get("rsi")
    macd = data.get("macd")
    signal = data.get("signal")
    trend = data.get("trend")
    volume = data.get("volume")
    avg_volume = data.get("avg_volume")

    # ---------- RSI ----------
    if rsi is not None:
        if rsi > 70:
            score -= 1
            reasons.append("RSI > 70 → Overbought (Bearish)")
        elif rsi < 30:
            score += 1
            reasons.append("RSI < 30 → Oversold (Bullish)")

    # ---------- MACD ----------
    if macd is not None and signal is not None:
        if macd > signal:
            score += 1
            reasons.append("MACD > Signal → Bullish crossover")
        else:
            score -= 1
            reasons.append("MACD < Signal → Bearish crossover")

    # ---------- TREND ----------
    if trend:
        if "Bullish" in trend:
            score += 1
            reasons.append("Market trend is Bullish")
        elif "Bearish" in trend:
            score -= 1
            reasons.append("Market trend is Bearish")

    # ---------- VOLUME ----------
    if volume and avg_volume:
        if volume > avg_volume:
            score += 1
            reasons.append("Volume above average → Strong move")
        else:
            score -= 1
            reasons.append("Low volume → Weak move")

    # ---------- FINAL DECISION ----------
    if score >= 2:
        decision = "BUY 📈"
    elif score <= -2:
        decision = "SELL ⚠️"
    else:
        decision = "HOLD 🤝"

    return {
        "decision": decision,
        "score": score,
        "reasons": reasons
    }