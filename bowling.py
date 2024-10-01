import numpy as np
import matplotlib.pyplot as plt



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

# Function to clean player list strings and convert them into actual lists
def clean_player_list(player_string):
    # Remove square brackets and extra quotes, then split by commas
    return player_string.strip("[]").replace("'", "").split(", ")

# Function to initialize team players
def initialize_team_players(match_data):
    team_players = {}

    # Process Team1Players and Team2Players columns
    for index, row in match_data.iterrows():
        # Clean player lists for both teams
        team1 = row['Team1']
        team2 = row['Team2']
        
        team1_players = clean_player_list(row['Team1Players'])
        team2_players = clean_player_list(row['Team2Players'])
        
        # Add players to their respective teams
        if team1 not in team_players:
            team_players[team1] = set()
        if team2 not in team_players:
            team_players[team2] = set()
        
        team_players[team1].update(team1_players)
        team_players[team2].update(team2_players)

    # Convert sets to sorted lists for easier reading
    team_players = {team: sorted(players) for team, players in team_players.items()}
    return team_players


def get_bowling_team(bowler,team_players):
    for team, players in team_players.items():
        if bowler in players:
            return team
    return None

# Function for bowling comparison analysis
def run_conced_comparision(Team1, Team2, ball_data):
    # Calculate runs conceded by Team 1 in different phases
    powerplay_runs_cd = ball_data[(ball_data['BowlingTeam'].isin(Team1)) & (ball_data["overs"] < 6)]["total_run"].sum()
    middle_overs_runs_cd = ball_data[(ball_data['BowlingTeam'].isin(Team1)) & (ball_data["overs"] > 5) & (ball_data["overs"] < 15)]["total_run"].sum()
    death_overs_runs_cd = ball_data[(ball_data['BowlingTeam'].isin(Team1)) & (ball_data["overs"] > 14)]["total_run"].sum()

    # Calculate runs conceded by Team 2 in different phases
    powerplay_runs_cd2 = ball_data[(ball_data['BowlingTeam'].isin(Team2)) & (ball_data["overs"] < 6)]["total_run"].sum()
    middle_overs_runs_cd2 = ball_data[(ball_data['BowlingTeam'].isin(Team2)) & (ball_data["overs"] > 5) & (ball_data["overs"] < 15)]["total_run"].sum()
    death_overs_runs_cd2 = ball_data[(ball_data['BowlingTeam'].isin(Team2)) & (ball_data["overs"] > 14)]["total_run"].sum()

    # Create arrays for phases, total runs conceded, and per over runs conceded
    phases = np.array(["Powerplay", "Middle Overs", "Death Overs"])
    total_runs_cd = np.array([powerplay_runs_cd, middle_overs_runs_cd, death_overs_runs_cd])
    total_runs_cd2 = np.array([powerplay_runs_cd2, middle_overs_runs_cd2, death_overs_runs_cd2])

    per_over_cd = np.array([powerplay_runs_cd / 6, middle_overs_runs_cd / 9, death_overs_runs_cd / 5])
    per_over_cd2 = np.array([powerplay_runs_cd2 / 6, middle_overs_runs_cd2 / 9, death_overs_runs_cd2 / 5])

    # Set the width of the bars and their positions
    bar_width = 0.35
    x = np.arange(len(phases))  # label locations
    
    max_total_runs_cd = max(max(total_runs_cd / (14*len(Team1))), max(total_runs_cd2 / (14*len(Team2)))) + 2
    max_per_over_runs_cd = max(max(per_over_cd / (14*len(Team1))), max(per_over_cd2 / (14*len(Team2)))) + 0.5

    # Set up the figure and subplots (2 subplots)
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10, 10))
    plt.subplots_adjust(wspace=0.4)

    # Total runs conceded comparison
    bars1 = ax1.bar(x - bar_width / 2, total_runs_cd/(14*len(Team1)), width=bar_width, label=f'{", ".join([short_names[team] for team in Team1])}', color='skyblue')
    bars2 = ax1.bar(x + bar_width / 2, total_runs_cd2/(14*len(Team2)), width=bar_width, label=f'{", ".join([short_names[team] for team in Team2])}', color='lightcoral')
    ax1.set(title='Total Runs Conceded per Match', ylabel="Total Runs", xlabel="Phases")
    ax1.set_ylim(0, max_total_runs_cd + 25)  # Ensure the same y-axis range for total runs comparison
    ax1.set_xticks(x)
    ax1.set_xticklabels(phases)
    ax1.legend()

    # Display values on each bar (Team 1 & Team 2 total runs conceded)
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    for bar in bars2:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    # Runs conceded per over comparison
    bars3 = ax2.bar(x - bar_width / 2, per_over_cd/(14*len(Team1)), width=bar_width, label=f'{", ".join([short_names[team] for team in Team1])}', color='skyblue')
    bars4 = ax2.bar(x + bar_width / 2, per_over_cd2/(14*len(Team2)), width=bar_width, label=f'{", ".join([short_names[team] for team in Team2])}', color='lightcoral')
    ax2.set(title='Runs Conceded per Over', ylabel="Runs per Over", xlabel="Phases")
    ax2.set_ylim(0, max_per_over_runs_cd + 2.5)
    ax2.set_xticks(x)
    ax2.set_xticklabels(phases)
    ax2.legend()

    # Display values on each bar (Team 1 & Team 2 runs conceded per over)
    for bar in bars3:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    for bar in bars4:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    # Add a main title for the entire figure
    fig.suptitle('Bowling Performance Analysis: Runs Conceded in Different Phases', fontsize=16)

    return fig






