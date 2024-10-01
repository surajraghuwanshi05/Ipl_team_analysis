import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




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

# Define the batting comparison function
def batting_comparision(Team1, Team2, ball_data):
    # Calculate runs for team 1
    powerplay_runs = ball_data[(ball_data["BattingTeam"].isin(Team1)) & (ball_data['overs'] < 6)]["total_run"].sum()
    middle_overs_runs = ball_data[(ball_data["BattingTeam"].isin(Team1)) & (ball_data['overs'] > 5) & (ball_data['overs'] < 15)]["total_run"].sum()
    death_overs_runs = ball_data[(ball_data["BattingTeam"].isin(Team1)) & (ball_data['overs'] > 14)]["total_run"].sum()

    # Calculate runs for team 2
    powerplay_runs_2 = ball_data[(ball_data["BattingTeam"].isin(Team2)) & (ball_data['overs'] < 6)]["total_run"].sum()
    middle_overs_runs_2 = ball_data[(ball_data["BattingTeam"].isin(Team2)) & (ball_data['overs'] > 5) & (ball_data['overs'] < 15)]["total_run"].sum()
    death_overs_runs_2 = ball_data[(ball_data["BattingTeam"].isin(Team2)) & (ball_data['overs'] > 14)]["total_run"].sum()

    # Create arrays for phases, total runs, and per over runs for both teams
    phases = np.array(["Powerplay", "Middle Overs", "Death Overs"])
    total_runs_1 = np.array([powerplay_runs, middle_overs_runs, death_overs_runs])
    total_runs_2 = np.array([powerplay_runs_2, middle_overs_runs_2, death_overs_runs_2])

    per_over_1 = np.array([powerplay_runs / 6, middle_overs_runs / 9, death_overs_runs / 5])
    per_over_2 = np.array([powerplay_runs_2 / 6, middle_overs_runs_2 / 9, death_overs_runs_2 / 5])

    # Set the width of the bars and their positions
    bar_width = 0.35
    x = np.arange(len(phases))  # label locations
    
    max_total_runs = max(max(total_runs_1 / (14*len(Team1))), max(total_runs_2 / (14*len(Team2)))) + 2
    max_per_over_runs = max(max(per_over_1 / (14*len(Team1))), max(per_over_2 / (14*len(Team2)))) + 0.5

    # Set up the figure and subplots (2 subplots)
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10, 10))
    
    
    plt.subplots_adjust(wspace=0.4)

    # Total runs comparison
    bars1 = ax1.bar(x - bar_width / 2, total_runs_1/(14*len(Team1)), width=bar_width, label=f'{", ".join([short_names[team] for team in Team1])}', color='skyblue')
    bars2 = ax1.bar(x + bar_width / 2, total_runs_2/(14*len(Team2)), width=bar_width, label=f'{", ".join([short_names[team] for team in Team2])}', color='lightcoral')
    ax1.set(title='Total Runs per Match', ylabel="Total Runs", xlabel="Phases")
    ax1.set_ylim(0, max_total_runs + 25)  # Ensure the same y-axis range for total runs comparison
    ax1.set_xticks(x)
    ax1.set_xticklabels(phases)
    ax1.legend()

    # Display values on each bar (Team 1 & Team 2 total runs)
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    for bar in bars2:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    # Runs per over comparison
    bars3 = ax2.bar(x - bar_width / 2, per_over_1/(14*len(Team1)), width=bar_width, label=f'{", ".join([short_names[team] for team in Team1])}', color='skyblue')
    bars4 = ax2.bar(x + bar_width / 2, per_over_2/(14*len(Team2)), width=bar_width, label=f'{", ".join([short_names[team] for team in Team2])}', color='lightcoral')
    ax2.set(title='Runs per Over', ylabel="Runs per Over", xlabel="Phases")
    ax2.set_ylim(0, max_per_over_runs + 2.5)
    ax2.set_xticks(x)
    ax2.set_xticklabels(phases)
    ax2.legend()

    # Display values on each bar (Team 1 & Team 2 runs per over)
    for bar in bars3:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    for bar in bars4:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    # Add a main title for the entire figure
    fig.suptitle('Team Performance Analysis in Different Phases', fontsize=16)

    return fig

