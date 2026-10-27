# def show_profile(name, age, profession):
#     print("\n=========User Profile=====")
#     print(f"Name:{name}")
#     print(f" Age:{age}")
#     print(f"Profession:{profession}")


# def add_number(a, b):
#     result = a + b
#     return result

# def greet():
#     print("hi hello")

# def main():
#     name = input("Enter your name:")
#     age = int(input("enter your age:"))
#     profession = input("Enter your profession")

#     show_profile(name, age, profession)

#     greet()


# num1 = int(input("\n enter first number:"))
# num2 = int(input("\n enter second number:"))
# total = num1 + num2

# print(f"Sum:{total}")

# main()


from profile import show_profile
from calculator import add_number
from greeting import greeting
from calculator import check_even


def main():
    # name = input("enter a name")
    # age = input("Enter an age")
    # profession = input("enter your profession")

    # show_profile(name, age, profession)
    # greeting()

    # # add_number(num1, num2)

    # num1 = int(input("enter a number 1"))
    # num2 = int(input("enter a number 2"))

    # total = add_number(num1, num2)
    # print(f"total :{total}")
    # sum = check_even(total)
    # print(f"total check even and odd {sum}")

    age = 17
    if age >= 18:
        print("you can vote")
    else:
        print("you canot vote")

    marks = 75
    if marks >= 90:
        print("Grarde A")
    elif marks >= 70:
        print("Grade B")
    elif marks >= 50:
        print("Grade C")
    else:
        print("Fail")

    fruits = ["apple", "banana", "mango"]
    fruits.append("lemo")

    print(f"now make fruits {fruits}")

    students = {
        "name": "tahaa",
    }

    students["age"] = 35

    print(f"add student {students}")

    any_students = [
        {"name": "Ali", "marks": 85},
        {"name": "Ahmed", "marks": 45},
        {"name": "Sara", "marks": 92},
    ]

    print(any_students)


main()
