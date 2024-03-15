import check_input
import greenbeans
import pie
import turkey
import stuffing
import potatoes

import smallplate
import largeplate

# Author: Diego Cid, Lela Wondafrash, Sarena Hieng
# Date: 11/16/2023
# Description: Game where user adds as much thankgiving foods to their plate without overiflling the plate and dropping it

def examine_plate(p):
  """
  Examines the area and weight on the plate and prints hints depending on the area and weight
  ARG:
  p (Plate): the plate to be examined
  """
  if p.area() >= 41:
    print("There's plenty of space!")
  elif p.area() >= 21:
    print("There some space left.")
  elif p.area() >= 1:
    print("There's a little space left...")
  elif p.area() <= 0:
    print("You ran out of room on your plate, and your food spilled all over the floor!\nGAME OVER :(")
    return True
  
  if p.weight() >= 13:
    print("Your plate is holding strong!")
  elif p.weight() >= 7:
    print("Your plate is starting to feel weak.")
  elif p.weight() >= 1:
    print("Your plate is bending...")
  elif p.weight() <= 0:
    print("Your plate was too heavy, and your food spilled all over the floor!\nGAME OVER :(")
    return True
    
def main():
  #intro
  print("~~ Thanksiving Dinner ~~")
  print("Serve yourself as much food as you like from the buffet, but make sure that your plate will hold without spilling everywhere!")

  #sets the plate to either large or small depending on user input
  user_plate = check_input.get_int_range("Choose a plate:\n1. Small Sturdy Plate\n2. Large Flimsy Plate\n", 1, 2)
  p = ""
  match user_plate:
    case 1:
      p = smallplate.SmallPlate()
    case 2:
      p = largeplate.LargePlate()

  choice = 0

  #loops until user quits or they overfill their plate
  while choice != 6:
    choice = check_input.get_int_range("Choose food options:\n1. Turkey\n2. Stuffing\n3. Potatoes\n4. Green Beans\n5. Pie\n6. Quit\n", 1, 6)
    match choice:
      case 1:
        p = turkey.Turkey(p)
      case 2:
        p = stuffing.Stuffing(p)
      case 3:
        p = potatoes.Potatoes(p)
      case 4:
        p = greenbeans.GreenBeans(p)
      case 5:
        p = pie.Pie(p)
      case 6:
        break
        
    print(p.description())
    if examine_plate(p):
      break

  #prints out how much area and weight the user had left on their plate
  print(p.description())
  print(f"Great job you made it to the table with {str(p.count())} items")
  print(f"There was still {str(p.area())} square inches left on your plate")
  print(f"Your plate could have held {str(p.weight())} more ounces of food.")
  print("Dont worry you can always go back to the table for more food.\nHappy Thanksgiving!")
main()