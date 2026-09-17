dic1 = {
  "name" : "Johen",
  "age" : "45",
  "city" : "New York"
}

print(dic1)
print(dic1.values())
print(dic1.keys())
print(dic1.items())

print(type(dic1))

print(dic1.get("name"))
print(dic1["age"])

dic1["city"] = "Mumbai"
print(dic1)