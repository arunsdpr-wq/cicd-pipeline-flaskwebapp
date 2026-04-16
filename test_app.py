import unittest
from app import app

class BasicTests(unittest.TestCase):
    def test_main_page(self):
        # Create a test client for the Flask app
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, Jenkins! Your CI/CD pipeline is working!.")

if __name__ == '__main__':
    unittest.main()
