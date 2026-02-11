"""
Dictionary
    key:value pairs

keys are always unique

dictionary is mutable
dictionary is unordered
"""

empty_dict = {}
print(empty_dict)  # {}
print(type(empty_dict))  # <class 'dict'>

student = {
    "id": 1,
    "name": "Krish",
    "age": 21,
    "city": "Meerut",
    "subjects": ["cloud", "devops", "ai", "ml", "mern", "python"],
    "marks": (90, 91, 99, 100, 100),
    3.14: "PI",
}

print(student)
print(student["id"])
print(student["name"])
print(student["age"])

print(student.keys())  # dict_keys(['id', 'name', 'age', 'city', 'subjects', 'marks'])
dict_keys = student.keys()
print(dict_keys)
for val in dict_keys:
    print(val)
"""
id
name
age
city
subjects
marks
"""

print(
    student.values()
)  # dict_values([1, 'Krish', 21, 'Meerut', ['cloud', 'devops', 'ai', 'ml', 'mern', 'python'], (90, 91, 99, 100, 100)])

print(student.items())
"""
dict_items([('id', 1), ('name', 'Krish'), ('age', 21), ('city', 'Meerut'), ('subjects', ['cloud', 'devops', 'ai', 'ml', 'mern', 'python']), ('marks', (90, 91, 99, 100, 100))])
"""

student["cgpa"] = 9
print(student)

student["id"] = 100
print(student)

"""
## dictionary methods
1. d.keys(): returns all keys
2. d.values(): returns all values
3. d.items(): returns (key,value) pairs
4. d.get(val): returns val according to key
5. d.update(new_item)

"""

print("\n\n new Dictionary\n\n")
new_dict = {"id": "2", "name": "krish kumar", "age": "21", "email": "krish@gmail.com"}

print(new_dict.get(1))  # None
print(new_dict.get("2"))  # None
# print(new_dict[2])  # error
print(new_dict.get("id"))  # 2
print(new_dict.get("email"))  # krish@gmail.com

new_dict.update({"cgpa": 10})
print(new_dict)

dict_keys = new_dict.keys()
print(dict_keys)
print(type(dict_keys))  # <class 'dict_keys'>
dict_keys = list(new_dict.keys())  # dict_keys(['id', 'name', 'age', 'email'])
print(dict_keys)  # ['id', 'name', 'age', 'email']
print(type(dict_keys))  # <class 'list'>

dict_values = list(new_dict.values())
print(dict_values)  # ['2', 'krish kumar', '21', 'krish@gmail.com']

dict_items = list(new_dict.items())
print(
    dict_items
)  # [('id', '2'), ('name', 'krish kumar'), ('age', '21'), ('email', 'krish@gmail.com')]

new_dict.update({
    "city":"delhi",
    "name":"krishna",
    "id":3033,
    7:8,
    9:10
})

print(new_dict)