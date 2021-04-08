from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {
        "appName": {{ data.appName }},
        "equipe": {{ data.equipe }},
        "login": {{ data.login }},
        "email": {{ data.email }},
    }

@app.route('/healthcheck')
def healthcheck():
    return  "working" 

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,port="8080")
