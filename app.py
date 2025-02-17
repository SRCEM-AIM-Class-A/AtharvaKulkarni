from flask import Flask , render_template

app = Flask(__name__, template_folder='template')

@app.route("/")
def main():
     return render_template("index.html")
 
@app.route("/products")
def product():
     return "<p>this is a product page</p>"
 
@app.route("/about")
def about():
     return "<p>this is the about page</p>"
 
@app.route("/res")
def res():
     return render_template("responsive.html")

if __name__ == "_main_":
     app.run(debug=True, host='0.0.0.0', port=5000)