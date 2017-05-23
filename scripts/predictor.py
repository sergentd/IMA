# ! /usr/bin/python3
# @Djavan Sergent
from function import list, get_filename
from matplotlib import pyplot as plt
import csv


class Predictor:
    def __init__(self, params):
        self.par = params
        self.au_dir = self.par.au_path + self.par.user + '/'

    def launch(self):
        labels = self.get_labels(self.par.eval_path + self.par.user + '.csv')
        for m in self.get_matrix():
            video_name = get_filename(m)
            csv_path = self.au_dir + m
            self.analyze(csv_path, labels[video_name])

    def get_matrix(self):
        return list(self.au_dir)

    def get_labels(self, ufile):
        labels = dict()
        with open(ufile, newline='') as csvfile:
            labels_reader = csv.DictReader(csvfile)
            for line in labels_reader:
                labels[get_filename(line['video_name'])] = line['funny']
        return labels

    def analyze(self, mfile, label):
        au5 = []; au5v = []; au6 = []; au6v = []
        au7 = []; au7v = []; au12 = []; au12v = []

        with open(mfile, newline='') as csvfile:
            matrix_reader = csv.DictReader(csvfile)
            for line in matrix_reader:
                au5.append(line["AU05_c"]); au5v.append(line["AU05_r"])
                au6.append(line["AU06_c"]); au6v.append(line["AU06_r"])
                au7.append(line["AU07_c"]); au7v.append(line["AU07_r"])
                au12.append(line["AU12_c"]); au12v.append(line["AU12_r"])

            plt.subplot(211)
            plt.plot(au5, 'y')
            plt.plot(au6, 'g')
            plt.plot(au7, 'r')
            plt.plot(au12, 'b')

            plt.subplot(212)
            plt.plot(au5v, 'y')
            plt.plot(au6v, 'g')
            plt.plot(au7v, 'r')
            plt.plot(au12v, 'b')

            plt.show()
