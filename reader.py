class CustomReader:

    def __init__(self, path, number):
        self.path = path
        self.number = number

    def read_file(self, file_name, num):
        with open(self.path + file_name + str(num) + ".txt", "r") as file:
            lines = file.readlines()

        return [line.strip() for line in lines]

    def inputs(self):
        input_values = list()

        for n in range(1, self.number + 1):
            input_values.append(self.read_file("input", n))

        return input_values

    def outputs(self):
        input_values = list()

        for n in range(1, self.number + 1):
            input_values.append(self.read_file("output", n))

        return input_values
