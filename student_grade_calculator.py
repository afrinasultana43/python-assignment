choice = "c"
while choice == "c":
    
    name = input("Student's name : ")
    print("Please enter your marks for these subjects.")
    
    sub1 = int(input("subject 1 : "))
    sub2 = int(input("subject 2 : "))
    sub3 = int(input("subject 3 : "))
    
    if (sub1<0 or sub1>100 or sub2<0 or sub2>100 or sub3<0 or sub3>100):
        print("Please enter correct marks!")
    else:
        
        total = sub1 + sub2 + sub3
        avg = total/3
        avg = round(avg, 2)
        if (sub1<50 or sub2<50 or sub3<50):
            grade="F"
        elif (avg>=80):
            grade = "A+"
        elif (avg>=70):
            grade = "A"
        elif (avg >=60):
            grade = "B"
        elif (avg>=50):
            grade = "C"


        print(f"Student Name: {name}")   
        print(f"Total Marks: {total}")
        print(f"Average: {avg}")
        print(f"Grade: {grade}")

    
    choice =  input("Type 'c' for rechecking or anything for exiting : ").lower()
    if(choice=="c"):
        print("Rechecking...")
    else:
        print("Exiting...")