from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])
def dropdown():
    names = ['Wizard', 'Elf', 'Dwarf', 'Knight', 'Hobbit']
    return render_template('test.html', Names=names)

if __name__ == "__main__":
    app.run()