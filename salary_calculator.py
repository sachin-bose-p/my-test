"""Calculate employee bonuses and print a salary report."""

from typing import TypedDict


class Employee(TypedDict):
    id: int
    name: str
    salary: int
    bonus_percent: int


employees: list[Employee] = [
    {"id": 1, "name": "Alice", "salary": 50000, "bonus_percent": 10},
    {"id": 2, "name": "Bob", "salary": 60000, "bonus_percent": 15},
    {"id": 3, "name": "Charlie", "salary": 45000, "bonus_percent": 5},
]


def calculate_bonus(employee: Employee) -> float:
    """Return an employee's bonus based on their salary and bonus percentage."""
    return employee["salary"] * employee["bonus_percent"] / 100


def calculate_total_salary(employee: Employee) -> float:
    """Return an employee's salary plus their calculated bonus."""
    return employee["salary"] + calculate_bonus(employee)


def print_salary_report(employee_records: list[Employee]) -> None:
    """Print a formatted salary report for the supplied employees."""
    print(f"{'Employee ID':<12} {'Name':<12} {'Salary':>10} {'Bonus':>10} {'Total':>10}")
    for employee in employee_records:
        bonus = calculate_bonus(employee)
        total = calculate_total_salary(employee)
        print(
            f"{employee['id']:<12} {employee['name']:<12} "
            f"{employee['salary']:>10} {bonus:>10.0f} {total:>10.0f}"
        )


if __name__ == "__main__":
    print_salary_report(employees)
