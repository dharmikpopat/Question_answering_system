from flask import Flask, jsonify, render_template, request
from deeppavlov import build_model, configs
model = build_model(configs.squad.squad, download=False)

app = Flask(__name__)

@app.route('/_findanswer')
def findanswer():
    a = request.args.get('a', '', type=str)
    b = request.args.get('b', '', type=str)
    content = [a]
    ques = [b]
    main = model(content, ques)
    return jsonify(result= main[0])

@app.route('/')
def ice():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug = True)
