from flask import Flask, request, jsonify, url_for, send_from_directory
import pandas as pd
import json
import os

# Initialize Flask application
app = Flask(__name__)

# Define a directory to store the generated Excel files
UPLOAD_FOLDER = '/Users/bear840401/Desktop/OSU/CS_361/Microservice/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the upload folder if it doesn't already exist
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

    # Generate a download link
    download_url = url_for('download_file', filename=excel_filename, _external=True)

    print("Received JSON: ", json_data["Table"])

    # Return a JSON response with the download link
    return jsonify({"download_url": download_url})


# Route for downloading the generated Excel file
@app.route('/uploads/<filename>')
def download_file(filename):
    # Send the file from the upload directory
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# Main function to run the Flask application
@app.route('/')
def index():
    return "This is the upload page!"


# Check if the script is being run directly and not imported elsewhere
if __name__ == '__main__':
    # Start the Flask app on port 5000
    app.run(port=5000)
