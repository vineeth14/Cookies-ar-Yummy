from flask import Flask, render_template,flash
from forms import LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] ='1'

@app.route("/")
@app.route("/login",methods=['GET','POST'])
def login():
	form= LoginForm()
	if form.validate_on_submit():
		flash(f'Successfullylogged in as  {form.username.data}!','success')
	return render_template('login.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)