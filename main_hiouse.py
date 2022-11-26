from qualification import age
from ordersize_1 import size
from ordersize_2 import medium
from ordersize_3 import large
from ordersize_4 import x_large




def mainpizza():
    input_age = int((input("Enter your age ")))
    if input_age > 18:
        input_On = (input("Enter your size "))
        input_Two = int(input("Enter your amount or quantity"))
        if input_On == 's':
            print("\n The solution of the addition is :", (size(input_On, input_Two)))
        elif input_On == 'm':
            print("\n The solution of the substation is :", (medium(input_On, input_Two)))
        elif input_On == 'l':
            print("\n The solution of the multiplication is :", (large(input_On, input_Two)))
        elif input_On == 'xl':
            print("\n The solution of the division is :", (x_large(input_On, input_Two)))
        con = input('do you want continue yes/no')
        if con == 'yes':
            mainpizza()

    else:
        print("\nInvalid operator!")
