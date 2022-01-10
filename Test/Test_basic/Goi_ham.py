def description_city (country, city):
    print (f"{city} la thanh pho cua {country}")

description_city(country="Viet Nam", city = "Ha Noi")
t = 3
while t>0:
    description_city(country="Viet Nam", city = input())
    t-=1