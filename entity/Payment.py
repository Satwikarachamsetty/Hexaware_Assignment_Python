class Payment:
   def __init__(self,PaymentID, CourierID, LocationId, Amount, PaymentDate):
     self.__PaymentID = PaymentID
     self.__CourierID = CourierID
     self.__LocationID = LocationId
     self.__Amount = Amount
     self.__PaymentDate = PaymentDate
 # Getters
def get_PaymentID(self):
 return self.__PaymentID

def get_CourierID(self):
 return self.__CourierID

def get_LocationId(self):
 return self.__LocationId

def get_Amount(self):
 return self.__Amount

def get_PaymentDate(self):
 return self.__PaymentDate

 # Setters
def set_PaymentID(self, PaymentID):
 self.__PaymentID = PaymentID

def set_CourierID(self, CourierID):
 self.__CourierID = CourierID

def set_LocationId(self, LocationId):
 self.__LocationId = LocationId

def set_Amount(self, Amount):
 self.__Amount = Amount

def set_PaymentDate(self, PaymentDate):
 self.__PaymentDate = PaymentDate

