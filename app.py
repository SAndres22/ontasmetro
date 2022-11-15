from  config import config
from flask import Flask, redirect, render_template, request, url_for, flash
#Models
from models.ModelUser import ModelUser
#Entities
from models.entities.User import User

#Preparar la conexion a la BD   
from flaskext.mysql import MySQL

#Para las sesiones
from flask_login import LoginManager,login_user,logout_user, login_required

app = Flask(__name__, template_folder='templates')

app.secret_key = "Develoteca"
db = MySQL(app)

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def cargar_Usuario(id):
    return ModelUser.get_by_id(db,id)

@app.route('/')
def index():
    return render_template('/auth/index.html')

# Registrar un usurario
@app.route('/registro',  methods =['GET','POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nombreUsuario = request.form['userName']
        claveUsuario = request.form['password']
        registro_user =  ModelUser.registro(db,0,nombre,nombreUsuario,claveUsuario)

        return render_template('auth/login.html')
    else:
        return render_template('auth/registro.html')

@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0,'',request.form['userName'],request.form['password'])
        user_logueado = ModelUser.login(db,user)

        if user_logueado != None:
            if user_logueado.password:
                #Funcion login user que importamos
                login_user(user_logueado)
                return redirect(url_for('home'))
            else:
                flash("Usuario o clave incorrecta")
                print("Clave incorrecta")
                return render_template('auth/login.html')
        else:
            flash("Usuario incorrecto")
            print("User no existe")

        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home')
@login_required
def home():
    return render_template("auth/home.html")

def estado_401(error):
    return redirect(url_for('login'))

#Url que no exista
def estado_404(error):
    return render_template("auth/error404.html"), 404


#Ver rutas
@app.route('/ver_Rutas')
@login_required
def ver_Rutas():
    
    return render_template("auth/ver_Rutas.html")

#Ver estaciones
@app.route('/ver_estaciones')
@login_required
def ver_estaciones():
    
    return render_template("auth/ver_estaciones.html")

#Ver ubicacion actual
@app.route('/ubicacion_actual')
@login_required
def ubicacion_actual():
    
    return render_template("auth/ubicacion_actual.html")

#Ver perfil
@app.route('/ver_perfil')
@login_required
def ver_perfil():
    
    return render_template("auth/ver_perfil.html")



if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(401,estado_401)
    app.register_error_handler(404,estado_404)
    
    app.run()
