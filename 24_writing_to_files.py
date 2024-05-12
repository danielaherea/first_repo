# employee_file = open("employees", "r")
employee_file = open("employees", "a")

#print(employee_file.read())

#employee_file.write("Toby - Human Resources")

employee_file.write("\nKelly - Customer Service")

employee_file.close()

'''
THIS REPLACES EVERYTHING IN THE FILE WITH KELLY LINE
employee_file = open("employees", "w")
employee_file.write("\nKelly - Customer Service")
employee_file.close()
'''

#CREATING ANOTHER FILE
employee_file = open("employees1", "w")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

#CREATING AN HTML PAGE
employee_file = open("index.html", "w")
employee_file.write("<p>This is HTML</p>")
employee_file.close()
