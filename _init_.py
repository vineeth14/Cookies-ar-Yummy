from flask import Flask, render_template,flash,request
from forms import LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] ='1'


@app.route("/login",methods=['GET','POST'])
def login():
	form= LoginForm()
	if form.validate_on_submit():
		if request.cookies.get('admin') == "true":
			flash(f'flag{cookies_are_fun}')
		flash(f'Successfullylogged in as  {form.username.data}!','success')
	return render_template('login.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)