
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends[0]) #prints the name for the index number
print(friends[-1]) #prints the last name
print(friends[1:]) #prints the names after index 1 including index 1
print(friends[1:3]) #prints the names between index 1 and 3 including index 1 without index 3

friends[1] = "Mike" #updates the friends list index 1 name with Mike
print(friends[1])

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers) #extinde lista friends cu lista lucky numbers
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Creed") #it adds Creed to the friends list at the end of the list
print(friends)

friends.insert(1,"Kelly") #insert in the friends list at index 1 name Kelly
print(friends)

friends.remove("Jim") #removes Jim element
print(friends)

friends.clear() #clears the friends list
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop() #removes last element
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends.index("Oscar")) #it prints the index number for Oscar which is 3

friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friends.count("Jim")) #it counts how many times Jim appears in the list which is 2 times
friends.sort()  #sorts the list alphabetically
print(friends)

lucky_numbers.sort() #sorts the numbers
print(lucky_numbers)

lucky_numbers.reverse() #it prints the numbers in reverse order
print(lucky_numbers)

friends2 = friends.copy() #it copies the friends list into the friends2 list
print(friends2)