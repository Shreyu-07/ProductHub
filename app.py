from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        username = request.form['Username']
        gmail = request.form['email']+'@gmail.com'
        link = request.form['link']
        price = request.form['prise']
        product = request.form['product']
        describe = request.form['describe']
        btn = request.form.get('btn')
        print(btn)
        return render_template('index.html',username=username,gmail=gmail,link=link,price=price,product=product,describe=describe,btn=btn)
    
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)

