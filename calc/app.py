# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def add_route():
    """Add a and b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)
    return str(result)


@app.route('/sub')
def sub_route():
    """Subtract a and b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)
    return str(result)


@app.route('/mult')
def mult_route():
    """Multiply a and b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)
    return str(result)


@app.route('/div')
def div_route():
    """Divide a and b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)
    return str(result)


OPERATORS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}


@app.route('/math/<oper>')
def do_math(oper):
    """Do math on a and b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = OPERATORS[oper](a, b)
    return str(result)
