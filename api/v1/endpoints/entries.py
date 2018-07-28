""" This is the entries module.

This module has the endpoints used for entries.
It utilises the my_classes module to get return values
"""

from flask import jsonify, request, make_response

from api import app
from api.v1.my_classes import Entry


my_entry = Entry()
my_entries = []


@app.route('/api/v1/entries', methods=['GET'])
def get_all_entries():
    """use http get method to return all diary entries"""

    entries = Entry.get_all_entries(entries=my_entries)

    return make_response(jsonify({'My entries': entries}),
                         200)


@app.route('/api/v1/entries/<int:entry_id>', methods=['GET'])
def get_specific_entry(entry_id):
    """
    use http get method to return specific entry based on entry_id
    :param entry_id:
    :return:
    """

    res = Entry.get_specific_entry(entry_id=entry_id,
                                   entries=my_entries)

    return make_response(jsonify({"response": res['message']}),
                         res['code'])


@app.route('/api/v1/entries', methods=['POST'])
def new_entry():
    """use http post method to create a new entry"""

    response = request.get_json()

    res = my_entry.create_new_entry(entry_data=response,
                                    entries=my_entries)

    return make_response(jsonify({'Message': res['message']}),
                         res['code'])


@app.route('/api/v1/entries/<int:entry_id>', methods=['PUT'])
def modify_entry(entry_id):
    """use http put method to update an entry based on specified entry_id"""

    updating_data = request.get_json()

    response = Entry.modify_entry(
                                    entry_id=entry_id,
                                    new_data=updating_data,
                                    entries=my_entries
                                 )

    return make_response(jsonify({'Message': response['message']}),
                         response['code'])
