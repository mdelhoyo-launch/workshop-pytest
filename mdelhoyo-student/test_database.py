import mysql.connector

def test_case_create_new_user():
    cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='pytest_workshop')

    cursor = cnx.cursor()

    add_consultant = ("INSERT INTO consultant " 
                      "(consultant_name, consultant_title, consultant_location, consultant_discipline) "
                      "VALUES (%s, %s, %s, %s)")
    
    data_consultant = ('Matias del Hoyo', 'Quality Assurance Engineer', 'ARG', 'Test & Test Automation')

    cursor.execute(add_consultant, data_consultant)

    cnx.commit()

    cursor.close()
    cnx.close()