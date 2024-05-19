class User:
 def __init__(self,UserID,Name,Email,Password,ContactNumber,Address):
   self.__UserID = UserID
   self.__Name = Name
   self.__Email = Email
   self.__Password = Password
   self.__ContactNumber = ContactNumber
   self.__Address = Address
   
 # Getters
 def get_UserID(self):
   return self.__UserID
 
 def get_Name(self):
   return self.__Name
 
 def get_Email(self):
   return self.__Email
 
 def get_Password(self):
   return self.__Password
 
 def get_ContactNumber(self):
   return self.__ContactNumber
 
 def get_Address(self):
   return self.__Address
 
 # Setters
 def set_UserID(self, UserID):
   self.__UserID = UserID

 def set_Name(self, Name):
   self.__Name = Name

 def set_Email(self, Email):
   self.__Email = Email

 def set_Password(self, Password):
   self.__Password = Password

 def set_ContactNumber(self, ContactNumber):
   self.__ContactNumber = ContactNumber

 def set_address(self, Address):
   self.__Address = Address
