def get_num_words(file_content):
    temp = file_content.split()
    return len(temp)

def get_car_count(file_content):
    file_content = file_content.lower()
    car_count = dict()

    for caract in file_content:
        if not caract in car_count:
            car_count[caract] = file_content.count(caract)

    return car_count

def format_car_count(car_count):
    formated_car_count = list()

    return formated_car_count