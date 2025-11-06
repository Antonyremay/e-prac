person=dict(
    std1=dict(name="remay",dept="cse",mark=98),
    std2=dict(name="Andrew",dept="mech",mark=95),
    std3=dict(name="Jerizz",dept="B.com",mark=99),
)
print(person["std1"]["mark"])
for s in person.values():
    print(s["mark"])
for key,value in person.items():
    print(key,":",value["mark"])
print([person[s]["mark"]for s in person])
