from datetime import datetime
from entities.user import User
from enums.log_type import LogType
from persistence.db import get_connection
import pymysql

class Log:
    def __init__(self, id: int, date: datetime, user: User, description: str, type: LogType):
        self.id = id
        self.date = date
        self.user = user
        self.description = description
        self.type = type

    @staticmethod
    def saveLog(user: User, description: str, type: LogType):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            sql = "INSERT INTO log (id_user, date, description, type) VALUES (%s, NOW(), %s, %s)"
            cursor.execute(sql, (user.id, description, type.value, datetime.now()))
            
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as ex:
            print("Error al guardar el log:", ex)
            return False    