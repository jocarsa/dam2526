from flask import Flask, render_template 

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  return render_template("index.html")
  
if __name__ == "__main__":
  aplicacion.run()
