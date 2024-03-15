
import tasklist
import check_input

# Author: Diego Cid, Lela Wondafrash, Sarena Hieng
# Date: 9/26/2023
# Description: 

def main_menu():
  """
  displays a main menu for the user
  """
  print(f"1. Display current task \n2. Display all tasks \n3. Mark current task complete \n4. Add new task \n5. Search by date\n6. Save and quit\n")
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

  while choice != 6:
    #prompts user to enter choice from main menu
    print("-Tasklist-")
    print("Tasks to complete:", len(newList))
    main_menu()
    choice = check_input.get_int_range("Enter choice: ", 1, 6)
    #displays the current task in tasklist
    if choice == 1:
      if len(newList) > 0:
        print(newList.get_current_task())
      else:
        print("All tasks are complete.")
    #displays all the task in tasklist
    elif choice == 2:
      if len(newList) > 0:
        position = 1
        for tasks in newList:
          print(f"{position}. {tasks}\n")
          position += 1

      else:
        print("All tasks are complete.")
    #marks current task as complete and removes it from list and displays the next current task
    elif choice == 3:
      if len(newList) != 0:
        print("Marking current task as complete: ")
        print(newList.get_current_task())
        newList.mark_complete()
        if len(newList) != 0:
          print("New current task is: ")
          print(newList.get_current_task())
      else:
        print("There are no tasks to complete.")
      
    #adds a new task into our tasklist
    elif choice == 4:
        desc = input("Enter task description: \n")
        newList.add_task(desc, get_date(), get_time())
    #saves the tasks in our list to a txt file and ends program
    elif choice == 5:
      search_date = get_date()
      search_result = []
      for tasks in newList:
        if tasks.date == search_date:
          search_result.append(tasks)
      print(f"Tasks due on {search_date}\n")
      position = 1
      for tasks in search_result:
        print(f"{position}. {tasks}")
        position += 1
      
    elif choice == 6:
      print("Saving file...")
      newList.save_file()
    print("")


main()