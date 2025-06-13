import streamlit as st
from agents.langgraph_multiagent import multi_agent
from services.plot_utils import plot_stock_price
from streamlit_chat import message as chat_message


st.set_page_config(page_title="📊 AI Financial Assistant", layout="wide")
st.title("📊 AI Financial Assistant")
st.caption("💼 Powered by Groq + LangGraph | Real-time financial insights")


if "history" not in st.session_state:
    st.session_state.history = []


query = st.chat_input("Ask a financial question (e.g. Show chart of TSLA)")


if query:
    
    st.session_state.history.append({"user": query})

    
    with st.spinner("🤖 Thinking..."):
        result = multi_agent.run(query)
        st.session_state.history.append({"ai": result})

        #Auto-detect and visualize stock chart
        words = query.upper().split()
        tickers = [w for w in words if w.isalpha() and len(w) <= 5]
        if tickers:
            try:
                fig = plot_stock_price(tickers[0])
                st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.warning(f"Could not load chart for {tickers[0]}: {e}")


for msg in st.session_state.history:
    if "user" in msg:
        chat_message(msg["user"], is_user=True)
    else:
        chat_message(msg["ai"])
