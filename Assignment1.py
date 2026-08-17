#1.

string1="Hello "
string2=input("Enter your Name: ")
print(string1+ string2)


String3 =",Welcome to Python Programming"
string4=string1+string2+String3 
print(string4)
#2.

print(string4[0]) 

print(string4[-1])

print(string4[:6])

print(string4[-12::-1])

print(string4[::-1])

print(string4[-18:-11])

#3.
strM="Python beginner tutorial"
print(strM.upper())
print(strM.lower())
print(strM.capitalize())
print(strM.count("t"))
print(strM.replace("Python","Machine Learning"))

#4.

tuple1=(10,20,30)
tuple2=(40,50,60)
t_combine=tuple1+tuple2
t_combine=t_combine*3
print(t_combine[2])
print(t_combine[0:3])
print(t_combine)
print(t_combine[:-4:-1])
