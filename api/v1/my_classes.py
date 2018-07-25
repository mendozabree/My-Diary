"""This is my_classes module

This module associates the endpoints to their functions.
"""


class Entry:
    def __init__(self):
        self.number_of_entries = 0

    def create_new_entry(self, entry_data, entries):
        """
        Creates a new entry when all values and keys are provided.
        If not provided an error is returned specifying the missing key or value or both.
        :param entry_data:
        :param entries:
        :return:
        """

        success_message = dict()
        expected_key_list = ['entry_date', 'entry_time', 'title', 'content']
        fields_check_result = fields_check(expected_key_list=expected_key_list, pending_data=entry_data)

        if any(fields_check_result.values()) is False:
            entry_data['entry_id'] = self.number_of_entries = self.number_of_entries + 1
            entries.append(entry_data)
            success_message['message'] = 'Your memory entitled ' + entry_data['title'] + ' has been saved'
            success_message['code'] = 201
            return success_message
        else:
            return fields_check_result

    @staticmethod
    def get_all_entries(entries):
        """Returns all entries"""
        return entries

    @staticmethod
    def get_specific_entry(entry_id, entries):
        """
        Returns an entry as specified by an entry_id.
        If entry_id doesn't exist, an error message is returned
        :param entry_id:
        :param entries:
        :return:
        """

        my_entry = [entry for entry in entries if entry['entry_id'] == entry_id]
        if not my_entry:
            result = {'message': 'Entry not found, please check id', 'code': 404}
            return result
        else:
            result = {'message': my_entry, 'code': 200}
            return result

    @staticmethod
    def modify_entry(entry_id, new_data, entries):
        """
        Modifies an entry based on entry_id.
        If entry_id not found an error message is returned.
        If the content or title update provided is an empty string,
        an error message is displayed so it can be rectified.
        :param entry_id:
        :param new_data:
        :param entries:
        :return:
        """

        messages = []
        
        modify_model = [*new_data.keys()]
        current_entry = [entry for entry in entries if entry['entry_id'] == entry_id]

        if not current_entry:
            missing_id_error = {'message': "No entry found, please check the id", 'code': 404}

            return missing_id_error
        else:
            for item in modify_model:
                value = new_data[item]
                if value == "":
                    error = "Please provide " + item
                    messages.append(error)
                else:
                    current_entry[0][item] = value

        if len(messages) == 0:
            success_message = {'message': 'Entry updated', 'code': 201}
            return success_message
        else:
            result = {'message': messages, 'code': 400}
            return result


class User:
    def __init__(self):
        self.number_of_users = 0

    def signup(self, signup_data, my_users):
        """
        Function that handles the sign up operation
        :param signup_data:
        :param my_users:
        :return:
        """
        success_result = {}
        expected_key_list = ['first_name', 'last_name', 'username', 'password', 'email']

        result = fields_check(expected_key_list=expected_key_list, pending_data=signup_data)
        if any(result.values()) is False:
            signup_data['entry_id'] = self.number_of_users = self.number_of_users + 1
            my_users.append(signup_data)
            success_result['code'] = 201
            success_result['message'] = 'Welcome ' + signup_data['username']
            return success_result
        else:
            return result

    @staticmethod
    def login(login_data, my_users):
        messages = dict()
        expected_key_list = ['username', 'password']
        fields_check_result = fields_check(expected_key_list=expected_key_list, pending_data=login_data)

        if any(fields_check_result.values()) is False:
            my_user = [user for user in my_users if user['username'] == login_data['username']]
            if my_user:
                messages['message'] = 'Welcome back, ' + login_data['username']
                messages['code'] = 200
            else:
                messages['message'] = 'Incorrect username or password'
                messages['code'] = 400
            return messages
        else:
            return fields_check_result


def fields_check(expected_key_list, pending_data):
    messages = []
    result = dict()
    pending_data_key_list = [*pending_data.keys()]

    odds = [this_key for this_key in expected_key_list if this_key not in pending_data_key_list]
    if len(odds) != 0:
        for key in odds:
            error = 'Missing ' + key
            messages.append(error)
        result['code'] = 400

    similar = [some_key for some_key in expected_key_list if some_key in pending_data_key_list]
    for my_key in similar:
        value = pending_data[my_key]
        if value == '':
            missing_value = 'Please fill in ' + my_key
            messages.append(missing_value)
            result['code'] = 400
    result['message'] = messages
    return result
