from mailbox import NoSuchMailboxError
from utils.db import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(45))
    apellido = db.Column(db.String(45))
    username = db.Column(db.String(45))
    password = db.Column(db.String(45))
    

    def __init__(self, nombre, apellido, username, password):
        self.nombre
        self.apellido
        self.username
        self.password