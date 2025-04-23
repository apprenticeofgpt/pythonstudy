def regular_pay(hours, wage):
    return hours * wage

def overtime_pay(hours, wage, standard_hours=12, overtime_rate=1.3):
    overtime_hours = hours - standard_hours
    return (standard_hours * wage) + (overtime_hours * wage * overtime_rate)

pay_calc = {
    True: regular_pay,
    False: overtime_pay
}

hours = float(input("주당 총 근무 시간: "))
wage = float(input("시간당 급여: "))

total_pay = pay_calc[hours <= 12](hours, wage)
print(f"1주일 급여는 {total_pay:.2f}원 입니다.")