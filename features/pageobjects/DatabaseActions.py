import json
import os

from Utilities import configReader
import mysql
from mysql.connector import Error


class DatabaseActions():

    def __init__(self):
        self.dbname = configReader.readConfig('DatabaseInfo', 'dbname')
        self.username = configReader.readConfig('DatabaseInfo', 'username')
        self.password = configReader.readConfig('DatabaseInfo', 'password')
        self.servername = configReader.readConfig('DatabaseInfo', 'servername')

    def connectTodataBase(self):
        connection = mysql.connector.connect(host=self.servername,
                                             database=self.dbname,
                                             user=self.username,
                                             password=self.password)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("You're connected to database: ")
        else:
            raise Exception("Could not connect to database")
        return connection

    def connectTomysql(self):
        connection = mysql.connector.connect(host=self.servername,

                                             user=self.username,
                                             password=self.password)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("You're connected to database: ")
        else:
            raise Exception("Could not connect to database")
        return connection


    def changeCompanyTohaveVoucher(self,name):
        connection = self.connectTodataBase()
        cursor = performDatabaseAction("""SELECT id FROM company WHERE name= %s""", connection, (name,), False)
        result=cursor.fetchone()
        companyId=result[0]
        action = """SELECT id FROM company_voucher_settings WHERE company_id= %s"""
        variables = (companyId,)
        cursor = performDatabaseAction(action, connection, variables, False)
        result = cursor.fetchone()
        companyId = result[0]


        action = """UPDATE company_voucher_settings SET is_voucher_settings_enabled = true WHERE id= %s"""
        variables = (companyId,)
        cursor = performDatabaseAction(action, connection, variables, True)

    def getThelastCollaboratorInviteLink(self,id):
        connection = self.connectTodataBase()
        cursor = performDatabaseAction("""SELECT id FROM company WHERE name= %s""", connection, (name,), False)
        result = cursor.fetchone()
        companyId = result[0]
        action = """SELECT id FROM company_voucher_settings WHERE company_id= %s"""
        variables = (companyId,)
        cursor = performDatabaseAction(action, connection, variables, False)
        result = cursor.fetchone()
        companyId = result[0]

        action = """UPDATE company_voucher_settings SET is_voucher_settings_enabled = true WHERE company_id= %s"""
        variables = (companyId,)
        cursor = performDatabaseAction(action, connection, variables, True)


    def getLatestInviteLink(self):
        connection = self.connectTodataBase()
        cursor = connection.cursor()
        result = cursor.execute("""SELECT token FROM `company_collaborator_token` ORDER BY `company_collaborator_token`.`modification_datetime` DESC LIMIT 1""")
        result = cursor.fetchone()
        token = result[0]
        return token

    def deletedatase(self,databaseName= None ):
        if databaseName is None:
            databaseName=self.dbname
        connection = self.connectTodataBase()
        variables=(databaseName,)
        cursor = performDatabaseAction("""DROP DATABASE IF EXISTS %s""", connection, variables, False)
        result = cursor.execute()

    def deletedatase(self,databaseName= None ):
        if databaseName is None:
            databaseName=self.dbname
        connection = self.connectTodataBase()
        variables=(databaseName,)
        cursor = performDatabaseAction("""DROP DATABASE IF EXISTS %s""", connection, variables, False)



    def createDatabase(self,databaseName= None ):
        if databaseName is None:
            databaseName=self.dbname
        connection = self.connectTodataBase()
        variables=(databaseName,)
        cursor = performDatabaseAction("""CREATE DATABASE %s""", connection, variables, False)
    def dumpMydatabase(self,databaseName= None ):
        if databaseName is None:
            databaseName=self.dbname
        connection = self.connectTodataBase()
        variables=(databaseName,)


    def createBackupDatabase(self):
        connection = self.connectTodataBase()
        cursor = connection.cursor()
        cursor.execute('SHOW TABLES;')
        table_names = []
        for record in cursor.fetchall():
            table_names.append(record[0])

        backup_dbname = self.dbname + '_backup'
        try:
            cursor.execute(f'CREATE DATABASE {backup_dbname}')
        except:
            pass

        cursor.execute(f'USE {backup_dbname}')

        for table_name in table_names:
            cursor.execute(
                f'CREATE TABLE {table_name} SELECT * FROM {self.dbname}.{table_name}')

    def createBackupDatabaseDump(self):
        os.system("mysqldump --host= {} -u {} -p {} {} >Databases/{}".format(self.servername, self.username,self.password,self.dbname,self.dbname+'_backup'))

    def deleteTheEmail(self, email):
        connection = self.connectTodataBase()


        action = """SELECT id FROM user_profile WHERE email= %s"""
        variables=(email,)
        cursor = performDatabaseAction(action, connection,variables,False)
        result = cursor.fetchone()
        if result is not None:
            userId = result[0]
            action = """SELECT id FROM user_account WHERE user_profile_id=  %s"""
            variables = (userId,)
            cursor = performDatabaseAction(action, connection,variables,False)
            result = cursor.fetchone()
            if result is not None:
                idAccount = result[0]

                action = """DELETE FROM user_account_token WHERE user_account_id =%s"""
                variables = (idAccount,)
                cursor = performDatabaseAction(action, connection,variables,True)

            action = """DELETE FROM user_account WHERE user_profile_id =%s"""
            variables = (userId,)
            cursor = performDatabaseAction(action, connection,variables,True)

            action = """DELETE FROM user_profile_role WHERE user_profile_id =%s"""
            variables = (userId,)
            cursor = performDatabaseAction(action, connection,variables,True)

            action = """DELETE FROM activity_log_collaborator_invite WHERE user_profile_id = %s"""
            variables = (userId,)
            cursor = performDatabaseAction(action, connection, variables, True)

            action = """DELETE FROM user_profile WHERE email = %s"""
            variables = (email,)
            cursor = performDatabaseAction(action, connection,variables,True)


def performDatabaseAction( action, conn,variables,commit):
    cursor = conn.cursor(prepared=True)
    try:
        result=cursor.execute(action,variables)
        if commit:
            conn.commit()
        else:
            if cursor.rowcount<0:
                print("Zero query results found")
    except:
        conn.rollback()
        raise Exception("Data base action failed")
    return cursor
