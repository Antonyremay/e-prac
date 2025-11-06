person={
    "std1":{
    "name":"Remay",
    "Dept":"CSE",
    "marks":98
    },
    "std2":{
    "name":"Andrew",
    "Dept":"MECH",
    "marks":95
    },
    "std3":{
    "name":"Jerizz",
    "Dept":"B.cpm",
    "marks":99
    },
}
print(person["std1"]["marks"])
for s in person.values():
    print(s["marks"])

for key,value in person.items():
    print(key,":",value["marks"])
print([person[s]["marks"]for s in person])