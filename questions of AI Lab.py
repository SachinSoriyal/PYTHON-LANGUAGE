# create a grade system (own)
rint(                   "Grade Program"               )

Subject1 = int(input("enter the first Subject marks:"))
Subject2 = int(input("enter the second Subject marks:"))
Subject3 = int(input("enter the third Subject marks:"))
Subject4 = int(input("enter the fourth Subject marks:"))
Subject5 = int(input("enter the fifth Subject marks:"))

Total_marks = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
Maximum_marks = 500
Total_percentage = (Total_marks*100) / 500

print("Total marks is:",Total_marks)

if Total_percentage >=90 and Total_percentage <=100:
    print("Grade A+")
elif Total_percentage >=75 and Total_percentage <=90:
    print("Grade A")
elif Total_percentage >=50 and Total_percentage <=75:
    print("Grade B")
elif Total_percentage >=33 and Total_percentage <=50:
    print("Grade C")
else:
    print("Fail")
    
    
print(                 "Sachin Singh"        )
