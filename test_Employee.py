from Employee import Employee_details
def test_Employee_details():
    result = Employee_details("Rahul","EMP101","IT","50000")
    expected="Name: Rahul\nEmployee ID : EMP101\nDepartment: IT\nSalary:50000"
    assert result == expected