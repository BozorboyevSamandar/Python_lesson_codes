#-- Python darsi N: 20 ------
#-- 19. Funksiyalar, Funksiyalarning sintaksisi -----
#-- Mentor: Samandar Bozorboyev ---

### funksiya sintaksisi
# def funksiya_nomi(parametr1, parametr2, ):
#     '''hujjat satri'''
#     buyruqlar

###
# def
# a-z, A-Z yoki 0-9
# 1uzgaruvchi - bu yaroqsiz, uzgaruvchi2 - bu yaroqli , my_function, test_func my_function2, ....
# : funksiyaning bosh qismi tugaganligi haqida bildiradi 

def my_function():
    '''Bu funksiya nima ish bararishini to'liq yoritib beradigan hujjat'''
    print("Hi from a function")
    print("My name is Alex")
my_function()
print(my_function.__doc__)