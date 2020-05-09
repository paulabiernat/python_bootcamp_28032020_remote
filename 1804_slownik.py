

#pol_ang = dict()
pol_ang = {
    "kot": "cat",
    "ptak": "bird"
}

pol_ang["pies"] = "dog"
pol_ang["kot"] = "kitty"

print(pol_ang)


# drugi sposob

dict_2 = dict(a=10, b=22, c=33)

print(dict_2)

# trzeci sposob
dict_3 = dict([
    ["x", "ala"]
])
print(dict_3.keys())
print(dict_3.values())
print(dict_3.items())

print(dict_3.get("x"))
print(dict_3.get("z", "brak"))

if 'z' in dict_3:
   print(dict_3["z"])
else:
    print("brak")