import mysql_db.db as mydb
from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/loginin',methods = ['GET','POST'])
def loginin():
	user = request.form.get('username')
	passwd = request.form.get('password')
	res = mydb.mysql("select * from user where username='%s'"%(user))
	if len(res) == 0:
		str_alert = 'you are not in'
		return render_template("login0.html")
	else:
		if passwd == str(res[0][1]):
			return redirect('/showbooks')	
		else:
			str_alert = 'wrong password!'
			return render_template("login1.html")	



@app.route('/showbooks')
def showbooks():
	'''
	list_books = [{'bookid':id,'bookname':'<bookname>','nums':'1','remark':''}]
	'''
	page = int(request.args.get('page',1))
	num = 10
	pages = int(mydb.mysql('select count(*) from bookinfo;')[0][0])
	total = pages
	if total % num == 0:
		pages = total / num
	else:
		pages = total / num +1
	start_position = (page - 1)*num
	res = mydb.mysql('select * from bookinfo limit %s,%s'%(start_position,num))
	
#	res = mydb.mysql('select * from bookinfo;')
	list_books = []
	dict_books = {}
	for i in res:
		dict_books['bookid'] = i[0]
		dict_books['bookname'] = i[1]
		dict_books['nums'] = i[2]
		dict_books['remark'] = i[3]
		list_books.append(dict_books.copy())
	return render_template("showbooks.html",list_books = list_books,pages=pages)	

@app.route('/deletebooks')
def deletebooks():
	dict_del = request.args.items()
	list_delbooks = zip(*dict_del)[0]
	for i in list_delbooks:
		old_nums = mydb.mysql("select * from bookinfo where id='%s'"%(i))[0][2]
		old_nums = int(old_nums)
		new_nums = old_nums - 1	
		new_nums = str(new_nums)			 
		mydb.mysql("update bookinfo set nums='%s' where id='%s'"%(new_nums,i))
	
	return redirect('/showbooks')	

@app.route('/addbooks')
def addbooks():
	dict_del = request.args.items()
	list_delbooks = zip(*dict_del)[0]
	for i in list_delbooks:
		old_nums = mydb.mysql("select * from bookinfo where id='%s'"%(i))[0][2]
		old_nums = int(old_nums)
		new_nums = old_nums + 1	
		new_nums = str(new_nums)			 
		mydb.mysql("update bookinfo set nums='%s' where id='%s'"%(new_nums,i))
	
	return redirect('/showbooks')	


if __name__ == '__main__':
	app.run()
