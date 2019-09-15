import os


def with_path(path):
    def rename():
        names = os.listdir(path)
        temp = list(range(20 * len(names)))

        for name in names:
            num = name.split(' ')[0]
            num = round(10 * float(num))
            temp[num] = name

        temp2 = []
        for item in temp:
            if type(item) is str:
                temp2.append(item)

        for idx, file in enumerate(temp2):
            part = ' '.join(file.split(' ')[1:])
            new_name = f'{idx + 1} {part}'
            os.rename(path + '\\' + file, path + '\\' + new_name)

    return rename
