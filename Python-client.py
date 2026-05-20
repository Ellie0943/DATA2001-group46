import psycopg2
import pandas as pd

class PythonClient:
    myHost = "localhost"
    myDB = "postgres"
    userid = "postgres"
    passwd = "1234"  # use your own password

    conn = None



    def connectToDatabase(self):
        try:
            self.conn = psycopg2.connect(database=self.myDB, user=self.userid, password=self.passwd, host=self.myHost)
            print("You are successfully connected to PostgreSQL server.")
            return True

        except psycopg2.Error as e:
            print(e)
            return False

    # **********Question 1***************
    def createTable(self):
        try:
            curs = self.conn.cursor()

            curs.execute("""
            DROP TABLE IF EXISTS ryde_poi;
        """)

            curs.execute("""
                CREATE TABLE IF NOT EXISTS ryde_poi
                (
                    sa4_name TEXT,
                    name TEXT,
                    x DOUBLE PRECISION,
                    y DOUBLE PRECISION
                )                       
            """)

            self.conn.commit()
            curs.close()

        except psycopg2.Error as e:
            print(e)
            return False
        

    def insertData(self):

     df = pd.read_csv('ryde_poi.csv')

     curs = self.conn.cursor()

     for index, row in df.iterrows():

        curs.execute(
            """
            INSERT INTO ryde_poi(sa4_name, name, x, y)
            VALUES(%s, %s, %s, %s)
            """,
            (row['sa4_name'], row['name'], row['x'], row['y'])
        )

     self.conn.commit()

     curs.close()

     print("Data inserted")

    def selectData(self):

     curs = self.conn.cursor()

     curs.execute(
        """
        SELECT * FROM ryde_poi
        LIMIT 10
        """
    )

     rows = curs.fetchall()

     for row in rows:
        print(row)

     curs.close()



client = PythonClient()

client.connectToDatabase()

client.createTable()

client.insertData()

client.selectData()



