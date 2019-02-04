#RESERVATION DETAILS

guest_name = input("Enter the your name :")
num_of_people = input("Enter the number of people :")
room = [1001, 1002, 1003, 1004, 1005, 1006, 1007]
Room_num = input("Which room number you want? :")


if Room_num == "1001":
    print(" It is a luxury")
elif Room_num  == "1002":
    print("It is a single bed")
elif Room_num   == "1003":
    print("It is a double bed")
elif Room_num  == "1004":
    print("It is a single bed with a lounge")
elif Room_num  == "1005":
    print("It is a double bed with a lounge")
elif Room_num  == "1006":
    print("It is a single bed with a terrace")
elif Room_num  == "1007":
    print("It is a double bed with a terrace")
else:
    print("There is no room with this number..")

cost1 = {"1uxury" : "88,000" , "single bed" : "32,000" , "double bed" : "39,000" , "single bed with a lounge" : "45,000" , "double bed with a lounge" : "41,000" ,
         "single bed with a terrace" : "50,000" , "double bed with a terrace" : "59,000"}
cost = input("The total cost of your rent including all the facilities will be :")

import calendar
check_in = input("Your check in time is :")
check_out = input("Your checking out time will be :")


#DETAIL OF ROOMS RESERVATION

Room_1001 = 10/2/19, 11/2/19, 12/2/19, 13/2/19, 14/2/19, 15/2/19, 16/2/19
Room_1002 = 10/2/19, 11/2/19, 12/2/19, 13/2/19, 14/2/19, 15/2/19, 16/2/19
Room_1003 = 10/2/19, 11/2/19, 12/2/19, 13/2/19, 14/2/19, 15/2/19, 16/2/19
Room_1004 = 10/2/19, 11/2/19, 12/2/19, 13/2/19, 14/2/19, 15/2/19, 16/2/19
Room_1005 = 10/2/19, 11/2/19, 12/2/19, 13/2/19, 14/2/19, 15/2/19, 16/2/19
Room_1006 = 10/2/19, 11/2/19, 12/2/19, 13/2/19, 14/2/19, 15/2/19, 16/2/19
Room_1007 = 10/2/19, 11/2/19, 12/2/19, 13/2/19, 14/2/19, 15/2/19, 16/2/19

print("ROOM 1001 is not available on 10/2/19")
print("ROOM 1002 is not available on 14/2/19")
print("ROOM 1003 is not available on 12/2/19")
print("ROOM 1005 is not available on 11/2/19")
print("ROOM 1006 is not available on 16/2/19")
print("ROOM 1007 is not available on 15/2/19")

