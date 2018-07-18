from api.v1 import app
from flask import jsonify, request, make_response
from api.v1.my_classes import Entry

# Dummy entries
my_entries = [
    {
        'entry_id': 1,
        'entry_date': '7 June 2018',
        'entry_time': '18 15',
        'title': 'Exhausted',
        'content': 'Today am spent!'
    },
    {
        'entry_id': 2,
        'entry_date': '8 June 2018',
        'entry_time': '18 15',
        'title': 'Excitement',
        'content': 'My first day at work!'
    }
            ]

my_entry = Entry()
my_entry.create_new_entry({
    'entry_id': 1,
    'entry_date': '7 June 2018',
    'entry_time': '18 15',
    'title': 'Exhausted',
    'content': 'Today am worn out!'
})
my_entry.create_new_entry({
    'entry_id': 2,
    'entry_date': '8 June 2018',
    'entry_time': '18 15',
    'title': 'Excitement',
    'content': 'My first day at work!'
})

entries = my_entry.my_entries


@app.route('/api/v1/entries', methods=['GET'])
def get_all_entries():
    return jsonify({'My entries': entries})


@app.route('/api/v1/entries/<int:entry_id>', methods=['GET'])
def get_specific_entry(entry_id):
    res = my_entry.get_specific_entry(entry_id=entry_id)
    return jsonify({"response": res})


@app.route('/api/v1/entries', methods=['POST'])
def new_entry():
    response = request.get_json()
    my_entry.create_new_entry(response)
    return make_response("Entry added")


@app.route('/api/v1/entries/<int:entry_id>', methods=['PUT'])
def modify_entry(entry_id):
    updating_data = request.get_json()
    response = my_entry.modify_entry(entry_id=entry_id, new_data=updating_data)
    return jsonify({"Message": response})
