import mysql.connector as dbc
import sqlite3
import psycopg2
import os # Se usará para borrar la base de datos por defecto cuando se seleccione
# una base de datos en caso de usar sqlite3.

class DBAccess:
    # Los motores de base de datos serán:
    #       1 - MySQL
    #       2 - PostgreSQL
    #       3 - SQLite
    def __init__(self, engine = "1", port = "3306", host = "localhost", user = "root", password = ""):
        # Se accede al motor de base de datos con los datos por defecto
        self.host = host
        self.user = user
        self.password = password
        self.engine = engine
        self.port = port
        self.connection = None  # Inicializar la conexión como None en el constructor
    
    def create_connection(self):
        # Para crear una conexión en base a los datos con los que se ha accedido
        if self.engine == "1": # El motor elegido es MySQL
            self.connection = dbc.connect(
            host = self.host, 
            user = self.user, 
            password = self.password,
            port = self.port
        )
        elif self.engine == "2": # El motor elegido es PostgreSQL
            self.connection = psycopg2.connect(
            host = self.host, 
            user = self.user, 
            password = self.password,
            port = self.port
        )
        elif self.engine == "3": # El motor elegido es sqlite
            self.connection = sqlite3.connect('db.db') # Para crear una conexión a sqlite3 se pone una base de datos fictica, que luego se cambiará.
    
    # Para crear el cursor se usa este método, válido para los tres motores de base de datos.
    def create_cursor(self):
        # Para crear un cursor en base a la conexion
        if not self.connection:
            self.create_connection()
        self.cursor = self.connection.cursor()
           
    def close(self):
        # Para destruir un cursor cuando ya no es necesario
        if self.engine == "1" or self.engine == "2": # MySQL o PostgreSQL
            try:
                self.cursor.close()
                self.connection.close()
                del self.cursor
                del self.connection
                return True
            except Exception as e:
                return (False, e)
        # Si el motor elegido es sqlite3 no es necesario destruir el cursor.
            
    def show_databases(self):
        # Devuelve una lista con las bases de datos que hay en la instalación.
        if self.engine == "1": # MySQL
            self.cursor.execute("show databases;")
        elif self.engine == "2": # PostgreSQL
            self.cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
        elif self.engine == "3": # SQLite
            self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        databases = [database[0] for database in self.cursor.fetchall()]
        return databases
         
    def select_database(self, database):
        # Selecciona una base de datos o la crea si no existe.
        if self.engine == "1": # MySQL
            self.database = database
            self.cursor.execute(f"create database if not exists {self.database}")
            self.cursor.execute(f"use {self.database}")
        elif self.engine == "2": # PostgreSQL
            self.database = database
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            self.cursor.execute(f"CONNECT TO {self.database}")
        elif self.engine == "3": # SQLite
            self.database = database
            self.cursor.execute(f"ATTACH DATABASE '{self.database}.db' AS {self.database}")
            if database != "db.db": # Si la base de datos seleccionada no es la que se creó por defecto, hay que eliminar esta última.
                try:
                    os.remove("db.db")
                    eliminacion = "El archivo db.db ha sido eliminado correctamente."
                except FileNotFoundError:
                    eliminacion = "El archivo db.db no existe."
                except PermissionError:
                    eliminacion = "No tienes permisos para eliminar el archivo db.db."
                except Exception as e:
                    eliminacion = f"Se produjo un error al eliminar el archivo: {e}"
                return eliminacion                 
        self.connection.commit()
        return None

    def show_user_grants(self):
        # Devuelve los permisos del usuario actual.
        if self.engine == "1": # MySQL
            self.cursor.execute("SHOW GRANTS")
        elif self.engine == "2": # PostgreSQL
            self.cursor.execute("SELECT array_to_string(ARRAY(SELECT pg_catalog.pg_get_userbyid(d.objoid) || '=' || d.objsubid || ' ' || a.typname || case when d.objsubid > 0 then '[' || d.objsubid || ']' else '' end || ' (' || pg_catalog.array_to_string(d.acl, ', ') || ')' FROM pg_catalog.pg_database AS d CROSS JOIN pg_catalog.pg_type AS a WHERE d.datdba = a.oid AND d.datname = current_database()), E'\n')")
        elif self.engine == "3": # SQLite
            self.cursor.execute("PRAGMA table_info(sqlite_master)")
        grants = [grant[1] for grant in self.cursor.fetchall()]
        return grants

    def get_tables(self):
        # Devuelve la lista de tablas de la base de daatos que esté seleccionada.
        if self.engine == "1": # MySQL
            query = f"show full tables from {self.database}"
        elif self.engine == "2": # PostgreSQL
            query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
        elif self.engine == "3": # SQLite
            query = "SELECT name FROM sqlite_master WHERE type='table'"
        self.cursor.execute(query)
        tables = [table[0] for table in self.cursor.fetchall()]
        return tables
    
    def get_columns(self, tabla):
        # Devuelve la lista de columnas de una tabla
        if self.engine == "1": # MySQL
            query = f"SHOW COLUMNS FROM {tabla}"
        elif self.engine == "2": # PostgreSQL
            query = f"SELECT column_name, data_type, character_maximum_length\
                FROM information_schema.columns WHERE table_name = {tabla};"
        elif self.engine == "3": # SQLite
            query = f"PRAGMA table_info({tabla});"
        self.cursor.execute(query)
        columnas = [column[0] for column in self.cursor.fetchall()]
        return columnas

    def get_data(self, query, params=None):
        # Ejecuta una consulta de recuperación de datos y devuelve el resultado de esa consulta.
        # Los params son para ejecutar consultas preparadas. Se pasan en una lista.
        # Este método funciona para MySQL, PostgreSQL y SQLite.
        # La diferencia está en la sintaxis de la consulta que se le pase.
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            data = [rec for rec in self.cursor.fetchall()]
        except Exception as e:
            data = False
        return data
    
    def set_data(self, query, params=None):
        # Ejecuta una consulta de no recuperación de datos (creación, edición o borrado)
        # Los params son para ejecutar consultas preparadas. Se pasan en una lista.
        # Este método funciona para MySQL, PostgreSQL y SQLite.
        # La diferencia está en la sintaxis de la consulta que se le pase.
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            result = [True]
        except Exception as e:
            self.connection.rollback()
            result = [False, e]
        return result