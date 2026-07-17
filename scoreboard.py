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


Step-by-Step Implementation Outline

Break your script down into these logical phases:

Initialization: Create your fixed list of 5 elements and an active loop variable 
(like while True:) to keep the program running indefinitely until you type "exit".

Input & Validation: Prompt the user to type a score. Ensure the user entered a valid number
. What happens if they accidentally type a letter? Prevent your program from crashing.

The Shift Logic: Figure out how to update the list indices. Hint: If i goes from 0 to 3
, how can you pass the value at scores[i+1] down to scores[i]?

Insertion & Processing: Place the new score at the very end of the list. Then, calculate the total sum of 
the list elements without using the built-in sum() function—write a quick for loop to add them up manually.

Output: Print out both the current state of the array and the calculated rolling sum so you can verify it visually.
"""


current_scores_board_list = [0, 0, 0, 0, 0]
while True:
  user_input = input("Enter A  valid score Ronaldo Scored in the ongoing match \n( or  type [ exit ] if the match has already Ended  ):  ")
  if user_input.lower() == "exit":
    print("thanks: GoodBye")
    break
  elif not int(user_input):
    print("oya Bye Bye")
    break
  
  
  new_score = int(user_input)

  

  for i in range(4):
    current_scores_board_list[i] = current_scores_board_list[i+1]

    current_scores_board_list[4] = new_score
    total_score = 0
    for total_count_ in current_scores_board_list:
      total_score = total_score+total_count_

    print(f"the current score table {current_scores_board_list} \n total score count in the last five round {total_score}")


      
