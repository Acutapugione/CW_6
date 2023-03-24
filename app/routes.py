from flask import\
    redirect,\
    render_template,\
    flash,\
    url_for
            
from app import app
from app.forms import LoginForm


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        flash(f"User {form.login.data} was logged")
        return redirect(url_for('index'))
    
    return render_template('login.html', form=form)