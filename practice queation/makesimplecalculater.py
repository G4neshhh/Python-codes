print("     mini calculator   ")
num1=float(input("enter a number 1 here ; "))
num2=float(input("enter a number 2 here ; "))

print("press 1 for addition\n press 2 for mminus \n press 3 for multiply \n press 4 for division ")

choice = int(input("press a any number between 1-4 :  "))

if choice == 1:
    print(num1 + num2 )
elif choice ==2 :
    print(num1-num2)
elif choice == 3:
    print(num1 *num2 )
elif choice == 4:
    print(num1 / num2 )
else :
    print("press right input between 1 to 4 only ")