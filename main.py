# Title: Address Book
# Author: Joseph Fox
# Email: josephtfox@gmail.com

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QListWidget, QPushButton, QWidget, QLabel, QLineEdit, QHBoxLayout

class AddressBookApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.address_book = AddressBook()
        self.filler_nested_list = self.address_book.contacts

        self.setWindowTitle("Address Book")
        self.setGeometry(700, 700, 900, 900)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.init_ui()

    def init_ui(self):
        # List View
        self.contact_list = QListWidget(self)

        # Buttons
        self.add_button = QPushButton("Add Contact", self)
        self.delete_button = QPushButton("Delete Contact", self)
        self.clear_button = QPushButton("Clear", self)

        # Form
        self.first_name_label = QLabel("First Name:")
        self.first_name_input = QLineEdit(self)

        self.last_name_label = QLabel("Last Name:")
        self.last_name_input = QLineEdit(self)

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit(self)

        self.phone_label = QLabel("Phone:")
        self.phone_input = QLineEdit(self)

        # Layout
        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.contact_list)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.clear_button)
        layout.addLayout(button_layout)

        # Forms
        form_layout = QVBoxLayout()
        form_layout.addWidget(self.first_name_label)
        form_layout.addWidget(self.first_name_input)

        form_layout.addWidget(self.last_name_label)
        form_layout.addWidget(self.last_name_input)

        form_layout.addWidget(self.email_label)
        form_layout.addWidget(self.email_input)
        
        form_layout.addWidget(self.phone_label)
        form_layout.addWidget(self.phone_input)
        layout.addLayout(form_layout)

        self.setStyleSheet('''
            QWidget {
                background-color: #f0f0f0;
                font-size: 16px;
            }

            QLabel {
                color: #333;
            }

            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #45a049;
            }
        ''')

        self.contact_list.itemClicked.connect(self. get_clicked_person)

        # Connect buttons to functions
        self.add_button.clicked.connect(self.add_contact)
        self.delete_button.clicked.connect(self.delete_contact)
        self.clear_button.clicked.connect(self.clear_fields)

    def add_contact(self):
        first_name_input = str(self.first_name_input.text())
        last_name_input = str(self.last_name_input.text())
        email_input = str(self.email_input.text())
        phoone_input = str(self.phone_input.text())
        self.address_book.add_contact(first_name_input, last_name_input, email_input, phoone_input)
        self.refresh_contacts()

    def delete_contact(self):
        selected_item = self.contact_list.currentItem()
        if selected_item:
            selected_name = selected_item.text()
        self.address_book.delete_contact(selected_name)
        self.refresh_contacts()
        self.clear_fields()

    def clear_fields(self):
        self.first_name_input.setText(str(""))
        self.last_name_input.setText(str(""))
        self.email_input.setText(str(""))
        self.phone_input.setText(str(""))

    def refresh_contacts(self):
        self.contact_list.clear()
        contacts_list = self.address_book.return_contacts_list()
        self.contact_list.addItems([f"{person['first_name']} {person['last_name']}" for person in contacts_list])


    def update_form(self, selected_person):
        if selected_person:
            self.first_name_input.setText(selected_person['first_name'])
            self.last_name_input.setText(selected_person['last_name'])
            self.email_input.setText(str(selected_person['email']))
            self.phone_input.setText(str(selected_person['phone']))
    
    def get_clicked_person(self, item):
        selected_person = next((person for person in self.filler_nested_list if person['first_name'] == item.text() and person['last_name'] == item.text()), None)
        self.update_form(selected_person)
        return selected_person


class AddressBook:
    def __init__(self):
        self.contacts = []
        
    def add_contact(self, first_name, last_name, email, phone):
        self.contacts.append({'first_name': first_name, 'last_name': last_name, 'email': email, 'phone': phone})

    def delete_contact(self, name):
        for contact in self.contacts:
            name_split = name.split(" ")
            first_name = name_split[0]
            last_name = name_split[1]
            if (contact['first_name'] == first_name) and (contact['last_name'] == last_name):
                self.contacts.remove(contact)
                break

    def edit_contact(self, index, first_name, last_name, email, phone):
        self.contacts[index] = [first_name, last_name, email, phone]

    def return_contacts_list(self):
        return self.contacts

if __name__ == '__main__':
    app = QApplication(sys.argv)
    address_book_app = AddressBookApp()
    address_book_app.show()
    sys.exit(app.exec_())
