import unittest
from index import handler

class TestHandler(unittest.TestCase):
    def test_handler_with_url(self):
        event = {
            "queryStringParameters": {
                "url": "https://example.com"
            }
        }
        response = handler(event)
        assert response["statusCode"] == 200
        assert response["body"] == "URL: https://example.com"

    def test_handler_without_url(self):
        event = {
            "queryStringParameters": {}
        }
        response = handler(event)
        assert response["statusCode"] == 200
        assert response["body"] == "URL: "

    def test_handler_no_query_string_parameters(self):
        event = {}
        response = handler(event)
        assert response["statusCode"] == 200
        assert response["body"] == "URL: "

if __name__ == '__main__':
    unittest.main()