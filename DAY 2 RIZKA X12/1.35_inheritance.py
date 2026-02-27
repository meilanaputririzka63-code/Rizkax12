class Person:
  def __init__(self, fname, iname):
    self.firstname = fname
    self.lastname = iname
  
  def printname(self):
    print(self.firstname, self.lastname) 