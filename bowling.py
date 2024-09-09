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
    # Runs conceded by Team 1 bowlers in different phases
    powerplay_runs_cd = ball_data[(ball_data['BowlingTeam'].isin(Team1)) & (ball_data["overs"] < 6)]["total_run"].sum()
    middle_overs_runs_cd = ball_data[(ball_data['BowlingTeam'].isin(Team1)) & (ball_data["overs"] > 5) & (ball_data["overs"] < 15)]["total_run"].sum()
    death_overs_runs_cd = ball_data[(ball_data['BowlingTeam'].isin(Team1)) & (ball_data["overs"] > 14)]["total_run"].sum()

    # Runs conceded by Team 2 bowlers in different phases
    powerplay_runs_cd2 = ball_data[(ball_data['BowlingTeam'].isin(Team2)) & (ball_data["overs"] < 6)]["total_run"].sum()
    middle_overs_runs_cd2 = ball_data[(ball_data['BowlingTeam'].isin(Team2)) & (ball_data["overs"] > 5) & (ball_data["overs"] < 15)]["total_run"].sum()
    death_overs_runs_cd2 = ball_data[(ball_data['BowlingTeam'].isin(Team2)) & (ball_data["overs"] > 14)]["total_run"].sum()


    # Creating arrays for the phases and runs conceded
    phases = np.array(["powerplay", "middle_overs", "death overs"])
    total_runs_cd = np.array([powerplay_runs_cd, middle_overs_runs_cd, death_overs_runs_cd])
    per_over_cd = np.array([powerplay_runs_cd/6, middle_overs_runs_cd/9, death_overs_runs_cd/5])

    total_runs_cd2 = np.array([powerplay_runs_cd2, middle_overs_runs_cd2, death_overs_runs_cd2])
    per_over_cd2 = np.array([powerplay_runs_cd2/6, middle_overs_runs_cd2/9, death_overs_runs_cd2/5])

    # Set up the figure and subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(15,10))
    plt.subplots_adjust(wspace=0.4, hspace=0.4)

    # Set the same ylim for both total runs and runs per over comparisons
    max_total_run = max(max(total_runs_cd / (14*len(Team1))), max(total_runs_cd2 / (14*len(Team2)))) + 5
    max_per_over_run = max(max(per_over_cd / (14*len(Team1))), max(per_over_cd2 / (14*len(Team2)))) + 1

    # Team 1: Total runs conceded
    bars1 = ax1.bar(phases, total_runs_cd/(len(Team1)*14), color='skyblue')
    ax1.set(title=f'{", ".join([short_names[team] for team in Team1])} - Runs Conceded per Match', ylabel="Runs", xlabel="Phases", ylim=(0, max_total_run))
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    # Team 2: Total runs conceded
    bars2 = ax2.bar(phases, total_runs_cd2/(len(Team2)*14), color='lightcoral')
    ax2.set(title=f'{", ".join([short_names[team] for team in Team2])} - Runs Conceded per Match', ylabel="Runs", xlabel="Phases", ylim=(0, max_total_run))
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    # Team 1: Runs conceded per over
    bars3 = ax3.bar(phases, per_over_cd/(len(Team1)*14), color='lightgreen')
    ax3.set(title=f'{", ".join([short_names[team] for team in Team1])} - Runs Conceded per Over', ylabel="Runs", xlabel="Phases", ylim=(0, max_per_over_run))
    for bar in bars3:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    # Team 2: Runs conceded per over
    bars4 = ax4.bar(phases, per_over_cd2/(len(Team2)*14), color='orange')
    ax4.set(title=f'{", ".join([short_names[team] for team in Team2])} - Runs Conceded per Over', ylabel="Runs", xlabel="Phases", ylim=(0, max_per_over_run))
    for bar in bars4:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    # Add a main title for the entire figure
    fig.suptitle('Bowling Performance Analysis: Runs Conceded in Different Phases', fontsize=16)

    # Add combined titles for better context
    fig.text(0.5, 0.92, 'Average Runs Conceded Comparison', ha='center', fontsize=14)
    fig.text(0.5, 0.48, 'Runs Per Over Conceded Comparison', ha='center', fontsize=14)
    return fig





