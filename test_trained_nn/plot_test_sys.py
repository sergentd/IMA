import json
import matplotlib.pyplot as plt


def by_epochs(values, lossoracc=False):
    name = "Loss"
    indice = 0
    if lossoracc:
        name = "Accuracy"
        indice = 1

    fig = plt.figure()
    plt.title('{} by Epochs'.format(name))

    for usr in sorted(values):
        plt.title('{} by Epochs\nfor user :{}'.format(name, usr))
        Y = [values[usr][ep][indice]
             for ep in sorted([ep for ep in values[usr]][:350])]
        X = sorted([int(ep) for ep in values[usr]][:350])
        plt.plot(X, Y)
        plt.show()


def main():
    with open('loss_acc_test_system.json', 'r') as stream:
        values = json.load(stream)
    by_epochs(values, True)


if __name__ == '__main__':
    main()
