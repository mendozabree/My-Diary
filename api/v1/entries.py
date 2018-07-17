from api.v1 import app
from flask import jsonify

# Dummy entries
my_entries = [{
    'entry_id': '1',
    'entry_date': '7 June 2018',
    'entry_time': '18 15',
    'title': 'Exhausted',
    'content': 'Today am spent!'
}, {
    'entry_id': '2',
    'entry_date': '8 June 2018',
    'entry_time': '18 15',
    'title': 'Excitement',
    'content': 'My first day at work!'
}]


@app.route('/api/v1/entries', methods=['GET'])
def get_all_entries():
    return jsonify({'My entries': my_entries})
