from flask import Flask, render_template, request, send_file, abort, jsonify
import json
from datetime import datetime

app = Flask(__name__)

def update_stats_file(count_type="visits"):
    today = datetime.now().strftime("%d.%m.%Y")
    stats_path = "stats.json"

    try:
        with open(stats_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    if today not in data:
        data[today] = {"visits": 0, "button_clicks": 0}

    data[today][count_type] += 1

    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


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
    update_stats_file()
    return render_template("index.html",
                           texts=texts, comments=comments_data, lang=lang)
@app.route('/privacy')
def privacy():
    return send_file('pdf/p.pdf')

@app.route('/offer')
def offer():
    return send_file('pdf/p.pdf')#

@app.route('/stats')
def show_stats():
    access_key = request.args.get('key')
    if access_key != "gfgsenjavnw5y8wuvchbq3748uifohygq8u34ifhbqu3iurfncuq834yfiu":
        abort(403)  # Access Denied

    try:
        with open("stats.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    return data  # або jsonify(data), якщо хочеш гарний JSON

@app.route('/log_click', methods=['POST'])
def log_click():
    update_stats_file("button_clicks")
    return jsonify({"message": "Click recorded"}), 200

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=80)
