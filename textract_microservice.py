from flask import Flask, request, send_file
import pandas as pd
import os

app = Flask(__name__)

# Define a directory to save Excel files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the directory if it does not exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# Route for converting JSON data to an Excel file
@app.route('/convert-to-excel', methods=['POST'])
def convert_to_excel():
    # Receive JSON data from the request
    json_data = request.get_json()

    # Extract the required data and create a DataFrame
    data = []
    for row in json_data["Table"]["Rows"]:
        for cell in row["Cells"]:
            cell_data = {
                "Row Index": cell["RowIndex"],
                "Column Index": cell["ColumnIndex"],
                "Confidence": cell["Confidence"],
                "Content": cell["Content"]
            }
            data.append(cell_data)

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data)

    # Build the Excel file's filename
    excel_filename = 'converted_excel_file.xlsx'
    excel_file_path = os.path.join(app.config['UPLOAD_FOLDER'], excel_filename)

    # Save the Excel file
    df.to_excel(excel_file_path, index=False)

    # Send the saved Excel file back to the client as an attachment
    return send_file(excel_file_path, as_attachment=True, download_name=excel_filename)


# Route for the main page displaying a simple welcome message
@app.route('/')
def index():
    return "This is the upload page!"


# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=5001)