# Define the function to compare batting by overs
def batting_comparison_by_over(Team1, Team2, ball_data):
    # Filter data for Team1 and Team2
    team1_data = ball_data[ball_data["BattingTeam"].isin(Team1)]
    team2_data = ball_data[ball_data["BattingTeam"].isin(Team2)]

    # Calculate total runs scored in each over for both teams
    runs_by_over_team1 = team1_data.groupby('overs')['total_run'].sum().reindex(range(0, 20), fill_value=0)
    runs_by_over_team2 = team2_data.groupby('overs')['total_run'].sum().reindex(range(0, 20), fill_value=0)

    # Create arrays for overs and runs
    overs = runs_by_over_team1.index
    total_runs_1 = runs_by_over_team1.values
    total_runs_2 = runs_by_over_team2.values

    # Convert overs from 0-19 to 1-20 for display
    overs_display = [over + 1 for over in overs]

    # Set up the figure and subplots
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))
    plt.subplots_adjust(hspace=0.4)

    # Team 1: Runs by Over
    bars1 = ax1.bar(overs_display, total_runs_1, color='skyblue', label=f'{Team1[0]}')
    ax1.set(title=f'{", ".join([short_names[team] for team in Team1])} - Runs per Over', xlabel='Over', ylabel='Runs')
    ax1.set_xticks(overs_display)  # Set x-ticks to show all overs
    ax1.set_xticklabels([str(over) for over in overs_display])  # Label x-ticks with over numbers

    # Add values on the bars for Team 1
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', ha='center', va='bottom')

    # Team 2: Runs by Over
    bars2 = ax2.bar(overs_display, total_runs_2, color='lightcoral', label=f'{Team2[0]}')
    ax2.set(title=f'{", ".join([short_names[team] for team in Team2])} - Runs per Over', xlabel='Over', ylabel='Runs')
    ax2.set_xticks(overs_display)  # Set x-ticks to show all overs
    ax2.set_xticklabels([str(over) for over in overs_display])  # Label x-ticks with over numbers

    # Add values on the bars for Team 2
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{height}', ha='center', va='bottom')

    # Add a main title for the entire figure
    fig.suptitle('Runs Scored by Each Over', fontsize=16)

    return fig


def wickets_comparison(Team1, Team2, ball_data):
    # Wickets lost for team 1 in different phases
    powerplay_wickets = ball_data[(ball_data["BattingTeam"].isin(Team1)) & (ball_data['overs'] < 6)]["isWicketDelivery"].sum()
    middle_overs_wickets = ball_data[(ball_data["BattingTeam"].isin(Team1)) & (ball_data['overs'] > 5) & (ball_data['overs'] < 15)]["isWicketDelivery"].sum()
    death_overs_wickets = ball_data[(ball_data["BattingTeam"].isin(Team1)) & (ball_data['overs'] > 14)]["isWicketDelivery"].sum()

    # Wickets lost for team 2 in different phases
    powerplay_wickets_2 = ball_data[(ball_data["BattingTeam"].isin(Team2)) & (ball_data['overs'] < 6)]["isWicketDelivery"].sum()
    middle_overs_wickets_2 = ball_data[(ball_data["BattingTeam"].isin(Team2)) & (ball_data['overs'] > 5) & (ball_data['overs'] < 15)]["isWicketDelivery"].sum()
    death_overs_wickets_2 = ball_data[(ball_data["BattingTeam"].isin(Team2)) & (ball_data['overs'] > 14)]["isWicketDelivery"].sum()
    
    
    
    
    
    # Total wickets lost per phase for each team
    total_wickets_1 = np.array([powerplay_wickets, middle_overs_wickets, death_overs_wickets])
    total_wickets_2 = np.array([powerplay_wickets_2, middle_overs_wickets_2, death_overs_wickets_2])

    # Average wickets lost per match for each team
    avg_wickets_1 = total_wickets_1 / (len(Team1) * 14)
    avg_wickets_2 = total_wickets_2 / (len(Team2) * 14)

    # Graph generation
    phases = np.array(["Powerplay", "Middle Overs", "Death Overs"])
    
    
    # Set the width of the bars and their positions
    bar_width = 0.35
    x = np.arange(len(phases))  # label locations

    fig,(ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10,10))
    plt.subplots_adjust(wspace=0.4)

    # Set the same y-axis limit for total wickets comparison
    max_total_wickets = max(max(total_wickets_1/len(Team1)), max(total_wickets_2/len(Team2))) + 5

    # Team 1 total wickets lost
    bars1=ax1.bar(x- bar_width / 2, total_wickets_1/len(Team1), width=bar_width, label=f'{", ".join([short_names[team] for team in Team1])}', color="skyblue")
    bars2 = ax1.bar(x+bar_width / 2, total_wickets_2/len(Team2), width=bar_width, label=f'{", ".join([short_names[team] for team in Team2])}',color="lightcoral")
    ax1.set_ylim(0, max_total_wickets + 10)
    ax1.set_xticks(x)
    ax1.set_xticklabels(phases)
    ax1.legend()
    
    
    # Display values on each bar (Team 1 & Team 2 total runs)
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    for bar in bars2:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    # Set the same y-axis limit for average wickets comparison
    max_avg_wickets = max(max(avg_wickets_1), max(avg_wickets_2)) + 0.5

    # Team 1 average wickets lost per match
    bars3 = ax2.bar(x- bar_width / 2, avg_wickets_1, width=bar_width, label=f'{", ".join([short_names[team] for team in Team1])}', color="skyblue")
    bars4 = ax2.bar(x+ bar_width / 2, avg_wickets_2, width=bar_width, label=f'{", ".join([short_names[team] for team in Team2])}', color="lightcoral" )
    ax2.set_ylim(0, max_avg_wickets + 1)
    ax2.set_xticks(x)
    ax2.set_xticklabels(phases)
    ax2.legend()
    
    
    
    # Display values on each bar (Team 1 & Team 2 runs per over)
    for bar in bars3:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    for bar in bars4:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')
    

    # Add a main title for the entire figure
    fig.suptitle('Wickets Lost Analysis in Different Phases', fontsize=16)

    # Add two combined titles
    fig.text(0.5, 0.92, 'Total Wickets Lost Comparison', ha='center', fontsize=14)
    fig.text(0.5, 0.48, 'Average Wickets Lost Comparison', ha='center', fontsize=14)

    return fig