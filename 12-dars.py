#-- Python darsi N: 12 ------
#-- Ro’yxat bilan ishlash. O’zgarmas ro’yxatlar (Tuples)   -----
#-- Mentor: Samandar Bozorboyev ---


# ro'yxatlarni tartiblash .sort() 

# mevalar = ['olma', 'gilos', 'shaftoli', 'anjir' , 'banan']
# mevalar.sort()
# print(mevalar)

# # ro'yxatni aylantirish
# mevalar.sort(reverse=True)
# print(mevalar)






# # ro'yxatni aylantirish
# mevalar = ['olma', 'gilos', 'shaftoli', 'anjir']
# print("sorted(): ", sorted(mevalar))
# print("Asl holat: ", mevalar)

# print(sorted(mevalar, reverse=True))






# sonlar  = [23, 3000, 213, 704, 43, 1000, 69]
# sonlar.sort()
# print(sonlar)
# kichik = min(sonlar)
# print(kichik)
# katta = max(sonlar)
# print(katta)
# umumiy = sum(sonlar)
# print(umumiy)
# print(" Eng kichik son: ",kichik,"\n","Eng katta son: ",katta,"\n","Umumiy qiymat: ",umumiy)









# mevalar = ['olma', 'gilos', 'shaftoli', 'anjir' , 'banan', 'olcha', 'apilsin']
# # like = mevalar[0:3]
# dislike = mevalar[2:5]
# print(dislike)



# sonlar = [23, 33, 54, 12, 456, 12, 321]

# sonlar2 = sonlar
# sonlar2.append(100)
# sonlar2.append(101)
# print(sonlar2)
# print(sonlar)

# sonlar2 = sonlar[:]
# sonlar2.append(100)
# print(sonlar2)
# print(sonlar)



# TUPLES - QATORLAR - o'zgarmas ro'yxarlar




# cars = ('bmw', 'nissan', 'damas', 'lacette', 'Cobalt', 'Nexia')
# # print(cars[-1])
# # print(cars[2:5])
# cars = list(cars)
# cars[2] = 'Malibu'
# cars = tuple(cars)
# print(cars)



# my_tuple = (23, 43, 66, 12)
# my_tuple2 = ('desktop', 'pen', 'coffee')
# qoshilma = my_tuple + my_tuple2
# print(qoshilma)





# my_tuple2 = ('desktop', 'pen', 'coffee')
# print(my_tuple2*3)






# Tuples - Qatorlarni o'chirib bo'lmaydi
# my_tuple2 = ('desktop', 'pen', 'coffee') 
# del my_tuple2
# print(my_tuple2)




#count - elementlani sanashda ishlatiladi

# my_tuple2 = ('desktop', 'pen', 'coffee', 'desktop', 'desktop')
# print(my_tuple2.count('desktop'))













