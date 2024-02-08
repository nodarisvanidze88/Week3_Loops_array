# thislist1 = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))
# thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
            #   0         1        2        3         4       5         6
# tropical = ["mango", "pineapple", "papaya"]
# thislist2.append("marckvi")
# thislist2.insert(2,"atami")
# thislist2.remove("kiwi")
# result = tropical + thislist2
# thislist2.extend(tropical)

# result = []
# for i in thislist2:
#     result.append(i.upper())
# result = [i for i in thislist2 ]
# print(result)
# print(result == thislist2)
# print(id(result))
# print(id(thislist2))
# result1 = thislist2[::-1]
# result2 = thislist2[:4]
# result3 = thislist2[2:]
# result4 = thislist2[2:4]
# result5 = thislist2[2]

# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)
# =======================================
# user = "hello world Tbilisi"
# result = list(user)
# print(result)
# for i in thislist2:
#     print(i)
# someText = "Hello World"
# print(someText[2])
# =======================================
# list1 = [22, 10, 16, 13, 25]
# list1.sort(reverse = True)
# print(list1)



# =======================================
# We have some list, may be next num is grater to previouse by 3, find missed number if ther is missing
# =======================================
# def main():
#     initialValues = [30, 9, 24, 12, 18, 15, 3, 21, 27, 6]
#     sortedIntegers = sortedFunction(initialValues)
#     print(sortedIntegers)
#     print(numChecker(sortedIntegers))


# def sortedFunction(ls):
#     return sorted(ls)

# def numChecker(ls):
#     counter = 0
#     for i in range(len(ls)-1):
#         if ls[i+1] - ls[i] == 3:
#             counter += 1
#     if len(ls)-1 == counter:
#         return "We have all nums"
#     elif (len(ls)-1) - counter == 1:
#         for i in range(len(ls)-1):
#             if not ls[i]+3 in ls:
#                 return ls[i]+3

# if __name__=="__main__":
#     main()



# =======================================
# Fibonachi sequence
# =======================================
# def main():
#     user = user_input_Checker()
#     result = fibonachiNum(int(user))
#     print(result)

# def user_input_Checker():
#     while True:
#         user = input("Give Me End Number: ")
#         if user.isdigit():
#             return user

# def fibonachiNum(n):
#     newArry = [0, 1]
#     for i in range(2,n):
#         newArry.append(newArry[-1]+newArry[-2])
#     return newArry

# if __name__=="__main__":
#     main()



# =======================================
# e-mail and password validator
# =======================================
# def main():
#     email = emailChecke()
#     password = input("Add new Password: ")
#     reenteredPassword = passValidator(password)
#     print(f"Your email is {email} and your password is {reenteredPassword}")


# def emailChecke():
#     checksymbols = ["@","."]
#     while True:
#         email = input("Add youe Mail:")
#         if checksymbols[0] in email and checksymbols[1] in email:
#             return email

# def passValidator(pas):
#     while True:
#         password = input("Reenter your Pssword:")
#         if pas != password:
#             continue
#         else:
#             return password
# if __name__=="__main__":
#     main()




# =======================================
# speed time distance calculator
# =======================================
# def main():
#     print("\nSelect your choise what you need to get\n")
#     print(f"1. Speed\n"
#           f"2. Distance\n"
#           f"3. time")
#     selected_mode = choise()
#     if selected_mode == "1":
#         distance = numChecker("Give the Distance: ")
#         time = numChecker("Give the Time: ")
#         print(get_speed(distance,time))
#     elif selected_mode == "2":
#         speed = numChecker("Give the Speed:")
#         time = numChecker("Give the Time: ")
#         print(get_distance(speed,time))
#     elif selected_mode == "3":
#         speed = numChecker("Give the Speed: ")
#         distance = numChecker("Give the Distance: ")
#         print(get_time(distance,speed))

# def choise():
#     choises = ["1", "2", "3"]
#     while True:
#         user = input("Select your choise 1,2,3 ")
#         if user in choises:
#             return user

# def numChecker(question):
#     while True:
#         user = input(question)
#         if user.isdigit():
#             return int(user)

# def get_speed(distance, time):
#     return distance/time

# def get_time(distance, speed):
#     return distance / speed

# def get_distance(speed, time):
#     return speed * time

# if __name__=="__main__":
#     main()
