from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)


# Configuración de la base de datos
def create_connection():
    connection = None
    try:
        # Establecer la conexión con la base de datos
        connection = mysql.connector.connect(
            host='195.179.238.58',  # por ejemplo, 'localhost'
            database='u927419088_testing_sql',
            user='u927419088_admin',
            password='#Admin12345#'
        )
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")

    return connection


# Ruta para obtener todos los cursos
@app.route('/cursos', methods=['GET'])
def obtener_cursos():
    try:
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM curso")
        cursos = cursor.fetchall()
        return jsonify(cursos)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)})
    finally:
        cursor.close()
        connection.close()


# Ruta para obtener un curso específico por ID
@app.route('/cursos/<int:curso_id>', methods=['GET'])
def obtener_curso_por_id(curso_id):
    try:
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM curso WHERE idCurso = %s", (curso_id,))
        curso = cursor.fetchone()

        if curso:
            return jsonify(curso)
        else:
            return jsonify({"error": "Curso no encontrado"}), 404

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)})
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    app.run(debug=True)
