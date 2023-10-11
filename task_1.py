money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months_count = 0

while True:
    current_month_budget = salary + money_capital

    if spend <= current_month_budget:
        current_month_budget -= spend
        money_capital = current_month_budget
        months_count += 1
    else:
        break

    spend = spend * (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", months_count)
