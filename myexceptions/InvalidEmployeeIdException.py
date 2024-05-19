class  InvalidEmployeeIdException(Exception):
     def __init__(self, EmployeeID):
        super().__init__(f"Employee with {EmployeeID} is not Found")