create database HexawareCourierDB
use HexawareCourierDB

Create Table  [User] (
    [UserID] INT PRIMARY KEY,
    [Name] VARCHAR(255),
    [Email] VARCHAR(255) UNIQUE,
    [Password] VARCHAR(255),
    [ContactNumber] VARCHAR(20),
    [Address] TEXT
);

Create Table [Courier](
    [CourierID] INT PRIMARY KEY,
	[UserID] INT,
	[SenderName] VARCHAR(255),
    [SenderAddress] TEXT,
    [ReceiverName] VARCHAR(255),
    [ReceiverAddress] TEXT,
    [Weight] DECIMAL(5, 2),
    [Status] VARCHAR(50),
    [TrackingNumber] VARCHAR(20) UNIQUE,
    [DeliveryDate] DATE
	FOREIGN KEY (UserID) REFERENCES [User](UserID)
);

Create Table [CourierServices](
     [ServiceID] INT PRIMARY KEY,
	 [ServiceName] VARCHAR(100),
	 Cost DECIMAL(8, 2)
);


Create Table [Employee](
    [EmployeeID] INT PRIMARY KEY,
	[Name] VARCHAR(255),
    [Email] VARCHAR(255) UNIQUE,
    [ContactNumber] VARCHAR(20),
	[Role] VARCHAR(50),
	[Salary] DECIMAL(10, 2)
);

Create Table [Location](
    [LocationID] INT PRIMARY KEY,
	[LocationName] VARCHAR(255),
    [Address] TEXT
);

CREATE TABLE Payment (
    [PaymentID] INT PRIMARY KEY,
    [CourierID] INT,
    [LocationID] INT,
    [Amount] DECIMAL(10, 2),
    [PaymentDate] DATE,
    FOREIGN KEY (CourierID) REFERENCES Courier(CourierID),
    FOREIGN KEY (LocationID) REFERENCES Location(LocationID)
);

CREATE TABLE CourierServiceMapping (
         CourierID INT,
         ServiceID INT,
         FOREIGN KEY (CourierID) REFERENCES Courier(CourierID),
         FOREIGN KEY (ServiceID) REFERENCES CourierServices(ServiceID)
 );

CREATE TABLE EmployeeCourier (
         EmployeeID INT,
         CourierID INT,
         FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
         FOREIGN KEY (CourierID) REFERENCES Courier(CourierID)
     );
