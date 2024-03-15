import task
class Tasklist:
  """
  Reads into a file of task and creates a list of task objects and sorts them
  """
  def __init__(self):
    """
    opens a tasklist file and iterates through it and creates task objects and adds them 
    to task list
    ATTRIBUTES:
    taskList - list type; stores task objects
    """
    file = open("tasklist.txt", "r")
    tasks = file.readlines()
    self.taskList = []
    for line in tasks:
      item = line.strip().split(",")
      self.taskList.append(task.Task(item[0], item[1], item[2]))
    self.taskList.sort()
    

  def add_task(self, desc, date, time):
    """ 
    Allows user to add tasks to the task list and sorts it into the correct position
    INPUT:
    desc - string; description of task
    date - string; date when task is due
    time - string; time task is due
    """
    self.taskList.append(task.Task(desc,date,time))
    self.taskList.sort()

  def mark_complete(self):
    """ 
    Removes the first task from the task list.
    """
    self.taskList.pop(0)

  def save_file(self):
    """ 
    Saves the current task list.
    """
    file = open("tasklist.txt", "w")
    for item in self.taskList:
      file.write(repr(item) + "\n")
    
  
  def __getitem__(self, index):
    """ 
    Retreives an item from the task list.
    INPUT:
    index - int; index of task user wants to get
    """
    return str(self.taskList[index])
    
  def __len__(self):
    """
    Returns the length of the task list
    """
    return len(self.taskList)
    
    
      

