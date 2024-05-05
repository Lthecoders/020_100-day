print("\033[34m", "COLOUR FULL-----> LIST number generator<------------------",
  "\033[0m")
print("\033[35m",
  "----------------------------------------------------------\n\n",
  "\033[0m")
try:
start_at = (input("start at -----> "))
end_at = (input("\nend at -------> "))
increment = (input("\nincrement between value --------> "))
print()  

color_code = 32  # Starting ANSI color code
for i in range(int(start_at), int(end_at), int(increment)):
print("\033[{}m".format(color_code), i, "\033[0m")
"basically .formate is used to insert any color code number in \033[{}m"
"""
"\033[{}m".format(color_code
we use this when we want to insert a value from the variable with respect to the color code

we are telling that 
look you have to INSERT----->.formate(color_code) into ----> "\033[{}m   
    -------------------- here color_code is name of a variable which are containing color codes ------------------
THIS IS THE WAY WE INSERT A COLOR CODE with the help of variable IN 033[{}m"
"\033[{}m" we have to put {} to let python know that i will insert here a color code which
i am gona bring through a varialble.
"""
color_code += 1  # Increment the color code
if color_code > 36:
  color_code = 32  # Reset to default color code

except:
print("\033[31m", "ERROR: PLEASE ENTER A NUMBER", "\033[0m")

