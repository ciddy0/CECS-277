import rectangle
import check_input

# Author: Diego Cid, Lela Wondafrash, Sarena Hieng
# Date: 9/21/2023
# Description: Allows user to create a rectangle with dimensions of the users choice (between 1-5). The user can then decide the direction the rectangle is able to move to ( one space up, down, left, or right) within the bounds of a 20 by 20 grid.

"""
Displays a rectangle on a 20 x 20 grid. And the user is able to move the rectangle
around in a 20x20 grid
"""


def display_grid(grid):
  """
  displays a 20x20 grid to user
  """
  for row in grid:
    for item in row:
        print(item, end=' ')
    print()
  

def reset_grid(grid):
  """
  resets the grid with no rectangle displayed on it
  """
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      grid[row][col] = "."

def place_rect(grid, rect):
  """
  Places the rectangle of given dimension onto the 20x20 grid  """
  for row in range(rect.h):
    for col in range(rect.w):
      grid[row + rect.y][col + rect.x] = "*"

def main():
  #ask user for dimensions
  width = check_input.get_int_range("Enter rectangle Width(1-5): ", 1, 5)
  height = check_input.get_int_range("Enter rectangle Height(1-5): ", 1, 5)
  
  #create 20x20 grid
  grid2D = []
  for i in range(20):
    grid = []
    for j in range(20):
      grid.append(".")
    grid2D.append(grid)

  #display grid with given rectangle
  rectangle1 = rectangle.Rectangle(width,height)
  place_rect(grid2D, rectangle1)
  display_grid(grid2D)

  #ask user to move rectangle and displays it unless the rectangle moves out of bounds
  while True:
    print("1. Up\n2. Down\n3. Right\n4. Left\n5. Quit")
    direction = check_input.get_int_range("Enter choice: ", 1, 5)
    
    if direction == 1:
      rectangle1.move_up()
      if(rectangle1.y < 0):
        rectangle1.move_down()
        print("OUT OF BOUNDS")
    elif direction == 2:
      rectangle1.move_down()
      if(rectangle1.y + height > 20):
        rectangle1.move_up()
        print("OUT OF BOUNDS")
    elif direction == 3:
      rectangle1.move_right()
      if(rectangle1.x + width > 20):
        rectangle1.move_left()
        print("OUT OF BOUNDS")
    elif direction == 4:
      rectangle1.move_left()
      if(rectangle1.x < 0):
        rectangle1.move_right()
        print("OUT OF BOUNDS")
    elif direction == 5:
      break
    reset_grid(grid2D)
    place_rect(grid2D, rectangle1)
    display_grid(grid2D)
  


main()