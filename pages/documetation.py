import streamlit as st

st.title("IPL 2022 Team Performance Analysis - Streamlit App Documentation")

st.header("Overview")
st.write("""
This Streamlit project allows users to analyze IPL 2022 team performance across different phases of the game, 
as well as player-level statistics for batters, bowlers, and all-rounders. 
The project is structured into three main pages:

1. **Main Page (Team Comparison)**: Analyze and compare team performance by batting and bowling phases.
2. **Player Analysis**: Dive into individual player statistics for batters, bowlers, and all-rounders.
3. **Team Comparison**: Compare IPL teams' key performance metrics like runs scored, wickets lost, runs conceded, and wickets taken.
""")

st.header("1. Main Page - main.py")
st.write("""
### Description:
This page provides an overview of IPL 2022 team performance, focusing on batting and bowling during different phases of the match. 
Users can select multiple teams to compare their performance using functions from the `batting.py` and `bowling.py` files.

### Key Functionalities:
- **Data Loading**: Loads two main datasets - `IPL_Matches_2022.csv` and `IPL_Ball_by_Ball_2022.csv` (filtered for valid match IDs).
- **Team Selection**: Users can select multiple teams for comparison using a multiselect widget.
- **Analysis Type Selection**: Users can choose between comparing batting or bowling performances.
    - **Batting Comparison**: Compares runs and wickets lost across different phases of the innings.
    - **Bowling Comparison**: Compares wickets taken and runs conceded during different phases.
- **Graph Generation**: Interactive graphs are generated using `matplotlib`, with each bar representing team performances in various phases like Powerplay, Middle Overs, and Death Overs.

### How to Use:
1. Select the teams you want to compare from the multiselect dropdown.
2. Choose the analysis type (batting or bowling).
3. Click on the "Generate Graph" button to view the comparative analysis.
4. The results will display multiple graphs, comparing the selected teams' performance by phase.
""")

st.header("2. Player Analysis - Player_Analysis.py")
st.write("""
### Description:
This page provides detailed statistics for individual players (batters, bowlers, and all-rounders). 
It allows users to filter, sort, and analyze player stats interactively.

### Key Functionalities:
- **Data Loading**: Loads CSV files containing batter, bowler, and all-rounder statistics (`batter_stats.csv`, `bowler_stats.csv`, and `all_rounders.csv`).
- **Batsman Stats**:
    - Filter by minimum runs scored.
    - Sort by runs, strike rate, impact score, or average.
- **Bowler Stats**:
    - Filter by minimum overs bowled.
    - Sort by wickets, economy, average, or impact score.
- **All-Rounder Stats**:
    - Filter by minimum runs and wickets.
    - Sort by various player statistics.

### How to Use:
1. Select a stat from the dropdown (e.g., Batsman Runs or Wickets).
2. Use the sliders to set minimum values for filtering (e.g., minimum runs or overs).
3. Choose the sorting order (ascending or descending).
4. Click on the button to view the filtered data in a table format.
""")

st.header("3. Team Comparison - Team_Comparison.py")
st.write("""
### Description:
This page allows users to compare IPL 2022 teams based on key metrics such as runs scored per match, wickets lost per match, 
runs conceded per match, and wickets taken per match. It provides an interactive way to visualize team performances across various categories.

### Key Functionalities:
- **Team Performance Metrics**:
    - **Runs scored per match**: Compares the average runs scored by each team per match.
    - **Wickets lost per match**: Displays the average number of wickets lost by each team per match.
    - **Runs conceded per match**: Shows the average runs conceded by the bowling team in each match.
    - **Wickets taken per match**: Visualizes the average wickets taken by each team's bowlers per match.
         
**Graph Generation**: Interactive bar charts are generated using matplotlib, with each bar representing a team's average performance across 14 matches.
          The teams are displayed using short names (e.g., CSK, RCB) for clarity.
         

### How to Use:
1. Select the type of comparison you want to see from the dropdown menu (Runs scored per Match, Wickets Lost per Match, etc.).
2. Click the "Generate Graph" button to view the selected comparison as a bar chart.
3. The chart will display team-wise data for the selected metric, allowing easy comparison between teams.
""")




