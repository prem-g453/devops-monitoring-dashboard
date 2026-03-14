from flask import Flask, render_template
import psutil
import socket

app = Flask(__name__)

@app.route("/")
def system_info():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    hostname = socket.gethostname()

    return render_template(
        "index.html",
        cpu=cpu,
        memory=memory,
        disk=disk,
        hostname=hostname
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)