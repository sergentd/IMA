#!/usr/bin/env python3
import utils.datasets as ds
import machine_learning.naivebayes as nb
import utils.mesure as ms


def main():
    str0 = ""
    all_usr_funny = []
    all_usr_grade = []

    usr_vid, vid_usr, lusr, lvid = ds.combine_datas()
    del usr_vid, lvid
    hyp2 = ds.by_X(vid_usr)
    for vid in sorted(hyp2):
        list_uv = hyp2[vid]["keys"]

        vecs_test = ds.list_features(
            hyp2, [vid], "test", lusr, "vec")
        labels_test_funny = ds.list_features(
            hyp2, [vid], "test", lusr, "funny")
        labels_test_grade = ds.list_features(
            hyp2, [vid], "test", lusr, "grade")

        vecs_train = ds.list_features(
            hyp2, [vid], "train", list_uv, "vec")
        labels_train_funny = ds.list_features(
            hyp2, [vid], "train", list_uv, "funny")
        labels_train_grade = ds.list_features(
            hyp2, [vid], "train", list_uv, "grade")

        model_funny = nb.create_nb_model(vecs_train, labels_train_funny)
        pred_funny = nb.nb_predict(model_funny, vecs_test, labels_test_funny)

        model_grade = nb.create_nb_model(vecs_train, labels_train_grade)
        pred_grade = nb.nb_predict(model_grade, vecs_test, labels_test_grade)

        str0 += "\n".join(["", vid, ms.all_mesure_funny(pred_funny),
                           ms.all_mesure_grade(pred_grade)])
        all_usr_funny.extend(pred_funny)
        all_usr_grade.extend(pred_grade)
    str0 += "\n".join(["", "all_vid", ms.all_mesure_funny(all_usr_funny),
                       ms.all_mesure_grade(all_usr_grade)])
    print(str0)


if __name__ == '__main__':
    main()
