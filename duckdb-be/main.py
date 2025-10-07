import user_data
import card_data
import duckdb_data
'''
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:4200"])

@app.route("/query", methods=["POST"])
def run_query():
    data = request.get_json()
    sql = data.get("sql")
    if not sql:
        return jsonify({"error": "No SQL query provided"}), 400

    try:
        result = duckdb_data.connection.execute(sql).fetchall()
        columns = [desc[0] for desc in duckdb_data.connection.description]
        return jsonify({"columns": columns, "rows": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
'''