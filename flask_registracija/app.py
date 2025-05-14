import os
from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user, logout_user, login_user, UserMixin, login_required
import forms
from datetime import datetime
from forms import IrasoForma
import secrets
from PIL import Image
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


class ManoModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.el_pastas == "el@pastas.lt"
    
    def inaccessible_callback(self, name, **kwargs):
        abort(403)
    
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profilio_nuotraukos', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = '4654f5dfadsrfasdr54e6rae'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'biudzetas.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'prisijungti'
login_manager.login_message_category = 'info'

class Vartotojas(db.Model, UserMixin):
    __tablename__ = "vartotojas"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String(20), unique=True, nullable=False)
    el_pastas = db.Column("El. pašto adresas", db.String(120), unique=True, nullable=False)
    nuotrauka = db.Column(db.String(20), nullable=False, default='default.jpg')
    slaptazodis = db.Column("Slaptažodis", db.String(60), nullable=False)

class Irasas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    turinys = db.Column(db.Text, nullable=False)
    data = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('vartotojas.id'), nullable=False)

    vartotojas = db.relationship('Vartotojas', backref=db.backref('irasai', lazy=True))

admin = Admin(app)
admin.add_view(ManoModelView(Irasas, db.session))
admin.add_view(ManoModelView(Vartotojas, db.session))

@login_manager.user_loader
def load_user(vartotojo_id):
    return Vartotojas.query.get(int(vartotojo_id))


@app.route("/registruotis", methods=['GET', 'POST'])
def registruotis():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forms.RegistracijosForma()
    if form.validate_on_submit():
        koduotas_slaptazodis = bcrypt.generate_password_hash(form.slaptazodis.data).decode('utf-8')
        vartotojas = Vartotojas(vardas=form.vardas.data, el_pastas=form.el_pastas.data, slaptazodis=koduotas_slaptazodis)
        db.session.add(vartotojas)
        db.session.commit()
        flash('Sėkmingai prisiregistravote! Galite prisijungti', 'success')
        return redirect(url_for('index'))
    return render_template('registruotis.html', title='Register', form=form)

@app.route("/prisijungti", methods=['GET', 'POST'])
def prisijungti():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forms.PrisijungimoForma()
    if form.validate_on_submit():
        user = Vartotojas.query.filter_by(el_pastas=form.el_pastas.data).first()
        if user and bcrypt.check_password_hash(user.slaptazodis, form.slaptazodis.data):
            login_user(user, remember=form.prisiminti.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Prisijungti nepavyko. Patikrinkite el. paštą ir slaptažodį', 'danger')
    return render_template('prisijungti.html', title='Prisijungti', form=form)

@app.route("/atsijungti")
@login_required
def atsijungti():
    logout_user()
    return redirect(url_for('index'))

@app.route("/paskyra", methods=['GET', 'POST'])
@login_required
def paskyra():
    form = forms.PaskyrosAtnaujinimoForma()
    if form.validate_on_submit():
        if form.nuotrauka.data:
            nuotrauka = save_picture(form.nuotrauka.data)
            current_user.nuotrauka = nuotrauka
        current_user.vardas = form.vardas.data
        current_user.el_pastas = form.el_pastas.data
        db.session.commit()
        flash('Tavo paskyra atnaujinta!', 'success')
        return redirect(url_for('paskyra'))
    elif request.method == 'GET':
        form.vardas.data = current_user.vardas
        form.el_pastas.data = current_user.el_pastas
    nuotrauka = url_for('static', filename='profilio_nuotraukos/' + current_user.nuotrauka)
    return render_template('paskyra.html', title='Account', form=form, nuotrauka=nuotrauka)


@app.route('/irasai', methods=['GET', 'POST'])
def irasai():
    form = IrasoForma()
    if form.validate_on_submit():  # jei forma pateikta ir validuota
        turinys = form.turinys.data
        new_entry = Irasas(turinys=turinys, user_id=current_user.id)
        db.session.add(new_entry)
        db.session.commit()
        flash('Įrašas sėkmingai pridėtas!', 'success')
        return redirect(url_for('irasai'))  # nukreipia atgal į įrašų puslapį
    page = request.args.get('page', 1, type=int)
    visi_irasai = Irasas.query.filter_by(user_id=current_user.id).order_by(Irasas.data.desc()).paginate(page=page, per_page=2)

    return render_template("irasai.html", form=form, visi_irasai=visi_irasai, datetime=datetime)


@app.route("/delete/<int:id>")
@login_required
def delete(id):
    irasas = Irasas.query.get_or_404(id)
    db.session.delete(irasas)
    db.session.commit()
    flash('Įrašas sėkmingai ištrintas!', 'success')
    return redirect(url_for('irasai'))

@app.route("/update/<int:id>", methods=['GET', 'POST'])
@login_required
def update(id):
    irasas = Irasas.query.get_or_404(id)
    form = IrasoForma()
    if form.validate_on_submit():
        irasas.turinys = form.turinys.data
        db.session.commit()
        # print(f'Atnaujintas įrašas: {irasas.turinys}') # DEBUG
        flash('Įrašas atnaujintas!', 'success')
        return redirect(url_for('irasai'))
    elif request.method == 'GET':
        form.turinys.data = irasas.turinys
    return render_template('update.html', form=form, irasas=irasas)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=8000, debug=True)
