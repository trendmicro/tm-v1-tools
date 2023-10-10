import sys
from os import path
from json import load
from glob import glob
from pandas import DataFrame, ExcelWriter

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', path.dirname(path.abspath(__file__)))
    return path.join(base_path, relative_path)

file_path = resource_path('files/mitre-v13.json')

def load_json_data():
    files = glob('TrendMicro_OAT_MITREATTACK_Navigator_*.json')
    if not files:
        print("No JSON file found")
        sys.exit(1)
    latest_file = max(files, key=path.getmtime)
    with open(latest_file, 'r', encoding='utf-8') as file:
        data = load(file)
    return data['techniques']

def process_json_data(techniques):
    data_list = [{'MITRE Tactic': tech['tactic'], 'MITRE Technique': tech['techniqueID'], 'Count': int(tech['comment'].split(': ')[1])} for tech in techniques]
    return data_list

def main():
    techniques = load_json_data()
    processed_data = process_json_data(techniques)
    df = DataFrame(processed_data)

    # Sort the DataFrame based on the Count and select the top 10
    df = df.sort_values(by='Count', ascending=False).head(10)

    with open(file_path, 'r', encoding='utf-8') as file:
        technique_array = load(file)
    technique_details = {item['ID']: item for item in technique_array}

    for index, row in df.iterrows():
        technique_id = row['MITRE Technique']
        details = technique_details.get(technique_id, {})
        for key, value in details.items():
            if key not in df.columns:
                df[key] = None
            if df[key].dtype != 'object':
                df[key] = df[key].astype('object')
            df.at[index, key] = value

    if 'ID' in df.columns:
        df = df.drop(columns=['ID'])

    with ExcelWriter('MitreReport.xlsx', engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Data')
    print("[info] - Final report saved to MitreReport.xlsx")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")