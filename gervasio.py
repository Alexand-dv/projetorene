from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'


# Função para criar a tabela no banco de dados
def create_table():
    conn = sqlite3.connect('spaceex.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT UNIQUE,
                 password TEXT, birth_date TEXT, mother_name TEXT)''')
    conn.commit()
    conn.close()


create_table()


# Rota para a página inicial (cadastro)
@app.route('/')
def index():
    return render_template('index.html')


# Rota para adicionar um usuário
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    birth_date = request.form['birth_date']
    mother_name = request.form['mother_name']

    conn = sqlite3.connect('spaceex.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (name, email, password, birth_date, mother_name) VALUES (?, ?, ?, ?, ?)",
                  (name, email, password, birth_date, mother_name))
        conn.commit()
        conn.close()
        return redirect(url_for('success'))
    except sqlite3.IntegrityError:
        conn.close()
        return render_template('index.html', message='E-mail já cadastrado. Tente outro.')


# Rota para a página de sucesso
@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
