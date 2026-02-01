#44 Python Dictionaries Access
studentInfo = {
    "Esan" : {
        "name" : "Esan",
        "location" : "Rajshahi",
        "study" : "12",
        "Subject" : "commerce",
        "Roll" : 18,
        "Number" : 171765675765
    },
    "Tutul" : {
        "name" : "Tutul",
        "location" : "Dhaka",
        "study" : "12",
        "Subject" : "commerce",
        "Roll" : 20,
        "Number" : 7576567567
    },
    "Year" : 1981
}
print(studentInfo["Year"])
x = studentInfo.get("Tutul")
print(x)
y = studentInfo.keys()
print(y)
z = studentInfo.values()
print(z)
