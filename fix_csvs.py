if __name__ == '__main__':

    filenames = [
        '3_galv_2.csv',
    ]

    for filename in filenames:
        with open(filename, 'r') as f:
            lines = f.readlines()

        lines = [l for l in lines if l != '\n' and l != ',,\n']

        with open(filename, 'w') as f:
            for l in lines:
                f.write(l)
