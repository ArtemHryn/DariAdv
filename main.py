from flask import Flask, render_template, request, send_file
import json

app = Flask(__name__)

def load_translations(lang):
    with open(f'static/text_content/locales/{lang}.json', encoding='utf-8') as f:
        return json.load(f)

def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

@app.route('/')
def home():
    lang = request.args.get('lang', 'ua')
    texts = load_translations(lang)
    comments_data = load_json("static/text_content/coments.json")
    return render_template("index.html",
                           texts=texts, comments=comments_data, lang=lang)
@app.route('/privacy')
def privacy():
    return send_file('p.pdf')

@app.route('/offer')
def offer():
    return send_file('pdf/p.pdf')


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=80)
