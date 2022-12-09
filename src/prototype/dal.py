import sqlite3


class BotDataBase:

    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def user_exists(self, email):
        result = self.cursor.execute("SELECT email FROM Users WHERE email = ?",
                                     (email,))
        return bool(len(result.fetchall()))

    def add_user(self, email, role_id, campus_id):
        self.cursor.execute
        ("INSERT INTO Users ('email', 'role_id', 'campus_id', 'user_tg_id')"
         " VALUES (?, ?, ?, ?)",
         (email, role_id, campus_id, 0))
        return self.conn.commit()

    def pop_user(self, email):
        self.cursor.execute("DELETE FROM Users WHERE email = ?", (email,))
        return self.conn.commit()

    def add_object(self, object):
        self.cursor.execute
        ("INSERT INTO Objects ('campus_id', 'type_id', 'name', 'note',"
         " 'floor', 'room_num') VALUES (?, ?, ?, ?, ?, ?)",
         (object.campus, object.type, object.name, object.note, object.floor,
          object.room_name,))
        return self.conn.commit()

    def object_exist(self, campus_id, type_id):
        result = self.cursor.execute
        ("SELECT * FROM Objects WHERE campus_id = ? AND type_id = ?",
            (campus_id, type_id))
        return bool(len(result.fetchall()))

    def pop_object(self, id):
        self.cursor.execute("DELETE FROM Objects WHERE id = ?", (id,))
        return self.conn.commit()

    def get_object_all(self, campus_id, type_id):
        result = self.cursor.execute(
            "SELECT * FROM Objects WHERE campus_id = ? AND type_id = ?",
            (campus_id, type_id))
        return result.fetchall()

    def book_object(self, user_id, object_id, dt_begin, dt_end):
        self.cursor.execute(
            "INSERT INTO Bookings ('user_id', 'object_id', 'dt_begin',"
            " 'dt_end', 'status_id') VALUES (?, ?, ?, ?, ?)",
            (user_id, object_id, dt_begin, dt_end, 0))
        return self.conn.commit()

    def get_user_booking(self, user_id):
        result = self.cursor.execute("SELECT * FROM Bookings WHERE user_id"
                                     " = ?", (user_id,))
        return result.fetchall()

    def cancel_booking(self, id):
        self.cursor.execute("DELETE FROM Bookings WHERE id = ?", (id,))
        return self.conn.commit()

    def close(self):
        self.connection.close()

    # return False if object free
    def get_status_object_begin(self, object_id):
        result_begin = self.cursor.execute("SELECT dt_begin FROM"
                                           " Bookings WHERE"
                                           " object_id = ?", (object_id,))
        return result_begin.fetchall()

    def get_status_object_end(self, object_id):  # return False if object free
        result_end = self.cursor.execute("SELECT dt_end FROM Bookings WHERE"
                                         " object_id = ?", (object_id,))
        return result_end.fetchall()

    def put_id_and_return_role(self, email, user_tg_id):
        self.cursor.execute("UPDATE Users SET user_tg_id = ? WHERE email ="
                            " ?", (user_tg_id, email))
        return self.conn.commit()

    def get_mail_return_role(self, email):
        result = self.cursor.execute("SELECT role_id FROM Users WHERE email"
                                     " = ?", (email,))
        role = result.fetchone()[0]
        return role

    def get_mail_return_user_id(self, email):
        result = self.cursor.execute("SELECT id FROM Users WHERE email = ?",
                                     (email,))
        user_id = result.fetchone()[0]
        return user_id

    def get_object_with_id(self, object_id):
        result = self.cursor.execute("SELECT * FROM Objects WHERE id = ?",
                                     (object_id,))
        return result.fetchall()

    def get_object_booking(self, object_id):
        result = self.cursor.execute("SELECT * FROM Bookings WHERE object_id "
                                     "= ?", (object_id, ))
        return result.fetchall()
