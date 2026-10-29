from employee import employee_details

def test_employee_details():
    result = employee_details("John", "EMP275", "Engineering", "75000")

    expected = "Name:John\nEmployee ID:EMP275\nDepartment:Engineering\nSalary:75000"

    assert result == expected