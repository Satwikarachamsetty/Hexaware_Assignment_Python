from abc import ABC, abstractmethod
from util.DBconn import DBConnection
from myexceptions.InvalidEmployeeIdException import InvalidEmployeeIdException

class ICourierAdminService(ABC):

    @abstractmethod
    def addCourierStaff(self, employee):
        pass
    
    @abstractmethod
    def getEmployeeByID(self,employee):
        pass


class CourierAdminService(ICourierAdminService,DBConnection):

    def addCourierStaff(self,employee):
        try:
            self.cursor.execute(
                "INSERT INTO Employee (EmployeeID, Name, Email, ContactNumber, Role, Salary) VALUES (?,?,?,?,?,?)",
                (employee.EmployeeID, employee.Name, employee.Email, employee.ContactNumber, employee.Role, employee.Salary),
            )
            self.conn.commit()  # Permanent storing | If no commit then no data
        except Exception as e:
            print(e)
    
    def getEmployeeByID(self,employee):
        try:
            self.cursor.execute(
                "Select * from Employee Where EmployeeID = ?", employee
            )
            employees = self.cursor.fetchall()  # Get all data
            if len(employees) == 0:
                raise InvalidEmployeeIdException(employee)
            else:
                print(employees)
        except Exception as e:
            print("Ooops Error happened: ", e)