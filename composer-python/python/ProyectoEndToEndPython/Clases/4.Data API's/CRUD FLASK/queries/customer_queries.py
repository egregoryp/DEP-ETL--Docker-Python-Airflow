from models.customer_models import Customer
from utils.db import db

def create_customer(params):
    fname = params['fname']
    lname = params['lname']
    email = params['email']

    try:
        new_customer = Customer(fname, lname, email)
        db.session.add(new_customer)
        db.session.commit()        
        payload = {
            "success": True,
            "data": new_customer.to_dict_customer()
        }
    except Exception as error:        
        payload = {
            "success": False,
            "errors" : [str(error)]                                    
        }

    return payload
    
def get_customer(id):
    try:
        customer = Customer.query.get(id)
        #customer = Customer.query.all #to get all customers        
        customerResult = customer.to_dict_customer()

        payload = {
            "success": True,
            "data": customerResult
        }
    except Exception as error:        
        payload = {
            "success": False,
            "errors" : [str(error)]                                    
        }

    return payload

def update_customer(id, params):
    try:
        customer = Customer.query.get(int(id))
        #customer = Customer.query.filter_by(id=id).first()
        #params['name'] #if not exists then gives error
        #params.get('name') #if not exists then null        

        #use values defined in model not param names
        if params.get('fname'):            
            customer.customer_fname = params['fname']            

        if params.get('lname'):
            customer.customer_lname = params['lname']

        if params.get('email'):
            customer.customer_email = params['email']            
        
        db.session.commit()        
        customerResult = customer.to_dict_customer()        

        payload = {
            "success": True,
            "data": customerResult
        }
    except Exception as error:        
        payload = {
            "success": False,
            "errors" : [str(error)]                                    
        }

    return payload

def delete_customer(id):
    try:
        customer = Customer.query.get(id)        
        customerResult = customer.to_dict_customer()
        db.session.delete(customer)
        db.session.commit()

        payload = {
            "success": True,
            "data": customerResult
        }
    except Exception as error:        
        payload = {
            "success": False,
            "errors" : [str(error)]                                    
        }

    return payload
