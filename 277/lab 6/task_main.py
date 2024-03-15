import tasklist
import check_input

# Author: Diego Cid, Lela Wondafrash, Sarena Hieng
# Date: 9/26/2023
# Description: Allows user to create a rectangle with dimensions of the users choice (between 1-5). The user can then decide the direction the rectangle is able to move to ( one space up, down, left, or right) within the bounds of a 20 by 20 grid.

def main_menu():
  """
  displays a main menu for the user
  """
  print(f"1. Display current task \n2. Display all tasks \n3. Mark current task complete \n4. Add new task \n5. Save and quit\n")
def get_date():
  """
  ask user for year, month, and day the task is due and formats in MM/DD/YYYY
  """
  year = check_input.get_int_range("Enter year: ", 2000, 2100)
  month = check_input.get_int_range("Enter month: ", 1, 12)
  day = check_input.get_int_range("Enter day: ", 1, 31)
  if month < 10:
    month = "0" + str(month)
  if day < 10:
    day = "0" + str(day)
  return f"{str(month)}/{str(day)}/{str(year)}"
  pass
def get_time():
  """
  ask user for hour and minutes and formats in HH:MM
  """
  hour = check_input.get_int_range("Enter hour: ", 0, 23)
  minute = check_input.get_int_range("Enter minute: ", 0, 59)
  if hour < 10:
    hour = "0" + str(hour)
  if minute < 10:
    minute = "0" + str(minute)
  return f"{str(hour)}:{str(minute)}"
  
def main():
  #creates a tasklist object
  newList = tasklist.Tasklist()
  choice = 0

  while choice != 5:
    #prompts user to enter choice from main menu
    print("-Tasklist-")
    print("Task to complete:", len(newList))
    main_menu()
    choice = check_input.get_int_range("Enter choice: ", 1, 5)
    #displays the current task in tasklist
    if choice == 1:
      if len(newList) > 0:
        print(str(newList[0]))
      else:
        print("All tasks are complete.")
    #displays all the task in tasklist
    elif choice == 2:
      if len(newList) > 0:
        for num in newList:
          print(num)
          print("")
      else:
        print("All tasks are complete.")
    #marks current task as complete and removes it from list and displays the next current task
    elif choice == 3:
      if len(newList) != 0:
        print("Marking current task as complete: ")
        print(str(newList[0]))
        newList.mark_complete()
        print("New current task is: ")
        print(str(newList[0]))
      else:
        print("There are no tasks to complete.")
    #adds a new task into our tasklist
    elif choice == 4:
        desc = input("Enter task description: \n")
        newList.add_task(desc, get_date(), get_time())
    #saves the tasks in our list to a txt file and ends program
    elif choice == 5:
      newList.save_file()
    print("")
  
  
main()