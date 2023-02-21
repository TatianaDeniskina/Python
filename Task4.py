vyruchka = int(input("Введите выручку фирмы:"))
isderjki = int(input("Введите издержки фирмы:"))
if vyruchka > isderjki:
    pribyl = vyruchka - isderjki
    print("Финансовый результат - прибыль. Ее величина", pribyl)
    r_vyruchki = pribyl/vyruchka
    print("Рентабельность выручки =", r_vyruchki)
    sotrudniki = int(input("Введите число сотрудников:"))
    print("Прибыль фирмы на одного сотрудника:", (pribyl/sotrudniki))
else:
    print("Финансовый результат - убыток.")