st.header("4. Batting and Bowling Comparison - `batting.py` & `bowling.py`")
st.write("""
### Description:
These two modules handle the detailed comparison of IPL teams' batting and bowling performances during various match phases. 
They generate bar graphs comparing team performances for metrics such as runs scored, wickets lost, runs conceded, 
and wickets taken during Powerplay, Middle Overs, and Death Overs.

### Key Functionalities:

#### `batting.py`
- **Batting Comparison by Phases**:
    - Compares teams based on runs scored during Powerplay (Overs 1-6), Middle Overs (Overs 7-15), and Death Overs (Overs 16-20).
    - Visualizes total runs per match and runs per over for each phase.
    - Functions:
        - `batting_comparision(Team1, Team2, ball_data)`: Generates bar plots for total runs and runs per over during different phases.
        - `batting_comparison_by_over(Team1, Team2, ball_data)`: Compares runs scored by each over across the entire 20 overs.
        - `wickets_comparison(Team1, Team2, ball_data)`: Compares wickets lost during different phases.

#### `bowling.py`
- **Bowling Comparison by Phases**:
    - Compares teams based on their bowling performance by runs conceded and wickets taken during Powerplay, Middle Overs, and Death Overs.
    - Functions:
        - `run_conced_comparision(Team1, Team2, ball_data)`: Visualizes total runs conceded and runs conceded per over by teams.
        - `taken_wkt_comparision(Team1, Team2, ball_data)`: Compares the number of wickets taken during different phases of the match.
""")

st.header("Impact Score - Player Performance Evaluation")
st.write("""
### Overview:
The Impact Score is a custom metric developed to quantify the overall performance of players based on their batting and bowling statistics. This score helps to identify the players who have the most significant influence on a game.
""")

st.subheader("Impact Score Calculation")
st.write("#### For Bowlers:")
st.latex(r'''
\text{Impact Score} = \left( (\text{Wickets} \times 0.5) + \left( \frac{100}{\text{Economy}} \times 0.3 \right) + \left( \frac{100}{\text{Average}} \times 0.2 \right) \right) \times 10
''')
st.write("""
- **Wickets**: Number of wickets taken by the bowler.
- **Economy**: Runs conceded per over.
- **Average**: Runs conceded per wicket.

Each factor is assigned a weight to indicate its importance, with **Wickets** contributing the most (50%), followed by **Economy** (30%), and **Average** (20%).
""")

st.write("#### For Batters:")
st.latex(r'''
\text{Impact Score} = \left( (\text{Batsman Runs} \times 0.4) + (\text{Strike Rate} \times 0.3) + (\text{Average} \times 0.3) \right)
''')
st.write("""
- **Batsman Runs**: Total runs scored by the batter.
- **Strike Rate**: Rate at which the batter scores runs.
- **Average**: Average runs scored per dismissal.

Each metric is weighted based on its influence, with **Runs** contributing 40%, while **Strike Rate** and **Average** each contribute 30%.
""")

st.write("""
### Purpose and Significance:
The Impact Score provides a holistic view of a player’s contribution, making it easier to evaluate performances across different roles (batters and bowlers) using a single unified metric. A higher Impact Score indicates a player who significantly influences the game and has a consistent positive effect on their team's performance.
""")


st.header("Project Structure")
st.code("""
.
|-- main.py  # Main page for team comparison
|-- Player_Analysis.py  # Page for player-level analysis
|-- Team_Comparison.py  # Page for team performance comparison
|-- batting.py  # Batting performance analysis functions
|-- bowling.py  # Bowling performance analysis functions
|-- data/
    |-- IPL_Matches_2022.csv  # Match-level data for IPL 2022
    |-- IPL_Ball_by_Ball_2022.csv  # Ball-by-ball data for IPL 2022
    |-- batter_stats.csv  # Stats for batters
    |-- bowler_stats.csv  # Stats for bowlers
    |-- all_rounders.csv  # Stats for all-rounders
""")

st.header("How to Run the App:")
st.write("""
1. Ensure you have Python and Streamlit installed:
    ```bash
    pip install streamlit pandas matplotlib
    ```
2. Run the Streamlit app:
    ```bash
    streamlit run main.py
    ```
3. Navigate through the pages using the sidebar to access the main team comparison, player analysis, and other features.
""")