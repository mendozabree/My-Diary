class Entry:
    def __init__(self):
        self.number_of_entries = 0
        self.my_entries = []

    def create_new_entry(self, entry_data):
        entry_data['entry_id'] = self.number_of_entries = self.number_of_entries + 1
        self.my_entries.append(entry_data)
        return self.my_entries

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
