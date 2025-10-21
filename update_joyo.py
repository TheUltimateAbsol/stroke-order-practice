import json
import csv

def update_joyo_json():
    # Read the CSV file and store its data in a dictionary
    csv_data = {}
    with open('joyo.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            csv_data[row['kanji']] = {
                'frequency': row['frequency'],
                'jlpt': row['jlpt'] if row['jlpt'] else None
            }

    # Read the JSON file
    with open('joyo.json', 'r', encoding='utf-8') as json_file:
        joyo_data = json.load(json_file)

    # Update the JSON data if 'freq' or 'jlpt_new' is null
    for kanji, details in joyo_data.items():
        if kanji in csv_data:
            if details.get('freq') is None:
                frequency = csv_data[kanji].get('frequency')
                if frequency and frequency.isdigit():
                    joyo_data[kanji]['freq'] = int(frequency)

            if details.get('jlpt_new') is None:
                jlpt = csv_data[kanji].get('jlpt')
                if jlpt and jlpt.isdigit():
                    joyo_data[kanji]['jlpt_new'] = int(jlpt)
    
    # Write the updated data back to the JSON file
    with open('joyo.json', 'w', encoding='utf-8') as json_file:
        json.dump(joyo_data, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    update_joyo_json()