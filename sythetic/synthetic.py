from faker import Faker
import mysql.connector
fake = Faker()
# create a person


def createContact():
    person = {'firstName': fake.first_name(),
              'lastName': fake.last_name(),
              'email': fake.ascii_email()
              }
    return person


cnx = mysql.connector.connect(user='root',
                              password='tangoHTML9',
                              host='127.0.0.1',
                              database='Farm',
                              auth_plugin='mysql_native_password')


def writeToDb():
    # query with flattended data
    contact = createContact()
    query = f'INSERT INTO `Customers` VALUES ("{contact["firstName"]}", "{contact["lastName"]}", "{contact["email"]}")'
    # write to db
    cursor = cnx.cursor()
    cursor.execute(query)
    # commit data to db
    cnx.commit()
    cursor.close()


# write
for counter in range(100):
    writeToDb()
    print(counter)
