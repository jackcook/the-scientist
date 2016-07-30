import json
import syntaxnet

root = syntaxnet.pass_sentence("My name is Jack.")
print json.dumps(root, indent=2)
