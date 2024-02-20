my_dict = {
    "students": [
        {"id": 20, "name": "giorgi", "age": 25},
        {"id": 25, "name": "giorgi", "age": 23},
        {"id": 100, "name": "nika", "age": 22},
        {"id": 56, "name": "nika", "age": 25},
        {"id": 1232, "name": "dato", "age": 22},
        {"id": 846723, "name": "archili", "age": 32}
    ],
    "subjects": [
        {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
        {"id": 2, "name": "Physics",
         "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
        {"id": 3, "name": "English",
         "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
        {"id": 4, "name": "Chemistry",
         "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
        {"id": 5, "name": "History",
         "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
    ]
}
availableIDs = map(lambda x: x["id"], my_dict["students"])
print(*availableIDs)
chosen = int(input("Please choose student from this id list: "))

tmp = list(filter(lambda x: x["id"] == chosen, my_dict["students"]))
print()
print(*list(map(lambda k: f"{k[0]}: {k[1]}", tmp[0].items())), sep=", ")
for i in my_dict["subjects"]:
    print("subject:", i['name'], end=", grade: ")
    for j in i["grades"].items():
        if j[0] == str(chosen):
            print(j[1])