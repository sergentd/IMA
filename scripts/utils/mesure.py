#!/usr/bin/env python3

from collections import defaultdict as dd
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


def create_dic(pred_label):
    dic = dd(lambda: dd(int))
    for pred, label in pred_label:
        dic[pred][label] += 1
    return dic


def conf_tab(label_pred):
    y_label = pd.Series([y for y, _ in label_pred], name='Actual')
    y_pred = pd.Series([y for _, y in label_pred], name='Predicted')
    df_confusion = pd.crosstab(y_label, y_pred, rownames=['Actual'], colnames=[
                               'Predicted'], margins=True)
    return str(df_confusion)


def accuracy(label_pred):
    y_label = [y for y, _ in label_pred]
    y_pred = [y for _, y in label_pred]
    return "Accuracy:\t{:.0%}".format(accuracy_score(y_label, y_pred))


def precision(label_pred):
    y_label = [y for y, _ in label_pred]
    y_pred = [y for _, y in label_pred]
    return "Precision:\t{:.0%}".format(
        precision_score(y_label, y_pred, average='micro'))


def recall(label_pred):
    y_label = [y for y, _ in label_pred]
    y_pred = [y for _, y in label_pred]
    return "Recall:\t\t{:.0%}".format(
        recall_score(y_label, y_pred, average='micro'))


def error_grade(label_pred):
    return "Error percent:\t{:.0%}".format(
        sum([abs(x - y) for x, y in label_pred]) / (len(label_pred) * 10))


def all_mesure_grade(label_pred):
    return "\n".join([
        conf_tab(label_pred), error_grade(label_pred)])


def all_mesure_funny(label_pred):
    return "\n".join([
        conf_tab(label_pred),
        accuracy(label_pred),
        precision(label_pred),
        recall(label_pred)])


def main():
    label_pred = [[2, 3], [4, 10], [1, 2], [3, 4]]

    # a = all_mesure_funny(label_pred)
    a = all_mesure_grade(label_pred)
    print(a)


if __name__ == '__main__':
    main()
