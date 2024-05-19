class Location:
 def __init__(self,LocationID, LocationName, Address ):
   self.__LocationID = LocationID
   self.__LocationName = LocationName
   self.__Address = Address
 # Getters
def get_LocationID(self):
 return self.__LocationID

def get_LocationName(self):
 return self.__LocationName

def get_Address(self):
 return self.__Address

# Setters
def set_LocationID(self, LocationID):
 self.__LocationID = LocationID

def set_LocationName(self, LocationName):
 self.__LocationName = LocationName

def set_Address(self, Address):
 self.__Address = Address
