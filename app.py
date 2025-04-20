from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = 'data.json'

# Yardımcı: Veriyi oku
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Yardımcı: Veriyi kaydet
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# Tüm girişleri listele
@app.route('/log', methods=['GET'])
def log():
    data = load_data()
    return render_template('log.html', data=data)

# Belirli bir kaydın detay sayfası
@app.route('/log/<int:entry_id>', methods=['GET', 'POST'])
def log_detail(entry_id):
    data = load_data()
    if entry_id >= len(data):
        return "Kayıt bulunamadı", 404

    entry = data[entry_id]

    if 'history' not in entry:
        entry['history'] = []

    if request.method == 'POST':
        new_note = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "note": request.form.get("note"),
            "water_amount": request.form.get("water_amount"),
            "humidity": request.form.get("humidity")
        }
        entry['history'].append(new_note)
        data[entry_id] = entry
        save_data(data)
        return redirect(url_for('log_detail', entry_id=entry_id))

    return render_template('detail.html', entry=entry, entry_id=entry_id)



if __name__ == '__main__':
    app.run(debug=True)
