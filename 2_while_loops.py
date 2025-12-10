# Given:
colors = ["red", "blue", "green", "yellow", "purple"]

# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.

index = 0
while index < len(colors):
    if colors[index] == "yellow":
        break
    print(colors[index])
    index += 1
    # index += 1 is shortned for index = index + 1
#expalanation: 
# We start with index 0 (first color).
#while index is less than length of colors list (5):
#check if color at current index is "yellow":
