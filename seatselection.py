#app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import rds_db as db
 
app = Flask(__name__)

 
@app.route('/')
def Index():
     list_users = db.get_details()
     #print(list_users)
     return render_template('seatSelectionPage.html', list_users = list_users)
 

@app.route('/update_seates', methods=['POST'])
def add_student():
    if request.method == 'POST':
       listup = request.form.getlist('mycheckbox')
       for i in listup:
           print(int(i))
           db.update_by_id(int(i))
    return redirect(url_for("Index"))
       
 

 
if __name__ == "__main__":
    app.run(debug=True)