def taken_wkt_comparision(Team1, Team2, ball_data):
    # Wickets taken by Team 1 bowlers in different phases
    powerplay_wickets_tk = ball_data[(ball_data['BowlingTeam'].isin(Team1)) & (ball_data["overs"] < 6)]['isWicketDelivery'].sum()
    middle_overs_wickets_tk = ball_data[(ball_data['BowlingTeam'].isin(Team1)) & (ball_data["overs"] > 5) & (ball_data["overs"] < 15)]['isWicketDelivery'].sum()
    death_overs_wickets_tk = ball_data[(ball_data['BowlingTeam'].isin(Team1)) & (ball_data["overs"] > 14)]['isWicketDelivery'].sum()

    # Wickets taken by Team 2 bowlers in different phases
    powerplay_wickets_tk2 = ball_data[(ball_data['BowlingTeam'].isin(Team2)) & (ball_data["overs"] < 6)]['isWicketDelivery'].sum()
    middle_overs_wickets_tk2 = ball_data[(ball_data['BowlingTeam'].isin(Team2)) & (ball_data["overs"] > 5) & (ball_data["overs"] < 15)]['isWicketDelivery'].sum()
    death_overs_wickets_tk2 = ball_data[(ball_data['BowlingTeam'].isin(Team2)) & (ball_data["overs"] > 14)]['isWicketDelivery'].sum()

    # Total wickets taken per phase for each team
    total_wickets_tk1 = np.array([powerplay_wickets_tk, middle_overs_wickets_tk, death_overs_wickets_tk])
    total_wickets_tk2 = np.array([powerplay_wickets_tk2, middle_overs_wickets_tk2, death_overs_wickets_tk2])

    # Average wickets taken per match for each team
    avg_wickets_tk1 = total_wickets_tk1 / (len(Team1) * 14)
    avg_wickets_tk2 = total_wickets_tk2 / (len(Team2) * 14)

    # Graph generation
    phases = np.array(["Powerplay", "Middle Overs", "Death Overs"])
    
    # Set the width of the bars and their positions
    bar_width = 0.35
    x = np.arange(len(phases))  # label locations

    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10,10))
    plt.subplots_adjust(wspace=0.4)

    # Set the same y-axis limit for total wickets comparison
    max_total_wickets = max(max(total_wickets_tk1/len(Team1)), max(total_wickets_tk2/len(Team2))) + 5

    # Team 1 total wickets taken
    bars1 = ax1.bar(x - bar_width / 2, total_wickets_tk1 / len(Team1), width=bar_width, label=f'{", ".join([short_names[team] for team in Team1])}', color="skyblue")
    # Team 2 total wickets taken
    bars2 = ax1.bar(x + bar_width / 2, total_wickets_tk2 / len(Team2), width=bar_width, label=f'{", ".join([short_names[team] for team in Team2])}', color="lightcoral")
    
    ax1.set_ylim(0, max_total_wickets + 10)
    ax1.set_xticks(x)
    ax1.set_xticklabels(phases)
    ax1.legend()

    # Display values on each bar (Team 1 & Team 2 total wickets taken)
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    for bar in bars2:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    # Set the same y-axis limit for average wickets comparison
    max_avg_wickets = max(max(avg_wickets_tk1), max(avg_wickets_tk2)) + 0.5

    # Team 1 average wickets taken per match
    bars3 = ax2.bar(x - bar_width / 2, avg_wickets_tk1, width=bar_width, label=f'{", ".join([short_names[team] for team in Team1])}', color="skyblue")
    # Team 2 average wickets taken per match
    bars4 = ax2.bar(x + bar_width / 2, avg_wickets_tk2, width=bar_width, label=f'{", ".join([short_names[team] for team in Team2])}', color="lightcoral")
    
    ax2.set_ylim(0, max_avg_wickets + 1)
    ax2.set_xticks(x)
    ax2.set_xticklabels(phases)
    ax2.legend()

    # Display values on each bar (Team 1 & Team 2 average wickets taken)
    for bar in bars3:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    for bar in bars4:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    # Add a main title for the entire figure
    fig.suptitle('Wickets Taken Analysis in Different Phases', fontsize=16)

    # Add combined titles
    fig.text(0.5, 0.92, 'Total Wickets Taken Comparison', ha='center', fontsize=14)
    fig.text(0.5, 0.48, 'Average Wickets Taken Comparison', ha='center', fontsize=14)

    return fig
