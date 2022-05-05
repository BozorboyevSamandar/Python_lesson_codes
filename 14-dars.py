#-- Python darsi N: 12 ------
#-- Ro’yxatlar bilan ishlash. Lug’atlar (Dictionaries) -----
#-- Mentor: Samandar Bozorboyev ---

# my_dict = {
#     "brand": "Samsung",
#     "model": "A32",
#     "year": 2022
# }
# print(my_dict)
# x = my_dict["brand"] #elementga murojat qilish
# y = my_dict.get("model") #elementga murojat qilish
# print(x)
# print(y)

# kalit = my_dict.keys() #lug'at ro'yxatini faqat keys() kalitlarini chaqirib olishda ishlatiladi
# print(kalit)




# my_dict = {
#     "brand": "Samsung",
#     "model": "A32",
#     "year": 2022
# }
# my_dict["color"] = "white" #element qo'shdik
# my_dict.update({"model":"S23Ultra"}) #o'zgartishish kiritildi
# my_dict["year"] = 2021  #o'zgartishish kiritildi 2-usul
# print(my_dict)


my_dict = {
    "brand": "Samsung",
    "model": "A32",
    "year": 2022,
    "color": "blue",
}
# my_dict.pop("color") #o'chish
# my_dict.popitem()
# del my_dict["model"]
# my_dict.clear()

print(my_dict.keys())
print(my_dict.values())


