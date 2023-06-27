from exercises import exercise1
from reader import CustomReader

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green

if __name__ == '__main__':

    file_name = "sample-VnlpUllna3dOVnZRMndFUVhndWw4Zz09Ojqgl8NyhOxIq9MdJq32k8IZ"

    reader = CustomReader(f"./samples/{file_name}/", 10)

    results = list()

    for lines, output_values in zip(reader.inputs(), reader.outputs()):
        results.append(exercise1(lines))

    for index, (result, output_values) in enumerate(zip(results, reader.outputs())):
        if result == output_values:
            print(G + str(index) + " - Success !" + W)
        else:
            print(R + str(index) + " - Fail !" + W)

        print(str(index) + str(result) + " == " + str(output_values))
