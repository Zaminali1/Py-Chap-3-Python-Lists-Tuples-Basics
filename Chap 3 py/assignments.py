# Assignments:
# 1️⃣ List Operations:

# Create a list of 5 numbers.

# Append two new numbers to the list.

# Remove the third element.

# Sort the list in descending order.

# Print the final list 

list=[2,1,4,3,5]
list.append(7)
list.append(6)
list.pop(3)
list.sort(reverse=True)
print(list)




# Assignment :2

# Write a Python program to:
# 1️⃣ Create a tuple with 7 elements (mix of numbers and strings).
# 2️⃣ Count how many times a specific number appears in the tuple.
# 3️⃣ Find the index of a specific string inside the tuple.
# 4️⃣ Print the final results.


tupl=(1,"zamin",3,"hey",2,4,1)
print(tupl.count(1))
print(tupl.index("hey"))
print(tupl)


# Assignment 3=
#     Modify your movie program to:
# 1️⃣ Take 5 favorite movies from the user.
# 2️⃣ Check if "Inception" is in the list.
# 3️⃣ Replace the second movie with "The Matrix".
# 4️⃣ Print the updated list.


movies=[]
movie1=input("Enter 1st Movie:")
movie2=input("Enter 2nd Movie:")
movie3=input("Enter 3rd Movie:")
movie4=input("Enter 4th Movie:")
movie5=input("Enter 5th Movie:")

movies.append(movie1)
movies.append("The Matrix")
movies.append(movie3)
movies.append(movie4)
movies.append(movie5)
print(movies)


# Assignment=3: Grade Sorting
# 1️⃣ Ask the user to enter grades (A, B, C, etc.) for 5 students.
# 2️⃣ Store them in a list.
# 3️⃣ Sort the grades in ascending order.
# 4️⃣ Print the sorted list.

grades=[]
grades.append(input("Enter grades of Ali :"))
grades.append(input("Enter grades of Zohaib :"))
grades.append(input("Enter grades of Moin :"))
grades.append(input("Enter grades of Saim :"))
grades.append(input("Enter grades of Babar :"))
grades.sort()
print(grades)


