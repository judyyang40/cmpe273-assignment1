from flask import Flask
from github import Github
import json
import yaml

app = Flask(__name__)
g = Github("judyyang40", "jy820821")
user = g.get_user()
repo = user.get_repo("cmpe273-assignment1")

@app.route("/v1/<filename>")
def hello2(filename):
	name, extension = filename.split(".")
	if extension == "yml":
		if name == "dev-config":
			return repo.get_contents("dev-config.yml").content.decode('base64')
		elif name == "test-config":
			return repo.get_contents("test-config.yml").content.decode('base64')
		else:
			return "error: bad file name"
	elif extension == "json":
		if name == "dev-config":
			y = repo.get_contents("dev-config.yml").content.decode('base64')
			return json.dumps(yaml.load(y))
		elif name == "test-config":
			y = repo.get_contents("test-config.yml").content.decode('base64')
			return json.dumps(yaml.load(y))
		else:
			return "error: bad file name"
	else:
		return "error: invalid file extension"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')