import pandas as pd
import json

def excel_to_json(excel_file_path, json_file_path):
    try:
        data_frame = pd.read_excel(excel_file_path, "FinalList")
        data_frame.to_json(json_file_path, orient='records')

        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)

        with open("/home/ubuntu/lohit/new.json", "w") as output_file:
            json.dump(data, output_file, indent=2)
        print("Excel file converted to JSON successfully!")
    except Exception as e:
        print(f"Error: {e}")
		
		
excel_file_path = "/home/ubuntu/lohit/Python_Package_List.xlsx"
json_file_path = "/home/ubuntu/lohit/abc.json"
excel_to_json(excel_file_path, json_file_path)
