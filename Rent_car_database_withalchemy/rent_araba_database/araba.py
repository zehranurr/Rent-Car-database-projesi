from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = "change your url"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Arabalar(db.Model):
    __tablename__ = 'Arabalar'

    id = db.Column(db.Integer, primary_key=True)
    marka = db.Column(db.String(255))
    model = db.Column(db.String(255))
    fiyat = db.Column(db.String(15)) 
    
    is_active = db.Column(db.Boolean)
    resim = db.Column(db.String(255))

class aboutus(db.Model):
    __tablename__= 'aboutus'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    resim = db.Column(db.String(255))
    aciklama = db.Column(db.String(255))
    

class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    resim = db.Column(db.String(255))
    isim = db.Column(db.String(255))
    yorum = db.Column(db.String(255))


    

@app.route('/')
def index():
    rows = Arabalar.query.all()
    aboutus_= aboutus.query.all()
    customer=Customer.query.all()
    first_car = Arabalar.query.filter_by(id=2)


    return render_template('index.html', rows=rows,aboutus_=aboutus_,customer=customer,first_car=first_car)



@app.route('/admin')
def admin():
    return render_template('admin.html')



@app.route('/admin/arabaekle', methods=['GET', 'POST'])
def arabaekle():
    if request.method == 'GET':
        return render_template('arabaekle.html')
    
    if request.method == 'POST':
        marka_resim = request.form['resim']
        marka_marka = request.form['marka']
        marka_fiyati = request.form['fiyat']
        marka_model = request.form['model']

        # Create a new Arabalar object and add it to the database
        new_araba = Arabalar(
            resim=marka_resim,
            marka=marka_marka,
            fiyat=marka_fiyati,
            model=marka_model
        )
        db.session.add(new_araba)
        db.session.commit()

        # Fetch all Arabalar records from the database
        araba= Arabalar.query.all()

        return render_template('arabalar.html',araba=araba)

    


    
@app.route('/admin/arabaguncelle', methods=['GET', 'POST'])
def arabaupdate():
        if request.method == 'GET':
            araba_id = request.args.get('id')
            araba = Arabalar.query.filter_by(id=araba_id)
            return render_template('arabaguncelle.html', araba=araba)

        if request.method == 'POST':
            araba_id = request.args.get('id')
            araba = Arabalar.query.get(araba_id)

        if araba:
            araba.resim = request.form['resim']
            araba.marka = request.form['marka']
            araba.fiyat = request.form['fiyat']
            araba.model = request.form['model']

            db.session.commit()
        araba= Arabalar.query.all()    

        return render_template('arabalar.html',araba=araba) # Redirect to the list of Arabalar

@app.route('/admin/arabasil', methods=['GET'])
def arabasil():
    araba_id = request.args.get('id')
    araba = Arabalar.query.get(araba_id)

    if araba:
        db.session.delete(araba)
        db.session.commit()
        

        
    araba = Arabalar.query.all()

    return render_template('arabalar.html',araba=araba)

@app.route('/admin/arabalar')
def gallery():
    araba= Arabalar.query.all()  # Fetch all records from the Arabalar table

    return render_template('arabalar.html', araba=araba)
    





if __name__ == '__main__':
    app.run(debug=True)
