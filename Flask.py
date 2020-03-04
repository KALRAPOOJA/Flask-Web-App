from flask import Flask,request
from flask_restplus import Api,Resource,fields
from database_form import Database_Login
Login_object=Database_Login()
app=Flask(__name__)
api=Api(app,version = "1.0",title = "Registration Application", description = "Registration Application")
resource_model=api.model('Registration',{'UserName':fields.String(required=True,description="Username for Registration"),
    'Password': fields.String(required=True,description='Password required to login',min_length=3)})
@api.route('/information')
class User_Login(Resource):
    @api.marshal_with(resource_model, as_list=True)
    def get(self):
        return(Login_object.get_all_info())
    
    @api.expect(resource_model)
    def post(self):
        info=api.payload
        return Login_object.insert_user_info(info)

@api.route('/<particular_user>')
@api.param('UserName','User information')
class Specific_User(Resource):
    @api.marshal_with(resource_model)
    def get(self,particular_user):
        return(Login_object.get_particular_user(particular_user))
        
if __name__=='__main__':
    app.run(debug=True)


