"""Print a salary and bonus report for the sample employees."""

import math
from collections.abc import Mapping, Sequence
from typing import TypedDict


class SalarySummary(TypedDict):
    total_employees: int
    average_salary: float | None
    highest_paid_employee: str | None


Employee = Mapping[str, object]

EMPLOYEES: list[dict[str, object]] = [
    {"id": 1, "name": "Jordan", "salary": 50000, "bonus_percent": 10},
    {"id": 2, "name": "Alice", "salary": 60000, "bonus_percent": 15},
    {"id": 3, "name": "Morgan", "salary": 45000, "bonus_percent": 5},
]


def _validate_employee(employee: Employee, index: int) -> None:
    """Validate one employee record and ensure its compensation is calculable."""
    if not isinstance(employee, Mapping):
        raise TypeError(f"Employee at index {index} must be a dictionary.")

    for field in ("id", "name", "salary", "bonus_percent"):
        if field not in employee:
            raise ValueError(f"Employee at index {index} is missing required field '{field}'.")

    employee_id = employee["id"]
    if isinstance(employee_id, bool) or not (
        isinstance(employee_id, int) and employee_id >= 0
        or isinstance(employee_id, str) and employee_id.strip()
    ):
        raise ValueError(f"Employee at index {index} has an invalid 'id'.")

    name = employee["name"]
    if not isinstance(name, str) or not name.strip():
        raise ValueError(f"Employee at index {index} has an invalid 'name'.")

    values: dict[str, float] = {}
    for field in ("salary", "bonus_percent"):
        value = employee[field]
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(
                f"Employee at index {index} has an invalid '{field}'; "
                "expected a finite, non-negative number."
            )
        try:
            numeric_value = float(value)
        except OverflowError as error:
            raise ValueError(
                f"Employee at index {index} has an invalid '{field}'; "
                "expected a finite, non-negative number."
            ) from error
        if not math.isfinite(numeric_value) or numeric_value < 0:
            raise ValueError(
                f"Employee at index {index} has an invalid '{field}'; "
                "expected a finite, non-negative number."
            )
        values[field] = numeric_value

    bonus = values["salary"] * values["bonus_percent"] / 100
    if not math.isfinite(bonus) or not math.isfinite(values["salary"] + bonus):
        raise ValueError(f"Employee at index {index} has compensation outside the supported range.")


def validate_employees(employees: Sequence[Employee]) -> None:
    """Reject malformed employee data before calculations or report output."""
    if not isinstance(employees, Sequence) or isinstance(employees, (str, bytes)):
        raise TypeError("Employees must be a sequence of employee dictionaries.")

    for index, employee in enumerate(employees):
        _validate_employee(employee, index)


def calculate_bonus(employee: Employee) -> float:
    """Return an employee's bonus amount based on base salary and bonus percent."""
    _validate_employee(employee, 0)
    salary = float(employee["salary"])
    bonus_percent = float(employee["bonus_percent"])
    return salary * bonus_percent / 100


def calculate_total_salary(employee: Employee) -> float:
    """Return an employee's base salary plus bonus."""
    _validate_employee(employee, 0)
    salary = float(employee["salary"])
    return salary + calculate_bonus(employee)


def calculate_summary(employees: Sequence[Employee]) -> SalarySummary:
    """Calculate headcount, average base salary, and highest total compensation."""
    validate_employees(employees)
    if not employees:
        return {
            "total_employees": 0,
            "average_salary": None,
            "highest_paid_employee": None,
        }

    salaries = [float(employee["salary"]) for employee in employees]
    try:
        average_salary = math.fsum(salaries) / len(salaries)
    except OverflowError as error:
        raise ValueError("The average salary is outside the supported numeric range.") from error
    if not math.isfinite(average_salary):
        raise ValueError("The average salary is outside the supported numeric range.")

    highest_paid = max(employees, key=calculate_total_salary)
    return {
        "total_employees": len(employees),
        "average_salary": average_salary,
        "highest_paid_employee": str(highest_paid["name"]),
    }


def format_report(employees: Sequence[Employee]) -> str:
    """Format the complete employee report and summary as a string."""
    validate_employees(employees)
    lines = ["Employee Salary Report"]
    for employee in employees:
        bonus = calculate_bonus(employee)
        total_salary = float(employee["salary"]) + bonus
        lines.append(
            f"ID: {employee['id']} | Name: {employee['name']} | "
            f"Base Salary: {float(employee['salary']):.2f} | "
            f"Bonus: {bonus:.2f} | Total Salary: {total_salary:.2f}"
        )

    summary = calculate_summary(employees)
    average_salary = (
        f"{summary['average_salary']:.2f}"
        if summary["average_salary"] is not None
        else "N/A"
    )
    highest_paid = summary["highest_paid_employee"] or "N/A"
    lines.extend(
        [
            "",
            "Summary",
            f"Total Employees: {summary['total_employees']}",
            f"Average Salary: {average_salary}",
            f"Highest Paid Employee: {highest_paid}",
        ]
    )
    return "\n".join(lines)


def print_report(employees: Sequence[Employee]) -> None:
    """Print the employee report after all records have been validated."""
    print(format_report(employees))


def main() -> None:
    """Run the salary report for the sample employees."""
    print_report(EMPLOYEES)


if __name__ == "__main__":
    main()
