# 🚀 Team Name: Neural Vissionaries 🌟

## Description
An AI-powered Recommendation System for Banking and Finance. 
This project build s a hyper Personalisation tool for an Individual or Organisation. It give highly personal banking and personal finance related recommendation based on users data, socialmedia, ans transaction histoty.


## 🎯 Introduction
The **AI Hyper Recommendation Tool** addresses the challenges faced by the user to get the recommendations based on their area of Interest.

## 🎥 Demo
📹 Video-Link :https://www.loom.com/share/cc4431c62f744f3a9cc57cf7447c592d?sid=61011ab6-17e6-4cbc-8966-30bc45b74df7 

🖼️ Screenshots: https://github.com/shalyaj/Neural_Vissionaries/blob/master/Screenshots.pdf

## 💡 Inspiration
This project was created during the [Technology Hackathon 2025] to showcase how Gen AI integration to a reccomendation system is so useful.

## ⚙️ What It Does
This application integrates transaction details, social media feedback, and user account profiles to provide personalized banking and personal finance recommendations. Using Gen AI, it analyzes user behavior and preferences to suggest tailored financial products, services, and offers that align with the user’s financial goals and lifestyle. The platform aims to enhance financial decision-making by providing intelligent, data-driven insights.

## Working
**Input Data**: User Details, Social Media
Insights, Transaction History
**Weighting Strategy**:
- Recent transactions and posts given higher priority
**Weighted** by recency (0.1 to 1)
**Prompt Designing** Importance of Prioritization Based on Timestamp and Purchase Date

## 🛠️ How We Built It

1. **Run the Application**:
   - Start the backend:
     ```bash
     python app.py
     ```
   - Start the frontend
     ```bash
     npm start
     ```

2. **Access the Service**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:3000
   ```

---

## Usage
**API Call Process:**
- Data Ingestion, Pre-processing, Chain
Invocation

**• Key Methods:**
- get_recommendations()
- Data Extraction, Transformation, and JSON
Cleaning


## 🚧 Challenges We Faced
1.Coming up with precise and best prompt tempelate for LLM
2.Prioritizing Recency for Transactions andSocial Media
3.Handling Errors and Invalid JSON from LLM response
4.Figuring out how to use LLM model

## 🏃 How to Run
1.## Setup Instructions
Follow these steps to set up the project locally.

1. **Clone the Repository**:
   ```bash
   git clone (https://github.com/shalyaj/Neural_Vissionaries.git)
   ```

2. **Set Up Dependencies**:
   - Install Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Install Node.js dependencies (if required):
     ```bash
     npm install
     ```

## 🏗️ Tech Stack
- 🔹 Frontend: - React, JavaScript, HTML, CSS
- 🔹 Backend:  Python (LangChain Framework)
- 🔹 AI/LLM: llama 3.3
- 🔹 Integration Tools: Jira REST API, Pandas
- 🔹 Other: OpenAI API , Jupyter Notebooks (for exploratory data analysis)

## 👥 Team
-  **Mukul Kumar** - https://github.com/demonescool
- **Abhishek Anand** - https://github.com/abhishek1030
- **Rishi Shalyaj** - https://github.com/shalyaj
