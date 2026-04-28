# 📊 AI Personal Finance Advisor

<div align="center">

![AI Finance Advisor](https://img.shields.io/badge/AI-Finance%20Advisor-blueviolet)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

### 💡 AI-Driven Financial Intelligence Platform

**Turn raw transaction data into actionable financial strategy using Machine Learning & Predictive Analytics**

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app.streamlit.app)
[![Live Demo](https://img.shields.io/badge/Live-Demo-orange)](https://your-app.streamlit.app)

</div>

---

## 🚀 Overview

**AI Personal Finance Advisor** is a full-stack data-driven application designed to help users **analyze, predict, and optimize their financial behavior**.

It combines **data analytics, machine learning, and intuitive UI/UX** to deliver:

* Deep spending insights
* Predictive financial forecasting
* Personalized AI recommendations

👉 Built with a strong focus on **real-world usability + recruiter-level engineering clarity**

---

## Demo Images 

![demo](https://github.com/Tanmay1112004/AI-Personal-Finance-Advisor/blob/main/scrennshots/Screenshot%202025-12-07%20215655.png)

![demo](https://github.com/Tanmay1112004/AI-Personal-Finance-Advisor/blob/main/scrennshots/Screenshot%202025-12-07%20215718.png)

![demo](https://github.com/Tanmay1112004/AI-Personal-Finance-Advisor/blob/main/scrennshots/Screenshot%202025-12-07%20215755.png)

![demo](https://github.com/Tanmay1112004/AI-Personal-Finance-Advisor/blob/main/scrennshots/Screenshot%202025-12-07%20215811.png)

![demo](https://github.com/Tanmay1112004/AI-Personal-Finance-Advisor/blob/main/scrennshots/Screenshot%202025-12-07%20215838.png)

![demo](https://github.com/Tanmay1112004/AI-Personal-Finance-Advisor/blob/main/scrennshots/Screenshot%202025-12-07%20215854.png)


---

## ✨ Core Value Proposition

> “Not just tracking expenses — enabling smarter financial decision-making.”

This system acts like a **digital financial analyst**, helping users:

* Understand where money goes
* Predict future financial scenarios
* Identify savings opportunities

---

## 🔥 Key Features

### 📊 Smart Analytics Dashboard

* Real-time KPIs (Income, Expenses, Savings Rate)
* Category-wise spend analysis
* Interactive charts (Plotly-powered)
* Budget utilization tracking

---

### 🤖 AI-Powered Insights Engine

* Automated transaction categorization (NLP-based)
* Smart spending pattern detection
* Subscription identification
* Personalized financial recommendations

---

### 🔮 Predictive Forecasting

* 30 / 60 / 90-day expense predictions
* Multiple ML models:

  * ARIMA
  * LSTM
  * Prophet
* Confidence intervals & risk indicators

---

### 💬 Conversational AI Advisor

* Natural language queries (chat interface)
* Context-aware responses
* Budgeting & savings advice
* Financial Q&A system

---

### 🎨 Modern UI/UX

* Dark theme with glassmorphism design
* Fully responsive layout
* Clean and intuitive navigation
* Optimized for performance

---

### 🔄 Data Management

* CSV / Excel upload support
* Auto data cleaning & preprocessing
* Export reports (CSV/PDF)
* Sample dataset included

---

## 🛠️ Tech Stack

| Layer                  | Technology                    |
| ---------------------- | ----------------------------- |
| **Frontend**           | Streamlit, Plotly, Custom CSS |
| **Backend**            | Python                        |
| **Data Processing**    | Pandas, NumPy                 |
| **Machine Learning**   | Scikit-learn, Statsmodels     |
| **Forecasting Models** | ARIMA, LSTM                   |
| **Visualization**      | Plotly, Matplotlib            |
| **NLP**                | Regex-based classification    |

---

## 📦 Installation

### Prerequisites

* Python 3.8+
* pip

---

### Setup

```bash
# Clone repository
git clone https://github.com/yourusername/ai-finance-advisor.git

# Navigate
cd ai-finance-advisor

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run finance_app_fixed.py
```

Open:

```
http://localhost:8501
```

---

## 📁 Project Structure

```
ai-finance-advisor/
│
├── finance_app_fixed.py
├── requirements.txt
├── sample_transactions.csv
│
├── utils/
│   ├── data_processor.py
│   ├── forecasting.py
│   ├── nlp_categorizer.py
│   └── visualizations.py
│
└── assets/
    ├── images/
    └── css/
```

---

## 📊 How It Works

### 1️⃣ Upload Data

* Upload CSV with transaction details
* System auto-cleans & categorizes

### 2️⃣ Analyze

* Dashboard shows trends & KPIs
* Identify spending behavior

### 3️⃣ Generate Insights

* AI suggests optimizations
* Detect unnecessary expenses

### 4️⃣ Forecast

* Predict upcoming expenses
* Evaluate financial risk

### 5️⃣ Interact

* Ask financial questions via chat
* Get real-time AI guidance

---

## 📋 Sample Data Format

```csv
Date,Description,Amount,Type,Category
2024-01-15,Amazon Shopping,2499,Debit,Shopping
2024-01-16,Uber Ride,350,Debit,Transport
2024-01-17,Netflix,649,Debit,Entertainment
2024-01-19,Salary,75000,Credit,Income
```

---

## 🚀 Deployment

### Streamlit Cloud (Recommended)

1. Push repo to GitHub
2. Connect to Streamlit Cloud
3. Deploy in minutes

---

### Docker

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "finance_app_fixed.py"]
```

---

## 🔒 Privacy & Security

* No persistent data storage
* Session-based processing
* Local data handling
* API usage optional

---

## 📈 Why This Project Stands Out (Recruiter POV)

✔ Real-world problem solving
✔ End-to-end project (Data + ML + UI)
✔ Production-ready architecture
✔ Clean modular codebase
✔ Strong business use-case

👉 This is not just a project — it's a **portfolio-grade product**

---

## 🤝 Contributing

```bash
git checkout -b feature/your-feature
git commit -m "Add feature"
git push origin feature/your-feature
```

Pull Requests are welcome.

---

## 🛣️ Roadmap

* Bank API integration
* Multi-user authentication
* Investment tracking
* Mobile app version
* Real-time financial alerts

---

## 📄 License

MIT License

---

## 🙌 Acknowledgements

* Streamlit
* Plotly
* Open-source ML ecosystem

---

## 📞 Contact

**Author**: Tanmay
**Email**: [your.email@example.com](mailto:your.email@example.com)
**GitHub**: [https://github.com/yourusername](https://github.com/yourusername)

---

<div align="center">

### ⭐ If this helped you, drop a star

**“Data + AI + Finance = Smarter Decisions”**

</div>

---
