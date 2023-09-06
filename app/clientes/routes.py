from . import clientes
from flask import render_template
from .forms import NuevoCliente
import app


@clientes.route('/crear_usuario', methods=['GET','POST'])
def crear_cliente():
    p = app.models.Cliente()
    form = NuevoCliente()
    if form.validate_on_submit():
        app.db.session.add(p)
        app.db.session.commit()

    return render_template('newCliente.html', form=form)


@clientes.route('/listeCliente')
def listar():
    clientes= app.Cliente.query.all()

    return render_template('listarCliente.html',
                           clientes=clientes)