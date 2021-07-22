from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '이선우 머리 대머리머리머머리!!'

if __name__ == '__main__':
    app.run()
