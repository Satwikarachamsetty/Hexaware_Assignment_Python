--Inserting values into Tables
INSERT INTO [User] ([UserID],[Name],[Email],[Password],[ContactNumber],[Address]) VALUES
(1,'Anika','anika@gmail.com','password1','9876543211','12 Gandhi Nagar,Delhi'),
(2,'Arjun','arjun@gmail.com','password2','9876543212','21 Main St,Ooty'),
(3,'Shivika','shivika@gmail.com','password3','9876543213','34 Ganga St,Varanasi'),
(4,'Shiva','shiva@gmail.com','password4','9876543214','43 Church St,Kerala'),
(5,'Raya','raya@gmail.com','password5','9876543215','56 Joshi Nagar,Pune'),
(6,'Ram','ram@gmail.com','password6','9876543216','65 Indira Market,Chennai'),
(7,'Vihana','vihana@gmail.com','password7','9876543217','78 Khan St,Hyderabad'),
(8,'Varun','varun@gmail.com','password8','9876543218','87 Verma Colony,Mumbai');


INSERT INTO Courier (CourierID,UserID,SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate) VALUES

(1,1,'Anika', '12 Gandhi Nagar,Delhi', 'Arjun', '21 Main St,Ooty', 2.5, 'In Transit', 'TN11234', '2024-04-01'),
(2,3, 'Shivika', '34 Ganga St,Varanasi', 'Anika', '12 Gandhi Nagar,Delhi', 3.0, 'Delivered', 'TN21234', '2024-04-02'),
(3,2, 'Arjun', '21 Main St,Ooty', 'Shivika', '34 Ganga St,Varanasi', 1.5, 'In Transit', 'TN31234', '2024-04-03'),
(4,4, 'Shiva', '43 Church St,Kerala', 'Raya', '56 Joshi Nagar,Pune', 2.0, 'In Transit', 'TN41234', '2024-04-04'),
(5,6, 'Ram', '65 Indira Market,Chennai', 'Vihana', '78 Khan St,Hyderabad', 4.5, 'Delivered', 'TN51234', '2024-04-05'),
(6,5, 'Raya', '56 Joshi Nagar,Pune', 'Varun', '87 Verma Colony,Mumbai', 4.0, 'In Transit', 'TN61234', '2024-04-06'),
(7,7, 'Vihana', '78 Khan St,Hyderabad', 'Ram', '65 Indira Market,Chennai', 3.5, 'Delivered', 'TN71234', '2024-04-07'),
(8,8, 'Varun', '87 Verma Colony,Mumbai', 'Shiva', '43 Church St,Kerala', 1.0, 'Delivered', 'TN81234', '2024-04-30');


INSERT INTO CourierServices (ServiceID, ServiceName, Cost) VALUES
(1, 'Standard Delivery', 10.00),
(2, 'Express Delivery', 15.00),
(3, 'Overnight Delivery', 20.00),
(4, 'International Delivery', 30.00),
(5, 'Same-Day Delivery', 25.00);

INSERT INTO CourierServiceMapping (CourierID,ServiceID) VALUES
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,1),
(7,2),
(8,3);

INSERT INTO  EmployeeCourier(EmployeeID,CourierID) VALUES
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
(7,7),
(8,8);

INSERT INTO Employee (EmployeeID, Name, Email, ContactNumber, Role, Salary) VALUES
(1, 'Rahul', 'rahul@gmail.com', '9187654320', 'Manager', 50000.00),
(2, 'Rihana', 'rihana@gmail.com', '9287654320', 'Delivery Person', 30000.00),
(3, 'John', 'john@gmail.com', '9387654320', 'Manager', 45000.00),
(4, 'Jessica', 'jessica@gmail.com', '9487654320', 'Customer Service', 32000.00),
(5, 'Surya', 'surya@gmail.com', '9587654320', 'Driver', 28000.00),
(6, 'Sanjana', 'sanjana@gmail.com', '9687654320', 'Customer Support', 35000.00),
(7, 'Daksh', 'daksh@gmail.com', '9787654320', 'Dispatcher', 38000.00),
(8, 'Dhanvi', 'dhanvi@gmail.com', '9887654320', 'Supervisor', 42000.00);

INSERT INTO Location (LocationID, LocationName, Address) VALUES
(1, 'Delhi', '12 Gandhi Nagar,Delhi'),
(2, 'Ooty', '21 Main St,Ooty'),
(3, 'Varanasi', '34 Ganga St,Varanasi'),
(4, 'Kerala', '43 Church St,Kerala'),
(5, 'Pune', '56 Joshi Nagar,Pune'),
(6, 'Chennai', '65 Khan,Chennai'),
(7, 'Hyderabad', '78 Khan St,Hyderabad'),
(8, 'Mumbai', '87 Verma Colony,Mumbai');

INSERT INTO Payment (PaymentID, CourierID, LocationId, Amount, PaymentDate) VALUES
(1, 1, 2, 120.00, '2024-04-01'),
(2, 2, 1, 130.00, '2024-04-02'),
(3, 3, 4, 150.00, '2024-04-03'),
(4, 4, 3, 180.00, '2024-04-04'),
(5, 5, 6, 200.00, '2024-04-05'),
(6, 6, 5, 120.00, '2024-04-06'),
(7, 7, 8, 170.00, '2024-04-07'),
(8, 8, 7, 160.00, '2024-04-30');