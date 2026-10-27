import math


employees = [
    {"id": 1, "name": "Alice Johnson", "salary": 50000, "bonus_percent": 10},
    {"id": 2, "name": "Bob Smith", "salary": 60000, "bonus_percent": 15},
    {"id": 3, "name": "Carol Davis", "salary": 45000, "bonus_percent": 5},
]


def _is_finite_number(value: object) -> bool:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    try:
        return math.isfinite(value)
    except OverflowError:
        return False


def _validate_employee(employee: object) -> tuple[int | float, int | float]:
    if not isinstance(employee, dict):
        raise TypeError("employee must be a dictionary")

    for field in ("id", "name", "salary", "bonus_percent"):
        if field not in employee:
            raise ValueError(f"employee is missing required field '{field}'")

    salary = employee["salary"]
    if not _is_finite_number(salary):
        raise ValueError("employee field 'salary' must be a finite number")

    bonus_percent = employee["bonus_percent"]
    if not _is_finite_number(bonus_percent):
        raise ValueError("employee field 'bonus_percent' must be a finite number")

    return salary, bonus_percent


def calculate_bonus(employee: dict[str, object]) -> float:
    salary, bonus_percent = _validate_employee(employee)
    return salary * bonus_percent / 100


def calculate_total_salary(employee: dict[str, object]) -> float:
    salary, _ = _validate_employee(employee)
    return salary + calculate_bonus(employee)


def print_salary_report() -> None:
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
