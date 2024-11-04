import math
# print('Andry Canel')
# print('o----')
# print(' ||||')
# print('L' * 20)
# price = 100
# print(price)
# print("Welcome to Florida Hospital! Please sign in the patient on our clipboard")
# last_name = input("Last Name: ")
# first_name = input("First Name: ")
# sex = input("Sex: M(male) or F(female): ")
# DOB = input("Birthdate: ")
# phoneNum = int(input("Cell: "))
# is_Emergency = bool(input("Is this an emergency? True or False:"))
#
# if sex == 'M':
#     print(f"Good morning Mr. {last_name}")
# else:
#     print(f"Good morning Ms. {last_name}")
#
# print(f"Your date of birth is {DOB}. And we can contact you at { phoneNum}")
# if is_Emergency:
#     print("""You stated this is an emergency so can you please tell me what the situation is so we can help
#           you right away""")
#     emergency_notes = input("...: ")
# else:
#     print("""Since this is not an emergency can you please wait in the lobby area until you hear your name called.
#           thank you for your patience""")

# birthyear = int(DOB[-4:])
# print(birthyear)
# age = 2022 - birthyear
# print(age)
#
# weight_lbs = float(input("Weight (lbs"))
# weight_kgs = weight_lbs * 0.45
# print(weight_kgs)
course = "hi my name is andry"
print(len(course))
print(course.upper())
print(course.replace('andry','mosh'))
print('hi' in course)

list = [1,2,3,4,6]
x = 3.1459
print(math.ceil(x))
print(math.floor(x))
print(math.fsum(list))
print(abs(round(x)))

is_credit_good = False
downpayment = 0.0;
if is_credit_good:
    downpayment = 1000000 * 0.1
else:
    downpayment = 1000000 * 0.2

print(downpayment)