from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
  name = request.form.get('name')
  email = request.form.get('email')
  classno = request.form.get('classno')
  satisfaction = request.form.get('satisfaction')
  feedback = request.form.get('feedback')

  with open('responses.txt', 'a') as file:
   file.write(name + ' ,' + email + ' ,' + classno + ' ,' + satisfaction + ' ,' + feedback + '\n')
    
  return 'Feedback submitted successfully! :)'     
  
  
app.run(host='0.0.0.0', port=81)
