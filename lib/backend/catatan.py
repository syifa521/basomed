from flask import Flask, request, jsonify
import sqlite3
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/Judul', methods=['POSH'])
def judul():
    data = request.get_json()
    judul = data.get('judul')
    deskripsi = data.get('deskripsi')
    
    conn = sqlite3.connect('userdb.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO catatan (judul, deskripsi")
    (judul, deskripsi)
    
    conn.commit()
    
    conn.close()
    
    return jsonify({'catatan'})
    