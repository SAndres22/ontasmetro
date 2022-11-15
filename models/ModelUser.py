from .entities.User import User


class ModelUser():

    def registro(db,id,nombre,nombreUsuario,claveUsuario):
        try:
            datos = (nombre, nombreUsuario, User.convertir(claveUsuario))
            sql = "INSERT INTO `usuarios`(`idUser`, `nombre`, `nombreUsuario`, `claveUsuario`) VALUES (NULL,%s,%s,%s)"
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute(sql,datos)
            conn.commit()

            if cursor.fetchone != '':
                print("Guardado con exito")
            else:
                print("Error")

        except Exception as ex:
            raise Exception(ex)

    
    def login(db, user):
        try:
            sql = """SELECT idUser, nombre, nombreUsuario, claveUsuario FROM usuarios
            WHERE nombreUsuario = '{}'""".format(user.userName)
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            fila = cursor.fetchone()
            if fila != None:
                user = User(fila[0],fila[1], fila[2], User.check_Password(fila[3],user.password))
                return user
            else:
                return None

        except Exception as ex:
            raise Exception(ex)
    

    def get_by_id(db, id):
        try:
            sql = "SELECT idUser, nombre, nombreUsuario FROM usuarios WHERE idUser ={}".format(id)
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            fila = cursor.fetchone()
            if fila != None:
                return User(fila[0],fila[1], fila[2], None)
                
            else:
                return None

        except Exception as ex:
            raise Exception(ex)