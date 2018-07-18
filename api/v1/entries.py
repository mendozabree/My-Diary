from api.v1 import app
from flask import jsonify, make_response, request

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


@app.route('/api/v1/entries/<int:entry_id>', methods=['GET'])
def get_specific_entry(entry_id):
    my_entry = [entry for entry in my_entries if entry['entry_id'] == entry_id]
    if my_entry:
        return jsonify({'Your entry':my_entry[0]})
    else:
        return jsonify({'Message': 'No entry found!'})


@app.route('/api/v1/entries', methods=['POST'])
def new_entry():
    response = request.get_json()
    response['entry_id'] = len(my_entries) + 1
    my_entries.append(response)
    return make_response('Entry was successful', 201)
