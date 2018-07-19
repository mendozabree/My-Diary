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

        message = []
        expected_key_list = ['entry_date', 'entry_time', 'title', 'content']
        entry_data_key_list = [*entry_data.keys()]

        odds = [this_key for this_key in expected_key_list if this_key not in entry_data_key_list]
        if len(odds) != 0:
            for key in odds:
                error = 'Missing ' + key
                message.append(error)

        similar = [some_key for some_key in expected_key_list if some_key in entry_data_key_list]
        for my_key in similar:
            value = entry_data[my_key]
            if value == '':
                missing_value = 'Enter value for ' + my_key
                message.append(missing_value)

        if len(message) == 0:
            entry_data['entry_id'] = self.number_of_entries = self.number_of_entries + 1
            entries.append(entry_data)
            return "Your memory has been saved"
        else:
            return message

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
            return "Entry not found"
        else:
            return my_entry

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
            entry_id_error = "No entry, please check the id"
            messages.append(entry_id_error)
        else:
            for item in modify_model:
                value = new_data[item]
                if value == "":
                    error = "Please provide " + item
                    messages.append(error)
                else:
                    current_entry[0][item] = value

        if len(messages) == 0:
            return "Entry updated"
        else:
            return messages
