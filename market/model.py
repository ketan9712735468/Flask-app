from market import db,login_manager
from market import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Item(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(length=20),nullable=False,unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'
db.create_all()

class User(db.Model,UserMixin):
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True,nullable=False)
    username = db.Column(db.String(length=20),nullable=True,unique=True)
    email = db.Column(db.String(length=50),nullable=True,unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False,unique=False)
    budget = db.Column(db.Integer(),default=1000)


    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
        
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

db.create_all()