from fastapi import FastAPI
import mysql.connector
from pydantic import BaseModel

app = FastAPI()


class Consultant(BaseModel):
    consultant_name: str
    consultant_title: str | None = None
    consultant_location: str | None = None
    consultant_discipline: str


class Discipline(BaseModel):
    discipline_name: str
    studio_name: str


class Studio(BaseModel):
    studio_name: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/consultants")
def read_consultants():
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='pytest_workshop')

    cursor = cnx.cursor()

    return_set = []
    read_consultant_query = ("SELECT idconsultant, consultant_name, consultant_title, consultant_location,"
                             " consultant_discipline FROM pytest_workshop.consultants")

    # Execute and Print consultant information
    cursor.execute(read_consultant_query)

    for (idconsultant, consultant_name, consultant_title, consultant_location, consultant_discipline) in cursor:
        print(f"{idconsultant} {consultant_name} - {consultant_title} is located in {consultant_location} "
              f"and is part of the {consultant_discipline} Discipline")

        return_set.append({"idconsultant": idconsultant,
                           "consultant_name": consultant_name,
                           "consultant_title": consultant_title,
                           "consultant_location": consultant_location,
                           "consultant_discipline": consultant_discipline})

    results = {"consultants": return_set}
    return results


@app.get("/disciplines")
def read_disciplines():
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='pytest_workshop')

    cursor = cnx.cursor()

    return_set = []
    read_consultant_query = "SELECT iddisciplines, discipline_name, studio_name FROM pytest_workshop.disciplines"

    # Execute and Print consultant information
    cursor.execute(read_consultant_query)

    for (iddisciplines, discipline_name, studio_name) in cursor:
        print(f"{iddisciplines} {discipline_name} is in the {studio_name} studio")

        return_set.append({"iddisciplines": iddisciplines,
                           "discipline_name": discipline_name,
                           "studio_name": studio_name})

    results = {"disciplines": return_set}
    return results


@app.get("/studios")
def read_studios():
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='pytest_workshop')

    cursor = cnx.cursor()

    return_set = []
    read_consultant_query = "SELECT idstudios, studio_name FROM pytest_workshop.studios"

    # Execute and Print consultant information
    cursor.execute(read_consultant_query)

    for (idstudios, studio_name) in cursor:
        print(f"{idstudios} {studio_name}")

        return_set.append({"idstudios": idstudios,
                           "studio_name": studio_name})

    results = {"studios": return_set}
    return results


@app.post("/consultants/post")
def create_consultants(consultant: Consultant):
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='pytest_workshop')

    cursor = cnx.cursor()

    add_consultant = ("INSERT INTO consultants "
                      "(consultant_name, consultant_title, consultant_location, consultant_discipline) "
                      "VALUES (%s, %s, %s, %s)")

    data_consultant = (consultant.consultant_name, consultant.consultant_title,
                       consultant.consultant_location, consultant.consultant_discipline)

    # Insert new consultant
    cursor.execute(add_consultant, data_consultant)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()

    return {"consultant_name_return": consultant.consultant_name,
            "consultant_title_return": consultant.consultant_title,
            "consultant_location_return": consultant.consultant_location,
            "consultant_discipline_return": consultant.consultant_discipline}


@app.post("/disciplines/post")
async def create_disciplines(discipline: Discipline):
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='pytest_workshop')

    cursor = cnx.cursor()

    add_discipline = ("INSERT INTO disciplines "
                      "(discipline_name, studio_name) "
                      "VALUES (%s, %s)")

    data_discipline = (discipline.discipline_name, discipline.studio_name)

    # Insert new consultant
    cursor.execute(add_discipline, data_discipline)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()

    return {"discipline_name_returned": discipline.discipline_name,
            "studio_name_returned": discipline.studio_name}


@app.post("/studios/post")
async def create_studios(studio: Studio):
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='pytest_workshop')

    cursor = cnx.cursor()

    add_studio = f"INSERT INTO studios (studio_name) VALUES ('{studio.studio_name}')"
    print(add_studio)

    # Insert new consultant
    cursor.execute(add_studio)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()

    return {"studio_name_created": studio.studio_name}


@app.put("/disciplines/put")
async def update_disciplines(discipline: Discipline):
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='pytest_workshop')

    cursor = cnx.cursor()

    update_discipline = ("UPDATE disciplines SET "
                         "studio_name = %s "
                         "WHERE discipline_name = %s")

    data_discipline = (discipline.studio_name, discipline.discipline_name)

    # Insert new consultant
    cursor.execute(update_discipline, data_discipline)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()

    return {"discipline_name_updated": discipline.discipline_name,
            "studio_name_updated": discipline.studio_name}


@app.delete("/studios/delete")
async def update_studios(studio: Studio):
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='pytest_workshop')

    cursor = cnx.cursor()

    delete_studio = f"DELETE FROM studios WHERE studio_name = '{studio.studio_name}'"

    # Insert new consultant
    cursor.execute(delete_studio)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()

    return {"studio_name_removed": studio.studio_name}
