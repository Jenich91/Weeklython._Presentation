from dataclasses import dataclass


@dataclass
class User:
    name: str = "Unknown"
    role: str = "sta"
    campus: str = "Unknown"
    mail: str = "Unknown"
    ID_user: str = "Unknown"

    def __init__(self):
        self.role = "sta"
        self.campus = "Unknown"
        self.login = "Unknown"
        self.ID_user = "Unknown"


@dataclass
class Booking:
    ID: int = -1
    ID_user: str = "Unknown"
    ID_object: int = -1
    name: str = "Unknown"
    ds_begin: int = 0
    ds_end: int = 0
    status: str = "Unknown"

    def __init__(self):
        self.ID = -1
        self.ID_user = "Unknown"
        self.ID_object = -1
        self.name = "Unknown"
        self.ds_begin = 0
        self.ds_end = 0
        self.status = "Unknown"


@dataclass
class Object:
    ID_object: int
    type: str
    name: str
    note: str
    image: str
    campus: str
    floor: int
    room_name: str

    def __init__(self):
        self.ID_object: int = -1
        self.type = "Unknown"
        self.name = "Unknown"
        self.note = "Unknown"
        self.image = "Unknown"
        self.campus = "Unknown"
        self.floor = 0
        self.room_name = "Unknown"


@dataclass
class Way:
    campus: int
    type: int
    status: int  # 0 - smotret; 1 - bron; -1 - un bron.

    def __init__(self):
        self.campus = 0
        self.type = 0
        self.status = 0
