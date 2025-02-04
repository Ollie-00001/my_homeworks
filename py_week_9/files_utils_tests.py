from files_utils import (
    read_json, write_json, append_json,
    read_csv, write_csv, append_csv,
    read_txt, write_txt, append_txt,
    read_yaml
)

def run_tests():
    json_file = "test.json"
    data_json = {"name": "Egor", "age": 22}
    write_json(data_json, file_path=json_file)
    print("JSON после записи:", read_json(json_file))

    new_data_json = {"job": "developer"}
    append_json(new_data_json, file_path=json_file)
    print("JSON после добавления:", read_json(json_file))

    csv_file = "test.csv"
    csv_data = [["name", "age"], ["Egor", "22"]]
    write_csv(*csv_data, file_path=csv_file)
    print("CSV после записи:", read_csv(csv_file))

    new_csv_data = [["Alina", "23"]]
    append_csv(*new_csv_data, file_path=csv_file)
    print("CSV после добавления:", read_csv(csv_file))

    txt_file = "test.txt"
    write_txt("Hello, Egor!", file_path=txt_file)
    print("TXT после записи:", read_txt(txt_file))

    append_txt("This is a new line.", file_path=txt_file)
    print("TXT после добавления:", read_txt(txt_file))

    yaml_file = "test.yaml"
    yaml_data = {
        "weather_app": {
            "api_key": "1234567890",
            "location": "Istanbul",
            "units": "metric"
        }
    }
    with open(yaml_file, "w") as f:
        import yaml
        yaml.safe_dump(yaml_data, f)

    print("YAML данные:", read_yaml(yaml_file))


if __name__ == "__main__":
    run_tests()