"""
https://www.youtube.com/watch?v=0mcP8ZpUR38&t=1s

Very advanced Employee management system.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

#______________________________________________________________________
# Base classes - adding onto Employee class

class Commission(ABC):
    """Represents a generic commission"""

    @abstractmethod
    def get_payment(self) -> float:
        """Computes the commission to be paid out"""

@dataclass
class ContractCommission(Commission):
    """Represents a commission"""

    commission: float = 100
    contracts_landed: float = 0

    def get_payment(self) -> float:
        return self.commission * self.contracts_landed

class Contract(ABC):
    """Represents a contract anda payment process for a particular employeee."""

    @abstractmethod
    def get_payment(self) -> float:
        """Compute how much to pay an employee under this contract."""

# class where everything is combined into
@dataclass
class Employee:
    """Basic representation of an employee at the company."""

    name: str
    id: int
    contract: Contract
    commission: Optional[Commission] = None

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        payout = self.contract.get_payment()
        if self.commission is not None:
            payout += self.commission.get_payment()
        return payout

#______________________________________________________________________


@dataclass
class HourlyContract(Contract):
    """Contract type for an employee being paid on an hourly basis."""

    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def get_payment(self) -> float:
        return (
            self.pay_rate * self.hours_worked 
            + self.employer_cost         
        )

@dataclass
class SalariedContract(Contract):
    """Contract type for an employee being paid a monthly salary."""

    monthly_salary: float = 0
    percentage: float = 1

    def get_payment(self) -> float:
        return self.monthly_salary * self.percentage

@dataclass
class FreelancerContract(Contract):
    """Contract type for a freelancer (paid on an hourly basis)."""

    pay_rate: float = 0
    hours_worked: int = 0
    vat_number: str = ""

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked


def main() -> None:
    """Main function."""
    #___________________________________________________
    # Henry

    henry_contract = HourlyContract(pay_rate=50, hours_worked=100)
    henry = Employee(name="Henry", id=12346, contract=henry_contract)

    print(
        f"{henry.name} worked for {henry_contract.hours_worked} hours "
        f"and earned ${henry.compute_pay()}"
    )

    #___________________________________________________
    # Sarah

    sarah_contract = SalariedContract(monthly_salary=5000)
    sarah_commission = ContractCommission(contracts_landed=10)
    sarah = Employee(name="Sarah", id=47832, contract=sarah_contract, commission=sarah_commission)

    print(
        f"{sarah.name} landed {sarah_commission.contracts_landed} contracts and earned ${sarah.compute_pay()}"
    )

if __name__ == "__main__":
    main()