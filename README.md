<h1>**AI Pricing Analytics App**</h1>

A Streamlit-based AI-powered pricing analytics application built with Python to analyze revenue, margin, and demand patterns, and generate intelligent pricing recommendations.

This project demonstrates how data science, pricing strategy, and AI can be combined to move from descriptive analytics to prescriptive decision-making.

<h3><b></b>Key Features</b></h3>
Upload custom CSV datasets
Interactive KPI dashboard (Revenue, Margin, Pricing Metrics)
Price elasticity estimation using statistical modeling
Scenario-based pricing simulations
AI-powered pricing insights and recommendations
Data-driven decision support for pricing strategy

**What This Project Solves**

Traditional pricing analytics answers:
"What happened?"

This application goes further:
"What should we do next?"

It helps users:

• Understand demand sensitivity to pricing
• Evaluate pricing strategies
• Simulate revenue and profit impact
• Generate actionable recommendations

**Tech Stack**

  • Python
  • Streamlit
  • Pandas
  • NumPy
  • Scikit-learn
  • Plotly
  • OpenAI API (for AI insights)


**Environment Setup (Required)**

This application uses OpenAI (ChatGPT) APIs to generate AI-powered pricing insights.

Before running the app, you must configure your API key.

**Step 1: Create a .env file**

touch .env

**Step 2: Add your API key**

OPENAI_API_KEY=your_api_key_here

**Step 3: Ensure .env is not committed**
Add .env to `.gitignore

Important: Without this setup, AI-based insights will not function.

**Run Locally**
**1. Clone the repository**

git clone https://github.com/manas04/AI-Pricing-Analytics-App.git

cd AI-Pricing-Analytics-App

**2. Install dependencies**

pip install -r requirements.txt

**3. Set up environment variables**

(Refer to Environment Setup section above)

**4. Run the application**

streamlit run app.py

**Example Use Cases**

  • Pricing strategy optimization
  • Revenue and margin analysis
  • Promotional impact evaluation
  • Demand forecasting and sensitivity analysis
  • Business decision support for pricing teams

**Project Structure**

app.py
requirements.txt
README.md
data/
utils/

**Future Improvements**

• Advanced machine learning models for demand forecasting
• Dynamic pricing optimization engine
• Integration with real-time data sources
• Deployment as a web-based SaaS tool

**Contributing**

Feel free to fork this repository, raise issues, or submit pull requests.

**Contact**

If you're working on pricing, revenue analytics, or data science problems, feel free to connect!

If you found this useful, please star the repo!
