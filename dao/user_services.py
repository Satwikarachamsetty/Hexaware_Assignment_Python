from abc import ABC, abstractmethod
from util.DBconn import DBConnection
from myexceptions.TrackingNumberNotFoundException import TrackingNumberNotFoundException
from myexceptions. InvalidEmployeeIdException import  InvalidEmployeeIdException

class ICourierUserService(ABC):

    @abstractmethod
    def placeOrder(self,courierObj):
        pass

    @abstractmethod
    def getOrderStatus(self, trackingNumber):
        pass

    @abstractmethod
    def cancelOrder(self, trackingNumber):
        pass

    @abstractmethod
    def getAssignedOrder(self, courierStaffId):
        pass


class CourierUserService(ICourierUserService,DBConnection):

    def placeOrder(self,courierObj):
        try:
            self.cursor.execute(
                "INSERT INTO Courier(CourierID, UserID,SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate) VALUES (?, ?,?,?,?,?,?,?,?,?)",
                (courierObj.CourierID, courierObj.UserID,courierObj.SenderName, courierObj.SenderAddress, courierObj.ReceiverName, courierObj.ReceiverAddress, courierObj.Weight, courierObj.Status, courierObj.TrackingNumber, courierObj.DeliveryDate),
            )
            self.conn.commit()  # Permanent storing | If no commit then no data
        except Exception as e:
            print(e)
    
   
    def cancelOrder(self,trackingNumber):
        self.cursor.execute("Delete from Courier Where CourierID = ?",trackingNumber)
        self.conn.commit()

    def getOrderStatus(self, trackingNumber):
        try:
            self.cursor.execute(
                "Select * from Courier Where CourierID = ?", (trackingNumber,))
            orders = self.cursor.fetchall()  # Get all data
            if len(orders) == 0:
                raise TrackingNumberNotFoundException(trackingNumber)
            else:
                print(orders)
        except Exception as e:
            print("Ooops Error happened: ", e)

    def getAssignedOrder(self, courierStaffId):
        try:
            self.cursor.execute(
                "Select * from EmployeeCourier Where EmployeeID = ?", (courierStaffId,)
            )
            employees = self.cursor.fetchall()  # Get all data
            if len(employees) == 0:
                raise InvalidEmployeeIdException(courierStaffId)
            else:
                print(employees)
        except Exception as e:
            print("Ooops Error happened: ", e)