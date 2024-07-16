import pytest
import requests

"""
Welcome to the PyTest final assessment.
This assessment is our feeble attempt to determine if you learned anything 
over the past few weeks.

How this works is simple: Run the file, tests will fail.
It is your job to make all the tests pass.

Good luck!!!
"""

"""
Units 3 & 4 tests
Make these tests pass and follow any additional instructions as you go through the tests 
"""


def test_addition(secret_number):
    assert secret_number + 1 == 10


def test_subtraction(secret_number):
    assert secret_number - 7 == 2


def test_divide(secret_number):
    assert secret_number / 3 == 2


# create a marker to run only the multiply tests
def test_multiply(secret_number):
    assert secret_number * 3 == 27


def test_divide_decimals(secret_number):
    assert secret_number / 3.0 == 3.0


def test_multiply_decimals(secret_number):
    assert secret_number * 3.5 == 31.5


"""
Oh no!!! The addition test has become obsolete.
But it is still a nice test that we want to keep.
Mark the test so it will be executed, but not considered
part of failed or passed tests
"""

"""
The 2nd Divide Test is proving to be a very flaky tests
But I have confidence we can eventually figure out how to stabilize it.
For now, mark the test to be skipped upon execution.
"""

"""
Unit 5 - Database Testing
The next 2 test cases re-visit Unit 5-Database Testing.
"""


def test_create_new_consultant():
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='pytest_workshop')

    cursor = cnx.cursor()

    add_consultant = ("INSERT INTO consultant "
                      "(consultant_name, consultant_title, consultant_location, consultant_discipline) "
                      "VALUES (%s, %s, %s, %s)")

    data_consultant = ('Joe Cool Tester', 'Quality Assurance Engineer', 'USA', 'Test & Test Automation')

    cursor.execute(add_consultant, data_consultant)

    cnx.commit()

    cursor.close()
    cnx.close()


def test_read_new_consultant():
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='pytest_workshop')

    cursor = cnx.cursor()

    read_consultant_query = ("SELECT idconsultant, consultant_name, consultant_title, consultant_location, "
                             "consultant_discipline FROM consultant")

    cursor.execute(read_consultant_query)

    for (idconsultant, consultant_name, consultant_title, consultant_location, consultant_discipline) in cursor:
        print(f"{idconsultant} {consultant_name} - {consultant_title} is located in {consultant_location} "
              f"and is part of the {consultant_discipline} Discipline")

        if consultant_name == 'Matt Eakin':
            assert consultant_title == 'Quality Assurance Engineer'
            assert consultant_location == 'USA'
            assert consultant_discipline == 'Test & Test Automation Discipline'

    cursor.close()
    cnx.close()


"""
Unit 6-API Testing
Before you run this test, you must first start the API created for the Unit.
'workshop_api.py' should still be in your /api directory. Run it.

Once you have confirmed it is running, make the following test work.
"""


def test_post():
    url = "http://127.0.0.1:8000/studios/post"
    new_studio = {
        "studio_name": "My Awesome Studio"
    }
    response = requests.post(url, json=new_studio)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 300
    assert response.headers["Content-Type"] == "application/json"

    data = response.json()
    assert data["studio_name_created"] == "Another cool Studio"


"""
Run the entire file and capture the results in an XML formatted file
named 'test_assessment_results.xml
"""
