
GROSS_SALARY = input("enter gross pay: ")
STATE = input("enter state (NY, CA or TX): ")

def USA(salary, state):

    # variable for federal_tax tax
    federal_tax = 0

    STANDARD_DEDUCTION_FEDERAL = 12950
    STANDARD_DEDUCTION_NY = 8000
    STANDARD_DEDUCTION_CA = 4601

    salary = int(salary)

    deducted_salary = salary - STANDARD_DEDUCTION_FEDERAL


    if deducted_salary < 0:
        federal_tax = 0

    elif deducted_salary < 10275:
        federal_tax = 0.1 * deducted_salary

    elif 10275 <= deducted_salary < 41775:
        federal_tax = 1027.5 + 0.12 * (deducted_salary - 10275)

    elif 41775 <= deducted_salary < 89075:
        federal_tax = 4807.5 + 0.22 * (deducted_salary - 41775)

    elif 89075 <= deducted_salary <= 100000:
        federal_tax = 15213.5 + 0.24 * (deducted_salary - 89075)

    # fica

    if salary <= 147000:
        fica = 0.0765 * salary

    elif 147000 < salary <= 200000:
        fica = 0.062 * 147000 + 0.0145 * salary

    elif salary > 200000:
        fica = 0.062 * 147000 + 0.0145 * 200000 + 0.0235 * (salary - 200000)


    # state_tax taxes

    def NY():
        # standard deduction

        deducted_salary_ny = salary - 8000

        if deducted_salary_ny < 0:
            state_tax = 0

        elif deducted_salary_ny < 8500:
            state_tax = 0.04 * deducted_salary_ny

        elif 8500 <= deducted_salary_ny < 11700:
            state_tax = 340 + 0.045 * (deducted_salary_ny - 8500)

        elif 11700 <= deducted_salary_ny < 13900:
            state_tax = 484 + 0.0525 * (deducted_salary_ny - 11700)

        elif 13900 <= deducted_salary_ny < 21400:
            state_tax = 600 + 0.059 * (deducted_salary_ny - 13900)

        elif 21400 <= deducted_salary_ny < 80650:
            state_tax = 1042 + 0.0609 * (deducted_salary_ny - 21400)

        elif 80650 <= deducted_salary_ny < 215400:
            state_tax = 4650 + 0.0641 * (deducted_salary_ny - 80650)

        elif 215400 <= deducted_salary_ny <= 100000:
            state_tax = 13288 + 0.0685 * (deducted_salary_ny - 215400)


        return state_tax


    def CA():
        # standard deduction

        deducted_salary_ca = salary - 4601

        if deducted_salary_ca < 0:
            state_tax = 0

        elif deducted_salary_ca < 8932:
            state_tax = 0.01 * deducted_salary_ca

        elif 8932 <= deducted_salary_ca < 21175:
            state_tax = 89.32 + 0.02 * (deducted_salary_ca - 8932)

        elif 21175 <= deducted_salary_ca < 33421:
            state_tax = 334.18 + 0.04 * (deducted_salary_ca - 21175)

        elif 33421 <= deducted_salary_ca < 46394:
            state_tax = 824.02 + 0.06 * (deducted_salary_ca - 33421)

        elif 46394 <= deducted_salary_ca < 58634:
            state_tax = 1602.4 + 0.08 * (deducted_salary_ca - 46394)

        elif 58634 <= deducted_salary_ca <= 100000:
            state_tax = 2581.6 + 0.093 * (deducted_salary_ca - 59634)

        return state_tax


    # federal_tax + state_tax

    total_tax = 0

    if state == 'NY':
        total_tax = federal_tax + NY()

    elif state == 'CA':
        total_tax = federal_tax + CA()

    elif state == 'TX':
        total_tax = federal_tax

    taxrate = (total_tax + fica) / salary
    netpay = salary - (total_tax + fica)

    USA = {
        "netpay": netpay,
        "taxrate": taxrate
    }

    return USA


result = USA(GROSS_SALARY, STATE)
print(result['netpay'])
print(result['taxrate'])

print(f'Your net pay is ${result["netpay"]} with a tax rate of {result["taxrate"]}')