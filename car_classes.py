import os
import csv
import argparse


class CarBase:
    def __init__(self, car_type, brand, carrying, photo_file_name):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand=None, photo_file_name=None, carrying=None, passenger_seats_count=0):
        super().__init__('car', brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand=None, photo_file_name=None, carrying=0, whl=None, width=0., height=0., length=0.):
        super().__init__('truck', brand, photo_file_name, carrying)
        self.body_whl = whl
        self.body_width, self.body_height, self.body_length = width, height, length

    def get_body_volume(self):
        return self.body_width * self.body_length * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand=None, photo_file_name=None, carrying=0, extra=None):
        super().__init__('spec_machine', brand, photo_file_name, carrying)
        self.extra = extra


def create_car(car_data: list) -> [Car, None]:
    if car_data[2]:
        try:
            k = int(car_data[2])
        except ValueError:
            return None
        else:
            return Car(brand=car_data[1], photo_file_name=car_data[3], carrying=car_data[5], passenger_seats_count=k)


def create_truck(car_data: list) -> [Truck, None]:
    if car_data[4]:
        try:
            w, h, le = tuple(map(float, car_data[4].split('x')))
        except ValueError:
            return None
        else:
            return Truck(brand=car_data[1], photo_file_name=car_data[3], carrying=car_data[5], whl=car_data[4], width=w, height=h,
                         length=le)
    else:
        return Truck(brand=car_data[1], photo_file_name=car_data[3], carrying=car_data[5], whl="0x0x0", width=0, height=0, length=0)


def create_spec(car_data: list) -> [SpecMachine, None]:
    if car_data[6]:
        return SpecMachine(brand=car_data[1], photo_file_name=car_data[3], carrying=car_data[5], extra=car_data[6])


def invalid_type(car_data: list) -> None:
    return None


c_a_r__t_y_p_e_s = {'car': create_car, 'truck': create_truck, 'spec_machine': create_spec}


def create_proper_car_class(car_data: 'list') -> "CarBase":
    if car_data[1] and car_data[3] and car_data[5]:
        return c_a_r__t_y_p_e_s.get(car_data[0], invalid_type)(car_data)


def get_car_list(csv_filename: "str") -> "list":
    car_classes = []
    with open(csv_filename, encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for car_data in reader:
            if len(car_data) == 7:
                car_model = create_proper_car_class(car_data)
                if car_model:
                    car_classes.append(car_model)
    return car_classes


def check_input_file(filename):
    if not filename.endswith('csv'):
        raise argparse.ArgumentTypeError(" '{0}', only .csv files allowed".format(filename))
    try:
        f = open(filename, 'r', encoding='utf-8')
        f.close()
    except IOError as err:
        raise argparse.ArgumentTypeError("{}".format(err))
    else:
        return filename


if __name__ == '__main__':
    ap = argparse.ArgumentParser("parse CSV file with cars data")
    ap.add_argument('csv_file_name', type=check_input_file)
    args = ap.parse_args()

    car_list = get_car_list(args.csv_file_name)

    for car in car_list:
        print(car.__class__)