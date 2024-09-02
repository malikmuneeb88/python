class Scoreboard:
    def __init__(self):
        self.total_runs = 0
        self.batsman = [0, 0]
        self.total_wickets = 0
        self.runs_to_win = 0
        self.overs = 0.0 
        self.extras = 0
        self.bowler = None
        self.fielder = None
        self.how_out = None
        self.last_man_out = None
        self.opponent_score = 0
        self.overs_breakdown = []

    def take_input(self):
        self.total_runs = int(input("Enter total runs: "))
        self.opponent_score = int(input("Enter Opponent team score: "))
        self.batsman[0] = int(input("Enter batsman 1 score: "))
        self.batsman[1] = int(input("Enter batsman 2 score: "))
        self.last_man_out = input("Enter Last man out name: ")
        self.how_out = input("Enter How batsman got out(caught, bowled, LBW, Stumped, Runout: )")
        self.total_wickets = int(input("Enter total wickets fall down: "))
        self.runs_to_win = int(input("Enter runs to win: "))
        self.overs = int(input("Enter Overs: "))
        self.extras = int(input("Enter Extras: "))
        self.bowler = input("Enetr bowler: ")
        self.fielder = input("Enter fielder name: ")
        overs_list = input("Enter overs Breakdown: ")
        self.overs_breakdown = [int(ov) for ov in overs_list.split(',')]

    def display(self):
        print(f"Total runs: {self.total_runs}")
        print(f"Batsmen: {self.batsman[0]}*, {self.batsman[1]}*")
        print(f"Total Wickets: {self.total_wickets}")
        print(f"Runs to win: {self.runs_to_win}")
        print(f"Overs: {self.overs}")
        print(f"Extras; {self.extras}")
        print(f"Bowler: {self.bowler}")
        print(f"Fielder: {self.fielder}")
        print(f"How out: {self.how_out}")
        print(f"Last man out: {self.last_man_out}")
        print(f"Opponent team Score: {self.opponent_score}")
        print(f"Overs braekDown: {self.overs_breakdown}")

#Create a scoreboard class
scoreboard = Scoreboard()

#Take input from the user
scoreboard.take_input()

#Display the scoreboard
scoreboard.display()