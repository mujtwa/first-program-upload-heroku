from flask import Flask
app= Flask(__name__)

@app.route('/',methods=['GET','POST'])
def yah():
    return "<h2> I am from Kumhariya Rampur</h2>"

if __name__ == '__main__':
    app.run()

