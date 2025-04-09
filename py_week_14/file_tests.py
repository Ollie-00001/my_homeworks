import os
from file_classes import JsonFile, TxtFile, CsvFile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

json_path = os.path.join(BASE_DIR, "test.json")
txt_path = os.path.join(BASE_DIR, "test.txt")
csv_path = os.path.join(BASE_DIR, "test.csv")

if __name__ == "__main__":
    # JSON
    json_file = JsonFile(json_path)
    json_file.write({"name": "Egor", "age": 22})
    print("JSON Read:", json_file.read())
    json_file.append({"name": "Alina", "age": 21})
    print("JSON After Append:", json_file.read())

    # TXT
    txt_file = TxtFile(txt_path)
    txt_file.write("Hello, world!\n")
    print("TXT Read:", txt_file.read())
    txt_file.append("Appended line.\n")
    print("TXT After Append:", txt_file.read())

    # CSV
    csv_file = CsvFile(csv_path)
    csv_file.write([["Name", "Age"], ["Egor", "22"]])
    print("CSV Read:", csv_file.read())
    csv_file.append(["Alina", "21"])
    print("CSV After Append:", csv_file.read())