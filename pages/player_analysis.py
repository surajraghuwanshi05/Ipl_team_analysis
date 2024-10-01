import streamlit as st
import pandas as pd

# Load CSV files
batsman_df = pd.read_csv('dataset/batter_stats.csv')
bowler_df = pd.read_csv('dataset/bowler_stats.csv')
player_df = pd.read_csv("dataset/all_rounders.csv")

# Streamlit layout
st.title('Cricket Stats Dashboard')

# Batsman filters
st.subheader('Batsman Stats')

# Selectbox for batsman stat
batsman_stat = st.selectbox('Select Batsman Stat', ['Batsman Runs', 'Strike Rate',"Impact Score", 'Average'])
batsman_value = st.slider(f'Select minimum Batsman Runs', min_value=0, max_value=int(batsman_df['Batsman Runs'].max()), value=150)

# Selectbox for sorting order
batsman_sort_order = st.selectbox('Sort Batsman Stats', ['Descending', 'Ascending'])

# Filter batsman data
filtered_batsman_df = batsman_df[batsman_df['Batsman Runs'] >= batsman_value]
# Sort data

if batsman_sort_order == 'Ascending':
    filtered_batsman_df = filtered_batsman_df.sort_values(by=batsman_stat, ascending=True)
else:
    filtered_batsman_df = filtered_batsman_df.sort_values(by=batsman_stat, ascending=False)

if st.button("show batter's data"):
    st.dataframe(filtered_batsman_df)

# Bowler filters
st.subheader('Bowler Stats')

# Selectbox for bowler stat
bowler_stat = st.selectbox('Select Bowler Stat', ['Overs', 'Wickets',"Impact Score", 'Economy', 'Average'])
bowler_value = st.slider(f'Select minimum Overs', min_value=0, max_value=int(bowler_df['Overs'].max()), value=8)

# Selectbox for sorting order
bowler_sort_order = st.selectbox('Sort Bowler Stats', ['Descending','Ascending' ])

# Filter bowler data
filtered_bowler_df = bowler_df[bowler_df["Overs"] >= bowler_value]
# Sort data


if bowler_sort_order == 'Ascending':
    filtered_bowler_df = filtered_bowler_df.sort_values(by=bowler_stat, ascending=True)
else:
    filtered_bowler_df = filtered_bowler_df.sort_values(by=bowler_stat, ascending=False)

if st.button("show bowler's data"):
    st.dataframe(filtered_bowler_df)




# Player filters
st.subheader('All Rounders Stats')

# Selectbox for batsman stat
player_stats = st.selectbox('Select  Stat', ['Batsman Runs', 'Strike Rate', 'Average', 'Wickets', 'Economy'])
player_value_runs = st.slider(f'Select minimum Runs', min_value=0, max_value=int(player_df['Batsman Runs'].max()), value=100)
player_value_wkt = st.slider(f'Select minimum Wickets', min_value=0, max_value=int(player_df['Wickets'].max()), value=5)

# Selectbox for sorting order
player_sort_order = st.selectbox('Sort Stats', ['Descending', 'Ascending'])

# Filter batsman data
filtered_player_df = player_df[(player_df['Batsman Runs'] >= player_value_runs)& (player_df['Wickets'] >= player_value_wkt)]
# Sort data

if player_sort_order == 'Ascending':
    filtered_player_df = filtered_player_df.sort_values(by=player_stats, ascending=True)
else:
    filtered_player_df = filtered_player_df.sort_values(by=player_stats, ascending=False)

if st.button("show allrounder's data"):
    st.dataframe(filtered_player_df)
