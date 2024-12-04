# Game Plan Generator

## Problem Statement

In the world of football, team formation and player selection are crucial factors in determining a team's success on the pitch. Many teams struggle with identifying the optimal formation and the best combination of players to field in order to maximize performance, whether it's points per match or overall player balance. This project aims to address that gap by building a "Game Plan Generator" — a Streamlit app that helps users create an optimal formation and predict a team's expected performance metrics based on player selection.

## Research Question

The core question driving this project is:

*"What is the best team formation and player combination that can maximize performance, in terms of predicted points per match and balanced performance metrics?"*

This app seeks to provide football enthusiasts, analysts, and coaches with data-driven insights on which player combinations and formations yield the best expected results.

## Table of Contents

- Game Plan Generator
  - Problem Statement
  - Research Question
  - Analysis and Structure
  - Data Collection and Processing
  - Exploratory Data Analysis (EDA)
  - Model Development
  - Model Evaluation and Performance
  - App Features
  - Setup Instructions and Software Requirements

---

## Analysis and Structure

### Notebooks:
1. **Data Collection and Preparation:** Data cleaning, feature extraction, and dataset consolidation for both player and team datasets.
2. **Model Development and Benchmarks:** Initial model training for both the team and player datasets using algorithms like Linear Regression and XGBoost.
3. **Model Tuning and Evaluation:** Fine-tuning models and selecting the optimal configuration for predicting points per match and balanced performance.
4. **Final App Implementation:** Integrating the model into the Streamlit interface, creating a cohesive user experience for optimal formation generation.

---

## Executive Summary

### Introduction
The Game Plan Generator provides a practical interface for users to simulate different football team formations, select individual players, and understand how these selections impact team performance. Using machine learning models trained on Premier League club statistics and individual player stats, the app calculates the expected points per match and balanced player performance, providing insights on which players fit well together and which formation would yield the best outcome.

### Data Collection and Processing
The project used player-level and club-level datasets:

- **Player Dataset:** Contains filtered individual player statistics from the Premier League.
- **Club Dataset:** Contains club-level aggregated data and statistics that serve as features for predicting points per match (Pts/MP).

Key data cleaning and preparation steps:
- **Dropping Redundant Features:** Removed columns like Player Name, Nation, Team, etc., to prevent data leakage during training.
- **One-Hot Encoding:** Categorical features were converted using `pd.get_dummies()` to prepare data for modeling.
- **Splitting Data:** Data was split into training and testing sets for both the team and player models.

### Exploratory Data Analysis (EDA)
EDA was conducted to gain insights into the data distribution and correlations among various features:

- **Team Performance vs. Formation:** Correlations between team formations and total points were examined.
- **Player Attributes:** Different player roles (FW, MF, DF) were analyzed in relation to their balanced performance metrics.

### Model Development
Two main models were developed for this project:

1. **Club Model (XGBoost):** Predicts the points per match for different team formations and player combinations.
2. **Player Model (Linear Regression):** Predicts individual balanced performance metrics.

**Models Evaluated:**
- **Linear Regression** for predicting player performance.
- **XGBoost Regressor** for predicting the overall club performance based on the selected team.

**Evaluation Metrics:** Root Mean Squared Error (RMSE) and R² were used to assess model performance on training and test datasets.

### Model Evaluation and Performance
Summary of model performance metrics for the chosen algorithms:

- **Linear Regression (Player Model):** Achieved consistent predictions with an acceptable RMSE.
- **XGBoost (Club Model):** Outperformed other models in terms of predicting points per match, with an R² score of 0.95 and a very low RMSE.

---

## App Features

### User Functionality
- **Player Selection:** Users can select players to form a team. The app allows selection based on formation.
- **Formation Prediction:** Users can select a formation, and the app will predict which formation works best for the selected players.
- **Predicted Metrics:**
  - **Best Formation:** Calculates the best fit based on the selected players' roles.
  - **Predicted Points per Match:** Predicts the team's performance in points per match.
  - **Average Balanced Performance:** Predicts average player performance.

**Interactive Elements**:
- A button for calculating results based on the selected team.
- Dropdowns for selecting players based on formation and role.

---

## Setup Instructions and Software Requirements

To run the Game Plan Generator locally, follow these steps:

### Prerequisites
- Python 3.8 or higher.
- A modern web browser.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/game-plan-generator.git
   cd game-plan-generator
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App
1. Navigate to the project directory and run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```
2. The app will open in your default web browser at `http://localhost:8501`.

---

## Required Packages
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: For model building and evaluation.
- **XGBoost**: For training the club model.
- **Streamlit**: For creating the user interface.
- **Pickle**: For saving and loading models.

---

## Conclusion
The Game Plan Generator demonstrates the power of machine learning in helping users optimize player selection and formation in football. It provides data-driven insights into formations, individual player contributions, and expected match outcomes, allowing for better decision-making and planning.

Key Takeaways:
- **Optimal Team Selection:** The models help find the best possible combination of players and formations.
- **Performance Prediction:** The app provides a realistic expectation of points per match and player performance.

### Next Steps
- **Expand Dataset**: Include additional features like player injury history, fatigue metrics, or other team statistics.
- **Further Model Improvements**: Use advanced models such as ensemble techniques or neural networks.

---
This README provides a comprehensive overview of the project, including installation steps and usage instructions. Feel free to explore, contribute, or adapt the Game Plan Generator for your use case.

