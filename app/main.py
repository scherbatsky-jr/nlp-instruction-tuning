import os
from flask import Flask, render_template, request, jsonify
from flask_assets import Environment, Bundle
from lib.generator import TextGenerator

app = Flask(__name__)
assets = Environment(app)

scss = Bundle('styles.scss', filters='scss', output='gen/main.css')
assets.register('scss_all', scss)

text_generator = TextGenerator()

@app.route('/', methods=['GET','POST'])
def index():
    result = ''
    prompt = ''
    instruction = ''
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        instruction = request.form.get('instruction')
        output = text_generator.get_result(instruction, prompt)
        result = output[0]['generated_text'].split("### Response:\n")[-1]
    return render_template('index.html', prompt=prompt, instruction=instruction, result = result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
