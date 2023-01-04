import json

from flask import Flask



app = Flask(__name__)
app.config["SECRET_KEY"] = "KASDLFJKASFA1283912jkdas1293jaDFSAFSAfssSFsF89saf87s78SA"


with open ("d:/Projects/jump-point-search/config.json") as f:
    config_info = json.load(f)

app.config.update(config_info)

from web import routes