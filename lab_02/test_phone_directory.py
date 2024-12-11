import unittest
from unittest.mock import patch
from phone_directory import addNewElement, deleteElementByName, updateElement, directory

class TestPhoneBook(unittest.TestCase):
    def setUp(self):
        global directory
        directory = [
        {"name": "Bob", "phone": "0631234567", "email": "bob@example.com", "address": "895 Street"},
        {"name": "Emma", "phone": "0631234567", "email": "emma@example.com", "address": "123 Street"}
    ]


    def test_addNewElement(self):
        addNewElement("Zak", "0631234567", "zak@example.com", "9 Street")
        self.assertEqual(len(directory), 3)
        self.assertEqual(directory[2]["name"], "Zak")

    def test_deleteElementByName(self):
        deleteElementByName("Emma")
        self.assertEqual(len(directory), 1)
        self.assertEqual(directory[0]["name"], "Bob")
        
        
    def test_updateElement(self):
        addNewElement("Jon", "0631234567", "jon@example.com", "27 Street")
        with patch("builtins.input", side_effect=["Jon", "John", "0998765432", "", "New Address"]):
            updateElement()
        
        updatedStudent = next((s for s in directory if s["name"] == "John"), None)
        self.assertIsNotNone(updatedStudent)
        self.assertEqual(updatedStudent["phone"], "0998765432")

if __name__ == "__main__":
    unittest.main()

