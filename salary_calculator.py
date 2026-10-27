import math
from collections.abc import Sequence
from dataclasses import dataclass


employees = [
    {"id": 1, "name": "Alice Johnson", "salary": 50000, "bonus_percent": 10},
    {"id": 2, "name": "Bob Smith", "salary": 60000, "bonus_percent": 15},
    {"id": 3, "name": "Carol Davis", "salary": 45000, "bonus_percent": 5},
]


@dataclass(frozen=True, slots=True)
class EmployeeSummary:
    employee_count: int
    average_base_salary: float
    highest_paid_employee: str | None
    highest_total_salary: float | None


def _is_finite_number(value: object) -> bool:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    try:
        return math.isfinite(value)
    except OverflowError:
        return False


def _validate_employee(
    employee: object,
) -> tuple[int | float, int | float, str]:
    if not isinstance(employee, dict):
        raise TypeError("employee must be a dictionary")

    for field in ("id", "name", "salary", "bonus_percent"):
        if field not in employee:
            raise ValueError(f"employee is missing required field '{field}'")

    employee_id = employee["id"]
    if not _is_finite_number(employee_id):
        raise ValueError("employee field 'id' must be a finite number")

    name = employee["name"]
    if not isinstance(name, str):
        raise ValueError("employee field 'name' must be a string")

    salary = employee["salary"]
    if not _is_finite_number(salary):
        raise ValueError("employee field 'salary' must be a finite number")

    bonus_percent = employee["bonus_percent"]
    if not _is_finite_number(bonus_percent):
        raise ValueError("employee field 'bonus_percent' must be a finite number")

    return salary, bonus_percent, name


def calculate_bonus(employee: dict[str, object]) -> float:
    salary, bonus_percent, _ = _validate_employee(employee)
    return salary * bonus_percent / 100


def _calculate_total_salary(
    salary: int | float,
    bonus_percent: int | float,
) -> float:
    return salary + salary * bonus_percent / 100


def calculate_total_salary(employee: dict[str, object]) -> float:
    salary, bonus_percent, _ = _validate_employee(employee)
    return _calculate_total_salary(salary, bonus_percent)


def summarize_employees(
    employee_records: Sequence[dict[str, object]],
) -> EmployeeSummary:
    if not employee_records:
        return EmployeeSummary(
            employee_count=0,
            average_base_salary=0.0,
            highest_paid_employee=None,
            highest_total_salary=None,
        )

    salaries: list[int | float] = []
    highest_paid_employee: str | None = None
    highest_total_salary: float | None = None
    for employee in employee_records:
        salary, bonus_percent, name = _validate_employee(employee)
        total_salary = _calculate_total_salary(salary, bonus_percent)
        salaries.append(salary)
        if highest_total_salary is None or total_salary > highest_total_salary:
            highest_paid_employee = name
            highest_total_salary = total_salary

    return EmployeeSummary(
        employee_count=len(employee_records),
        average_base_salary=sum(salaries) / len(salaries),
        highest_paid_employee=highest_paid_employee,
        highest_total_salary=highest_total_salary,
    )


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

    summary = summarize_employees(employees)
    print("-" * 77)
    print(f"Employee Count: {summary.employee_count}")
    print(f"Average Base Salary: {summary.average_base_salary:,.2f}")
    if (
        summary.highest_paid_employee is not None
        and summary.highest_total_salary is not None
    ):
        print(
            f"Highest-Paid Employee: {summary.highest_paid_employee} "
            f"({summary.highest_total_salary:,.2f})"
        )


if __name__ == "__main__":
    print_salary_report()
