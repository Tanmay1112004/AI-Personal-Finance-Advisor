# 📊 AI Personal Finance Advisor

<div align="center">

![AI Finance Advisor](https://img.shields.io/badge/AI-Finance%20Advisor-blueviolet)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**Transform Your Financial Management with AI-Powered Insights**

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app.streamlit.app)
[![Demo](https://img.shields.io/badge/View-Demo-orange)](https://your-app.streamlit.app)

*Smart financial tracking, AI-powered forecasting, and personalized recommendations*

</div>

## 🚀 Overview

**AI Personal Finance Advisor** is a comprehensive financial management application that leverages artificial intelligence to provide deep insights into your spending patterns, forecast future expenses, and offer personalized financial recommendations. With a beautiful dark theme interface and powerful analytics, it transforms raw transaction data into actionable financial intelligence.

![Dashboard Preview](https://via.placeholder.com/800x400/8B5CF6/FFFFFF?text=AI+Finance+Advisor+Dashboard)

## ✨ Key Features

### 📊 **Smart Analytics Dashboard**
- Real-time financial metrics and KPIs
- Interactive visualizations with Plotly
- Spending trends and category analysis
- Budget tracking with progress indicators

### 🤖 **AI-Powered Insights**
- Personalized spending recommendations
- Automated expense categorization using NLP
- Smart detection of recurring subscriptions
- Savings opportunity identification

### 🔮 **Predictive Forecasting**
- 30/60/90 day spending forecasts
- Multiple forecasting models (ARIMA, LSTM, Prophet)
- Confidence interval predictions
- Risk assessment and alerts

### 💬 **AI Financial Advisor Chat**
- Natural language financial queries
- Context-aware responses
- Quick financial advice
- Investment and savings guidance

### 📱 **Modern User Interface**
- Beautiful dark theme with gradient accents
- Glass morphism design elements
- Responsive and mobile-friendly
- Intuitive navigation

### 🔄 **Data Management**
- CSV/Excel file upload
- Automatic data cleaning and categorization
- Export reports (PDF, CSV)
- Sample data templates

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Streamlit, Plotly, Custom CSS |
| **Backend** | Python 3.8+ |
| **AI/ML** | Scikit-learn, Statsmodels |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Plotly, Matplotlib |
| **Forecasting** | ARIMA, LSTM models |
| **NLP** | Regex-based categorization |

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Internet connection for AI features

### Step-by-Step Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-finance-advisor.git
cd ai-finance-advisor
```

2. **Create virtual environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run finance_app_fixed.py
```

5. **Open in browser**
```
http://localhost:8501
```

## 📁 Project Structure

```
ai-finance-advisor/
│
├── finance_app_fixed.py          # Main application file
├── requirements.txt              # Python dependencies
├── README.md                     # This file
├── sample_transactions.csv       # Sample data file
│
├── utils/                        # Utility modules
│   ├── data_processor.py        # Data cleaning and processing
│   ├── forecasting.py           # Time series forecasting
│   ├── nlp_categorizer.py       # NLP transaction categorization
│   └── visualizations.py        # Plotting functions
│
└── assets/                       # Static assets
    ├── images/                  # App images
    └── css/                     # Custom stylesheets
```

## 📊 Using the Application

### 1. **Upload Your Data**
- Download the sample CSV template
- Format your transactions with: Date, Description, Amount, Type
- Upload via the "Upload Data" page
- AI will automatically categorize transactions

### 2. **Explore Dashboard**
- View key financial metrics
- Analyze spending patterns
- Monitor budget utilization
- Check financial health score

### 3. **Generate AI Insights**
- Click "Generate AI Insights"
- Review personalized recommendations
- See potential savings opportunities
- Implement suggested actions

### 4. **Forecast Future Spending**
- Select forecast period (30/60/90 days)
- Choose forecasting model
- View predictions with confidence intervals
- Assess financial risks

### 5. **Chat with AI Advisor**
- Ask financial questions naturally
- Get personalized advice
- Request budget planning help
- Discuss investment strategies

## 📋 Sample Data Format

Your CSV file should have these columns:

```csv
Date,Description,Amount,Type,Category
2024-01-15,Amazon Shopping,2499.00,Debit,Shopping
2024-01-16,Uber Ride,350.50,Debit,Transport
2024-01-17,Netflix Subscription,649.00,Debit,Entertainment
2024-01-18,Grocery Store,1250.75,Debit,Food
2024-01-19,Salary Credit,75000.00,Credit,Income
```

## 🔧 Configuration

### API Keys (Optional)

For enhanced AI features, add your Gemini API key:

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. In the app, navigate to Settings → API Configuration
4. Enter your API key

### Customization

Modify the CSS variables in the code to change the theme:

```css
:root {
    --primary: #8B5CF6;      /* Change primary color */
    --secondary: #06D6A0;    /* Change secondary color */
    --dark: #0F172A;         /* Change background */
}
```

## 🚀 Deployment

### Deploy to Streamlit Cloud (Recommended)

1. Push code to GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set up deployment configuration
5. Deploy!

### Deploy with Docker

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "finance_app_fixed.py", "--server.port=8501"]
```

Build and run:
```bash
docker build -t ai-finance-advisor .
docker run -p 8501:8501 ai-finance-advisor
```

### Deploy to Other Platforms

- **AWS EC2/Elastic Beanstalk**
- **Google Cloud Run**
- **Azure App Service**
- **Heroku** (with buildpack)

## 📈 Features in Detail

### 🎯 **Financial Analytics**
- **Spending Analysis**: Category-wise breakdown, trend analysis
- **Budget Tracking**: Real-time budget monitoring with alerts
- **Savings Rate**: Automatic calculation and optimization
- **Transaction History**: Searchable, filterable transaction logs

### 🤖 **AI Capabilities**
- **Smart Categorization**: NLP-based automatic transaction categorization
- **Pattern Recognition**: Identifies spending habits and anomalies
- **Personalized Recommendations**: Actionable insights based on your data
- **Forecasting Accuracy**: Multiple models for reliable predictions

### 🎨 **User Experience**
- **Dark Theme**: Easy on eyes, professional look
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Fast Performance**: Optimized data processing
- **Intuitive Navigation**: Easy to use for all skill levels

## 🔒 Privacy & Security

- **Local Processing**: All data processing happens locally in your browser
- **No Data Storage**: No personal data is stored on servers
- **Secure File Handling**: Uploaded files are processed in memory only
- **Session-based**: Data cleared when browser session ends
- **Optional Cloud**: AI features require API keys but data isn't stored

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
```bash
git checkout -b feature/AmazingFeature
```
3. **Commit your changes**
```bash
git commit -m 'Add some AmazingFeature'
```
4. **Push to the branch**
```bash
git push origin feature/AmazingFeature
```
5. **Open a Pull Request**

### Areas for Contribution
- Additional forecasting models
- Bank API integrations
- Multi-currency support
- Enhanced visualization types
- Mobile app development
- Translation/localization

## 🐛 Troubleshooting

### Common Issues

**Issue**: "Module not found" errors
**Solution**: 
```bash
pip install -r requirements.txt --upgrade
```

**Issue**: App runs but HTML shows as text
**Solution**: Ensure all HTML is wrapped in `st.markdown(..., unsafe_allow_html=True)`

**Issue**: Forecast not generating
**Solution**: Ensure you have enough transaction data (minimum 30 days)

**Issue**: Slow performance
**Solution**: 
- Reduce dataset size
- Clear browser cache
- Use sample data for testing

### Getting Help
1. Check the console for error messages
2. Review the sample CSV format
3. Ensure Python version is 3.8+
4. Verify all dependencies are installed

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pandas User Guide](https://pandas.pydata.org/docs/)
- [Plotly Python Documentation](https://plotly.com/python/)
- [Google Gemini API](https://ai.google.dev/)

## 🏆 Features Roadmap

### Coming Soon
- [ ] Bank API integration (Plaid, Yodlee)
- [ ] Multi-user support with authentication
- [ ] Investment portfolio tracking
- [ ] Tax optimization suggestions
- [ ] Voice commands interface
- [ ] Mobile app (React Native)
- [ ] Real-time stock market data
- [ ] Peer comparison analytics
- [ ] Gamification features
- [ ] Advanced debt management

### In Progress
- [x] Basic transaction categorization
- [x] Spending forecasting
- [x] AI recommendations
- [x] Dark theme UI
- [x] CSV export functionality

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Icons from [Font Awesome](https://fontawesome.com/)
- Color palette from [Tailwind CSS](https://tailwindcss.com/)
- Sample data inspired by real spending patterns
- Thanks to all contributors and testers

## 📞 Contact & Support

**Project Maintainer**: Your Name  
**Email**: your.email@example.com  
**GitHub Issues**: [Report a Bug](https://github.com/yourusername/ai-finance-advisor/issues)  
**Discord**: [Join our Community](https://discord.gg/your-invite-link)

---

<div align="center">

### ⭐ Star this repo if you find it useful!

**"Take control of your finances with AI intelligence"**

[![GitHub stars](https://img.shields.io/github/stars/yourusername/ai-finance-advisor?style=social)](https://github.com/yourusername/ai-finance-advisor)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/ai-finance-advisor?style=social)](https://github.com/yourusername/ai-finance-advisor)

</div>

## 📊 Screenshots

| Dashboard | Analytics | Forecast |
|-----------|-----------|----------|
| ![Dashboard](https://via.placeholder.com/300x200/8B5CF6/FFFFFF?text=Dashboard) | ![Analytics](https://via.placeholder.com/300x200/06D6A0/FFFFFF?text=Analytics) | ![Forecast](https://via.placeholder.com/300x200/FF6B6B/FFFFFF?text=Forecast) |

| AI Insights | Chat Advisor | Settings |
|-------------|--------------|----------|
| ![Insights](https://via.placeholder.com/300x200/FFD166/000000?text=AI+Insights) | ![Chat](https://via.placeholder.com/300x200/118AB2/FFFFFF?text=Chat+Advisor) | ![Settings](https://via.placeholder.com/300x200/A78BFA/FFFFFF?text=Settings) |
