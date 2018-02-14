#!/bin/env python
# coding: utf-8
import json
from bottle import route, run, request, HTTPResponse, template, static_file
import RPi.GPIO
import atexit

GPIO_PORT_LED_0 = 26

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
def root():
    return template("index")

# curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"num":"0", "onoff":$
@route('/setLed', method='POST')
def setLedEntry():
@route('/setLed', method='POST')
def setLedEntry():
    var = request.json
    # print (var)
    if (var["num"] == "0" ):
        RPi.GPIO.output(GPIO_PORT_LED_0, var["onoff"])
    retBody = {"ret": "ok"}
    r = HTTPResponse(status=200, body=retBody)
    r.set_header('Content-Type', 'application/json')
    return r

def main():
    print("Initialize port")
    RPi.GPIO.setmode(RPi.GPIO.BCM)
    RPi.GPIO.setup(GPIO_PORT_LED_0, RPi.GPIO.OUT)
    RPi.GPIO.output(GPIO_PORT_LED_0, 0)
    print('Server Start')
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)
    # run(host='0.0.0.0', port=8080, debug=False, reloader=False)
    # run(host='0.0.0.0', port=8080, debug=False, reloader=False)

def atExit():
print("atExit")
RPi.GPIO.cleanup()

if __name__ == '__main__':
atexit.register(atExit)
main()
