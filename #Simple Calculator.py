#Simple Calculator

Select = input("Choose what you would like to operate with : / * + - :  ")

type1 = float(input("Enter your number: "))
type2 = float(input("Enter your number: "))

if Select == "+":
    answer = type1 + type2
    print(round(answer, 2))
elif Select == "-":
    answer = type1 - type2
    print(round(answer, 2))

elif Select == "*":
    answer = type1 * type2
    print(round(answer, 2))

elif Select == "/":
    answer = type1 / type2
    print(round(answer, 2))

else :
    print(f"{Select} is Inavlid Select")




