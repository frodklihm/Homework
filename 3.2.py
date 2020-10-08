## Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def func(name, surname, birthyear, city, email, mobile_number):
    print(name, surname, birthyear, city, email, mobile_number)
func(name= "Arkasha", surname= "Sos", birthyear= 2004, city= "Nizny_Novgorod", email= "email", mobile_number= "09213921321")