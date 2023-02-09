from pprint import pprint

from .project import Project
from .employee import EmployeeType, Employee
from ..augurdb import AugurDatabase
from ..employee_client import use_employees


def main():
    p1 = Project(name="Project 1", assets=10_000.0)
    p2: Project = Project(name="Project 2", assets=12_000.0)

    db = AugurDatabase()

    e1 = Employee(
        id=123,
        name="Joe Random",
        salary=1000.0,
        overtime=5,
        employee_type=EmployeeType.REGULAR,
        project=p1,
        database=db,
    )

    e2 = Employee(
        id=124,
        name="Jane Ransom",
        salary=1500.0,
        overtime=43,
        employee_type=EmployeeType.HOURED,
        project=p1,
        database=db,
    )

    e3 = Employee(
        id=125,
        name="Jill Chance",
        salary=2500.0,
        overtime=2,
        employee_type=EmployeeType.COMMISSIONED,
        project=p2,
        database=db,
    )

    employees = [e1, e2, e3]

    use_employees(employees, db)


if __name__ == "__main__":
    main()
