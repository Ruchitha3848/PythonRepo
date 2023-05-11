import mysql.connector
from flask import Flask,request,render_template,flash,redirect


app=Flask(__name__)

@app.route("/")
def entry():
    return render_template('choice.html')

@app.route("/entry",methods=['POST','GET'])
def enter():
    return render_template('entry.html')

@app.route("/details",methods=['POST','GET'])
def details():
    return render_template('get.html')

@app.route("/delete",methods=['POST','GET'])
def delete():
    return render_template('remove.html')


@app.route("/submit",methods=['POST','GET'])
def submit():
    if request.method=='POST':
        connect=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='clarivate')

        mycursor=connect.cursor()
        id=request.form['eid']
        first_name=request.form['firstname']
        last_name=request.form['lastname']
        dob=request.form['dob']
        gender=request.form['gender']
        mobile=request.form['mobile']
        email=request.form['email']
        role=request.form['role']
        location=request.form['location']
        experience=request.form['experience']
        salary=request.form['salary']
        sql_2="select * from employee_details where id={0}".format(id)
        mycursor.execute(sql_2)
        result=mycursor.fetchall()
        
        mycursor2=connect.cursor()
        sql_1="insert  into employee_details(id ,first_name ,last_name ,dob ,gender ,mobile_number , email, erole ,location ,experience,salary) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(id,first_name,last_name,dob,gender,mobile,email,role,location,experience,salary)
        if (len(result)): 
         
            return render_template("sucess.html",message="Employee already Exist!")
        else:
            mycursor2.execute(sql_1,val)
            connect.commit()
            connect.close() 
            return render_template("sucess.html",message="Successfully submitted!")
            
    connect.commit()
    connect.close()  
       
@app.route("/get",methods=['POST','GET']) 
def get_details():
    if request.method=='POST':
        id=request.form['eid']
        connect=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='clarivate')
        
        mycursor=connect.cursor()
        sql_2="select * from employee_details where id={0}".format(id)
        mycursor.execute(sql_2)
        result=mycursor.fetchall()  
        connect.commit()
        connect.close() 
    if (len(result)):  
        return render_template("display_details.html",id=result[0][0],first_name=result[0][1],last_name=result[0][2],dob=result[0][3],gender=result[0][4],mobile=result[0][5],email=result[0][6],role=result[0][7],location=result[0][8],experience=result[0][9],salary=result[0][10])
    else:
        return render_template("no records.html",message="No Records found!")
    
    
@app.route("/remove",methods=['POST','GET']) 
def delete_details():
    if request.method=='POST':
        id=request.form['eid']
        connect=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='clarivate')
        
        mycursor=connect.cursor()
        sql_2="delete  from employee_details where id={0}".format(id)
        mycursor.execute(sql_2)
        result=mycursor.fetchall()  
        connect.commit()
        connect.close() 
    if (len(result)):
        return render_template("exist.html",message="Deleted Successfully!") 
    else:
         return render_template("exist.html",message="Deleted Successfully")
       
    
if __name__=='__main__':
    app.debug=True
    app.run()