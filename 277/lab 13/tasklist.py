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
    self._taskList = []
    for line in tasks:
      item = line.strip().split(",")
      self._taskList.append(task.Task(item[0], item[1], item[2]))
    self._taskList.sort()
    

  def add_task(self, desc, date, time):
    """ 
    Allows user to add tasks to the task list and sorts it into the correct position
    INPUT:
    desc - string; description of task
    date - string; date when task is due
    time - string; time task is due
    """
    self._taskList.append(task.Task(desc,date,time))
    self._taskList.sort()

  def mark_complete(self):
    """ 
    Removes the first task from the task list.
    """
    self._taskList.pop(0)

  def save_file(self):
    """ 
    Saves the current task list.
    """
    file = open("tasklist.txt", "w")
    for item in self._taskList:
      file.write(repr(item) + "\n")
    
  
  def get_current_task(self):
    """
    Retreives an item from the top of the list
    """
    return str(self._taskList[0])
  
    
  def __len__(self):
    """
    Returns the length of the task list
    """
    return len(self._taskList)

  """
  UPDATED METHODS TO CLASS GOES HERE
  """
  def __iter__(self):
    """
    Initializes an iterator value and returns itself.
    RETURNS:
    self, the object the function iterates through.
    """
    self._n = -1
    return self
    
  def __next__(self):
    """
    Iterates through the taskList.
    RETURNS:
    The different values within the taskList.
    """
    self._n += 1
    if self._n >= len(self._taskList):
      raise StopIteration
    else:
      return self._taskList[self._n]

      

