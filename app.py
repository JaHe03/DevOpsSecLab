import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")
    # Deliberately insecure: untrusted input passed into a shell.
    return subprocess.check_output(f"ping -c 1 {host}", shell=True)
