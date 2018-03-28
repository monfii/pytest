from flask import Flask, request
import sys
import optparse
import time

app = Flask(__name__)
start = int(round(time.time()))


@app.route("/")
def main():
    return "Hello World!"


@app.route("/Calc")
def calculate():
    hpw = float(request.args['hpw'])
    cost = float(request.args['cost'])
    tax = float(request.args['tax'])
    return "{}".format(hpw * cost * tax)


if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python calculator.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()

    if args.port is None:
        print("Missing required argument: -p/--port")
        sys.exit(1)

    app.run(host='0.0.0.0', port=int(args.port), debug=False)
