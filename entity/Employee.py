class Employee:
   def __init__(self,EmployeeID, Name, Email, ContactNumber, Role, Salary):
     self.EmployeeID = EmployeeID
     self.Name = Name
     self.Email = Email
     self.ContactNumber = ContactNumber
     self.Role = Role
     self.Salary = Salary

 # Getters
   def get_EmployeeID(self):
     return self.EmployeeID

   def get_Name(self):
     return self.Name

   def get_Email(self):
      return self.Email

   def get_ContactNumber(self):
     return self.ContactNumber

   def get_Role(self):
      return self.Role

   def get_Salary(self):
      return self.Salary

 # Setters
   def set_EmployeeID(self, EmployeeID):
      self.EmployeeID = EmployeeID

   def set_Name(self, Name):
      self.Name = Name

   def set_Email(self, Email):
      self.Email = Email
 
   def set_ContactNumber(self, ContactNumber):
      self.ContactNumber = ContactNumber

   def set_Role(self, Role):
     self.Role = Role

   def set_Salary(self, Salary):
     self.Salary = Salary
