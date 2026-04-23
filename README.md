<h1><b>AI Pricing Analytics App</b></h1>

<p>
  A Streamlit-based AI-powered pricing analytics application built with Python to analyze revenue, margin, and demand patterns, and generate intelligent pricing recommendations.
</p>

<p>
  This project demonstrates how data science, pricing strategy, and AI can be combined to move from descriptive analytics to prescriptive decision-making.
</p>

<h2><b>Key Features</b></h2>
<ul>
  <li>Upload custom CSV datasets</li>
  <li>Interactive KPI dashboard (Revenue, Margin, Pricing Metrics)</li>
  <li>Price elasticity estimation using statistical modeling</li>
  <li>Scenario-based pricing simulations</li>
  <li>AI-powered pricing insights and recommendations</li>
  <li>Data-driven decision support for pricing strategy</li>
</ul>

<h2><b>What This Project Solves</b></h2>
<p>
  Traditional pricing analytics answers:<br>
  <i>"What happened?"</i>
</p>

<p>
  This application goes further:<br>
  <i>"What should we do next?"</i>
</p>

<p>It helps users:</p>
<ul>
  <li>Understand demand sensitivity to pricing</li>
  <li>Evaluate pricing strategies</li>
  <li>Simulate revenue and profit impact</li>
  <li>Generate actionable recommendations</li>
</ul>

<h2><b>Tech Stack</b></h2>
<ul>
  <li>Python</li>
  <li>Streamlit</li>
  <li>Pandas</li>
  <li>NumPy</li>
  <li>Scikit-learn</li>
  <li>Plotly</li>
  <li>OpenAI API (for AI insights)</li>
</ul>

<h2><b>Environment Setup (Required)</b></h2>
<p>
  This application uses OpenAI (ChatGPT) APIs to generate AI-powered pricing insights.
</p>

<p>
  Before running the app, you must configure your API key.
</p>

<h3><b>Step 1: Create a <code>.env</code> file</b></h3>
<pre><code>touch .env</code></pre>

<h3><b>Step 2: Add your API key</b></h3>
<pre><code>OPENAI_API_KEY=your_api_key_here</code></pre>

<h3><b>Step 3: Ensure <code>.env</code> is not committed</b></h3>
<ul>
  <li>Add <code>.env</code> to your <code>.gitignore</code></li>
</ul>

<p>
  <b>Important:</b> Without this setup, AI-based insights will not function.
</p>

<h2><b>Run Locally</b></h2>

<h3><b>1. Clone the repository</b></h3>
<pre><code>git clone https://github.com/manas04/AI-Pricing-Analytics-App.git
cd AI-Pricing-Analytics-App</code></pre>

<h3><b>2. Install dependencies</b></h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3><b>3. Set up environment variables</b></h3>
<p>(Refer to the Environment Setup section above)</p>

<h3><b>4. Run the application</b></h3>
<pre><code>streamlit run app.py</code></pre>

<h2><b>Example Use Cases</b></h2>
<ul>
  <li>Pricing strategy optimization</li>
  <li>Revenue and margin analysis</li>
  <li>Promotional impact evaluation</li>
  <li>Demand forecasting and sensitivity analysis</li>
  <li>Business decision support for pricing teams</li>
</ul>

<h2><b>Project Structure</b></h2>
<pre><code>app.py
requirements.txt
README.md
data/
utils/</code></pre>

<h2><b>Future Improvements</b></h2>
<ul>
  <li>Advanced machine learning models for demand forecasting</li>
  <li>Dynamic pricing optimization engine</li>
  <li>Integration with real-time data sources</li>
  <li>Deployment as a web-based SaaS tool</li>
</ul>

<h2><b>Contributing</b></h2>
<p>
  Feel free to fork this repository, raise issues, or submit pull requests.
</p>

<h2><b>Contact</b></h2>
<p>
  If you're working on pricing, revenue analytics, or data science problems, feel free to connect.
</p>

<p>
  ⭐ If you found this useful, please star the repo!
</p>
