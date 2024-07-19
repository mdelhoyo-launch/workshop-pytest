import mysql.connector

def test_case_update_user():
    cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='pytest_workshop')

    cursor = cnx.cursor()

    update_consultant_query = ("UPDATE consultant "
                               "SET consultant_title='Software Development Engineer In Test'"
                                "WHERE consultant_name='Matias del Hoyo'")
    
    cursor.execute(update_consultant_query)

    cnx.commit()

    cursor.close()
    cnx.close()