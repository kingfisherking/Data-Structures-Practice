from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left = Stack("Left")
middle = Stack("Middle")
right = Stack("Right")
stacks.extend((left, middle, right))


#Set up the Game
num_disks = int((input("\nHow many disks do you want to play with?\n")))
while num_disks < 3:
  num_disks = int((input("\nI am BEGGING you to pick a number greater than 2?\n")))

for x in range(num_disks, 0, -1):
  left.push(x)
num_optimal_moves = 2**num_disks - 1
print("\nThe fastest you can solve this game is in {%d} moves" % num_optimal_moves) 

#Get User Input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter %s for %s" % (letter, name))
    user_input = input("")
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]

        
#Play the Game
num_user_moves = 0
while(right.get_size() != num_disks):
  print("\n\n\n...Current Stacks")
  for x in stacks:
    x.print_items()
  while True:
    print("\nwhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.is_empty():
      print("\n\nInvalid Move. Try Again")
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again")
print("\n\nYou completed the game in {%d} moves, and the optimal number of moves is {%d}" % (num_user_moves, num_optimal_moves))

  
