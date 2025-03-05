def sort_on(dict):
    return dict["num"]

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

    for key, value in car_count.items():
        formated_car_count.append({'caracter': key, 'num': value})
    formated_car_count.sort(reverse=True, key=sort_on)
    return formated_car_count