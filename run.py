from flask import Flask,render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   return render_template('hello.html',**templateData)

if __name__ == '__main__':
    app.run(debug=True)