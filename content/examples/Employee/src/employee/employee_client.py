from pprint import pprint


def use_employees(employees, db):
    for e in employees:
        print("=" * 35)
        print(f"{e.name} has a salary of {e.calculate_pay():.2f}")
        e.print_report()
        e.save_employee()
    print("=" * 35)

    pprint(db.records)
