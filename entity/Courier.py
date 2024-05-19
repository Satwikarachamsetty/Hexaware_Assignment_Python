class Courier:
    def __init__(self, CourierID, UserID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate):
        self.CourierID = CourierID
        self.UserID = UserID
        self.SenderName = SenderName
        self.SenderAddress = SenderAddress
        self.ReceiverName = ReceiverName
        self.ReceiverAddress = ReceiverAddress
        self.Weight = Weight
        self.Status = Status
        self.TrackingNumber = TrackingNumber
        self.DeliveryDate = DeliveryDate

    # Getters
    def getCourierID(self):
        return self.CourierID

    def getUserID(self):
        return self.UserID

    def getSenderName(self):
        return self.SenderName

    def getSenderAddress(self):
        return self.SenderAddress

    def getReceiverName(self):
        return self.ReceiverName

    def getReceiverAddress(self):
        return self.ReceiverAddress

    def getWeight(self):
        return self.Weight

    def getStatus(self):
        return self.Status

    def getTrackingNumber(self):
        return self.TrackingNumber

    def getDeliveryDate(self):
        return self.DeliveryDate

    # Setters
    def setCourierID(self, CourierID):
        self.CourierID = CourierID

    def setUserID(self, UserID):
        self.UserID = UserID

    def setSenderName(self, SenderName):
        self.SenderName = SenderName

    def setSenderAddress(self, SenderAddress):
        self.SenderAddress = SenderAddress

    def setReceiverName(self, ReceiverName):
        self.ReceiverName = ReceiverName

    def setReceiverAddress(self, ReceiverAddress):
        self.ReceiverAddress = ReceiverAddress

    def setWeight(self, Weight):
        self.Weight = Weight

    def setStatus(self, Status):
        self.Status = Status  

    def setTrackingNumber(self, TrackingNumber):
        self.TrackingNumber = TrackingNumber

    def setDeliveryDate(self, DeliveryDate):
        self.DeliveryDate = DeliveryDate 
