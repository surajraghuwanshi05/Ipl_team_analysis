import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
from main import ball_data


short_names = {
    'Sunrisers Hyderabad': 'SRH',
    'Punjab Kings': 'PBKS',
    'Delhi Capitals': 'DC',
    'Mumbai Indians': 'MI',
    'Chennai Super Kings': 'CSK',
    'Rajasthan Royals': 'RR',
    'Gujarat Titans': 'GT',
    'Royal Challengers Bangalore': 'RCB',
    'Lucknow Super Giants': 'LSG',
    'Kolkata Knight Riders': 'KKR'
}

def plot_runs_per_match(ball_data):
    total_runs = ball_data.groupby("BattingTeam")["total_run"].sum() / 14
    total_runs.index = total_runs.index.map(short_names)
    fig, ax1 = plt.subplots(figsize=(10, 6))
    total_runs.plot(kind='bar', color='skyblue', ax=ax1)
    ax1.set_title('Runs per Match by Teams', fontsize=20)
    ax1.set_ylabel('Runs', fontsize=15)
    ax1.set_xlabel('Batting Team', fontsize=15)
    ax1.set_xticklabels(total_runs.index, rotation=0, ha='right')
    for bar in ax1.patches:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')
    plt.tight_layout()
    return fig

def plot_lost_wkt_per_match(ball_data):
    total_wkt = ball_data.groupby("BattingTeam")["isWicketDelivery"].sum() / 14
    total_wkt.index = total_wkt.index.map(short_names)
    fig, ax1 = plt.subplots(figsize=(10, 6))
    total_wkt.plot(kind='bar', color='lightcoral', ax=ax1)
    ax1.set_title('Wicket Lost per Match by Teams', fontsize=20)
    ax1.set_ylabel('Wickets', fontsize=15)
    ax1.set_xlabel('Batting Team', fontsize=15)
    ax1.set_xticklabels(total_wkt.index, rotation=0, ha='right')
    for bar in ax1.patches:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')
    plt.tight_layout()
    return fig

def plot_runs_conceded_per_match(ball_data):
    total_runs = ball_data.groupby("BowlingTeam")["total_run"].sum() / 14
    total_runs.index = total_runs.index.map(short_names)
    fig, ax1 = plt.subplots(figsize=(10, 6))
    total_runs.plot(kind='bar', color='skyblue', ax=ax1)
    ax1.set_title('Runs Conceded per Match by Teams', fontsize=20)
    ax1.set_ylabel('Runs', fontsize=15)
    ax1.set_xlabel('Bowling Team', fontsize=15)
    ax1.set_xticklabels(total_runs.index, rotation=0, ha='right')
    for bar in ax1.patches:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')
    plt.tight_layout()
    return fig

def plot_wkt_taken_per_match(ball_data):
    total_wkt = ball_data.groupby("BowlingTeam")["isWicketDelivery"].sum() / 14
    total_wkt.index = total_wkt.index.map(short_names)
    fig, ax1 = plt.subplots(figsize=(10, 6))
    total_wkt.plot(kind='bar', color='lightgreen', ax=ax1)
    ax1.set_title('Wickets Taken per Match by Teams', fontsize=20)
    ax1.set_ylabel('Wickets', fontsize=15)
    ax1.set_xlabel('Bowling Team', fontsize=15)
    ax1.set_xticklabels(total_wkt.index, rotation=0, ha='right')
    for bar in ax1.patches:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')
    plt.tight_layout()
    return fig

st.title("IPL 2022 Teams Performance Comparison")
    

    
option = st.selectbox(
    'Select the type of plot',
    ('Runs per Match', 'Wickets Lost per Match', 'Runs Conceded per Match', 'Wickets Taken per Match')
)

# Button to trigger analysis
if st.button("Generate Graph"):    
    if option == 'Runs per Match':
        fig = plot_runs_per_match(ball_data)
    elif option == 'Wickets Lost per Match':
        fig = plot_lost_wkt_per_match(ball_data)
    elif option == 'Runs Conceded per Match':
        fig = plot_runs_conceded_per_match(ball_data)
    elif option == 'Wickets Taken per Match':
        fig = plot_wkt_taken_per_match(ball_data)
        
    st.pyplot(fig)