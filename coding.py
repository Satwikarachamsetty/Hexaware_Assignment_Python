#Coding -Task 2
#1----------------------------------------------------------------------

def checkStatus(status):
   if status=='Delivered':
    print('Order is delivered')
   elif status=='Processing':
    print('Order is processing')
   elif status=='Cancelled':
    print('Order is Cancelled')
   else:
    print('Unknown Status')
status=input('Enter the order status: ')
checkStatus(status)

#2-----------------------------------------------------------------------
def detectWeiht(weight):
    match weight:
      case w if w<10:
        return 'Light'
      case w if w>=10 and w<50:
       return 'Medium'
      case default:
       return 'Heavy'
weight=int(input('Enter the weight of parcel: '))
print(detectWeiht(weight))

#3----------------------------------------------------------------
employeeDetails = {
 "Satwika":"satwika123",
 "Shiva":"shiva123"
}
customerDetails = {
 "Surya":"surya123",
 "Satya":"satya123"
}
def login():
   loginType = int(input('Enter your role\n 1.Employee\n 2.Customer\n'))
   name = input('Enter username: ')
   password = input('Enter password: ')
   if loginType==1:
     if name in employeeDetails and password == employeeDetails[name]:
       print(f'Welcome back {name}!')
     else:
       print('Invalid username or password')
   elif loginType == 2:
     if name in customerDetails and password == customerDetails[name]:
       print(f'Welcome back {name}!')
     else:
       print(f'Invalid username or password')
login()

#4-----------------------------------------------------------------------------

couriers = [
    {"name": "Courier 1", "load_capacity": 50},
    {"name": "Courier 2", "load_capacity": 100},
    {"name": "Courier 3", "load_capacity": 150}
]

def assignment_courier(ship_weight):
    for courier in couriers:
        if courier["load_capacity"] >= ship_weight:
            return courier["name"]
    return "No courier found with suitable load capacity"

ship_weight = float(input("Enter ship weight: "))
result = assignment_courier(ship_weight)
print("Assigned courier:", result)

#5 - Task 2--------------------------------------------------------------------------------
orders=[
    {"order_id":1,"customer":"Shiva"},
    {"order_id":2,"customer":"Anika"},
    {"order_id":3,"customer":"Shiva"},
    {"order_id":4,"customer":"Arjun"},
    {"order_id":5,"customer":"Shiva"},
    {"order_id":6,"customer":"Varun"},
]


def orders_customer(customer):
    print(f"Orders for Customer {customer}:")
    for order in orders:
        if order["customer"] == customer:
            print(f"Order ID: {order['order_id']}")

customer=input("Enter specific customer name:")
orders_customer(customer)

#6----------------------------------------------------------------------------
import time

def track_courier(destination):
    current_location = "Tenali"
    print(f"The courier is currently at: {current_location}")

    while current_location != destination:
    
        if current_location == "Tenali":
            current_location = "Guntur"
        elif current_location == "Guntur":
            current_location = "Suryapet"
        elif current_location == "Suryapet":
            current_location = "Hyderabad"
        time.sleep(1) 
        print(f"The courier is currently at: {current_location}")

    print("The courier has reached its destination!")

destination = input("Enter destination:")
track_courier(destination)


#7---------------------------------------------------------------------------------------
tracking_history = []
updates = ["Tenali", "Guntur", "Suryapet", "Hyderabad"]
for i in range(len(updates)):
 tracking_history.append(updates[i])
print("Tracking History:")
for i in range(len(tracking_history)):
 print(f"Update {i+1}: {tracking_history[i]}")


#8---------------------------------------------------------------------------------------------
def nearest_courier(pickup, couriers):
 nearest = None
 min_dist = float('inf')
 for courier in couriers:
   difference = abs(pickup - courier['distance'])
   if difference < min_dist:
    min_dist = difference
    nearest = courier['distance']
    location=courier['name']
 return nearest,location
 
