# Textract_Microservice

1. Introduction:
A microservice designed to convert JSON data into an Excel format.

2. Requesting Data:
- Endpoint: http://localhost:5000/convert-to-excel
- Method: POST
- Data Format: JSON (with structure as provided in the client script)
- Example Request: 

3. Receiving Data:
- Response: a link to the downloaded Excel file
- Status Codes: 200 for success, others for error handling
- Error Handling: If the server encounters an error while processing the request (e.g., invalid input data), it can return a response with an appropriate status code (like 400 Bad Request) and a JSON object containing the error message. The client, upon receiving this response, checks the status code. If it's not 200, the client prints the error message, alerting the user to the issue.

4. UML Sequence Diagram:
<img width="745" alt="截圖 2023-11-19 上午1 23 38" src="https://github.com/AaronHsiung/Textract_Microservice/assets/114290842/8da023c8-9fd3-4066-be97-fdaa85e06465">
