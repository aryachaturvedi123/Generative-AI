⚖️ FAIRPRESS – AI-Powered News Bias Detection Tool
📌 Problem Statement

Media bias affects public perception and trust. Manual detection is slow and subjective — there’s a need for an automated, AI-driven tool to identify and explain bias in news content.

💡 Solution

FAIRPRESS uses NLP and sentiment analysis to detect bias, highlight emotional tones, and visualize how balanced or skewed a news article is. It provides clear insights into media fairness through charts and AI-generated explanations.

✨ Key Features

✅ Bias & Sentiment Detection (Positive / Negative / Neutral)
✅ GPT-Based Explanations of detected bias
✅ Interactive visual reports and PDF export
✅ Simple Streamlit UI for quick analysis

🛠️ Tech Stack

Python, Streamlit

Hugging Face Transformers, OpenAI GPT API

Matplotlib, Plotly, ReportLab

Render / Streamlit Cloud for deployment

🚧 Challenges

Handling long text latency in transformer models

Managing API rate limits & deployment secrets

Improving context-sensitive bias detection

🚀 Future Scope

🔹 Real-time news feed analysis
🔹 Multilingual & regional language support
🔹 Chrome extension for bias detection on web pages

⚡ How to Run
git clone https://github.com/yourusername/FAIRPRESS.git
cd FAIRPRESS
pip install -r requirements.txt
streamlit run app.py
