import pprint
employees={
    "emp1":{
    "name":"Remay",
    "role":"CEO",
    "salary":"100 Z"
    },
    "emp2":{
    "name":"Andrew",
    "role":"CO-CEO",
    "salary":"100 Z"
    },
    "emp3":{
    "name":"Hanni",
    "role":"AMBASSDOR",
    "salary":"100 Z"
    },
    "emp4":{
    "name":"Jerizz",
    "role":"MD",
    "salary":"100 Z"
    },
    "emp5":{
    "name":"Thiyok",
    "role":"CHAIRMAN",
    "salary":"100 Z"
    },
}
employees.update({
    "emp6":{
    "name":"Jeslin",
    "role":"CTO",
    "salary":"100 Z"
    }
})
employees.update({"emp7":{"name":"Rino","role":"PM","salary":"100 z"}})
employees["emp6"]["name"]="Aron"

rank=1
for s in employees:
    employees[s]["rank"]=rank
    rank+=1


print(employees["emp1"]["name"])
for i in employees.values():
    print(i["name"])
print([employees[s]["rank"] for s in employees])
for key,value in employees.items():
    print(key,":",value["role"])
print([employees[i]["salary"] for i in employees])
for key,value in employees.items():
    print(key,":",value["rank"])
for s in employees.values():
    print(f" the People {s["name"]} and their Rank is {s["rank"]}")


employees.pop("emp7")
pprint.pprint(employees)

for s in employees.values():
    print(F"the name {s["name"]} and thier position{s["role"]}")

del employees["emp6"]
pprint.pprint(employees)
for s in employees.values():
    del s["role"]

employees.pop("abc",None)
pprint.pprint(employees)


employees.popitem()
pprint.pprint(employees)

for s in employees.values():
    if s["rank"]<4:
        print(s["name"], "is elite")
count=0
for s in employees.values():
    if "name" in s:
        count+=1
print(count)