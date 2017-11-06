class FileReader:
    def __init__(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.file_data = file.read()
        except IOError:
            self.file_data = ""

    def read(self):
        return self.file_data


if __name__ == '__main__':
    print(FileReader('etetete').read())
    print(FileReader('storage.txt').read())
