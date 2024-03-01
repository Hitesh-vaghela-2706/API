from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = Flask(__name__)

# Database connection parameters
DB_HOST = "localhost"
DB_NAME = "Test_db"
DB_USER = "postgres"
DB_PASS = "postgres"

# Database connection
def get_db_connection():
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS, cursor_factory=RealDictCursor,port="5432")
    return conn

@app.route('/')
def index():
    return "Employee Management API"

@app.route('/employees', methods=['POST'])
def add_employee():
    conn = get_db_connection()
    cur = conn.cursor()
    employee = request.json
    try:
        query = f"INSERT INTO employee(name, email, department) VALUES ('{employee['name']}', '{employee['email']}', '{employee['department']}')"
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(employee), 201
    except psycopg2.Error as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 400


@app.route('/employees', methods=['GET'])
def get_employees():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM employee;')
    employees = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(employees)

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM employee WHERE id = %s;', (str(id),))
    employee = cur.fetchone()
    cur.close()
    conn.close()
    if employee:
        return jsonify(employee)
    else:
        return jsonify({"error": "Employee not found"}), 404

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    conn = get_db_connection()
    cur = conn.cursor()
    employee = request.json
    cur.execute('UPDATE employee SET name = %s, email = %s, department = %s WHERE id = %s',
                (employee['name'], employee['email'], employee['department'], str(id)))
    conn.commit()
    updated_rows = cur.rowcount
    cur.close()
    conn.close()
    if updated_rows == 0:
        return jsonify({"error": "Employee not found"}), 404
    else:
        return jsonify(employee)

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM employee WHERE id = %s;', (str(id),))
    conn.commit()
    deleted_rows = cur.rowcount
    cur.close()
    conn.close()
    if deleted_rows == 0:
        return jsonify({"error": "Employee not found"}), 404
    else:
        return jsonify({"message": "Employee deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)


#     {
#     "name" : "hitesh",
#     "email" : "vhitesh927@gmail.com",
#     "department" : "software"
# }