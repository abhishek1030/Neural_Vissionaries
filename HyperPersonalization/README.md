# 🚀 Team Name: Neural Vissionaries 🌟

## Description
An AI-powered Recommendation System for Banking and Finance. 
This project build s a hyper Personalisation tool for an {Customer Type}. You need to give highly persona banking and personalto user whose interest, preferences and occupation will be provided to the user.


## 🎯 Introduction
The **AI Reconciliation Tool** addresses the challenges faced in modern-day financial reconciliations by:
1. Automating anomaly detection in large datasets.
2. Allowing reconcilers to provide feedback via an interactive UI.
3. Logging anomalies and their resolutions in platforms like Jira for collaborative tracking.

4. ## 🎯 Introduction
The **AI Reconciliation Tool** addresses the challenges faced in modern-day financial reconciliations by:
1. Automating anomaly detection in large datasets.
2. Allowing reconcilers to provide feedback via an interactive UI.
3. Logging anomalies and their resolutions in platforms like Jira for collaborative tracking.

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:
[Screenshot 1](link-to-image)
---
Here are some screenshots of the application:

1. **Dashboard**:
   ![Dashboard Screenshot](https://via.placeholder.com/800x400?text=Dashboard+Screenshot)

2. **Feedback UI**:
   ![Feedback Screenshot](https://via.placeholder.com/800x400?text=Feedback+UI+Screenshot)

3. **Jira Integration**:
   ![Jira Screenshot](https://via.placeholder.com/800x400?text=Jira+Integration+Screenshot)

## 💡 Inspiration
This project was created during the [Technology Hackathon 2025] to showcase how AI-driven workflows can improve manual auditing processes.

## ⚙️ What It Does

## Features
- **Anomaly Detection**:
   - Identifies mismatches in financial datasets.
   - Highlights `PRICE` and `QUANTITY` discrepancies.
- **Feedback Collection**:
   - Interactive UI for reconcilers to resolve mismatches manually.
   - Supports custom feedback for anomalies.
- **Jira Integration**:
   - Logs anomalies as tasks or tickets in Jira.
   - Fetches resolutions and updates results in real-time.
- **Reporting**:
   - Generates CSV reports for resolved anomalies, including user feedback.

## 🛠️ How We Built It

3. **Environment Variables**:
   - Create a `.env` file in the root folder and add the following environment variables:
     ```
     JIRA_URL=https://yourcompany.atlassian.net
     JIRA_USERNAME=your_email@example.com
     JIRA_API_TOKEN=your_token
     DB_CONNECTION_STRING=<your_database_connection_string>
     ```

4. **Run the Application**:
   - Start the backend:
     ```bash
     python app.py
     ```
   - Start the Streamlit frontend:
     ```bash
     streamlit run app.py
     ```

5. **Access the Service**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:8501
   ```

---

## Usage
1. **Upload Dataset**:
   Upload your financial dataset (e.g., a CSV file) via the provided interface.
   
2. **Review Anomalies**:
   - View auto-detected mismatches in the dataset.
   - Resolve discrepancies by replacing values or adding manual comments.
   
3. **Jira Integration**:
   - The app automatically logs detected anomalies as tasks in Jira.
   - Team members can collaborate and provide feedback via Jira tickets.

4. **Generate Report**:
   - Save the final reconciliation dataset with both user feedback and Jira resolutions.


## 🚧 Challenges We Faced
Using the OPEN API was a challenging task as it required a key.

## 🏃 How to Run
1.## Setup Instructions
Follow these steps to set up the project locally.

1. **Clone the Repository**:
   ```bash
   git clone (https://github.com/ewfx/sradg-new-comers)
   cd AI-Reconciliation-Tool
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
- 🔹 Frontend: - Streamlit (for user interface)
- 🔹 Backend:  Flask RESTful API
- 🔹 Database: PostgreSQL
- 🔹 Integration Tools: Jira REST API, Pandas
- 🔹 Other: OpenAI API , Jupyter Notebooks (for exploratory data analysis)

## 👥 Team
- **Your Name** - [GitHub](#) | [LinkedIn](#)
- **Teammate 2** - [GitHub](#) | [LinkedIn](#)
