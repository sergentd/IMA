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
    i = 10
    for usr in sorted(values):
        #plt.title('{} by Epochs\nfor user :{}'.format(name, usr))
        Y = [values[usr][ep][indice]
             for ep in sorted([ep for ep in values[usr]])]
        X = sorted([int(ep) for ep in values[usr]])
        plt.text(X[i], Y[i], usr)
        plt.plot(X, Y, label=usr)
        i += 20
    plt.legend()
    plt.show()


def main():
    with open('../loss_acc_test_system.json', 'r') as stream:
        values = json.load(stream)
    by_epochs(values)


if __name__ == '__main__':
    main()
