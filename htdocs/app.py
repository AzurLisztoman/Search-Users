from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
users = [
   {"id": 1, "name": "Иван Иванов", "avatarUrl": "https://i.pinimg.com/736x/6f/38/80/6f3880251fba7c6b28c8fde4908f298c.jpg"},
   {"id": 2, "name": "Анна Петрова", "avatarUrl": "https://example.com/avatar2.jpg"},
   {"id": 3, "name": "Сергей Сидоров", "avatarUrl": "https://example.com/avatar3.jpg"}
 ]
results = users
@app.route('/')
def index():
    return render_template('index.html', data=users)

# Endpoint для получения списка пользователей
@app.route('/api/users', methods=['POST'])
def get_users():
    searchTerm = request.form.get('searchTerm')
    if searchTerm:
        # Поиск пользователей, имена которых содержат searchTerm
        results = [user for user in users if searchTerm.lower() in user['name'].lower()]
        return render_template('templ.html', data=results)

    else:
        # Возврат всех пользователей
        return render_template('templ.html', data=users)
    
    
if __name__ == '__main__':
    app.run(debug=True)

