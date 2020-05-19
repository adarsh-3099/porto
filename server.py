from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)

#@app.route('/<username>/<int:post_id>')
#def hello_world(username=None,post_id=None):                                                                                      
#	return render_template('index.html',name=username,post_id=post_id)  

@app.route('/')

def my_html():
    return render_template('index.html')                                                                                                    

@app.route('/<string:page_name>')
def contact(page_name):
    return render_template(page_name)

def write_to_csv(data):
	with open("database.csv",newline='',mode='a') as database2:
		email=data['email']
		subject=data['subject']
		message=data['message']
		csv_writer=csv.writer(database2,delimiter=":",   quotechar='|', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])
 
def write_to_data(data):
	with open("database.txt",mode='a') as database:
		email=data['email']
		subject=data['subject']
		message=data['message']
		file=database.write(f"\n{email},{subject},{message}")


@app.route('/submit_forum', methods=['POST', 'GET'])
def submit_forum():
	if request.method=="POST":
		try:
			data=request.form.to_dict()
			write_to_csv(data)
			return redirect("/thnk-you.html")
		except:
			return "did not saved to database"
   