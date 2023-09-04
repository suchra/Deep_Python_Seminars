import os
import json

class DirectorySerializer:
    def __init__(self, directory_path):
        self._directory_path = directory_path
        self._content_list = []

    @property
    def directory_path(self):
        return self._directory_path

    @property
    def content_list(self):
        return self._content_list

    def serialize_content(self):
        if not os.path.exists(self.directory_path):
            print("Указанная директория не существует.")
            return

        for item in os.listdir(self.directory_path):
            item_path = os.path.join(self.directory_path, item)
            item_info = {
                'name': item,
            }

            if os.path.isfile(item_path):
                item_info['type'] = 'file'
                item_info['extension'] = os.path.splitext(item)[1]
            elif os.path.isdir(item_path):
                item_info['type'] = 'directory'

            self._content_list.append(item_info)

    def save_to_json(self, output_path):
        self.serialize_content()
        with open(output_path, 'w') as json_file:
            json.dump(self.content_list, json_file, indent=4)
        print(f"Содержимое директории сохранено в файл: {output_path}")


directory_path = "/путь/к/директории"
serializer = DirectorySerializer(directory_path)


output_path = "directory_content.json"
serializer.save_to_json(output_path)