print("\033[34m", "COLOUR FULL-----> LIST number generator<------------------",
      "\033[0m")
print("\033[35m",
      "----------------------------------------------------------\n",
      "\033[0m")

while True:
  try:
    start_at = input("\nstart at -----> ")
    end_at = input("\nend at -------> ")
    increment = input("\nhow many should be added each time? --------> ")
    print()

    # Convert inputs to integers
    start_at = int(start_at)
    end_at = int(end_at)
    increment = int(increment)

    color_code = 32  # Starting ANSI color code
    for i in range(start_at, end_at, increment):
      print("\033[{}m".format(color_code), i, "\033[0m")
      color_code += 1  # Increment the color code
      if color_code > 36:
        color_code = 32  # Reset to default color code
    if not range(start_at, end_at, increment):
      print(
          "\033[31m",
          "WRONG LOGIC INPUT. make sure you place all three number logicaly and try again......",
          "\033[0m")
      continue

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == 'no':
      break
    elif play_again == 'yes':
      continue  # this will again restart the loop from line 10
    else:
      print("\033[31m", "please answer ONLY in yes or no . LOWERCASE",
            "\033[0m")
      play_again = input("\nDo you want to play again? (yes/no): ").lower()
      if play_again == 'no':
        break  # this will through us from the while loop
      elif play_again == 'yes':
        continue
      else:
        print("\033[31m",
              "please answer ONLY in yes or no . RUN THE PROGRAME AGAIN",
              "\033[0m")
        break

  except ValueError:
    print(
        "\033[31m",
        "ERROR: PLEASE ENTER POSITIVE AND NEGATIVE NUMBERS ONLY.\n-------------------> make sure you place all 3 numbers according to correct LOGICS and try again <---------------------",
        "\033[0m")

print(
    "\033[35m",
    "\n---------------> if you wish to play, simply run again <----------------",
    "\033[0m")
