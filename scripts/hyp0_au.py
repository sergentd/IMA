# ! /usr/bin/python3
# @Djavan Sergent
from utils.function import list, get_filename, plot
from params import Params
import csv


class Predictor:
    def __init__(self, params):
        self.par = params
        self.au_dir = self.par.au_path + self.par.user + '/'

    def launch(self):
        labels = self.get_labels(self.par.eval_path + self.par.user + '.csv')
        predictions = []
        for m in self.get_matrix():
            video_name = get_filename(m)
            csv_path = self.au_dir + m
            predictions.append([self.analyze(csv_path, labels[video_name], video_name), labels[video_name]])

        # for p in predictions:
        #     print(p + str(predictions[p]))

        truePos, trueNeg, falsePos, falseNeg = self.scoring(predictions)
        return {'tp':truePos, 'tn':trueNeg, 'fp':falsePos, 'fn':falseNeg}

    def facialExp(self):
        faxp = self.get_facial_exp(self.par.eval_path + self.par.user + '.csv')
        predictions = []
        for m in self.get_matrix():
            video_name = get_filename(m)
            csv_path = self.au_dir + m
            predictions.append([self.eval_facial_expression(csv_path, faxp[video_name]), float(faxp[video_name])])
        return self.scoring_faxp(predictions)


    def get_matrix(self):
        return list(self.au_dir)

    def get_labels(self, ufile):
        labels = dict()
        with open(ufile, newline='') as csvfile:
            labels_reader = csv.DictReader(csvfile)
            for line in labels_reader:
                labels[get_filename(line['video_name'])] = line['funny']
        return labels

    def get_facial_exp(self, ufile):
        faxp = dict()
        with open(ufile, newline='') as csvfile:
            faxp_reader = csv.DictReader(csvfile)
            for line in faxp_reader:
                faxp[get_filename(line['video_name'])] = line['grade']
        return faxp


    # prediction
    def eval_facial_expression(self, mfile, grade):
        au = {'AU12_c':0}
        with open(mfile, newline='') as csvfile:
            matrix_reader = csv.DictReader(csvfile)
            cpt=0
            tot=0
            for line in matrix_reader:
                for el in line:
                    if el in au:
                        au[el] += float(line[el])
                        tot+= float(line[el])
                cpt += 1
        res = (tot/cpt)*10
        print(res, " : ", grade)
        return res


    # prediction
    def analyze(self, mfile, label, name):
        au6 = []; au6v = []
        au12 = []; au12v = []
        au5 = []; au5v = []
        match = 0

        with open(mfile, newline='') as csvfile:
            matrix_reader = csv.DictReader(csvfile)
            cpt = 0
            for line in matrix_reader:
                au6.append(line["AU06_c"]); au6v.append(line["AU06_r"])
                au12.append(line["AU12_c"]); au12v.append(line["AU12_r"])
                # au5.append(line["AU05_c"]); au5v.append(line["AU05_r"])
                if (line["AU06_c"] == str(1)) and (line["AU12_c"] == str(1)):
                    match += 1
                cpt += 1

        res = str((match/cpt >= 0.2))

        # Plot
        au = [au6, au12, au5]
        auv = [au6v, au12v, au5v]
        plot(name, label, res, au, auv)

        # Prediction
        return res

    def scoring(self, predictions):
        true_positif = 0; true_negatif = 0; false_positif = 0; false_negatif = 0
        for p in predictions:
            if p[0] == 'True':
                if p[1] == 'True':
                    true_positif += 1
                else:
                    false_positif += 1
            else:
                if p[1] == 'True':
                    false_negatif += 1
                else:
                    true_negatif += 1
        # print("P : TRUE\t|\tT : TRUE\t" + str(true_positif))
        # print("P : TRUE\t|\tT : FALSE\t" + str(false_positif))
        # print("P : FALSE\t|\tT : FALSE\t" + str(true_negatif))
        # print("P : FALSE\t|\tT : TRUE\t" + str(false_negatif))
        return true_positif, true_negatif, false_positif, false_negatif

    def scoring_faxp(self, predictions):
        avg = 0
        for p in predictions:
            avg += abs(p[0] - p[1])
        if len(predictions)>0:
            moy = avg/len(predictions)
        else:
            moy = 0
        return moy


if __name__ == "__main__":
    par = Params(env="dev")

    # list users
    evals = list(par.eval_path)
    list_users = []
    preds = {'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0}
    for e in evals:
        list_users.append(get_filename(e))

    results = 0
    for user in list_users:
        par.set_user(user)
        # predictor
        predic = Predictor(params=par)
        results = predic.launch()
        preds['tp'] += results['tp']
        preds['tn'] += results['tn']
        preds['fp'] += results['fp']
        preds['fn'] += results['fn']
        results += predic.facialExp()
    print(preds)
    print((preds['tp'] + preds['tn']) * 100 / (preds['tp'] + preds['tn'] + preds['fp'] + preds['fn']))
    print("*** écart moyen : " , results/len((list_users)), " ***")
