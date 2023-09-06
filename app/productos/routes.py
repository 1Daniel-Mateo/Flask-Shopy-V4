from . import productos
#el . es para que nos importe todo el modulo
from . import productos
from flask import render_template
from .forms import NuevoProducto
import app#se llama al modelo
import os 

@productos.route('/crear', methods=["GET","POST"])
def crear_producto():
    p = app.models.Producto()
    form=NuevoProducto()
    if form.validate_on_submit():
       #El formulario va a llenar
       #El nuevo objeto producto
       #automaticamente
       form.populate_obj(p)
       p.imagen=form.imagen.data.filename
       app.db.session.add(p)
       app.db.session.commit()
       
       #Ubicar el archivo imagen
       #se ubicara en app/productos/imagenes
       file = form.imagen.data
       file.save(os.path.abspath(os.getcwd()+'/app/productos/imagenes/'+p.imagen))
       
    return render_template('new.html', form = form)


@productos.route('/listar')
def listar():
   #Traeremos los productos  de la base de datos
   productos = app.Producto.query.all()
   #mostrar la vista de listar
   #envieandole los productos seleccionados
   return render_template('listar.html',
                          productos=productos)
   