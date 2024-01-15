import json
import pandas as pd
from pathlib import Path

source_dir = Path('./json files (size=1000)')
data_list = []
for json_file in source_dir.glob('psu*.json'):
    with open(json_file, 'r', encoding='utf-8') as f:
        json_content = f.read()
        # json_data = json.dumps(json_content)
        json_data = json.loads(json_content)
        # print(len(json_content))
        # print(type(json_file))
        # print(type(json_content))
        # print(len(json_content))
        # print(json_data)
        # print("==============")
        for result in json_data:
            name = result["displayName"] if result["displayName"] else None
            name_parts = name.split() if name else None
            titles = ["dr", "professor","prof","mr","md", "mrs","ms","dr.", "professor.","mr.","md.", "mrs.","ms.","Dr.","Prof.", "Professor.","Mr.","Md.", "Mrs.","Ms.","Dr","Prof","Miss " "Professor","Mr","Md", "Mrs","Ms" ]
            if name_parts :
                if name_parts[0] in titles:
                    first_name = name_parts[1] if name_parts else None
                elif name_parts[0] == "Associate":
                    first_name = name_parts[2] if name_parts else None
                else:
                    first_name = name_parts[0]
            else:
                None
            email = result["universityEmail"] if result["universityEmail"] else None
            position = result.get('primaryAffiliation', None)
            university = "Pennsylvania"
            faculty = ""
            phone =""
            print(first_name)
            print(name)
            print(email)
            print(position)
            print("=================================")
            data_list.append([first_name, email, name,position, university, faculty, phone])

df = pd.DataFrame(data_list, columns=[
                  'First Name', 'Email', 'Name', 'Position', 'University', 'Faculty', 'Phone'])
print(df)

#Export the DataFrame to an Excel file
df.to_excel('Pennsylvania-final-2nd time.xlsx', index=False)
