# file = open("death_causes.csv", "r")

# index = 0
# for line in file:
#     index += 1
#     print(line.split(","))
    
#     if index == 3:
#         break
        

# # Year,Cause Name,Cause Name,State,Deaths,Age-adjusted Death Rate

# file = open("death_causes.csv", "r")
# deaths = 0
# count = 0
# for line in file:
#     if count == 0:
#         pass
#     else:
#         raw = line.split(",")
#         print(raw)
#         if raw[0] == "2014":
#             deaths += int(raw[4])
#     count += 1

 
# print(deaths/365)

# Year,Cause Name,Cause Name,State,Deaths,Age-adjusted Death Rate


# with open("twist.txt", "r") as file:
#     for line in file:
#         print(line)
# file.close()

import pymysql.cursors

class mortality:
    def __init__(self, year, cause_name_full, cause_name, state, deaths, age_adjusted_death_rate):
        self.year = year
        self.cause_name_full = cause_full_name
        self.cause_name = cause_name  






# Connect to the database
connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='db',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

def create_database():
    try:
        with connection.cursor() as cursor:
            # Create a new record

            sql = """CREATE TABLE films 
                    (id int NOT NULL KEY AUTO_INCREMENT,
                    year INT(4), 
                    cause_name_full VARCHAR(500), 
                    cause_name VARCHAR(500), 
                    state VARCHAR(50), 
                    deaths INT(10), 
                    Age_adjusted_death_rate INT(50)"""

            cursor.execute(sql)
            connection.commit()
    except:
        # connection is not autocommit by default. So you must commit to save
        # your changes.

        print('Table Exists')


def open_file():

    file = open("death_causes.csv", "r")

    deaths = 0
    count = 0

    for line in file:
        if count == 0:
            pass
        else:
            raw = line.split(",")

def post_to_db():

    with connection.cursor() as cursor:
        # Create a new record
        sql = f"""insert into mortality_rate (year, cause_name_full, cause_name, state, deaths, age_adjusted_death_rate)
value