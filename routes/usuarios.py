from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.usuario import Usuario
from utils.db import db

usuarios = Blueprint('usuarios', __name__)

@usuarios.route('/')
def index():
    usuarios = Usuario.query.all()
    return render_template('index.html', usuarios = usuarios)


@usuarios.route('/new', methods = ['POST'])
def add_user():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    username = request.form['username']
    password = request.form['password']
    
    new_usuario = Usuario(nombre, apellido, username, password)
    
    db.session.add(new_usuario)
    db.session.commit()
    
    flash("Usuario agregado satisfactoriamente.")
    
    return redirect(url_for('usuarios.index'))


@usuarios.route('/update/<id>', methods = ['POST', 'GET'])
def update_user(id):
    usuario = Usuario.query.get(id)
    
    if request.method == "POST":
        usuario.nombre = request.form['nombre']
        usuario.apellido = request.form['apellido']
        usuario.username = request.form['username']
        usuario.password = request.form['password']
        
        db.session.commit()
        
        flash("Usuario actualizado satisfactoriamente.")
        
        return redirect(url_for("usuarios.index"))
        
    return render_template('update_user.html', usuario = usuario)


@usuarios.route('/delete/<id>')
def delete_user(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    
    flash("Usuario eliminado satisfactoriamente.")
    
    return redirect(url_for('usuarios.index'))


@usuarios.route('/about')
def about():
    return render_template('about.html')