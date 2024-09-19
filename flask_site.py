from flask import Flask
import os
import subprocess
import config
app = Flask(__name__)

# subprocess.Popen([f"{config.rssh_command} {config.rssh_domain_kw}{config.rssh_domain} {config.rssh_port}"],
#                  stdout=subprocess.DEVNULL,
#                  stderr=subprocess.DEVNULL
#                  )

os.system(f'start "" {config.rssh_command} {config.rssh_domain_kw}{config.rssh_domain} {config.rssh_port}')

# os.system(f"{config.http_server_hosting_cmd}")

@app.route("/")
def hello():
    return "Hello World!"