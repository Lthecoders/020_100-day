# for i in range(100, 110):
#   print(i)

# for i in range(1, 7):
#   print("Day", i+1)

# print("Thirteen Times Table")
# for i in range(1, 13):
#   print(i, "x 13 =", i * 13)

# for i in range(1, 8):
# print("Day", i)

# for i in range (0, 1000000, 25):
#   print(i)
"""
in range under brackets first value we put is starting point and 
second value which we put after the comma is ending point,
and the value which we write at last is increment value
"""
"for negtive number we have to start with greater value and then smaller values"
# for i in range(-60, -50 + 1, 2):
#   print(i)
"for both positive value we have to write first smaller value and then bigger value"
# for k in range(50, 61, 2):
#   print(k)
"""
"we are telling logically that start from this number so basically the number"
which we will put at must logically must me smaller than the 
number which we will put after the coma"""
"""
if we want to increment down word than we have to use - sing and if we want to increament
upwards we have to use + and it's default

The third value in the range function, increment, is missing. We need to add an increment of -1 to go backward. Without the increment written, the computer does the default of +1.

Without the increment listed, we are telling the computer: "start at 10, keep going until 0, and add one each time." This can't be done so nothing will run unless we add an increment."""

# for i in range(10, 0, -1):
#   print(i)
"""
if we say increement by -1 it will start print from backwords from that perticular number
if we say increement by +1 it will start print from afterwords from that perticular number

19
20 if minus value like -1 is give iwill go back up ⬆️ and if plus 1 is give it will go down ⬇️
21
22
23
24
.
.
.
38
39
40
"""
# for i in range(20, 40, 1):
#   print(i)



# print("List generator\n\n")

# start_at = int(input("Start at -----> "))
# end_at = int(input("\nEnd at -------> "))
# increment = int(input("\nIncrement between value --------> "))
# print()

# color_codes = [30, 31, 32, 33, 34, 35, 36]

# for i in range(start_at, end_at, increment):
#   for index, val in enumerate(range(start_at, end_at, increment)):
#     if index < len(color_codes):
#       print("\033[{}m".format(color_codes[index]), val, "\033[0m")


elif (end_at) != int():
  print(
      "\033[31m",
      "you can only input negative or postive numbers.\n PLEASE RETRY and make sure this time you input an negative or positive number in all three criteria \n run the code again.....",
      "\033[0m")
  exit()
elif (increment) != int():
  print(
      "\033[31m",
      "you can only input negative OR postive numbers.\n PLEASE RETRY and make sure this time you input an negative or positive number in all three criteria \n run the code again.....",
      "\033[0m")
  exit()