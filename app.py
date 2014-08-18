from flask import *
from audit import academicaudit, auditfromstring

app = Flask(__name__)
app.debug = True

@app.route('/audit', methods=['GET', 'POST'])
def displayaudit():
    if request.method == 'POST':
        if request.form.get('user') and request.form.get('passwd'):
            try:
                auditobj = academicaudit(request.form['user'], request.form['passwd'])
            except:
                raise Exception("There was a problem logging in. Please try again.")
        elif request.form.get('rawaudit'):
            auditobj = auditfromstring(request.form['rawaudit'])
        else:    
            raise ValueError("Please fill in all fields.")    
        return render_template('audit.html', audit=auditobj)
    else:
        return redirect( url_for('home') )    

@app.route('/')
def home():
    return render_template('entry.html')
    
if __name__ == '__main__':
    app.run()    