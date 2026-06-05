class Person:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def get_contact_info(self):
        return "Email: {}, Phone: {}, Address: {}".format(self.email, self.phone, self.address)
    
    def __str__(self):
        return "Name: {}, Contact Info: {}".format(self.name, self.get_contact_info())