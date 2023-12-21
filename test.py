"""About
"""


cars_list = [[], []]
cars_zip = []
model = " "
color = None


def add_cars():

    if model not in cars_list:
        cars_list[0].append(model)
        cars_list[1].append(color)
    return cars_list


def cars_model_color():

    for car, color in zip(cars_list[0], cars_list[1]):
        cars_zip.append((car, color))


while len(model) > 0:
    model = None
    # noinspection PyRedeclaration
    model = input("Enter the car model: ")
    if len(model) > 0:
        color = input("Enter the car color: ")
        add_cars()
        print(cars_list)
        print(cars_zip)
    else:
        break
    continue
cars_model_color()
print(cars_zip)
