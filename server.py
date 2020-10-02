from flask import Flask , render_template, url_for, request, redirect
import csv
app = Flask(__name__)
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/<string:my_page>')
def htmlPage(my_page):
    return render_template(my_page)

def writ_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')    

def writ_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_write = csv.writer(database2, delimiter=',',quotechar='|', quoting = csv.QUOTE_MINIMAL)
        csv_write.writerow([email,subject,message])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            writ_to_csv(data)
        except:
            return 'Did not save to the database!!!!!!'
        return render_template('thanku.html')
    else:
        return 'Something went wrong here!'