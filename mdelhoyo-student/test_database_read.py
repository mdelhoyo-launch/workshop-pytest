import mysql.connector

def test_case_read_user():
    cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='pytest_workshop')

    cursor = cnx.cursor()

    read_consultant_query = ("SELECT idconsultant, consultant_name, consultant_title, consultant_location, "
                             "consultant_discipline FROM consultant")
    
    cursor.execute(read_consultant_query)

    for (idconsultant, consultant_name, consultant_title, consultant_location, consultant_discipline) in cursor:
        print(f"{idconsultant} - {consultant_name} - {consultant_title} is located in {consultant_location} "
              f"and is part of the {consultant_discipline} Discipline")
        
        if consultant_name == 'Matias del Hoyo':
            assert consultant_title == 'Quality Assurance Engineer'
            assert consultant_location == 'ARG'
            assert consultant_discipline == 'Test & Test Automation'

    cursor.close()
    cnx.close()