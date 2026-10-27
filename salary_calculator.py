"""Validate employee records and calculate salary bonuses and totals."""

from collections.abc import Iterable, Mapping
from math import isfinite
from typing import TypedDict


class Employee(TypedDict):
    id: int
    name: str
    salary: int | float
    bonus_percent: int | float


class EmployeeResult(Employee):
    bonus: int | float
    total_salary: int | float


EMPLOYEES: list[Employee] = [
    {"id": 1, "name": "Alice", "salary": 50000, "bonus_percent": 10},
    {"id": 2, "name": "Bob", "salary": 60000, "bonus_percent": 15},
    {"id": 3, "name": "Charlie", "salary": 45000, "bonus_percent": 5},
]

_REQUIRED_FIELDS = ("id", "name", "salary", "bonus_percent")


def _validate_nonnegative_number(value: object, field: str) -> int | float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a number")
    if value < 0:
        raise ValueError(f"{field} must not be negative")
    if isinstance(value, float) and not isfinite(value):
        raise ValueError(f"{field} must be finite")
    return value


def validate_employee(employee: object) -> Employee:
    """Validate a record and return its fields in a typed dictionary."""
    if not isinstance(employee, Mapping):
        raise ValueError("record must be a dictionary")

    missing_fields = [field for field in _REQUIRED_FIELDS if field not in employee]
    if missing_fields:
        raise ValueError(f"missing required field(s): {', '.join(missing_fields)}")

    employee_id = employee["id"]
    if isinstance(employee_id, bool) or not isinstance(employee_id, int):
        raise ValueError("id must be an integer")
    if employee_id < 1:
        raise ValueError("id must be positive")

    name = employee["name"]
    if not isinstance(name, str) or not name.strip():
        raise ValueError("name must be a non-empty string")

    salary = _validate_nonnegative_number(employee["salary"], "salary")
    bonus_percent = _validate_nonnegative_number(
        employee["bonus_percent"], "bonus_percent"
    )
    return {
        "id": employee_id,
        "name": name,
        "salary": salary,
        "bonus_percent": bonus_percent,
    }


def calculate_bonus(salary: int | float, bonus_percent: int | float) -> int | float:
    """Return the bonus amount for a salary and bonus percentage."""
    salary = _validate_nonnegative_number(salary, "salary")
    bonus_percent = _validate_nonnegative_number(bonus_percent, "bonus_percent")
    try:
        bonus = salary * bonus_percent / 100
    except OverflowError as error:
        raise ValueError("bonus calculation exceeds the supported numeric range") from error
    if isinstance(bonus, float) and not isfinite(bonus):
        raise ValueError("bonus calculation exceeds the supported numeric range")
    return bonus


def calculate_total_salary(salary: int | float, bonus_percent: int | float) -> int | float:
    """Return salary plus the calculated bonus."""
    salary = _validate_nonnegative_number(salary, "salary")
    total_salary = salary + calculate_bonus(salary, bonus_percent)
    if isinstance(total_salary, float) and not isfinite(total_salary):
        raise ValueError("total salary exceeds the supported numeric range")
    return total_salary


def process_employees(
    employees: Iterable[object],
) -> tuple[list[EmployeeResult], list[str]]:
    """Return calculated results and explicit errors for invalid records."""
    results: list[EmployeeResult] = []
    errors: list[str] = []

    for index, employee in enumerate(employees, start=1):
        try:
            validated_employee = validate_employee(employee)
            bonus = calculate_bonus(
                validated_employee["salary"], validated_employee["bonus_percent"]
            )
            try:
                total_salary = validated_employee["salary"] + bonus
            except OverflowError as error:
                raise ValueError(
                    "total salary exceeds the supported numeric range"
                ) from error
            if isinstance(total_salary, float) and not isfinite(total_salary):
                raise ValueError("total salary exceeds the supported numeric range")
            results.append(
                {
                    **validated_employee,
                    "bonus": bonus,
                    "total_salary": total_salary,
                }
            )
        except ValueError as error:
            record_id = (
                employee.get("id", "unknown")
                if isinstance(employee, Mapping)
                else "unknown"
            )
            errors.append(f"Record {index} (id: {record_id}): {error}")

    return results, errors


def main() -> None:
    results, errors = process_employees(EMPLOYEES)
    for result in results:
        print(
            f"{result['name']}: bonus={result['bonus']}, "
            f"total_salary={result['total_salary']}"
        )
    for error in errors:
        print(f"Invalid employee: {error}")


if __name__ == "__main__":
    main()
