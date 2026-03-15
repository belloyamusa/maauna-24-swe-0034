from datetime import datetime

class Business:
    def __init__(self, name, location, category):
        self.name = name
        self.location = location
        self.category = category
        self.created_at = datetime.now()

    def display(self):
        return f"{self.name} - {self.category} ({self.location})"
