import os
import base64

from flask import Flask, request
from model import Message 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        m = Message(content=request.form['content'])
        m.save()

    body = """
<html>
<body>
<h1>Class Message Board</h1>
<h2>Contribute to the Knowledge of Others</h2>
<form method="POST">
    <textarea name="content"></textarea>
    <input type="submit" value="Submit">
</form>

<h2>Wisdom From Your Fellow Classmates</h2>
"""
    
    for m in Message.select():
        body += """
<div class="message">
{}
</div>
""".format(m.content.replace('<','&lt').replace('>','&gt'))

    return body 


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

