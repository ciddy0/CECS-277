class Task:
  """
  Class that creates task 
  ATTRIBUTES:
    desc - string type; description of the task
    date - string type; date task needed to be completed by MM/DD/YYYY
    time - string type; time task needed to be completed by HH:MM
  """
  def __init__(self, desc, date, time):
    self._desc = desc
    self._date = date
    self._time = time
  @property
  def date(self):
    return self._date
  def __str__(self):
    """
    returns a formatted string of the task for user
    """
    return f"{self._desc} - Due: {self._date} at {self._time}"
    
  def __repr__(self):
    """
    returns a formated string in order tp be stored in a txt file
    """
    return f"{self._desc},{self._date},{self._time}"
    
  def __lt__(self, other):
    """
    compares two task objects. Compares year, then month, then day, then hour, then
    minute, and finally alphabetically 
    """
    selfYear, otherYear = self._date[6:], other._date[6:]
    selfMonth, otherMonth = self._date[0:2], other._date[0:2]
    selfDay, otherDay = self._date[3:5], other._date[3:5]
    return(selfYear,selfMonth,selfDay, self._time, self._desc) < (otherYear,otherMonth,otherDay,other._time,other._desc)
    
    
  