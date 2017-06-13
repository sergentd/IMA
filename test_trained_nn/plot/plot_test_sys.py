import json
import matplotlib.pyplot as plt


def by_epochs(values, lossoracc=False):
    name = "Loss"
    indice = 0
    if lossoracc:
        name = "Accuracy"
        indice = 1

    fig = plt.figure()
    plt.title('{} by Epochs\n5 Epochs on Train'.format(name))
    i = 1
    for usr in sorted(values)[:10]:
        #plt.title('{} by Epochs\nfor user :{}'.format(name, usr))
        Y = [values[usr][ep][indice]
             for ep in sorted([ep for ep in values[usr]])]
        X = sorted([int(ep) for ep in values[usr]])
        # plt.text(X[0] * i, Y[0], usr)
        plt.plot(X, Y, label=usr)
        i *= 1.1
    plt.legend()
    plt.show()


def main():
    with open('../loss_acc_test_system_train.json', 'r') as stream:
        values = json.load(stream)
    by_epochs(values)
    by_epochs(values, True)


if __name__ == '__main__':
    main()
