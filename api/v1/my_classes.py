class Entry:
    def __init__(self):
        self.number_of_entries = 0
        self.my_entries = []

    def create_new_entry(self, entry_data):
        message = []
        expected_key_list = ['entry_date', 'entry_time', 'title', 'content']
        entry_data_key_list = [*entry_data.keys()]

        odds = [x for x in expected_key_list if x not in entry_data_key_list]
        if len(odds) != 0:
            for key in odds:
                error = 'Missing ' + key
                message.append(error)

        similar = [y for y in expected_key_list if y in entry_data_key_list]
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
        my_entry = [entry for entry in self.my_entries if entry['entry_id'] == entry_id]
        if not my_entry:
            error = "Entry not found"
            messages.append(error)
        else:
            if my_entry[0]['title'] != new_data['title']:
                my_entry[0]['title'] = new_data['title']
                message1 = "Title has been updated"
                messages.append(message1)
            if my_entry[0]['content'] != new_data['content']:
                my_entry[0]['content'] = new_data['content']
                message2 = "Content has been updated"
                messages.append(message2)
        return messages
