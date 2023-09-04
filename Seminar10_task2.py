import os
import json
import pickle

class JSONToPickleConverter:
    def __init__(self, directory):
        self._directory = directory

    @property
    def directory(self):
        return self._directory

    @directory.setter
    def directory(self, path):
        if not os.path.exists(path):
            print("Указанная директория не существует.")
        else:
            self._directory = path

    def convert_json_to_pickle(self):
        if not os.path.exists(self.directory):
            print("Указанная директория не существует.")
            return

        for filename in os.listdir(self.directory):
            if filename.endswith('.json'):
                json_path = os.path.join(self.directory, filename)
                pickle_path = os.path.splitext(json_path)[0] + '.pickle'

                try:
                    with open(json_path, 'r') as json_file:
                        json_content = json.load(json_file)

                    with open(pickle_path, 'wb') as pickle_file:
                        pickle.dump(json_content, pickle_file)

                    print(f"Файл {filename} успешно сконвертирован в {pickle_path}")
                except Exception as e:
                    print(f"Ошибка при конвертации файла {filename}: {e}")

directory_path = "/путь/к/директории"
converter = JSONToPickleConverter(directory_path)

converter.convert_json_to_pickle()