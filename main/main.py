from flask import Flask, request
import requests
import sys
import optparse
import time

app = Flask(__name__)
start = int(round(time.time()))


@app.route("/")
def main():
    hpw = request.args['hpw']
    cost = request.args['cost']
    tax = request.args['tax']

    r = requests.get('http://calculator:7000/Calc?hpw={0}&cost={1}&tax={2}'.format(hpw, cost, tax))

    return "Your result is {}".format(r.text)


if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python main.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()

    if args.port is None:
        print("Missing required argument: -p/--port")
        sys.exit(1)

    app.run(host='0.0.0.0', port=int(args.port), debug=False)
