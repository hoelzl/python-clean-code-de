# %% {{ employee_srp_tags }}
from dataclasses import dataclass
from augurdb import AugurDatabase
from project import Project
from abc import ABC, abstractmethod

# %% {{ employee_srp_tags }}
@dataclass
class Employment(ABC):
    @abstractmethod
    def calculate_pay(self) -> float:
        ...

    @abstractmethod
    def report_hours(self) -> int:
        ...


# %% {{ employee_srp_tags }}
@dataclass
class RegularEmployment(Employment):
    salary: float
    overtime: int

    def calculate_pay(self) -> float:
        return self.salary + 60.0 * self.overtime

    def report_hours(self) -> int:
        return 40 + self.overtime


# %% {{ employee_srp_tags }}
@dataclass
class CommissionedEmployment(Employment):
    project: "Project"

    def calculate_pay(self) -> float:
        return self.project.assets * 0.1

    def report_hours(self) -> int:
        return 40


# %% {{ employee_srp_tags }}
@dataclass()
class HouredEmployment(Employment):
    billable_hours: int

    def calculate_pay(self) -> float:
        return 50.0 * self.billable_hours

    def report_hours(self) -> int:
        return self.billable_hours


# %% {{ employee_srp_tags }}
class ReportPrinter:
    def print_report(self, employee: "EmployeeSrp") -> None:
        print(f"{employee.name} worked {employee.report_hours()} hours.")


# %% {{ employee_srp_tags }}
@dataclass
class EmployeeDao:
    database: AugurDatabase

    def save_employee(self, employee: "EmployeeSrp") -> None:
        self.database.start_transaction()
        self.database.store_field(employee.id, "name", employee.name)
        self.database.store_field(employee.id, "employment", employee.employment)
        self.database.commit_transaction()


# %% {{ employee_srp_tags }}
@dataclass
class EmployeeSrp:
    id: int
    name: str
    employment: Employment
    report_printer: ReportPrinter
    dao: EmployeeDao

    def calculate_pay(self):
        return self.employment.calculate_pay()

    def report_hours(self):
        return self.employment.report_hours()

    def print_report(self):
        return self.report_printer.print_report(self)

    def save_employee(self):
        return self.dao.save_employee(self)
