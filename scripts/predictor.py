# ! /usr/bin/python3
# @Djavan Sergent
from function import list, get_filename, plot
from params import Params
from views import IdView
import csv


class Predictor:
    def __init__(self, params):
        self.par = params
        self.au_dir = self.par.au_path + self.par.user + '/'

    def launch(self):
        labels = self.get_labels(self.par.eval_path + self.par.user + '.csv')
        predictions = dict()
        for m in self.get_matrix():
            video_name = get_filename(m)
            csv_path = self.au_dir + m
            predictions[video_name] = [self.analyze(csv_path, labels[video_name], video_name), labels[video_name]]

        # for p in predictions:
        #     print(p + str(predictions[p]))

        truePos, trueNeg, falsePos, falseNeg = self.scoring(predictions)
        return {'tp':truePos, 'tn':trueNeg, 'fp':falsePos, 'fn':falseNeg}

    def get_matrix(self):
        return list(self.au_dir)

    def get_labels(self, ufile):
        labels = dict()
        with open(ufile, newline='') as csvfile:
            labels_reader = csv.DictReader(csvfile)
            for line in labels_reader:
                labels[get_filename(line['video_name'])] = line['funny']
        return labels

    # Dummy prediction
    def analyze(self, mfile, label, name):
        au5 = []; au5v = []; au6 = []; au6v = []
        au7 = []; au7v = []; au12 = []; au12v = []
        match = 0

        with open(mfile, newline='') as csvfile:
            matrix_reader = csv.DictReader(csvfile)
            cpt = 0
            for line in matrix_reader:
                au5.append(line["AU05_c"]); au5v.append(line["AU05_r"])
                au6.append(line["AU06_c"]); au6v.append(line["AU06_r"])
                au7.append(line["AU07_c"]); au7v.append(line["AU07_r"])
                au12.append(line["AU12_c"]); au12v.append(line["AU12_r"])
                if (line["AU06_c"] == str(1)) and (line["AU12_c"] == str(1)):
                    match +=1
                cpt += 1

            # Plot
            au = [au5, au6, au7, au12]
            auv = [au5v, au6v, au7v, au12v]
            # plot(name, label, au, auv)

            # Prediction
            if match/cpt >= 0.2:
                return 'True'
            else:
                return 'False'

    def scoring(self, predictions):
        true_positif = 0; true_negatif = 0; false_positif = 0; false_negatif = 0
        for p in predictions:
            # Prediction = TRUE
            if predictions[p][0] == 'True':
                # True label = TRUE
                if predictions[p][1] == 'True':
                    true_positif += 1
                # True label = FALSE
                else:
                    false_positif += 1
            # Prediction = FALSE
            else:
                # True label = TRUE
                if predictions[p][1] == 'True':
                    false_negatif += 1
                # True label = FALSE
                else:
                    true_negatif += 1
        # print("P : TRUE\t|\tT : TRUE\t" + str(true_positif))
        # print("P : TRUE\t|\tT : FALSE\t" + str(false_positif))
        # print("P : FALSE\t|\tT : FALSE\t" + str(true_negatif))
        # print("P : FALSE\t|\tT : TRUE\t" + str(false_negatif))
        return true_positif, true_negatif, false_positif, false_negatif


if __name__ == "__main__":
    par = Params(env="dev")

    # user id to evaluate
    # main_view = IdView(par)
    # main_view.create()
    # main_view.show()

    # list users
    evals = list(par.eval_path)
    list_users = []
    preds = {'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0}
    for e in evals:
        list_users.append(get_filename(e))

    for user in list_users:
        par.set_user(user)
        # predictor
        predic = Predictor(params=par)
        results = predic.launch()
        preds['tp'] += results['tp']
        preds['tn'] += results['tn']
        preds['fp'] += results['fp']
        preds['fn'] += results['fn']
    print(preds)
    print((preds['tp'] + preds['tn'])*100 / (preds['tp'] + preds['tn'] + preds['fp'] + preds['fn']))
