from flask import Flask, render_template
import json

app = Flask(__name__)

def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

@app.route('/')
def home():
    texts = load_json("static/text_content/text.json")
    comments_data = load_json("static/text_content/coments.json")
    cards = load_json("static/text_content/cards.json")
    results_data = load_json("static/text_content/results.json")
    return render_template("index.html",
                           texts=texts, comments=comments_data, cards=cards,
                           results=results_data)

@app.route('/pol')
def gog():
    return "Політика конфіденційності Публічна офертаIMPORTANT: Do not enter your name and email until you have read the Legal Disclaimer. We are not able to make any guarantees and we will not make any guarantees about your ability to generate results with our ideas, information, tools and resources, or strategies. You should know that all products and services by our company are for educational and informational purposes only. Nothing on this website, or any of our websites, or any of our content or curriculum is a implication, promise, or guarantee of results. Use caution and always consult your accountant, lawyer or professional adviser before acting on this or any information related to a lifestyle change, your business and finances. You are responsible for your decisions, actions and results. By registering on this website you agree not to attempt to hold us liable for your decisions, actions or results, at any time, under any circumstance.ВАЖЛИВО: не вводьте свою контактну інформацію, доки не прочитаєте legal disclaimer. Ми не даємо жодних гарантій, що ви досягнете якихось результатів за допомогою наших інструментів, стратегій або інформації. Всі продукти і сервіси компанії призначені для освітніх цілей. Жодна інформація на цьому сайті або будь-яких інших сайтах компанії не гарантує і не обіцяє отримання результатів. Ви несете відповідальність за свої дії і результати. Реєструючись на даному сайті, ви знімаєте з нас відповідальність за ваші дії та результати."

if __name__ == '__main__':
    app.run(debug=True)