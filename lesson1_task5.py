# Усовершенствовать программу «Банковский депозит» (lesson1_task4.py).
# Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада.
# Необходимо в главной функции реализовать вложенную функцию подсчета процентов для пополняемой суммы.
# Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
# Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев. Вложенная функция возвращает
# сумму дополнительно внесенных средств (с процентами), а главная функция — общую сумму по вкладу на конец периода.

def get_ending_amount(beginning_amount, duration_in_months, monthly_deposit, interest_capitalization=True):
    tariffs = [
        {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
        {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
        {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5},
    ]

    def interest_on_monthly_deposit(amount, months_num, rate):
        return amount * months_num + sum([round(amount * (rate / 100 * (n + 1) / 12), 2) for n in range(months_num)])

    for tariff in tariffs:
        if tariff['begin_sum'] <= beginning_amount < tariff['end_sum']:
            if interest_capitalization:
                ending_amount = beginning_amount
                for i in range(duration_in_months):
                    if i >= 2:
                        ending_amount += monthly_deposit
                    ending_amount = round(ending_amount * (1 + tariff[duration_in_months] / 12 / 100), 2)
            else:
                ending_amount = round(beginning_amount * (1 + (tariff[duration_in_months] / 100) *
                                      (duration_in_months / 12)), 2)
                ending_amount += interest_on_monthly_deposit(monthly_deposit, duration_in_months - 2,
                                                             tariff[duration_in_months])
            return ending_amount
