info = {
    "Shreya": "humanbeing",
    "age":19,
    "origin": "Indian",
    "course": "Python"

}
print(info)
print(info["Shreya"])
print(info.get('age2'))

for keys in info.keys():
    print(info[keys])
print(info.items())
for key, value in info.items():
    print(f"value corresponding to the key {key} is {value}")

#methods
ep ={
    123:45,
    122:89,
    89:69,
    79:67
}

ep2={222:55, 223:67, 224:78}
ep.update(ep2)
ep.clear()
ep.pop(123)
ep.popitem()
del ep[122]
print(ep)
