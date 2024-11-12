from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)
users = [
   {"id": 1, "name": "Иван Иванов", "avatarUrl": "https://i.pinimg.com/736x/6f/38/80/6f3880251fba7c6b28c8fde4908f298c.jpg"},
   {"id": 2, "name": "Анна Петрова", "avatarUrl": "https://i.pinimg.com/564x/f0/fc/31/f0fc31c3e34861b4bbb31317ed69a059.jpg"},
   {"id": 3, "name": "Сергей Сидоров", "avatarUrl": "https://i.pinimg.com/736x/2f/c4/6a/2fc46a8e06875cfd7ae173bb34a94c91.jpg"},
   {"id": 4, "name": "Серафима Зайцева", "avatarUrl": "https://i.pinimg.com/236x/58/ae/46/58ae4645701586376fc10aa8123f92c4.jpg"},
   {"id": 5, "name": "Алёна Васильева", "avatarUrl": "https://i.pinimg.com/564x/49/f9/20/49f920517760f32dad876052ad0b39ef.jpg"},
   {"id": 6, "name": "Амира Краснова", "avatarUrl": "https://i.pinimg.com/236x/b5/39/4f/b5394f5455580cb09b6efa6df8be8272.jpg"},
   {"id": 7, "name": "Ярослав Гришин", "avatarUrl": "https://i.pinimg.com/736x/e8/26/84/e826848f3b65332b80fc3c6fecf34458.jpg"},
   {"id": 8, "name": "Степан Крылов", "avatarUrl": "https://i.pinimg.com/236x/76/0d/8b/760d8b33a467ad577847e2aa287fc741.jpg"},
   {"id": 9, "name": "Сергей Сидоров", "avatarUrl": "https://i.pinimg.com/736x/81/09/1d/81091d9e000026bafee4928603f7a4a6.jpg"},
   {"id": 10, "name": "Тимофей Ларионов", "avatarUrl": "https://i.pinimg.com/236x/3e/0d/2c/3e0d2c74dfac1f34ba11307e6df8431f.jpg"},
   {"id":11, "name": "Таисия Полякова", "avatarUrl": "https://i.pinimg.com/236x/2b/a1/e2/2ba1e244631c0f5568a9479d20884792.jpg"},
   {"id": 12, "name": "Матвей Волков", "avatarUrl": "https://i.pinimg.com/236x/2b/e0/96/2be096ae9722b1c2bcc204b7cf3037b2.jpg"},
   {"id": 13, "name": "Александр Лукин", "avatarUrl": "https://i.pinimg.com/474x/9f/22/d6/9f22d6e7435ec067a4bd18bfc3338dd1.jpg"},
   {"id": 14, "name": "Евгения Фролова", "avatarUrl": "https://i.pinimg.com/236x/09/fe/87/09fe871bbc8a2ca63c31c70382d9d3e6.jpg"},
   {"id": 15, "name": "Даниил Демидов", "avatarUrl": "https://i.pinimg.com/236x/2f/12/9f/2f129f1765ae13339fe75778799d611a.jpg"},
   {"id": 16, "name": "Максим Козлов", "avatarUrl": "https://i.pinimg.com/564x/e2/96/97/e29697f9bc4c829850f6c4e778b5174b.jpg"},
   {"id": 17, "name": "Эмин Григорьев", "avatarUrl": "https://i.pinimg.com/236x/a5/47/1b/a5471b26ac4c79df47edbde295acf27e.jpg"},
   {"id": 18, "name": "Дарья Щербакова", "avatarUrl": "https://i.pinimg.com/736x/73/0f/3a/730f3a6751ef3e205f43ef66a3469159.jpg"}
 ]
results = users
@app.route('/')
def index():
    return render_template('index.html', data=users)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

# Endpoint для получения списка пользователей
@app.route('/api/users', methods=['POST'])
def get_users():
    searchTerm = request.form.get('searchTerm')
    if searchTerm:
        # Поиск пользователей, имена которых содержат searchTerm
        results = [user for user in users if searchTerm.lower() in user['name'].lower()]
        # return render_template('index.html', data=results)
        # return results
        return render_template('templ.html', data=results)

    else:
        # Возврат всех пользователей
        return render_template('templ.html', data=users)
    
app.config['STATIC_FOLDER'] = 'templates'
if __name__ == '__main__':
    app.run(debug=True)

