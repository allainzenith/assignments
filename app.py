from flask import Flask,render_template,request,redirect,url_for,session
#import db #database abstraction
import re
import db
from os.path import exists

app=Flask(__name__)
app.secret_key="jsdfskksdfk"

@app.route("/tech2go/<message>")
def main_page():
    return redirect(url_for("main_page"))
##########################################################################################

@app.route("/complains", methods=["GET"])
def complains():
    temp = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmo... "
    hlist:list=["E-mail", "Details","Actions"]
    
    clist:dict = [{'email' : 'ethanlee@gmail.com', 'message': temp},
                {'email' : 'ethanlee@gmail.com', 'message': temp},
                {'email' : 'simjakeu@gmail.com', 'message': temp},
                {'email' : 'sunny2019@gmail.com ', 'message': temp},
                {'email' : 'chulso700@gmail.com', 'message': temp},
                {'email' : 'itssnaevis@gmail.com', 'message': temp},
                {'email' : 'gettoknowkaye@gmail,com', 'message': temp},
                {'email' : 'allainzenith12@gmail.com', 'message': temp},
                ]
   
    username:str=request.args.get("user")
    return render_template("complains.html",title="Complains | Tech2Go", user=username, header = hlist, content = clist)

#FIRST MU APPEAR
@app.route("/tech2go")
def index():
    return render_template("login.html",title="Tech2Go | Login")


@app.route("/login",methods=["POST"])
def login():
    username:str=request.form["username"]
    password:str=request.form["password"]

    if len(username)>0 or len(password)>0:
        userName:str= db.read_userName("admin",username,password)
        if db.validate_user("admin",username,password):
            session['username']=username
            return redirect(url_for("mainpage",user=userName))
        else:
            return redirect(url_for("index",title="FAIL"))
    else:
        return redirect(url_for("index",title="FAIL"))

     
@app.route("/register",methods=["POST"])     
def register():
    username:str=request.form["username"]
    password:str=request.form["password"]
    fname:str=request.form["fname"]
    lname:str=request.form["lname"]
    phone:str=request.form["phone"]
    email:str=request.form["email"]
    #
    fields:list=['firstname','lastname','phone','email','username','password']
    data:list=[fname,lname,phone,email,username,password]
    #
    message:str=""
    #if flag==0: #add new student
    okey:bool=db.add_user("admin",fields,data)
    if okey:
        userName:str= db.read_userName("admin",username,password)
        return redirect(url_for("mainpage", user=userName))
    else:
        return redirect(url_for("index",title="FAIL",user=userName))
    
    return 
              
       
@app.route("/logout")
def logout():
    return redirect(url_for("index"))

@app.route("/main", methods=["GET"])
def mainpage():
     username:str=request.args.get("user")
     return render_template("main_page.html",title="Main | Tech2Go", user=username)

########################################################################

@app.route("/verifyapplications")
def verifyapplications():
    temp:str="- Email: jpark@gmail.com Username: jay_park Password: ******* Name: Jay Park Ad..."
    hlist:list=["E-mail", "Details","Actions"]
    
    clist:dict = [{'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                ]
    username:str=request.args.get("user")
    return render_template("verifyapplications.html",title="Verify Applications | Tech2Go", user=username,  header = hlist, content = clist)

@app.route("/manageaccounts")
def manageaccounts():
    username:str=request.args.get("user")
    return render_template("manageaccounts.html",title="Manage Accoutns | Tech2Go", user=username)

@app.route("/manageaccountclient")
def manageaccountclient():
    temp:str=" Email Address: ethanlee@gmail.com, Address: Quezon street corner M... "
    hlist:list=["Client Name", "Details","Actions"]
    clist:dict = [{'name' : 'Ethan Lee', 'message': temp},
                {'name' : 'Ethan Lee', 'message': temp},
                {'name' : 'Ethan Lee', 'message': temp},
                {'name' : 'Ethan Lee', 'message': temp},
                {'name' : 'Ethan Lee', 'message': temp},
                {'name' : 'Ethan Lee', 'message': temp},
                {'name' : 'Ethan Lee', 'message': temp},
                {'name' : 'Ethan Lee', 'message': temp},
                ]
    username:str=request.args.get("user")
    return render_template("manageaccountclient.html",title="Manage Account Client | Tech2Go", user=username,  header = hlist, content = clist)
    
@app.route("/manageaccountprof")    
def manageaccountprof():
    temp:str=" Date and Time of Appointment: 30th of November, Tuesday, 2021, 10:0... "
    hlist:list=["Technician Name", "Details","Actions"]
    clist:dict = [{'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                ]
    username:str=request.args.get("user")
    return render_template("manageaccountprof.html",title="Manage Account technician | Tech2Go", user=username,  header = hlist, content = clist)
   
    
@app.route("/viewappointments")
def viewappointments():
    username:str=request.args.get("user")
    return render_template("viewappointments.html",title="View Appointments | Tech2Go", user=username)

@app.route("/viewappclient")
def viewappclient():
    temp:str=" Date and Time of Appointment: 30th of November, Tuesday, 2021, 10:0... "
    hlist:list=["Client Name", "Details","Actions"]
    clist:dict = [{'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                ]
    username:str=request.args.get("user")
    return render_template("viewappclient.html",title="View Appointments Client | Tech2Go", user=username,  header = hlist, content = clist)
    
@app.route("/viewappprof")
def viewappprof():
    temp:str=" Date and Time of Appointment: 30th of November, Tuesday, 2021, 10:0... "
    hlist:list=["technician Name", "Details","Actions"]
    clist:dict = [{'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                {'name' : 'Jay Park', 'message': temp},
                ]
    username:str=request.args.get("user")
    return render_template("viewappprof.html",title="View Appointments technician | Tech2Go", user=username, header = hlist, content = clist)

 
        
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
    
    
    
    