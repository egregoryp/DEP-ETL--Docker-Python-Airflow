from utils.db import db

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    customer_fname = db.Column(db.Text)
    customer_lname = db.Column(db.Text)
    customer_email = db.Column(db.Text)

    def __init__(self, customer_fname, customer_lname, customer_email):
        self.customer_fname = customer_fname
        self.customer_lname = customer_lname
        self.customer_email = customer_email

    def to_dict_customer(self):
        return {
            "id": self.id,
            "customer_fname": self.customer_fname,
            "customer_lname" : self.customer_lname,            
            "customer_email": self.customer_email            
        }