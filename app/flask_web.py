from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname':'Miguel'}
	return render_template("index.html",user=user)



@app.route('/login')
def login():
	return render_template("login.html")


@app.route('/sigin')
def sigin():
	return render_template("signin.html")	

@app.route('/siginin',methods=['GET','POST'])
def siginin():
	user = request.args.get('username')
	passwd = request.args.get('password')
	with open("userdata","a+") as f:
		f.writelines(user + ' ' + passwd + '\n')
	return 'yes'
@app.route('/showuser')
def showuser():
	list_user = []
	dict_user = {}
	with open("userdata","r") as f:
		for line in f:
			user = line.split()[0]
			passwd = line.split()[1]
			dict_user['user'] = user
			dict_user['passwd'] = passwd
			list_user.append(dict_user.copy())
#	list_user = [{'user':'wang','passwd':'123'},{'user':'liu','passwd':'123'},{'user':'sun','passwd':'456'}]
	return render_template("showuser.html",list_user = list_user)

if __name__ == '__main__':
	app.run()
