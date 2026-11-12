a = int(input("Enter Number A:"))
b = int(input("Enter Number B:")) 
option = int(input("Enter Operation you wish to peform: 1 for addition,2 fro subtraction,3 for multiplication, 4 fro division"))
if option==1:
    print("The Sum Of Value A and B is ", a+b)
elif option==2:
    print("The Difference of Value A and B is", a-b)
if a> b:
       print("The Difference of Value A and B is",a-b)
elif option==3:
    print("Th e Product of value A and B is ",a*b)
elif option==4:
    print("The Division of Value A and B is",a/b)
else:
    print("Invalid Operation!! Please Enter Correct Value ")

 
for i in range(10):
    if i == 2:
        break
    print(i);

list1 = [1,2,3]
list2 = [4,5,6]
new_list = list1+list2
print(new_list)