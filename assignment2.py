#List Creation
age_list=[24,25,26,27,28]
name_list=["Anu","irin","Mincy","Bincy","Ancy"]

#List Operations
name_list.append("Yazhini")
age_list.insert(2,30)
print(name_list)
name_list.pop()
age_list.extend([29,30,26])
print(age_list)
age_list.sort(reverse=True)
print("Maximum",max(age_list))
print("Minimum",min(age_list))
print("Sum",sum(age_list))

#Accessing
print("First Element ",name_list[0])
print("Last element",name_list[-1])
print("From 2 to 4",name_list[2:5])
print("Reverse Order",name_list.reverse())

#dictionary
student_marks={
    "Anu":89,
    "Irin":99,
    "Mincy":98,
    "Bincy":90
         
}

student_marks.update({"Janani":80})
student_marks["Irin"]=82
print(student_marks)
print("All Keys",student_marks.keys())
print("All Values",student_marks.values())

#set
my_set={"a","e","i","o","u","a","a","i"}

#y_set.update(4)="s" #Reason : Set is immutable thing and unable to update

set1={1,3,5,7,9}
set2={2,3,5,8,10}
print("intesection",set1.intersection(set2))
print("Union",set1.union(set2))

#Operators

num1=int(input("Enter Score:(Score should be from 0 to 10:"))
if (num1>=7):
    print("Above Average")
elif(num1>=4):
    print("Average")
else:
   print("Below Average")

         