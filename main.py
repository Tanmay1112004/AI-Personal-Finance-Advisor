"""
AI Personal Finance Advisor – Premium
Dark theme, glass-morphism UI, Gemini-2.5-Flash AI advisor
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta
import warnings
import random
import os

warnings.filterwarnings("ignore")

# ------------------------------------------------------------------
# 1.  CUSTOM CSS  (dark glass-morphism theme)
# ------------------------------------------------------------------
def local_css():
    st.markdown(
        """
    <style>
    :root{--primary:#8B5CF6;--secondary:#06D6A0;--accent:#FF6B6B;--dark:#0F172A;--light:#F8FAFC;
           --gradient:linear-gradient(135deg,#8B5CF6 0%,#06D6A0 100%);}
    .stApp{background:var(--dark);color:var(--light);}
    .main-header{font-size:3.5rem;font-weight:900;background:var(--gradient);
                 -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                 text-align:center;margin-bottom:2rem;}
    .glass-card{background:rgba(30,41,59,.7);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.1);
                padding:1.5rem;border-radius:20px;box-shadow:0 10px 30px rgba(0,0,0,.3);}
    .custom-button{background:var(--gradient);color:white;border:none;padding:12px 30px;border-radius:10px;
                   font-weight:600;cursor:pointer;transition:all .3s ease;}
    .custom-button:hover{transform:translateY(-2px);box-shadow:0 8px 25px rgba(139,92,246,.6);}
    .custom-button-outline{background:transparent;color:#8B5CF6;border:2px solid #8B5CF6;
                           padding:12px 30px;border-radius:10px;font-weight:600;cursor:pointer;
                           transition:all .3s ease;}
    .custom-button-outline:hover{background:rgba(139,92,246,.1);}
    .metric-card{background:linear-gradient(135deg,#1E293B 0%,#0F172A 100%);padding:1.5rem;
                border-radius:15px;text-align:center;border:1px solid rgba(139,92,246,.2);}
    .metric-icon{font-size:2.5rem;background:var(--gradient);-webkit-background-clip:text;
                -webkit-text-fill-color:transparent;}
    .metric-value{font-size:2.8rem;font-weight:800;background:var(--gradient);
                 -webkit-background-clip:text;-webkit-text-fill-color:transparent;}
    .metric-label{color:#94A3B8;font-size:.9rem;text-transform:uppercase;letter-spacing:1.5px;}
    .insight-positive{border-left:5px solid #06D6A0;}
    .insight-warning{border-left:5px solid #FFD166;}
    .insight-danger{border-left:5px solid #FF6B6B;}
    </style>
    """,
        unsafe_allow_html=True,
    )

# ------------------------------------------------------------------
# 2.  GEMINI 2.5 FLASH SET-UP
# ------------------------------------------------------------------
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_KEY = os.getenv("GEMINI_KEY", "YOUR_GEMINI_2.5_FLASH_KEY")  # <- put real key here or in env

@st.cache_resource
def load_gemini():
    if GEMINI_KEY == "YOUR_GEMINI_2.5_FLASH_KEY":
        return None
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_KEY)
        return genai.GenerativeModel(GEMINI_MODEL)
    except Exception as e:
        st.error("Gemini 2.5 Flash could not be loaded – fallback to mock replies.")
        return None

gemini_model = load_gemini()

# ------------------------------------------------------------------
# 3.  FINANCIAL CORE
# ------------------------------------------------------------------
class FinancialAnalyzer:
    def __init__(self):
        self.cats = {
            "Food & Dining": ["restaurant", "cafe", "food", "dinner", "lunch", "breakfast", "coffee"],
            "Shopping": ["amazon", "flipkart", "myntra", "shopping", "store", "mall"],
            "Entertainment": ["netflix", "prime", "hotstar", "movie", "cinema", "game"],
            "Transportation": ["uber", "ola", "taxi", "fuel", "petrol", "flight"],
            "Bills & Utilities": ["electricity", "water", "internet", "mobile", "bill"],
            "Healthcare": ["hospital", "doctor", "medicine", "pharmacy"],
            "Income": ["salary", "credit", "deposit", "transfer"],
            "Investments": ["sip", "mutual", "stock", "investment"],
            "Other": [],
        }

    def fake_analysis(self):
        return dict(total_spent=25430, avg_daily=848, transaction_count=45,
                   top_category="Food & Dining", peak_day="Saturday", savings_rate=0.18)

    def generate_recommendations(self, df):
        return [
            {"title": "Optimize Food Delivery", "description": "Food delivery accounts for 35 % of food spending. Consider meal planning to save ₹3,000/month.", "impact": "high", "savings": 3000, "icon": "🍕"},
            {"title": "Review Subscriptions", "description": "3 unused subscriptions detected. Potential savings: ₹1,200/month.", "impact": "medium", "savings": 1200, "icon": "📱"},
            {"title": "Smart Shopping", "description": "80 % of shopping happens on weekends. Weekday purchases could save ₹2,000/month.", "impact": "medium", "savings": 2000, "icon": "🛍️"},
        ]

class DataProcessor:
    def process_csv(self, uploaded_file):
        try:
            df = pd.read_csv(uploaded_file)
            for col in ["Date", "Description", "Amount"]:
                if col not in df.columns:
                    st.error(f"Missing required column: {col}")
                    return None
            df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
            df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce").abs()
            analyzer = FinancialAnalyzer()
            df["Category"] = "Other"
            for idx, row in df.iterrows():
                desc = str(row["Description"]).lower()
                for cat, kw in analyzer.cats.items():
                    if any(k in desc for k in kw):
                        df.at[idx, "Category"] = cat
                        break
            return df
        except Exception as e:
            st.error(f"Processing error: {e}")
            return None

class ForecastingEngine:
    def forecast_spending(self, days=30):
        dates = pd.date_range(start=datetime.now(), periods=days, freq="D")
        base = np.linspace(800, 1200, days)
        seasonal = 200 * np.sin(np.linspace(0, 4 * np.pi, days))
        noise = np.random.normal(0, 50, days)
        forecast = base + seasonal + noise
        return {"dates": dates, "forecast": forecast, "upper": forecast * 1.2,
               "lower": forecast * 0.8, "total": forecast.sum()}

# ------------------------------------------------------------------
# 4.  HTML HELPERS
# ------------------------------------------------------------------
def create_button_pair(primary="Get Started", secondary="Watch Demo",
                      pid="get_started", sid="watch_demo"):
    return f"""
<div style="display:flex;gap:15px;margin-top:20px;">
  <button class="custom-button" id="{pid}" onclick="alert('Primary clicked')">{primary}</button>
  <button class="custom-button-outline" id="{sid}" onclick="alert('Secondary clicked')">{secondary}</button>
</div>
"""

def metric_html(title, value, change, icon="💰"):
    ch_html = ""
    if change is not None:
        color = "#06D6A0" if change >= 0 else "#FF6B6B"
        arrow = "↗" if change >= 0 else "↘"
        ch_html = f'<div style="color:{color};font-size:.9rem;margin-top:5px;">{arrow} {abs(change):.1f}%</div>'
    return f"""
<div class="metric-card">
  <div class="metric-icon">{icon}</div>
  <div class="metric-label">{title}</div>
  <div class="metric-value">{value}</div>
  {ch_html}
</div>
"""

def insight_html(title, content, typ="positive"):
    emoji = {"positive": "✅", "warning": "⚠️", "danger": "🚨"}.get(typ, "💡")
    cls = f"insight-{typ}"
    return f"""
<div class="glass-card {cls}">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
    <span style="font-size:1.5rem;">{emoji}</span>
    <strong style="font-size:1.1rem;color:white;">{title}</strong>
  </div>
  <p style="margin:0;color:#CBD5E1;line-height:1.5;">{content}</p>
</div>
"""

# ------------------------------------------------------------------
# 5.  PAGE FUNCTIONS
# ------------------------------------------------------------------
def show_dashboard(analyzer, forecaster):
    st.markdown('<div class="main-header">AI PERSONAL FINANCE ADVISOR</div>', unsafe_allow_html=True)
    c1, c2 = st.columns([3, 1])
    with c1:
        st.markdown("""
<div class="glass-card">
  <div style="display:flex;align-items:center;gap:20px;margin-bottom:20px;">
    <div style="font-size:3rem;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">🚀</div>
    <div>
      <h2 style="color:white;margin:0;font-size:2rem;">Welcome to Your Financial Command Center!</h2>
      <p style="color:#94A3B8;margin:10px 0 0;font-size:1.1rem;">Smart financial management powered by AI.</p>
    </div>
  </div>
</div>
        """, unsafe_allow_html=True)
        st.markdown(create_button_pair("Get Started", "Watch Demo"), unsafe_allow_html=True)
    with c2:
        st.markdown("""
<div class="glass-card" style="text-align:center;">
  <div style="font-size:3rem;margin-bottom:1rem;">🎯</div>
  <h3 style="color:white;margin-bottom:10px;">Financial Health</h3>
  <div style="color:#06D6A0;font-weight:700;font-size:1.1rem;">Excellent</div>
  <div style="color:#94A3B8;font-size:.9rem;">Top 20% of users</div>
</div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">📊 Key Performance Metrics</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown(metric_html("Monthly Spend", "₹25,430", -2.3, "💰"), unsafe_allow_html=True)
    with c2: st.markdown(metric_html("Savings Rate", "18%", +2.1, "💸"), unsafe_allow_html=True)
    with c3: st.markdown(metric_html("Investments", "₹1.2L", +5.7, "📈"), unsafe_allow_html=True)
    with c4: st.markdown(metric_html("Credit Score", "782", +15, "⭐"), unsafe_allow_html=True)

    st.markdown('<div class="section-header">💡 Quick Insights</div>', unsafe_allow_html=True)
    st.markdown(insight_html("Positive Trend!", "Your savings rate increased by 2.1 % this month.", "positive"), unsafe_allow_html=True)
    st.markdown(insight_html("Subscription Alert", "3 unused subscriptions detected. Potential savings: ₹1,200/month", "warning"), unsafe_allow_html=True)

def show_upload_page(processor):
    st.markdown('<div class="main-header">📤 UPLOAD & PROCESS DATA</div>', unsafe_allow_html=True)
    uploaded = st.file_uploader("Drag & drop CSV/Excel", type=["csv", "xlsx"], label_visibility="collapsed")
    if uploaded:
        with st.spinner("Processing..."):
            df = processor.process_csv(uploaded)
            if df is not None:
                st.session_state.processed_data = df
                st.success("✅ Loaded {} transactions".format(len(df)))
                with st.expander("Preview"):
                    st.dataframe(df.head(10), use_container_width=True)
    st.markdown(create_button_pair("Process Data", "Download Sample"), unsafe_allow_html=True)

def show_analytics_page(analyzer):
    st.markdown('<div class="main-header">📊 ADVANCED ANALYTICS</div>', unsafe_allow_html=True)
    if st.session_state.processed_data is None:
        st.warning("Please upload data first.")
        return
    st.markdown(create_button_pair("Export Analytics", "Generate Report"), unsafe_allow_html=True)
    st.markdown('<div class="section-header">Key Metrics</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Total Spent", "₹25,430")
    with c2: st.metric("Avg Daily", "₹848")
    with c3: st.metric("Transactions", "45")
    with c4: st.metric("Top Category", "Food & Dining")

def show_forecast_page(forecaster):
    st.markdown('<div class="main-header">🔮 AI FORECASTING</div>', unsafe_allow_html=True)
    st.markdown(create_button_pair("Quick Forecast", "Advanced Settings"), unsafe_allow_html=True)
    days = st.selectbox("Forecast Period", [30, 60, 90])
    if st.button("🚀 Generate Forecast", type="primary"):
        fc = forecaster.forecast_spending(days)
        st.session_state.forecast_data = fc
        st.success("Forecast generated!")
    if st.session_state.forecast_data:
        fc = st.session_state.forecast_data
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=fc["dates"], y=fc["forecast"], mode="lines", name="Forecast",
                                line=dict(color="#06D6A0", width=4, dash="dash")))
        fig.update_layout(plot_bgcolor="#0F172A", paper_bgcolor="#0F172A", font=dict(color="white"))
        st.plotly_chart(fig, use_container_width=True)

def show_insights_page(analyzer):
    st.markdown('<div class="main-header">🤖 AI POWERED INSIGHTS</div>', unsafe_allow_html=True)
    st.markdown(create_button_pair("Generate AI Insights", "View History"), unsafe_allow_html=True)
    if st.button("✨ Generate AI Insights", type="primary"):
        st.session_state.insights_generated = True
    if st.session_state.insights_generated:
        recs = analyzer.generate_recommendations(st.session_state.processed_data)
        for r in recs:
            st.markdown(insight_html(r["title"], r["description"], "positive"), unsafe_allow_html=True)

def show_advisor_page():
    st.markdown('<div class="main-header">💬 AI FINANCIAL ADVISOR</div>', unsafe_allow_html=True)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chat container
    container = st.container()
    with container:
        for msg in st.session_state.messages:
            emoji = "👤" if msg["role"] == "user" else "🤖"
            bg = "linear-gradient(135deg,#8B5CF6 0%,#7C3AED 100%)" if msg["role"] == "user" else "#1E293B"
            st.markdown(
                f"""
<div style="background:{bg};color:white;padding:1rem;border-radius:15px;margin-bottom:1rem;">
  <div style="display:flex;align-items:start;gap:10px;">
    <span style="font-size:1.5rem;">{emoji}</span>
    <div>{msg["content"]}</div>
  </div>
</div>
                """,
                unsafe_allow_html=True,
            )

    # Input
    prompt = st.chat_input("Ask anything about your finances…")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        if gemini_model:
            try:
                response = gemini_model.generate_content(prompt, stream=False)
                reply = response.text
            except Exception as e:
                reply = f"Gemini error: {e}"
        else:
            replies = [
                "Consider setting up an emergency fund covering 6 months of expenses.",
                "Your savings rate is healthy; boosting your SIP by 10 % could accelerate goal achievement.",
                "3 unused subscriptions detected – cancelling saves ₹1,200/month.",
            ]
            reply = random.choice(replies)
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()

def show_settings_page():
    st.markdown('<div class="main-header">⚙️ SETTINGS</div>', unsafe_allow_html=True)
    st.markdown('<div class="glass-card"><h3>Gemini 2.5 Flash API Key</h3>', unsafe_allow_html=True)
    key_inp = st.text_input("Enter key", value=GEMINI_KEY, type="password")
    if st.button("Save"):
        os.environ["GEMINI_KEY"] = key_inp
        st.success("Key saved – restart app to apply.")
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------------------------------
# 6.  MAIN ENTRY
# ------------------------------------------------------------------
def main():
    st.set_page_config(page_title="AI Finance Advisor | Premium", page_icon="💎", layout="wide")
    local_css()
    for k in ["current_page", "processed_data", "messages", "budget", "insights_generated", "forecast_data"]:
        if k not in st.session_state:
            st.session_state[k] = "dashboard" if k == "current_page" else [] if k == "messages" else None if "data" in k else False if k == "insights_generated" else 50000
    analyzer, processor, forecaster = FinancialAnalyzer(), DataProcessor(), ForecastingEngine()

    # Sidebar nav
    with st.sidebar:
        st.markdown('<div class="sidebar-title"><div style="display:flex;align-items:center;justify-content:center;gap:10px;"><div style="font-size:2rem;">💎</div><div>AI FINANCE</div></div></div>', unsafe_allow_html=True)
        pages = ["dashboard", "upload", "analytics", "forecast", "insights", "advisor", "settings"]
        icons = ["🏠", "📤", "📊", "🔮", "🤖", "💬", "⚙️"]
        for ic, p in zip(icons, pages):
            if st.button(f"{ic} {p.capitalize()}", key=f"nav_{p}", use_container_width=True,
                        type="primary" if st.session_state.current_page == p else "secondary"):
                st.session_state.current_page = p
                st.rerun()

    # Route to page
    if st.session_state.current_page == "dashboard":
        show_dashboard(analyzer, forecaster)
    elif st.session_state.current_page == "upload":
        show_upload_page(processor)
    elif st.session_state.current_page == "analytics":
        show_analytics_page(analyzer)
    elif st.session_state.current_page == "forecast":
        show_forecast_page(forecaster)
    elif st.session_state.current_page == "insights":
        show_insights_page(analyzer)
    elif st.session_state.current_page == "advisor":
        show_advisor_page()
    elif st.session_state.current_page == "settings":
        show_settings_page()

if __name__ == "__main__":
    main()