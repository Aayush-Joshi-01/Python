import csv

with open("Assets/student.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Roll-No.", "Marks", "Address"])
    while True:
        name = input("Enter name: ")
        roll = input("Enter Roll-No.: ")
        marks = input("Enter marks: ")
        address = input("Enter address: ")
        writer.writerow([name, roll, marks, address])
        option = input("Do you want to record more [y/n]: ")
        if option.lower() == "n":
            break
    print("Success")
