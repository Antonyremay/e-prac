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
print(employees["emp1"]["name"])
for s in employees.values():
    print(s["salary"])
for key,value in employees.items():
    print(key,":",value["role"])
print([employees[i]["salary"] for i in employees])