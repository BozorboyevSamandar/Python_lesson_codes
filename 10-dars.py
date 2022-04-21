#-- Python darsi N: 9 ------
#-- Ro’yxatlar bilan ishlash. Ro’yxatlarga o’zgartirish kiritish  -----
#-- Mentor: Samandar Bozorboyev ---

# colors = ['black', 'blue', 'red']
# colors[0] = 'yellow'
# colors[2] = 'pink'
# print(colors)

# raqamlar = [20, 65, 21, 50, 100, 30]
# raqamlar[0] = 130
# raqamlar[2] = raqamlar[2] + 9
# print(raqamlar)

# append() - yangi element qo'shish
# cars = []
# print(cars)
# cars.append('Spark')
# cars.append('Matiz')
# cars.append('Cobalt')
# cars.append('Nissan')
# print(cars)


# insert() metodi - ro'yxatning istalgan joyiga element qo'shadi
# cars = ['Laccetti', 'Nexia 3', "Damas"]
# cars.insert(0, "Mers")
# cars.insert(2, "Cobalt")
# print(cars)


# del va remove() - Elementlarni o'chirish
# cars = ['Laccetti', 'Damas', 'Nexia 3', "Damas"]
# del cars[1]
# print(cars)
# cars.remove('Damas')
# print(cars)

cars = ['Laccetti', 'Damas', 'Nexia 3', "Damas"]
buy = cars.pop(0)
print('Men', buy , 'sotib oldim')