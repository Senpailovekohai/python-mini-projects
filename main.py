student=[]
condition="yes"
while condition=="yes":
    name=input("Enter student name:")
    while True:
        try:
            id=int(input("Enter student id"))
            break
        except:
            print("Error!!Please! Enter number only")

    dep=input("Enter the department of the student:")

    detail={ "name":name,
            "student id":id,
            "department":dep
    }
    student.append(detail)
    condition=input("Do you want to add another ?").lower()
    while condition!="yes" and condition!="no":
        print("Error!! Please type only Yes/No")
        condition=input("Do you want to add another?").lower()

for info in student:
    print(info["name"],
          "-",
          "Student id:",
          info["student id"],
          "-",
          "Department:",
          info["department"]


    )





