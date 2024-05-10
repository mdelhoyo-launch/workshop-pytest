import mysql.connector


def test_create_new_consultant():
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='pytest_workshop')

    cursor = cnx.cursor()

    add_consultant = ("INSERT INTO consultant "
                      "(consultant_name, consultant_title, consultant_location, consultant_discipline) "
                      "VALUES (%s, %s, %s, %s)")

    data_consultant = ('Matt Eakin', 'Quality Assurance Engineer', 'USA', 'Test & Test Automation')

    # Insert new consultant
    cursor.execute(add_consultant, data_consultant)

    # Make sure data is committed to the database
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

    # Execute and Print consultant information
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


def test_update_consultant():
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='pytest_workshop')

    cursor = cnx.cursor()

    update_consultant_query = ("UPDATE consultant "
                               "SET consultant_title='Software Development Engineer in Test'"
                               "WHERE consultant_name = 'Matt Eakin'")

    # Execute and Print consultant information
    cursor.execute(update_consultant_query)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()


def test_delete_consultant():
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='pytest_workshop')

    cursor = cnx.cursor()

    delete_consultant_query = ("DELETE FROM consultant "
                               "WHERE consultant_name = 'Matt Eakin'")

    # Execute and Print consultant information
    cursor.execute(delete_consultant_query)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()
