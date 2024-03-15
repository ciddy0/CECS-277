class Task:
  """
  Class that creates task 
  ATTRIBUTES:
    desc - string type; description of the task
    date - string type; date task needed to be completed by MM/DD/YYYY
    time - string type; time task needed to be completed by HH:MM
  """
  def __init__(self, desc, date, time):
    self.desc = desc
    self.date = date
    self.time = time
  def __str__(self):
    """
    returns a formatted string of the task for user
    """
    return f"{self.desc} - Due: {self.date} at {self.time}"
    
  def __repr__(self):
    """
    returns a formated string in order tp be stored in a txt file
    """
    return f"{self.desc},{self.date},{self.time}"
    
  def __lt__(self, other):
    """
    compares two task objects. Compares year, then month, then day, then hour, then
    minute, and finally alphabetically 
    """
    selfYear, otherYear = self.date[6:], other.date[6:]
    selfMonth, otherMonth = self.date[0:2], other.date[0:2]
    selfDay, otherDay = self.date[3:5], other.date[3:5]
    return(selfYear,selfMonth,selfDay, self.time, self.desc) < (otherYear,otherMonth,otherDay,other.time,other.desc)
    
    
  