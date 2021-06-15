from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


from flask_wtf.csrf import CSRFProtect

from forms.student_form import StudentForm

app = Flask(__name__)
CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200)) 
    pin = db.Column(db.String(10))

    def __init__(self, name, city, address, pin):
        self.name = name
        self.city = city
        self.addr = address
        self.pin = pin

@app.route('/')
def show_all():
    form = StudentForm()
    return render_template('student_show_all.html', students = Students.query.all(), form=form)

@app.route('/new', methods = ['GET', 'POST'])
def new_student():
    form = StudentForm()
    # if form.validate_on_submit():
    #     return '<h3>' + form.name.data + ' ' + form.city.data + ' ' + form.address.data + ' ' + form.pin.data  + '</h3>'
    if form.validate_on_submit():
        student = Students(form.name.data, form.city.data, form.address.data, form.pin.data)
        form.populate_obj(student)
        db.session.add(student)
        db.session.commit()
        flash('Record was successfully added')
        return redirect(url_for('show_all'))
    # print(form.name.data, form.city.data, form.address.data, form.pin.data)
    return render_template("student_new.html", form=form, template="form-template")

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_student(id):
    form = StudentForm()
    if form.validate_on_submit():
        student_object = db.session.query(Students).get(id)
        form.populate_obj(student_object)
        db.session.add(student_object)
        db.session.commit()
        flash('Record was successfully added')
        return redirect(url_for('show_all'))
    return render_template('student_update.html', students = db.session.query(Students).get(id), form=form)

if __name__ == '__main__':
    db.create_all()
    app.debug = True
    app.run()
    app.run(debug = True)