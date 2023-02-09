from simple_pytest.my_data_type import MyDataType
import pytest


def test_compute_result():
    unit = MyDataType(2, 3)
    assert unit.compute_result() == 8


def test_compute_another_result():
    unit = MyDataType(2, 3)
    assert unit.compute_another_result() == 7


# With fixture:
@pytest.fixture()
def my_data_type():
    return MyDataType(2, 3)


def test_compute_result_with_fixture(my_data_type):
    assert my_data_type.compute_result() == 8


def test_compute_another_result_with_fixture(my_data_type):
    assert my_data_type.compute_another_result() == 7


def test_print_results(my_data_type, capsys):
    my_data_type.print_results()
    assert capsys.readouterr().out.strip() == "The results are: 8, 7."
