'''
open("employees", "r") #read
open("employees", "w") #write/edit
open("employees", "a") #append
open("employees", "r+") #read and write
'''

employee_file = open("employees", "r")
for employee in employee_file.readlines():
    print(employee)


#print(employee_file.readable())
#print("---------------------")

#print(employee_file.read())
#print("---------------------")

# print(employee_file.readline())
# print(employee_file.readline())
# print(employee_file.readline())
# print(employee_file.readline())

#print(employee_file.readlines())
#print(employee_file.readlines()[1])

employee_file.close()  #DON'T FORGET TO CLOSE THE FILE EVERYTIME