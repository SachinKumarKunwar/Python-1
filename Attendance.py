attend=int(input("Enter Classes attended by you: "))
total_classes=int(input("Enter total number of classes: "))
percent=(attend/total_classes)*100
if percent>=75:
    print("Enough Attendance")
    if percent>=90:
        print("Grade A")
    elif percent>=80 and percent<90:
        print("Grade B")
    elif percent>=75 and percent<80:
        print("Grade C")
    elif percent<=75:
        print("Grade D")
else:
    print("Less attendance .You need more attendance to give Exam.")