if __name__ == '__main__':

    filenames = ['exp_2_050_1.csv', 'exp_2_050_2.csv',
                 'exp_2_100_1.csv', 'exp_2_100_2.csv',
                 'exp_2_050_h_1.csv', 'exp_2_050_h_2.csv',
                 ]

    for filename in filenames:
        with open(filename, 'r') as f:
            lines = f.readlines()

        lines = [l for l in lines if l != '\n']

        with open(filename, 'w') as f:
            for l in lines:
                f.write(l)
