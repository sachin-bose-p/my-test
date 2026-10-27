"""Print a monthly salary report for the sample employees."""

from decimal import Decimal
import math
import sys


EMPLOYEES: list[dict[str, object]] = [
    {"id": 1, "name": "Alice Johnson", "salary": 5200.00, "bonus_percent": 10},
    {"id": 2, "name": "Brian Chen", "salary": 4750.00, "bonus_percent": 8},
    {"id": 3, "name": "Carla Diaz", "salary": 6100.00, "bonus_percent": 12},
]

REQUIRED_FIELDS = ("id", "name", "salary", "bonus_percent")


def _is_valid_amount(value: object) -> bool:
    """Return whether a value is a finite, non-negative number."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    if isinstance(value, float) and not math.isfinite(value):
        return False
    return value >= 0


def validate_employees(employees: list[dict[str, object]]) -> None:
    """Raise ValueError with a useful location when employee data is invalid."""
    if not isinstance(employees, list):
        raise ValueError("Employee records must be provided as a list.")

    for index, employee in enumerate(employees, start=1):
        if not isinstance(employee, dict):
            raise ValueError(f"Employee record {index} must be a dictionary.")

        for field in REQUIRED_FIELDS:
            if field not in employee:
                raise ValueError(f"Employee record {index} is missing required field '{field}'.")

        employee_id = employee["id"]
        if not (
            (isinstance(employee_id, int) and not isinstance(employee_id, bool))
            or (isinstance(employee_id, str) and employee_id.strip())
        ):
            raise ValueError(
                f"Employee record {index} has an invalid 'id'; use an integer or non-empty string."
            )

        name = employee["name"]
        if not isinstance(name, str) or not name.strip():
            raise ValueError(
                f"Employee record {index} has an invalid 'name'; it must not be empty."
            )

        for field in ("salary", "bonus_percent"):
            if not _is_valid_amount(employee[field]):
                raise ValueError(
                    f"Employee record {index} has an invalid '{field}'; "
                    "use a finite, non-negative number."
                )


def print_salary_report(employees: list[dict[str, object]]) -> None:
    """Validate and print each employee's ID, name, and monthly salary."""
    validate_employees(employees)

    print(f"{'Employee ID':<12} {'Name':<24} {'Monthly Salary':>16}")
    print("-" * 54)
    for employee in employees:
        salary = Decimal(str(employee["salary"]))
        print(f"{str(employee['id']):<12} {str(employee['name']):<24} {salary:>16,.2f}")


def main() -> int:
    """Run the report and return a nonzero status for invalid sample data."""
    try:
        print_salary_report(EMPLOYEES)
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