def taken_wkt_comparision(Team1, Team2, ball_data):
    # Wickets taken by Team 1 bowlers in different phases
    powerplay_total_wkts_tk = ball_data[(ball_data['BowlingTeam'].isin(Team1)) & (ball_data["overs"] < 6)]['isWicketDelivery'].sum()
    middle_overs_total_wkts_tk = ball_data[(ball_data['BowlingTeam'].isin(Team1)) & (ball_data["overs"] > 5) & (ball_data["overs"] < 15)]['isWicketDelivery'].sum()
    death_overs_total_wkts_tk = ball_data[(ball_data['BowlingTeam'].isin(Team1)) & (ball_data["overs"] > 14)]['isWicketDelivery'].sum()

    # Wickets taken by Team 2 bowlers in different phases
    powerplay_total_wkts_tk2 = ball_data[(ball_data['BowlingTeam'].isin(Team2)) & (ball_data["overs"] < 6)]['isWicketDelivery'].sum()
    middle_overs_total_wkts_tk2 = ball_data[(ball_data['BowlingTeam'].isin(Team2)) & (ball_data["overs"] > 5) & (ball_data["overs"] < 15)]['isWicketDelivery'].sum()
    death_overs_total_wkts_tk2 = ball_data[(ball_data['BowlingTeam'].isin(Team2)) & (ball_data["overs"] > 14)]['isWicketDelivery'].sum()

    
    # Creating arrays for the phases and wickets taken
    phases = np.array(["Powerplay", "Middle Overs", "Death Overs"])
    total_wickets_tk = np.array([powerplay_total_wkts_tk, middle_overs_total_wkts_tk, death_overs_total_wkts_tk])
    total_wickets_tk2 = np.array([powerplay_total_wkts_tk2, middle_overs_total_wkts_tk2, death_overs_total_wkts_tk2])

    # Set up the figure and subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(15,10))
    plt.subplots_adjust(wspace=0.4, hspace=0.4)

    # Set the same ylim for both total wickets and average wickets comparisons
    max_total_wickets = max(max(total_wickets_tk/len(Team1)), max(total_wickets_tk2/len(Team2))) + 5
    max_avg_wickets = max(max(total_wickets_tk /(len(Team1)*14)), max(total_wickets_tk2 /(len(Team2)*14)) + 0.5)


    # Team 1: Total wickets taken
    bars1 = ax1.bar(phases, total_wickets_tk/len(Team1), color='skyblue')
    ax1.set(title=f'{", ".join([short_names[team] for team in Team1])} - Total Wickets Taken', ylabel="Wickets", xlabel="Phases", ylim=(0, max_total_wickets))
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    # Team 2: Total wickets taken
    bars2 = ax2.bar(phases, total_wickets_tk2/len(Team2), color='lightcoral')
    ax2.set(title=f'{", ".join([short_names[team] for team in Team2])} - Total Wickets Taken', ylabel="Wickets", xlabel="Phases", ylim=(0, max_total_wickets))
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    # Team 1: Average wickets taken per match
    bars3 = ax3.bar(phases, total_wickets_tk /(len(Team1)*14), color='lightgreen')
    ax3.set(title=f'{", ".join([short_names[team] for team in Team1])} - Average Wickets per Match', ylabel="Wickets", xlabel="Phases", ylim=(0, max_avg_wickets))
    for bar in bars3:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    # Team 2: Average wickets taken per match
    bars4 = ax4.bar(phases, total_wickets_tk2 /(len(Team2)*14), color='orange')
    ax4.set(title=f'{", ".join([short_names[team] for team in Team2])} - Average Wickets per Match', ylabel="Wickets", xlabel="Phases", ylim=(0, max_avg_wickets))
    for bar in bars4:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')

    # Add a main title for the entire figure
    fig.suptitle('Wickets Taken Analysis in Different Phases', fontsize=16)

    # Add combined titles
    fig.text(0.5, 0.92, 'Total Wickets Comparison', ha='center', fontsize=14)
    fig.text(0.5, 0.48, 'Average Wickets Comparison', ha='center', fontsize=14)


    return fig
