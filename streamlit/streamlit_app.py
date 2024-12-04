import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

# Load data and models
player_data = pd.read_csv("../data/player_stats_by_team/combined/filtered_player_stats.csv")
club_model = pickle.load(open("../streamlit/xgboost_club_model.pkl", "rb"))
player_model = pickle.load(open("../streamlit/linear_regression_player_model.pkl", "rb"))
club_feature_names = pickle.load(open("../streamlit/club_model_feature_names.pkl", "rb"))

formation_data = {
    "4-3-3": ["Goalkeeper", "DF", "DF", "DF", "DF", "MF", "MF", "MF", "FW", "FW", "FW"],
    "4-4-2": ["Goalkeeper", "DF", "DF", "DF", "DF", "MF", "MF", "MF", "MF", "FW", "FW"],
    "3-5-2": ["Goalkeeper", "DF", "DF", "DF", "MF", "MF", "MF", "MF", "MF", "FW", "FW"],
}

# Helper function to preprocess data
def preprocess_data(data, feature_names):
    """
    Preprocesses the data by encoding categorical variables and aligning with feature names.
    """
    # One-hot encode categorical variables
    preprocessed_data = pd.get_dummies(data, drop_first=True)

    # Align columns with model features
    preprocessed_data = preprocessed_data.reindex(columns=feature_names, fill_value=0)

    return preprocessed_data

# Helper function to calculate team metrics
def calculate_team_metrics(selected_players):
    selected_data = player_data[player_data["Player"].isin(selected_players)]

    if selected_data.empty:
        st.warning("No players selected. Please select valid players.")
        return None, None, None

    # Preprocess data for the club model
    preprocessed_data = preprocess_data(selected_data.drop(columns=["Balanced_Performance"]), club_feature_names)

    # Predict points per match using the club model
    predicted_pts_mp = club_model.predict(preprocessed_data)

    # Calculate average balanced performance
    avg_balanced_performance = selected_data["Balanced_Performance"].mean()

    # Determine the best formation
    best_formation = max(
        formation_data,
        key=lambda x: len(set(selected_data["Pos"]) & set(formation_data[x]))
    )

    return best_formation, predicted_pts_mp.mean(), avg_balanced_performance

# Streamlit UI
st.title("Team Builder and Formation Predictor")
st.write("Select players to form a team and get insights on the best formation, predicted points per match, and balanced performance.")

# Allow user to select multiple players by position
positions = ["GK", "DF", "MF", "FW"]
selected_players = []

for position in positions:
    available_players = player_data[player_data["Pos"].str.contains(position, na=False)]["Player"].unique()
    selected_players_per_position = st.multiselect(f"Select {position}s", available_players, key=position)
    selected_players.extend(selected_players_per_position)

# Add button to calculate results
if st.button("Calculate Results"):
    if selected_players:
        best_formation, predicted_pts_mp, avg_balanced_performance = calculate_team_metrics(selected_players)

        if best_formation:
            st.subheader("Team Insights")
            st.write(f"**Best Formation (Based on Selected Players):** {best_formation}")
            st.write(f"**Predicted Points per Match:** {predicted_pts_mp:.2f}")
            st.write(f"**Average Balanced Performance:** {avg_balanced_performance:.2f}")

            st.write("### Selected Players")
            st.dataframe(player_data[player_data["Player"].isin(selected_players)])
    else:
        st.warning("Please select players for all positions.")
