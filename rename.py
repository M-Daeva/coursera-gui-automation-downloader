import os


def with_path(path):
    def rename():
        names = os.listdir(path)
        temp = list(range(len(names) + 10))

        for name in names:
            [num, *a] = name.split(' ')
            num = int(num)
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
