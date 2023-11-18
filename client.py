# Import the requests library to make HTTP requests
import requests
import json


# Define a function to send a message to the server
def send_message():
    # The server's URL for receiving messages
    url = 'http://localhost:5000/convert-to-excel'

    # JSON data to be sent to the server
    json_data = {
        "Table": {
            # JSON data structure
            "BlockType": "TABLE",
            "Confidence": 99.8046875,
            # Example rows with cell data
            "Rows": [
                {
                    "Cells": [
                        {
                            "BlockType": "CELL",
                            "Confidence": 81.8359375,
                            "RowIndex": 1,
                            "ColumnIndex": 1,
                            "RowSpan": 1,
                            "ColumnSpan": 1,
                            "EntityTypes": ["COLUMN_HEADER"],
                            "Content": "Header 1"
                        },
                        {
                            "BlockType": "CELL",
                            "Confidence": 85.12345,
                            "RowIndex": 1,
                            "ColumnIndex": 2,
                            "RowSpan": 1,
                            "ColumnSpan": 1,
                            "EntityTypes": ["COLUMN_HEADER"],
                            "Content": "Header 2"
                        }
                    ]
                },
                {
                    "Cells": [
                        {
                            "BlockType": "CELL",
                            "Confidence": 82.45789,
                            "RowIndex": 2,
                            "ColumnIndex": 1,
                            "RowSpan": 1,
                            "ColumnSpan": 1,
                            "EntityTypes": ["DATA"],
                            "Content": "Data 1-1"
                        },
                        {
                            "BlockType": "CELL",
                            "Confidence": 88.76543,
                            "RowIndex": 2,
                            "ColumnIndex": 2,
                            "RowSpan": 1,
                            "ColumnSpan": 1,
                            "EntityTypes": ["DATA"],
                            "Content": "Data 1-2"
                        }
                    ]
                }
            ]
        }
    }

    # Make a POST request to the server with the message as JSON data
    response = requests.post(url, json=json_data)

    # Check the response status code
    if response.status_code == 200:
        # print the server's response
        print(response.json())
        # If the response is successful, sent a message to the server
        print("Successfully download the Excel file!")
    else:
        print("Error:", response.status_code)


# Check if the script is being run directly and not imported elsewhere
if __name__ == '__main__':
    # Execute the send_message function
    send_message()
