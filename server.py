## https://xkcd.com/ gebruiken voor deze les
## python heeft een http server module 'HTTPServer'. Deze is echter erg standaard. Flask (lean) en Django (erg uitgebreid) zijn meer geadvanceerd en veiliger in gebruik
## pythonanywhere is een gratis server waar je je scripts op kan zetten https://www.pythonanywhere.com/
# adres = 'henky.88hh@gmail.com' (voor pythonanywhere)
# WW = 'Henky88*' (voor python anywehere)
## Github account 'henky.88hh@gmail.com, ww: Henky123456789



#http://www.mashup-template.com/templates.html
import csv
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
print(__name__) #Geeft __main__ want is main file

#Bij veranderingen moet je de server opnieuw draaien met flask run in de terminal. Zie dcc quick start
# Met debug mode 'on' hoef je niet de hele tijd de server opnieuw op te starten. Zie doc's.
# Met render_template kan je een html bestand verzende
# Favicon via HTML bestand toevoegen.

@app.route('/') #is een decorator.
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>') #variabele link
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET']) #wordt aangeroepen vanuit contact.html in stukje "send"
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict() #maakt een dictionary van de .html data
        write_to_csv(data) #Functie aanspreken
        print(data)
        return redirect('./thankyou.html')
    else:
        return 'er gaat iets fout'

def write_to_file(data):
    with open('database.txt',mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}') #\n is een nieuw regel

def write_to_csv(data):
    with open('database.csv',newline='',mode='a') as database2: #a staat voor append
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL) #delimiter is scheidingsteken
        csv_writer.writerow([email,subject,message])
# @app.route('/<username>/<int:post_id>') #is een <..> is een variabele in HTML. http://127.0.0.1:5000/koos bv in browser. Koos is dan de variabele naam
# def hello_world1(username = None, post_id = None): #Default instellen
#     return render_template('./index.html',name = username,post_id=post_id) #de functie zoekt in folder 'template', dus folder template aanmaken en daar de html bestanden in stoppen


# @app.route('/')
# def blog():
#     return render_template('/index.html')
#
# @app.route('/works.html')
# def blog1():
#     return render_template('/works.html')
#
# @app.route('/about.html')
# def blog2():
#     return render_template('/about.html')
#
# @app.route('/contact.html')
# def blog3():
#     return render_template('/contact.html')
#
# @app.route('/components.html')
# def blog4():
#     return render_template('/components.html')

# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'Dit is een mooi 2020 hondje'


