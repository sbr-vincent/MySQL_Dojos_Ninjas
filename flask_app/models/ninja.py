from flask_app.config.mysqlconnection import connectToMySQL
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        # we need to place the FK for the burger in the class. 
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO ninjas (first_name , last_name, age, dojo_id , created_at , updated_at ) VALUES (%(fname)s,%(lname)s,%(age)s,%(dojo_id)s,NOW(),NOW());"
        return connectToMySQL('dojos_ninjas').query_db(query,data)

