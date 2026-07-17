"""
  Technical Challenge: The Rolling Scoreboard Engine
Your mission is to build a command-line script that acts as a real-time data ingestion point for match scores. 
It must calculate a rolling sum of only the last 5 entries, dropping the oldest data as new data flows in.

1. The Constraints (How to make it an architectural test)    
To maximize your computational thinking, you must follow these rules:

No Advanced Built-ins: Do not use **collections.deque or Python's .pop(0) / .append()** shortcuts to shift elements.

Fixed Pre-allocated Memory: Start with a list of five zeros: scores = [0, 0, 0, 0, 0]. Treat this list as a rigid 
block of memory that cannot grow or shrink.

The Manual Shift: Every time a new score enters, you must write a loop or index-assignment
logic that manually shifts elements to the left to clear out index 4 for the incoming score.
"""

scores = [ 0,  0,  0,  0,  0 ]

while True:
    user_input = input("enter a valid score (or type [ EXIT ] to stop the program): ")
    if user_input.lower() == "exit":
        print("nice job GoodBye")
        break
         


    new_score = int(user_input)
    if not int(new_score):
        print("thanks: oya leave here")
        break

    for i in range(4):  
        scores[i] = scores[i+1]
        total_score = 0

        scores[4] = new_score
        for scor_sum in scores:
            total_score += scor_sum

    print(f"updated score, {scores} total score count {total_score}") 