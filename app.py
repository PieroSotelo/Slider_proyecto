from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    images = [
        url_for('static', filename='images/img1.png'),
        url_for('static', filename='images/img2.png'),
        url_for('static', filename='images/img3.png'),
    ]
    prev_icon = url_for('static', filename='icons/prev.svg')
    next_icon = url_for('static', filename='icons/next.svg')
    return render_template('index.html', images=images, prev_icon=prev_icon, next_icon=next_icon)

if __name__ == '__main__':
    app.run(debug=True)
