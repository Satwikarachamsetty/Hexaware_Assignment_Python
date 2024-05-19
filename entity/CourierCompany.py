class CourierCompany:
   def __init__(self, companyName, courierDetails, employeeDetails, locationDetails):
     self.__companyName = companyName
     self.__courierDetails = courierDetails
     self.__employeeDetails = employeeDetails
     self.__locationDetails = locationDetails

 # Getters
   def get_companyName(self):
     return self.__companyName

   def get_courierDetails(self):
     return self.__courierDetails

   def get_employeeDetails(self):
     return self.__employeeDetails

   def get_locationDetails(self):
     return self.__locationDetails

 # Setters
   def set_companyName(self, companyName):
     self.__companyName = companyName

   def set_courierDetails(self, courierDetails):
     self.__courierDetails = courierDetails

   def set_employeeDetails(self, employeeDetails):
     self.__employeeDetails = employeeDetails

   def set_locationDetails(self, locationDetails):
      self.__locationDetails = locationDetails




