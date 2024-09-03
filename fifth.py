#loop

#while loop

# Initialization
# while condition:
#     statement
#     Increment/Decrement

i = 1
while i <=10:
    print(i)
    i += 1

#break statement--(stop the loop)

i = 1
while i < 5:
  print(i)
  if i == 3:
    break
  i += 1

#continue statement--(stop the current iteration, and continue with the next)

i = 0
while i < 5:
  i += 1
  if i == 3:
    continue
  print(i)

#else Statement--(run a block of code once when the condition no longer is true)

i = 1
while i <=5:
    print(i)
    i += 1
else:
   print("Game is Over.")