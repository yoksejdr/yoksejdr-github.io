from flask import Flask, render_template

app = Flask("WebIraide")

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/example")
def example_route():
    return "Esto es una página de ejemplo"




if __name__ == "__main__":
    import os
    port = int(os.environget("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port='5000' )
