import mysql.connector
from flask import Flask,request,render_template,flash,redirect
from tkinter import messagebox


app=Flask(__name__)

@app.route("/")
def entry():
    return render_template('choice.html')

@app.route("/entry",methods=['POST'])
def enter():
    return render_template('entry.html')

@app.route("/details",methods=['POST'])
def details():
    return render_template('get.html')

@app.route("/submit",methods=['POST'])
def submit():
    if request.method=='POST':
        connect=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='clarivate')

        mycursor=connect.cursor()
        id=request.form['eid']
        name=request.form['ename']
        gender=request.form['egender']
        role=request.form['erole']
        location=request.form['elocation']
        salary=request.form['esalary']
        sql_2="select * from employees where emp_id={0}".format(id)
        mycursor.execute(sql_2)
        result=mycursor.fetchall()
        
        mycursor2=connect.cursor()
        sql_1="insert  into employees(EMP_ID,EMP_NAME,emp_gender,EMP_ROLE,emp_location ,EMP_SALARY) values(%s,%s,%s,%s,%s,%s)"
        val=(id,name,gender,role,location,salary)
        if (len(result)):  
            return render_template("sucess.html",message="Employee Exist!")
        else:
            mycursor2.execute(sql_1,val)
            connect.commit()
            connect.close() 
            return render_template("sucess.html",message="successful!")
            
    connect.commit()
    connect.close()  
       
@app.route("/get",methods=['POST']) 
def get_details():
    if request.method=='POST':
        id=request.form['eid']
        connect=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='clarivate')
        
        mycursor=connect.cursor()
        sql_2="select * from employees where emp_id={0}".format(id)
        mycursor.execute(sql_2)
        result=mycursor.fetchall()  
        connect.commit()
        connect.close() 
    if (len(result)):  
        return render_template("display_details.html",id=result[0][0],name=result[0][1],gender=result[0][2],role=result[0][3],location=result[0][4],salary=result[0][5])
    else:
        return render_template("no records.html")
    
    
if __name__=='__main__':
    app.debug=True
    app.run()