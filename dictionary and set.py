agedict = {
    "name": "prateek",
    "mobile": "9868",
    "marks": {
        "maths": 90,
        "english": 80,
        "physics": 85,
            "social science": {
                "history": 80,
                "geography": 85,
            }
    }
}
agedict["age"] = "arjun" 
print(agedict)
print(agedict["marks"]["social science"])
agedict.update({"marks": {"social science": {"history": 90}}})
print(agedict["marks"]["social science"]["history"])    

set2= {"hello", "world", "hello",1,2,3}
print(set2)
print(type(set2))
set3= {1,2,3,4,5,6,7}

print(set2.pop())
print(set2.intersection(set3))
print(set2)
print(set2.union(set3))
word= {
    "table" : ["a peice of furniture ", "list of facts and figure"],
    "cat" : "a small animal"



            }
print (word)