from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "11/22 大家好~中華大學"

@app.route("/test")
def test():
    return "test 11/22"
    
if __name__ == "__main__":
    app.run()
