from flask import *
from audit import academicaudit, auditfromstring
from flask_sslify import SSLify
app = Flask(__name__)
sslify = SSLify(app, permanent=True)
app.debug = False

@app.route('/audit', methods=['GET', 'POST'])
def displayaudit():
    if request.method == 'POST':
        if request.form.get('user') and request.form.get('passwd'):
            try:
                auditobj = academicaudit(request.form['user'], request.form['passwd'])
            except:
                return render_template('error.html', e="There was a problem logging in. Please try again.")
        elif request.form.get('rawaudit'):
            try:
                auditobj = auditfromstring(request.form['rawaudit'])
            except:
                return render_template('error.html', e="This audit doesn't seem to be formatted normally.")
        else:    
            return render_template('error.html', e="Please fill in all fields.")    
        return render_template('audit.html', audit=auditobj)
    else:
        return redirect( url_for('home') )    

@app.route('/')
def home():
    return render_template('entry.html')
    
if __name__ == '__main__':
    app.run()    
