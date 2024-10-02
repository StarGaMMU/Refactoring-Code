from dataclasses import dataclass
from typing import List

FIXED_VACATION_DAYS_PAYOUT = 5

@dataclass
class Employee:
    """Basic representation of an employee at the company."""
    name: str
    role: str
    vacation_days: int = 25

    def take_a_holiday(self, payout: bool) -> None:
        """Let the employee take a single holiday, or pay out 5 holidays."""
        if payout:
            self._payout_holiday()
        else:
            self._take_single_holiday()

    def _payout_holiday(self) -> None:
        """Payout holidays for the employee."""
        if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
            raise ValueError(
                f"Not enough holidays left for a payout. Remaining holidays: {self.vacation_days}."
            )
        self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
        print(f"Paying out a holiday. Holidays left: {self.vacation_days}")

    def _take_single_holiday(self) -> None:
        """Let the employee take a single holiday."""
        if self.vacation_days < 1:
            raise ValueError("No holidays left.")
        self.vacation_days -= 1
        print("Have fun on your holiday. Don't forget to check your emails!")


@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""
    hourly_rate: float = 50
    amount: int = 10

    def pay(self) -> None:
        print(
            f"Paying employee {self.name} a hourly rate of ${self.hourly_rate} for {self.amount} hours."
        )


@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""
    monthly_salary: float = 5000

    def pay(self) -> None:
        print(
            f"Paying employee {self.name} a monthly salary of ${self.monthly_salary}."
        )


class Company:
    """Represents a company with employees."""

    def __init__(self) -> None:
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the list of employees."""
        self.employees.append(employee)

    def find_employees_by_role(self, role: str) -> List[Employee]:
        """Find all employees with a particular role."""
        return [employee for employee in self.employees if employee.role.lower() == role.lower()]

    def pay_employee(self, employee: Employee) -> None:
        """Pay an employee."""
        employee.pay()


def main() -> None:
    """Main function."""
    company = Company()

    company.add_employee(SalariedEmployee(name="Louis", role="manager"))
    company.add_employee(HourlyEmployee(name="Brenda", role="president"))
    company.add_employee(HourlyEmployee(name="Tim", role="intern"))

    print(company.find_employees_by_role(role="Vice_President"))
    print(company.find_employees_by_role(role="Manager"))
    print(company.find_employees_by_role(role="Intern"))

    company.pay_employee(company.employees[0])
    company.employees[0].take_a_holiday(payout=False)


if __name__ == "__main__":
    main()
