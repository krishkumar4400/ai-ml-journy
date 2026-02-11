"""
Student Enrollments
Given a list of tuples with info(name, subject)
    - list all unique course
    - list students enrolled in English
    - create dictionary (student, set of course)



"""

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

subjects = set()
enrolled_in_english = []


for tup in info:
    subjects.add(tup[1])
    if tup[1] == "English":
        enrolled_in_english.append(tup[0])

print(subjects)
print(enrolled_in_english)


d = {}
s = set()
for name, course in info:
    if(d.get(name) == None):
        d.update({name: set()})
        d[name].add(course)
    else:
        d[name].add(course)
        
print(d)