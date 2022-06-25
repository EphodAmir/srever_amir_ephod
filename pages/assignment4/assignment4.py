from flask import Blueprint, render_template, redirect, request,jsonify
import mysql.connector
import requests

assignment4 = Blueprint(
    'assignment4',
    __name__,
    static_folder = 'static',
    static_url_path= '/assignment4',
    template_folder = 'templates'
)

@assignment4.route('/assignment4')
def index():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment4.html', users=users_list)

def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root1234',
                                         database='assignment_4_db')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)


    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

# -------------------- INSERT --------------------- #
@assignment4.route('/insert_user', methods=['POST'])
def insert_user():
    name = request.form['name']
    email = request.form['email']
    print(f'{name} {email}')
    query = "INSERT INTO users(name, email) VALUES ('%s', '%s')" % (name, email)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment4')


# -------------------- DELETE --------------------- #
@assignment4.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['user_id']
    query = "DELETE FROM users WHERE id='%s';" % user_id
    print(query)
    interact_db(query, query_type='commit')
    return redirect('/assignment4')

# -------------------- UPDATE --------------------- #
@assignment4.route('/update_user', methods=['POST'])
def update_user_func():
    name = request.form['name']
    email = request.form['email']
    query = "UPDATE users SET email = '%s' WHERE name='%s';" % (email, name)
    print(query)
    interact_db(query, query_type='commit')
    return redirect('/assignment4')

@assignment4.route('/assignment4/users')
def users():
    query = 'select * from users'
    users_json = jsonify((interact_db(query, query_type='fetch')))
    return (users_json)

@assignment4.route('/assignment4/Backend')
def extract_user():
    user_id = request.args.get('user_id')
    result = requests.get(f'https://reqres.in/api/users/{user_id}')
    result_json = result.json()
    return render_template('assignment4.html', users_BE= result_json)



@assignment4.route('/assignment4/restapi_users')
def users_api():
    user_id = request.args['user_id']
    if user_id =="":
        query = "select * from users limit 1"
        default_user = interact_db(query, query_type='fetch')
        return jsonify (default_user)
    return redirect(f'/assignment4/restapi_users/{user_id}')


@assignment4.route('/assignment4/restapi_users/<user_id>')
def show_user_json(user_id):
    query = "select * from users"
    users_list = interact_db(query, query_type='fetch')
    for user in users_list:
        if user_id == str(user.id):
            return jsonify(user)
    return jsonify("User not found, try different id")