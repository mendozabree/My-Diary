from api.v1 import app
from flask import jsonify, request, make_response

# Dummy entries
my_entries = [{
    'entry_id': 1,
    'entry_date': '7 June 2018',
    'entry_time': '18 15',
    'title': 'Exhausted',
    'content': 'Today am spent!'
}, {
    'entry_id': 2,
    'entry_date': '8 June 2018',
    'entry_time': '18 15',
    'title': 'Excitement',
    'content': 'My first day at work!'
}]


@app.route('/api/v1/entries', methods=['GET'])
def get_all_entries():
    return jsonify({'My entries': my_entries})


@app.route('/api/v1/entries/<int:entry_id>', methods=['PUT'])
def modify_entry(entry_id):
    updating_data = request.get_json()
    my_entry = [entry for entry in my_entries if entry['entry_id'] == entry_id]
    if my_entry:
        if 'title' in updating_data:
            my_entry[0]['title'] = updating_data['title']
        if 'content' in updating_data:
            my_entry[0]['content'] = updating_data['content']
        return make_response("Entry has been updated", 200)
