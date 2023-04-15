import mysql.connector
from flask import Flask,request,render_template

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
        name=request.form['ename']
        id=request.form['eid']
        role=request.form['erole']
        salary=request.form['esalary']
       
        connect=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='clarivate')

        mycursor=connect.cursor()
        sql_1="insert into employee_details(EMP_ID,EMP_NAME,EMP_ROLE ,EMP_SALARY) values(%s,%s,%s,%s)"
        val=(id,name,role,salary)
        mycursor.execute(sql_1,val)
        connect.commit()
        connect.close()  
    return render_template('sucess.html')

    
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
        sql_2="select * from employee_details where emp_id={0}".format(id)
        mycursor.execute(sql_2)
        result=mycursor.fetchall()  
        connect.commit()
        connect.close() 
    if (len(result)):  
        return render_template("display_details.html",id=result[0][0],name=result[0][1],role=result[0][2],sal=result[0][3])
    else:
        return render_template("no records.html")
    
    
if __name__=='__main__':
    app.debug=True
    app.run()