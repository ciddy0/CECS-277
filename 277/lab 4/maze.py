import check_input

# Author: Diego Cid, Lela Wondafrash, Sarena Hieng
# Date: 9/12/2023
# Description: Allows the user to solve a maze that is read in from a file

def read_maze():
  """
  reads into text file 
  RETURNS:
  a 2d list of the maze
  """
    file = open("maze.txt")
    maze2d = []

    for row in file:
      list = []
      for item in row:
        if item!= '\n':
          list.append(item)
      maze2d.append(list)
  
  return maze2d


def find_start(maze):
  """
  finds the start location of the maze
  INPUT:
  - maze: 2d list: 2d list that contains all the content of the maze
  RETURNS:
  a list of the coordinates of the start location
  
  """
  startLoc = []
  for row in range(0, len(maze)):
    for col in range(0, len(maze[row])):
      if maze[row][col] == "s":
        startLoc.append(row)
        startLoc.append(col)
        break
  
  
  return startLoc

def display_maze(maze, loc):
  """
  prints the maze as well as the location of the user
  INPUT:
  - maze 2d: list; the 2dlist of the maze
  - loc: list; list that contains the coordinates of location
  """
  for i in range(len(maze)):
    for j in range(len(maze[i])):
        if loc[0] == i and loc[1] == j:
          print("x", end= ' ')
        else:
          print(maze[i][j], end=' ')
    print() 

def main():

  #intro
  print("-Maze Solver-")
  maze1 = read_maze() 
  startLoc = find_start(maze1)
  playerLoc = startLoc #sets the players location the the start of the map
  moveFinished = False
  print(startLoc)
  display_maze(maze1, playerLoc)

  while maze1[playerLoc[0]][playerLoc[1]] != "f":
    print("1. Go North\n2. Go South\n3. Go East\n4. Go West")
    direction = check_input.get_int_range("Enter choice: ", 1, 4)
    #moves the players location by one move north unless there is a star in that space
    if direction == 1: 
      if maze1[playerLoc[0]-1][playerLoc[1]] == "*":
        print("Invalid movement. Try again")
      else:
        playerLoc[0] -= 1
        moveFinished = True
    #moves the players location by one space south
    elif direction == 2:
      if maze1[playerLoc[0]+1][playerLoc[1]] == "*":
        print("Invalid movement. Try again")
      else:
        playerLoc[0] += 1
        moveFinished = True
    #moves the players location by one space east
    elif direction == 3:
      if maze1[playerLoc[0]][playerLoc[1] +1] == "*":
        print("Invalid movement. Try again")
      else:
        playerLoc[1] += 1
        moveFinished = True
    #moves the players location by one space west
    elif direction == 4:
      if maze1[playerLoc[0]][playerLoc[1]-1] == "*":
        print("Invalid movement. Try again")
      else:
        playerLoc[1] -= 1
        moveFinished == True
    display_maze(maze1, playerLoc) #displays maze with the players new location
  print("CONGRADULATIONS DONE :D")  

main()