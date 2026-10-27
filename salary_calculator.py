"""Print a validated salary and bonus report for the sample employees."""

from collections.abc import Mapping, Sequence
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


EMPLOYEES: list[dict[str, object]] = [
    {"id": 1, "name": "Alice", "salary": 60000, "bonus_percent": 10},
    {"id": 2, "name": "Bob", "salary": 50000, "bonus_percent": 5},
    {"id": 3, "name": "Charlie", "salary": 45000, "bonus_percent": 8},
]

CENT = Decimal("0.01")
REQUIRED_FIELDS = {"id", "name", "salary", "bonus_percent"}


def validate_employee(employee: Mapping[str, object]) -> None:
    """Raise ValueError when an employee record is incomplete or invalid."""
    if not isinstance(employee, Mapping):
        raise ValueError("Employee record must be a mapping.")

    missing_fields = REQUIRED_FIELDS - employee.keys()
    if missing_fields:
        missing = ", ".join(sorted(missing_fields))
        raise ValueError(f"Employee record is missing required field(s): {missing}.")

    employee_id = employee["id"]
    if isinstance(employee_id, bool) or not isinstance(employee_id, int):
        raise ValueError("Employee id must be an integer.")

    name = employee["name"]
    if not isinstance(name, str) or not name.strip():
        raise ValueError(f"Employee {employee_id} must have a non-empty name.")

    for field in ("salary", "bonus_percent"):
        value = employee[field]
        if isinstance(value, bool) or not isinstance(value, (int, float, Decimal)):
            raise ValueError(f"Employee {employee_id} {field} must be a number.")
        try:
            amount = Decimal(str(value))
        except InvalidOperation as error:
            raise ValueError(f"Employee {employee_id} {field} must be a valid number.") from error
        if not amount.is_finite() or amount < 0:
            raise ValueError(f"Employee {employee_id} {field} must be finite and non-negative.")


def calculate_bonus(employee: Mapping[str, object]) -> Decimal:
    """Calculate an employee's bonus from base salary and bonus percentage."""
    validate_employee(employee)
    salary = Decimal(str(employee["salary"]))
    bonus_percent = Decimal(str(employee["bonus_percent"]))
    return (salary * bonus_percent / Decimal("100")).quantize(CENT, rounding=ROUND_HALF_UP)


def calculate_total_salary(employee: Mapping[str, object]) -> Decimal:
    """Calculate base salary plus bonus for an employee."""
    validate_employee(employee)
    return Decimal(str(employee["salary"])) + calculate_bonus(employee)


def format_money(amount: Decimal) -> str:
    """Format a monetary amount with two decimal places and thousands separators."""
    return f"${amount:,.2f}"


def generate_report(employees: Sequence[Mapping[str, object]]) -> str:
    """Validate all employees and return their salary report and summary."""
    if not employees:
        raise ValueError("At least one employee is required to generate a report.")

    for employee in employees:
        validate_employee(employee)

    report_lines = [
        "Employee Salary Report",
        "ID | Name | Base Salary | Bonus Amount | Total Salary",
        "-" * 67,
    ]
    for employee in employees:
        salary = Decimal(str(employee["salary"]))
        bonus = calculate_bonus(employee)
        total = calculate_total_salary(employee)
        report_lines.append(
            f"{employee['id']} | {employee['name']} | {format_money(salary)} | "
            f"{format_money(bonus)} | {format_money(total)}"
        )

    total_base_salary = sum(
        (Decimal(str(employee["salary"])) for employee in employees),
        start=Decimal("0"),
    )
    average_salary = (total_base_salary / len(employees)).quantize(
        CENT, rounding=ROUND_HALF_UP
    )
    highest_paid = max(employees, key=calculate_total_salary)

    report_lines.extend(
        [
            "",
            f"Total employees: {len(employees)}",
            f"Average base monthly salary: {format_money(average_salary)}",
            (
                "Highest-paid employee: "
                f"{highest_paid['name']} ({format_money(calculate_total_salary(highest_paid))})"
            ),
        ]
    )
    return "\n".join(report_lines)


def verify_sample_report(report: str) -> None:
    """Check that the bundled sample data produces the acceptance-criteria summary."""
    required_output = (
        "Total employees: 3",
        "Average base monthly salary: $51,666.67",
        "Highest-paid employee: Alice",
    )
    missing = [line for line in required_output if line not in report]
    if missing:
        raise AssertionError(f"Sample report verification failed: {', '.join(missing)}")


def main() -> None:
    report = generate_report(EMPLOYEES)
    verify_sample_report(report)
    print(report)


if __name__ == "__main__":
    main()
