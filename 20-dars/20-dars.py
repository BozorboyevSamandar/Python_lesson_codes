#-- Python darsi N: 20 ------
#-- 20. Funksiyalar argumentlari, Return operatori, Rekursiya, Lambada funksiyalari -----
# #-- Mentor: Samandar Bozorboyev ---



# def my_function(first_name):

#     print(first_name + " Abduhalilov")

# my_function("Aziz")
# my_function("Farrux")


# def my_test(first_name, last_name):

#     print(first_name + ' ' + last_name)

# my_test("Aziz", "Abduhalilov")
# my_test("Farrux", "Erkinov")





# def my_func(car1, car2, car3):

#     print("Men " + car3 + " sotib oldim.")

# my_func(car1="Matiz", car2="Malibu", car3="Nexia 3")


# def my_function(meva1, meva2, meva3):
#     print(f"Men {meva1}ni yaxshi ko'raman")

# my_function(meva1="Shaftolini", meva2="Olma", meva3="Nok")






# *args
# def my_test2(*cars):
#     print("Men " + cars[2] + " sotib oldim.")
# my_test2("Matiz", "Malibu", "Nexia 3")


# def my_function(*noutbuk):
#     print(f"Men {noutbuk[1]} markali noutbuk ishlataman")

# my_function("Acer", "Lenovo", "Mac", "HP")






# **kwargs
# def my_function(**kid):
#     print("His last name is  " + kid['last_name'])
# my_function(first_name = "Aziz" , last_name="Abduhalilov")


# def my_test(**kitob):
#     print(f"Ushbu kitob muallifi {kitob['first_name']}")

# my_test(first_name="Said", last_name="Ahmad", age = 23 , addres = "Toshkent")



# ## standart funksiya
# def my_func(country = "Tashkent"):
#     print("I am from " + country)
# my_func("America")
# my_func()
# my_func("India")
# my_func()



### for and function
# def my_func(food):
#     for x in food:
#         print(x)
# fruits = ['apple', 'lemon', 'banana', 'cherry']
# my_func(fruits)




# def test(x):

#     return 5 * x

# print(test(4))
# print(test(5))
# print(test(8))


# def add(a, b):

#     return a + b

# def is_true(a):

#     return bool(a)

# res = add(2, 3)
# print("Qo'shish funksiyasini natijasi {}".format(res))

# res = is_true(2<5)
# print("\Is True funksiyasini natijasi {}".format(res))



# def add(a, b):
#     return a + b

# print(add(23, 34))





## REKURSIYA

# def factorial(x):
#     """Bu sonning faktorialini topuvchi rekursiv funksiya"""

#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
# num = 5

# print(num, "sonining faktoriali: ", factorial(num))

# factorial 3 --> 1*2*3 = 6



## lambda




# x = lambda a: a + 20
# print(x(5))

# x = lambda a, b: a * b
# print(x(5, 8))


# def myfunc(x):
#     return lambda a: a * x

# res = myfunc(3)
# print(res(12))