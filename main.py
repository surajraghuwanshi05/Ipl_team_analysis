import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from batting import batting_comparision, batting_comparison_by_over, wickets_comparison
from bowling import initialize_team_players, run_conced_comparision, taken_wkt_comparision, get_bowling_team



st.set_page_config(
    page_title="Multipage App",
)



# Load the data
match_data0 = pd.read_csv("IPL_Matches_2022.csv")
ball_data0 = pd.read_csv("IPL_Ball_by_Ball_2022.csv")

# Remove invalid match IDs
match_data = match_data0[~match_data0["ID"].isin([1312200, 1312199, 1312198, 1312197])]
ball_data = ball_data0[~ball_data0["ID"].isin([1312200, 1312199, 1312198, 1312197])]

# Initialize team players
team_players = initialize_team_players(match_data)
ball_data['BowlingTeam'] = ball_data['bowler'].apply(get_bowling_team, args=(team_players,))

# Streamlit app
st.title("IPL 2022 Team Performance Analysis")
st.sidebar.success("Select a page above.")

# Select teams (allow multiple selection)
team_list = sorted(ball_data["BattingTeam"].unique())
team1 = st.multiselect("Select Team 1 (multiple teams allowed)", team_list, default=[team_list[0]])
team2 = st.multiselect("Select Team 2 (multiple teams allowed)", team_list, default=[team_list[1]])

# Select analysis type
analysis_type = st.selectbox("Select Analysis Type", ["Compare Runs by Phases", "Compare Runs by Over", "Compare Lost Wickets", "Run Conceded by Bowlers", "Wicket Taken by Bowlers"])

# Button to trigger analysis
if st.button("Generate Graph"):
    if analysis_type == "Compare Runs by Phases":
        fig = batting_comparision(team1, team2, ball_data)  # Lists are passed
        st.pyplot(fig)
    elif analysis_type == "Compare Runs by Over":
        fig = batting_comparison_by_over(team1, team2, ball_data)
        st.pyplot(fig)
    elif analysis_type == "Compare Lost Wickets":
        fig = wickets_comparison(team1, team2, ball_data)
        st.pyplot(fig)
    elif analysis_type == "Run Conceded by Bowlers":
        fig = run_conced_comparision(team1, team2, ball_data)
        st.pyplot(fig)
    elif analysis_type == "Wicket Taken by Bowlers":
        fig = taken_wkt_comparision(team1, team2, ball_data)
        st.pyplot(fig)



