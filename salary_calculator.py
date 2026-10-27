employees = [
    {"id": 1, "name": "Alice Johnson", "salary": 50000, "bonus_percent": 10},
    {"id": 2, "name": "Bob Smith", "salary": 60000, "bonus_percent": 15},
    {"id": 3, "name": "Carol Davis", "salary": 45000, "bonus_percent": 5},
]


def calculate_bonus(employee):
    return employee["salary"] * employee["bonus_percent"] / 100


def calculate_total_salary(employee):
    return employee["salary"] + calculate_bonus(employee)


def print_salary_report():
    print("Employee Salary Report")
    print("-" * 77)
    print(
        f"{'ID':<5}{'Name':<20}{'Base Salary':>17}"
        f"{'Bonus':>15}{'Total Salary':>20}"
    )
    print("-" * 77)

    for employee in employees:
        bonus = calculate_bonus(employee)
        total_salary = calculate_total_salary(employee)
        print(
            f"{employee['id']:<5}{employee['name']:<20}"
            f"{employee['salary']:>17,.0f}{bonus:>15,.0f}"
            f"{total_salary:>20,.0f}"
        )


if __name__ == "__main__":
    print_salary_report()