couriers = [
    {"name": "Courier 1", "distance": 10},
    {"name": "Courier 2", "distance": 20},
    {"name": "Courier 3", "distance": 30}
]

new_order = int(input("Enter new order location:"))
result = nearest_courier(new_order, couriers)
print(f'Nearest Courier number : {result[0]} and courier name : {result[1]}')


#9-----------------------------------------------------------------------------------------------------
parcel_tracking=[[1,"Parcel in transit"],[2,"Parcel out for delivery"],[3,"Parcel delivered"]]
tracking_number=int(input("Enter your parcel Id:"))
for parcel in parcel_tracking:
 if parcel[0]==tracking_number:
   print("Parcel Status:",parcel[1])
   break

#10--------------------------------------------------------------------------------------------------
import re;
def data_Validation(data,detail):
   if(detail=="name"):
     if(data.isalpha() and data.istitle()):
       print(data," is valid name")
     else:
       print("Invalid ",detail)

   elif(detail=="address"):
     if(data.isalnum()):
       print(data, " is valid address")
     else:
       print("Invalid ",detail)
 
   elif(detail=='phone_number'):
     pattern = r'\d{3}-\d{3}-\d{4}'
     if re.match(pattern, data):
       print(data, " is valid number")
     else:
       print("Invalid",detail)

   else:
     print("Invalid detail")

detail = input("Enter type of data: ")
data = input("Enter "+ detail+": ")
data_Validation(data,detail)

#11-----------------------------------------------------------------------------------------
def format_Address(street,city,state,zip):
 result = ""
 result += street+", "+city+", "+state+", "+str(zip)
 result = result.title()
 return result

street=input("Enter street:")
city=input("Enter city:")
state=input("Enter state:")
zip=int(input("Enter zip:"))

print(f'Address: {format_Address(street,city,state,zip)}')

#12-----------------------------------------------------------------------------------------
def order_Confirmation(name,orderDate,address,expectedDate):
 emailContent = f"""
 Dear {name},
 Thank you for your order! Below are the details of your purchase:
 Order Number: {orderDate}
 Delivery Address: {address}
 Expected Delivery Date: {expectedDate}
 
 If you have any questions or concerns, feel free to contact us.
 Sincerely,
 FastDelivery courier company
 """
 return emailContent

name=input("Enter name:")
orderId=int(input("Enter orderId:"))
address=input("Enter address:")
expectedDate=input("Enter expected delivery date:")
print(order_Confirmation(name,orderId,address,expectedDate))

#13--------------------------------------------------------------------------------------------
def shipping_cost(distance,weight):
    cost=0
    cost_per_km=5
    cost_per_kg=5
    total_cost=cost+(cost_per_km*distance)+(cost_per_kg*weight)
    return total_cost

distance=float(input("Enter distance between source and destination:"))
weight=float(input("Enter weight of parcel:"))
source=input("Enter source:")
destination=input("Enter destination:")
cost_parcel=shipping_cost(distance,weight)
print(f"Shipping cost of parcel from {source} to {destination} is {cost_parcel}")

#14--------------------------------------------------------------------------------------------
import string
import random

def generate_password(length=8):
 letters = string.ascii_letters
 digits = string.digits
 special = string.punctuation
 characters = letters + digits + special
 password = ''.join(random.choices(characters, k=length))
 return password

password = generate_password()
print("Generated Password:", password)

#15-------------------------------------------------------------------------------------
def find_similar(address,target):
    similar_address=[]
    for add in address:
        if target.lower() in add.lower():
            similar_address.append(add)
    return similar_address

address=[
    '123 Main Street,Varanasi,1002',
    '456 Oak Street,Kerala,1003',
    '123 Main Street,Srisailam,1004',
    '789 Elm Street,Jaipur,1005'
]

target=input("Enter target:")
similar=find_similar(address,target)
print('Similar Address:',similar)

