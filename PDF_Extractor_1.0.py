import tkinter as tk
from tkinter import filedialog
import camelot
import pandas as pd
import json
import os
'''
Try-except-finally
File I/O operations
Network requests
Parsing data from untrusted sources
Arithmetic operations prone to errors (e.g., division by zero)
User input validation

EXAMPLE:

try:
    with open("config.json", "r") as file:
        config = file.read()
except FileNotFoundError:
    print("Configuration file missing. Using default settings.")
except PermissionError:
    print("Permission denied for accessing configuration file.")
else:
    print("Configuration loaded successfully.")
finally:
    print("Attempt to load configuration finished.")

'''
# Ensure Ghostscript paths are added to PATH
os.environ['PATH'] += r";C:\Program Files\gs\gs10.04.0\bin;C:\Program Files\gs\gs10.04.0\lib"


def open_file_dialog():
    """
    Opens a file dialog for selecting a PDF file.
    Returns the selected file path.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    file_path = filedialog.askopenfilename(
        title="Select a PDF File",
        filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
    )
    
    if not file_path:
        print("No file selected. Exiting.")
        exit()
    
    print(f"Selected PDF File: {file_path}")
    return file_path


def save_file_dialog():
    """
    Opens a save file dialog for specifying an output JSON file.
    Returns the selected file path.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    file_path = filedialog.asksaveasfilename(
        title="Save Output JSON",
        defaultextension=".json",
        filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]
    )
    
    if not file_path:
        print("No save location selected. Exiting.")
        exit()
    
    print(f"Output JSON will be saved to: {file_path}")
    return file_path


def format_table_data(df):

    # Extract headers (join header lines into a single string per column)
    headers = [header.replace('\n', ' ').strip() for header in df.iloc[0].tolist()]
    
    # Extract rows (exclude headers)
    rows = df.iloc[1:].values.tolist()
    
    formatted_data = []
    current_location = None
    
    for row in rows:
        location = row[0].strip()
        
        if location:  # If a new location appears
            current_location = {
                "Location": location,
                "Location_Data": []
            }
            formatted_data.append(current_location)
        
        # Split multiline data into separate entries
        multiline_entries = zip(*[cell.split('\n') for cell in row[1:]])
        for entry in multiline_entries:
            entry_data = dict(zip(headers[1:], [e.strip() for e in entry]))
            current_location["Location_Data"].append(entry_data)
    
    return formatted_data

def extract_tables_with_camelot(pdf_path):
    try:
        # Attempt table extraction using Lattice (grid-based detection)
        tables = camelot.read_pdf(pdf_path, pages='all', flavor='lattice')
        print(f"Number of tables detected with Lattice: {len(tables)}")
        
        if len(tables) == 0:
            print("No tables detected with Lattice. Switching to Stream mode...")
            tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream')
            print(f"Number of tables detected with Stream: {len(tables)}")
        
        json_output = {"file_name": os.path.basename(pdf_path), "pages": []}
        
        for index, table in enumerate(tables):
            if hasattr(table, 'df'):
                df = table.df 
                formatted_data = format_table_data(df)
            
                json_output["pages"].append({
                    "page": table.page,
                    "table_index": index,
                    "Data": formatted_data
            })
        
        print("Table extraction completed successfully.")
        return json_output
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def json_to_df(json_data):
    dataframes = {}
    # Extract file name
    file_name = json_data.get('file_name', 'UnknownFile').split('.')[0]
    # Iterate over the pages and group data by table_index
    for page in json_data['pages']:
        table_index = page['table_index']
        page_number = page['page']
    
        # Unique name for each DataFrame
        df_name = f"{file_name}_Page{page_number}_Table{table_index}"
    
        # Initialize table_data for this table_index
        table_data = []
    
        # Process each location and extract data
        for entry in page['Data']:
            location = entry['Location']
            for record in entry['Location_Data']:
                # Add Location metadata to each record
                record['Location'] = location
                record['Page'] = page_number
                record['Table_Index'] = table_index
                table_data.append(record)
    
        # Create DataFrame and reorder columns
        df = pd.DataFrame(table_data)
        df = df[['Location', 'Date', 'pH', 'EC  (mS/cm)', 'Temp.', 'Diss O2  (mg/l)', 'REDOX  (mV)']]
    
        # Save DataFrame to dictionary
        dataframes[df_name] = df

    for df_name, df in dataframes.items():
        df.to_csv(f"{df_name}.csv", index=False)
        print(f"Saved DataFrame as {df_name}.csv")
        print(f"\nDataFrame: {df_name}")
        print(df.head())

def main():
    # Select PDF file
    pdf_path = open_file_dialog()
    
    # Extract tables
    table_data = extract_tables_with_camelot(pdf_path)
    
    if table_data:
        json_to_df(table_data)
        # If table extraction was successful, open save file dialog
        output_json_path = save_file_dialog()
        
        # Save the extracted data to JSON
        with open(output_json_path, 'w') as json_file:
            json.dump(table_data, json_file, indent=4)
        
        print(f"Table data saved successfully to: {output_json_path}")
    else:
        print("Table extraction failed. No JSON file will be saved.")


if __name__ == "__main__":
    main()
