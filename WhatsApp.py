
import pywhatkit

length = int(input("Number of contacts \n"))
input_string = input("Enter all the numbers, separated by space \n")
contact = list(input_string.split(" "))
message = input("Message \n")
timeH = int(input("time in hours \n"))
timeM = int(input("Time in minutes \n"))
i = -1

while -1 <= i < length:
    i += 1
    pywhatkit.sendwhatmsg(str(contact[i]), message, timeH, timeM, 2)
    timeM += 0.2

print("Message sent")
