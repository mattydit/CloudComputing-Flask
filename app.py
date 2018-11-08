from flask import Flask
import json

app = Flask(__name__)


@app.route('/status')
def status():
    values = {}

    values["hostname"] = "linuxVM2"
    values["ip_address"] = "137.135.123.165"
    values["cpus"] = "1"
    values["memory"] = "1GB"

    return json.dumps(values, ensure_ascii=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
