#🧩 Assignment 2: Mastering Python Data Structures
#👨‍🏫 Instructors: Syed Mohsin Bukhari & Miss Aisha (Cyberfort Technologies)

fvrt_movies = ("Mission Mangal", "3 Idiots", "Interstellar", "PRDP", "RRR")
print("Third favorite movie:", fvrt_movies[2]) # Accessing and printing the third movie (index 2)

# Trying to modify a tuple element
#fvrt_movies[0] = "The Godfather"
# TypeError: 'tuple' object does not support item assignment

list1 = [1, 1, 2, 3, 4, 4, 5, 6, 6]
set1 = set(list1)
print("\nSet from list with no duplicates num:", set1)

set1.add(7) # Adding a new number to the set
print("After adding:", set1)

set1.remove(5) #Removing a number
print("After removing a num:", set1)

# Union of two sets
setA = {1, 2, 3}
setB = {3, 4, 5}
union_set = setA.union(setB)
print("Union of setA and setB:", union_set)

std = {
    "name": "Amar",
    "roll_no": 21,
    "marks": 84
}
std["grade"] = "A" # Adding a new key 'grade'
std["marks"] = 90 # Updating the 'marks' key
print("\nStudent details:") # Looping and printing keys and values
for key, value in std.items():
    print(f"{key}: {value}")

# Creating a dictionary of subjects and their marks
subs_marks = {
    "Math": 88,
    "Science": 92,
    "English": 85,
    "History": 78
}
# Calculating the average marks
total_marks = sum(subs_marks.values())
num_of_subs = len(subs_marks)
avg_marks = total_marks / num_of_subs
print(f"\nAverage marks across subjects: {avg_marks:.2f}")
