# %%
from .employee import (
    CommissionedEmployment,
    AugurAdapter,
    Employee,
    HouredEmployment,
    RegularEmployment,
    SimpleReportPrinter,
)
from .project import Project
from ..augurdb import AugurDatabase
from ..employee_client import use_employees


def main():
    p2: Project = Project(name="Project 2", assets=12_000.0)

    db = AugurDatabase()

    default_report_printer = SimpleReportPrinter()
    default_employee_dao = AugurAdapter(db)

    e1 = Employee(
        id=123,
        name="Joe Random",
        employment=RegularEmployment(
            salary=1000.0,
            overtime=5,
        ),
        report_printer=default_report_printer,
        db=default_employee_dao,
    )

    e2 = Employee(
        id=124,
        name="Jane Ransom",
        employment=HouredEmployment(billable_hours=43),
        report_printer=default_report_printer,
        db=default_employee_dao,
    )

    e3 = Employee(
        id=125,
        name="Jill Chance",
        employment=CommissionedEmployment(project=p2),
        report_printer=default_report_printer,
        db=default_employee_dao,
    )

    employees = [e1, e2, e3]

    use_employees(employees, db)


if __name__ == "__main__":
    main()
