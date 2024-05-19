from entity import Courier,CourierCompany,User,Location,Payment,Employee,EmployeeCourier
from dao import CourierAdminService
from dao import CourierUserService


class MainMenu:

    user_services= CourierUserService()
    admin_services=CourierAdminService()

    def user_menu(self):
        while True:
            print(
                """      
            1. Add an Courier
            2. Remove an Courier
            3. Get Courier by ID
            4. Get Assigned Order
            5. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))

            if choice == 1:
                CourierID = int(input("Please enter CourierID: "))
                UserID = int(input("Please enter UserID: "))
                SenderName = input("Please enter SenderName: ")
                SenderAddress = input("Please enter SenderAddress: ")
                ReceiverName = input("Please enter ReceiverName: ")
                ReceiverAddress = input("Please enter ReceiverAddress: ")
                Weight = input("Please enter Weight: ")
                Status = input("Please enter Status: ")
                TrackingNumber = input("Please enter TrackingNumber: ")
                DeliveryDate = input("Please enter DeliveryDate: ")
                new_courier = Courier(CourierID,UserID,SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate)
                self.user_services.placeOrder(new_courier)

            elif choice == 2:
                CourierID= int(input("Please tell a courier id to delete: "))
                self.user_services.cancelOrder(CourierID)

            elif choice== 3:
                CourierID = int(input("Please enter courier id: "))
                self.user_services.getOrderStatus(CourierID)

            elif choice ==4:
                EmployeeID = int(input("Please enter employee id: "))
                self.user_services.getAssignedOrder(EmployeeID)
    
            elif choice == 5:
                break

    def admin_menu(self):
        while True:
            print(
                """      
            1. Add an Employee
            2. Get employee details by id
            3. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))
            if choice == 1:
                EmployeeID = int(input("Please enter employeeID: "))
                Name = input("Please enter Name: ")
                Email = input("Please enter Email: ")
                ContactNumber = input("Please enter ContactNumber: ")
                Role = input("Please enter Role: ")
                Salary = input("Please enter Salary: ")
                new_employee = Employee(EmployeeID, Name, Email, ContactNumber, Role, Salary)
                self.admin_services.addCourierStaff(new_employee)

            elif choice== 2:
                EmployeeID = int(input("Please enter employee id: "))
                self.admin_services.getEmployeeByID(EmployeeID)

            elif choice == 3:
                break
                    
def main():
    main_menu = MainMenu()

    while True:
        print(
            """      
               1. Courier Management  
               2. Employee Management  
               3. Exit  
                """
        )

        choice = int(input("Please choose from above options: "))

        if choice == 1:
            main_menu.user_menu()
        elif choice == 2:
            main_menu.admin_menu()
        elif choice == 3:
            main_menu.user_services.close() 
            main_menu.admin_services.close()
            print("Visit Again Soon....Good Day! 😊\n")
            break


if __name__ == "__main__":
    print("✨ 🎊 Welcome to the Courier Management System App 🎊 ✨")
    main()

    

