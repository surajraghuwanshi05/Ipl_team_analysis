import streamlit as st
import pandas as pd

# Load CSV files
batsman_df = pd.read_csv('batter_stats.csv')
bowler_df = pd.read_csv('bowler_stats.csv')

# Streamlit layout
st.title('Cricket Stats Dashboard')

# Batsman filters
st.subheader('Batsman Stats')

# Selectbox for batsman stat
batsman_stat = st.selectbox('Select Batsman Stat', ['Batsman Runs', 'Strike Rate', 'Average'])
batsman_value = st.slider(f'Select minimum {batsman_stat}', min_value=0, max_value=int(batsman_df[batsman_stat].max()), value=0)

# Selectbox for sorting order
batsman_sort_order = st.selectbox('Sort Batsman Stats', ['Descending', 'Ascending'])

# Filter batsman data
filtered_batsman_df = batsman_df[batsman_df[batsman_stat] >= batsman_value]
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
bowler_stat = st.selectbox('Select Bowler Stat', ['Innings', 'Overs', 'Wickets', 'Economy', 'Average'])
bowler_value = st.slider(f'Select minimum {bowler_stat}', min_value=0, max_value=int(bowler_df[bowler_stat].max()), value=0)

# Selectbox for sorting order
bowler_sort_order = st.selectbox('Sort Bowler Stats', ['Descending','Ascending' ])

# Filter bowler data
filtered_bowler_df = bowler_df[bowler_df[bowler_stat] >= bowler_value]
# Sort data


if bowler_sort_order == 'Ascending':
    filtered_bowler_df = filtered_bowler_df.sort_values(by=bowler_stat, ascending=True)
else:
    filtered_bowler_df = filtered_bowler_df.sort_values(by=bowler_stat, ascending=False)

if st.button("show bowler's data"):
    st.dataframe(filtered_bowler_df)
