#!/usr/bin/env python3

from collections import defaultdict as dd
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import fbeta_score


def create_dic(pred_label):
    dic = dd(lambda: dd(int))
    for pred, label in pred_label:
        dic[pred][label] += 1
    return dic


def conf_tab(pred_label):
    y_label = pd.Series([y for _, y in pred_label], name='Actual')
    y_pred = pd.Series([y for y, _ in pred_label], name='Predicted')
    df_confusion = pd.crosstab(y_label, y_pred, rownames=['R:Actual'], colnames=[
                               'C:Predicted'], margins=True)
    return str(df_confusion)


def accuracy(pred_label):
    y_label = [y for _, y in pred_label]
    y_pred = [y for y, _ in pred_label]
    return "Accuracy:\t{:.0%}".format(accuracy_score(y_label, y_pred))


def precision(pred_label):
    y_label = [y for _, y in pred_label]
    y_pred = [y for y, _ in pred_label]
    return "Precision:\t{:.0%}".format(
        precision_score(y_label, y_pred, average='binary'))


def recall(pred_label):
    y_label = [y for _, y in pred_label]
    y_pred = [y for y, _ in pred_label]
    return "Recall:\t\t{:.0%}".format(
        recall_score(y_label, y_pred, average='binary'))


def error_grade(pred_label):
    return "Error percent:\t{:.0%}".format(
        sum([abs(x - y) for x, y in pred_label]) / (len(pred_label) * 10))


def fscore(pred_label):
    y_label = [y for _, y in pred_label]
    y_pred = [y for y, _ in pred_label]
    return "Fscore:\t\t{:.0%}".format(
        fbeta_score(y_label, y_pred, average='binary', beta=1))


def all_mesure_grade(pred_label):
    return "\n".join([
        conf_tab(pred_label), error_grade(pred_label), ""])


def all_mesure_funny(pred_label):
    return "\n".join([
        conf_tab(pred_label),
        accuracy(pred_label),
        fscore(pred_label),
        precision(pred_label),
        recall(pred_label),
        ""])


def main():
    pred_label = [[2, 3], [4, 10], [1, 2], [3, 4]]

    # a = all_mesure_funny(pred_label)
    a = all_mesure_grade(pred_label)
    print(a)


if __name__ == '__main__':
    main()
