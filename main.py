from flask import Flask, render_template, request
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
    texts = load_json("static/text_content/locales/ua.json")
    return render_template('privacy.html', texts=texts)

@app.route('/offer')
def offer():
    texts = load_json("static/text_content/locales/ua.json")
    return render_template('offer.html', texts=texts)


if __name__ == '__main__':
    app.run(debug=True)