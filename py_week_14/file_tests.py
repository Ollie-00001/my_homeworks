from file_classes import JsonFile, TxtFile, CsvFile

if __name__ == "__main__":
    # JSON
    json_file = JsonFile("test.json")
    json_file.write({"name": "Egor", "age": 22})
    print("JSON Read:", json_file.read())
    json_file.append({"name": "Alina", "age": 21})
    print("JSON After Append:", json_file.read())

    # TXT
    txt_file = TxtFile("test.txt")
    txt_file.write("Hello, world!\n")
    print("TXT Read:", txt_file.read())
    txt_file.append("Appended line.\n")
    print("TXT After Append:", txt_file.read())

    # CSV
    csv_file = CsvFile("test.csv")
    csv_file.write([["Name", "Age"], ["Egor", "22"]])
    print("CSV Read:", csv_file.read())
    csv_file.append(["Alina", "21"])
    print("CSV After Append:", csv_file.read())