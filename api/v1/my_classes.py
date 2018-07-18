class Entry:
    def __init__(self):
        self.number_of_entries = 0
        self.my_entries = []

    def create_new_entry(self, entry_data):
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
            self.my_entries.append(entry_data)
            return "Your memory has been saved"
        else:
            return message

    def get_specific_entry(self, entry_id):
        my_entry = [entry for entry in self.my_entries if entry['entry_id'] == entry_id]
        if not my_entry:
            return "Entry not found"
        else:
            return my_entry

    def modify_entry(self, entry_id, new_data):
        messages = []
        modify_model = [*new_data.keys()]
        current_entry = [entry for entry in self.my_entries if entry['entry_id'] == entry_id]
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
