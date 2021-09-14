from flask import Flask

# __name__ es decir el nombre de nuestro fichero
app = Flask(__name__) 

@app.route("/")
# el nombre que queramos 
def function1():
    return "Hola, mundo!".upper()

@app.route("/bye")
def function2():
    return "Adiós, mundo!"

# export FLASK_ENV=development ----> variable de entorno para actualización automática
# pip install python-dotenv ----> para generar variables de entonrno -----> generar .env

