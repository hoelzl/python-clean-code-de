# %% {{ employee_ocp_tags }}
from project import Project
from employee_ocp import (
    CommissionedEmployment,
    AugurDbAdapter,
    EmployeeOcp,
    HouredEmployment,
    RegularEmployment,
    SimpleReportPrinter,
)
from augurdb import AugurDatabase
from pprint import pprint


# %% {{ employee_ocp_tags }}
p1 = Project(name="Project 1", assets=10_000.0)
p2: Project = Project(name="Project 2", assets=12_000.0)

# %% {{ employee_ocp_tags }}
db = AugurDatabase()

# %% {{ employee_ocp_tags }}
default_report_printer = SimpleReportPrinter()
default_employee_dao = AugurDbAdapter(db)

# %% {{ employee_ocp_tags }}
e1 = EmployeeOcp(
    id=123,
    name="Joe Random",
    employment=RegularEmployment(
        salary=1000.0,
        overtime=5,
    ),
    report_printer=default_report_printer,
    dao=default_employee_dao,
)

# %% {{ employee_ocp_tags }}
e2 = EmployeeOcp(
    id=124,
    name="Jane Ransom",
    employment=HouredEmployment(billable_hours=43),
    report_printer=default_report_printer,
    dao=default_employee_dao,
)

# %% {{ employee_ocp_tags }}
e3 = EmployeeOcp(
    id=125,
    name="Jill Chance",
    employment=CommissionedEmployment(project=p2),
    report_printer=default_report_printer,
    dao=default_employee_dao,
)

# %% {{ employee_ocp_tags }}
employees = [e1, e2, e3]

# %% {{ employee_ocp_tags }}
for e in employees:
    print("=" * 35)
    print(f"{e.name} has a salary of {e.calculate_pay():.2f}")
    e.print_report()
    e.save_employee()
print("=" * 35)

# %% {{ employee_ocp_tags }}
pprint(db.records)
