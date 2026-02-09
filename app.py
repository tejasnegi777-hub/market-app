import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Market Predictor", page_icon="📈")

st.title("📈 Market Trend Finder")
st.write("Check if the market is Bullish or Bearish")

# यूजर से स्टॉक का नाम पूछना
symbol = st.text_input("Enter Stock Symbol (e.g., ^NSEI for Nifty, RELIANCE.NS)", "^NSEI")

if st.button('Predict Trend'):
    try:
        # डेटा डाउनलोड करना
        data = yf.download(symbol, period="2d", interval="1d")
        
        if len(data) >= 2:
            close_today = data['Close'].iloc[-1]
            close_yesterday = data['Close'].iloc[-2]
            
            st.metric(label="Current Price", value=f"{close_today:.2f}", delta=f"{close_today - close_yesterday:.2f}")

            if close_today > close_yesterday:
                st.success("The Market looks **BULLISH** today! 📈")
            else:
                st.error("The Market looks **BEARISH** today! 📉")
        else:
            st.warning("Not enough data found.")
    except Exception as e:
        st.error(f"Error: {e}")
