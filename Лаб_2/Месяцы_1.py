money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 0
flag = 1

while flag != 0:
    money_capital += salary
    if money_capital < spend:
        flag = 0
    else:
        money_capital -= spend
        months += 1
    spend *= 1 + increase
print("Количество месяцев, которое можно протянуть без долгов:", months)