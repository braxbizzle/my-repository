from flask import Flask 
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

@app.route('/second')
def second():
    return "this is second page"

@app.route("/third/subthird")
def third():
    return " this is the third sub page"

@app.route("/whichpage/<string:page_id")

def whichpage(page_id):
    if page_id.isdigit():
        message = f"the id of this page is {page_id}"
    else:
        message = f"{page_id} is not vaild id"

    return message



if __name__ == '__main__':

    app.run(debug=True, port=8081)


