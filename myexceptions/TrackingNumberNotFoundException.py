class TrackingNumberNotFoundException(Exception):
     def __init__(self, CourierID):
        super().__init__(f"Order with {CourierID} is not Found")