import os
import tempfile


class File:
    def __init__(self, file_name: str):

        if not os.path.exists(file_name):
            with open(file_name, 'w', encoding='utf-8'):
                pass
            self.file_data = ''
        else:
            with open(file_name, 'r', encoding='utf-8') as file:
                self.file_data = file.read()
        self.file_name = file_name
        self.current = 0
        self.end = len(self.file_data.split('\n'))

    def write(self, data: str):
        self.file_data += data
        with open(self.file_name, 'w', encoding='utf-8') as file:
            file.write(self.file_data)
        self.end = len(self.file_data.split('\n'))

    def __str__(self):
        return self.file_name

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            self.current = 0
            raise StopIteration
        result = self.file_data.split('\n')[self.current]
        self.current += 1
        return result

    def __add__(self, other):
        if not isinstance(other, File):
            raise TypeError

        new_file_name = os.path.join(tempfile.gettempdir(), 'sum_of_two_files.txt')
        with open(new_file_name, 'w', encoding='utf-8') as file:
            file.write(self.file_data + other.file_data)

        return File(new_file_name)


if __name__ == '__main__':
    dir_name = os.getcwd()
    file_name_1 = os.path.join(dir_name, 'test_1.txt')
    file_name_2 = os.path.join(dir_name, 'test_2.txt')
    file_name_3 = os.path.join(dir_name, 'test_3.txt')

    f1 = File(file_name_1)
    f2 = File(file_name_2)
    f3 = File(file_name_3)

    f4 = f1 + f3

    for line in f4:
        print(line)
