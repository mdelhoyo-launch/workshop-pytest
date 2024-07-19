import mysql.connector

def test_case_delete_user():
    cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='pytest_workshop')

    cursor = cnx.cursor()

    delete_consultant_query = ("DELETE FROM consultant "
                                "WHERE consultant_name='Matias del Hoyo'")
    
    cursor.execute(delete_consultant_query)

    cnx.commit()

    cursor.close()
    cnx.close()