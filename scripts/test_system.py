#!/usr/bin/env python3
import utils.datasets as ds
import machine_learning.naivebayes as nb
import utils.mesure as ms


def main():
    str0 = ""
    all_usr_funny = []
    all_usr_grade = []
    usr_vid, vid_usr, lusr, lvid = ds.combine_datas()
    del vid_usr
    test_system = ds.usr_specific(usr_vid, lvid, 10)
    for tested_usr in lusr:
        # print(tested_usr)
        vecs_train = ds.list_features(
            test_system, [tested_usr], "train", lvid, "vec")
        vecs_test = ds.list_features(
            test_system, [tested_usr], "test", lvid, "vec")
        labels_test_funny = ds.list_features(
            test_system, [tested_usr], "test", lvid, "funny")
        labels_train_funny = ds.list_features(
            test_system, [tested_usr], "train", lvid, "funny")
        labels_train_grade = ds.list_features(
            test_system, [tested_usr], "train", lvid, "grade")
        labels_test_grade = ds.list_features(
            test_system, [tested_usr], "test", lvid, "grade")

        model_funny = nb.create_nb_model(vecs_train, labels_train_funny)
        pred_funny = nb.nb_predict(model_funny, vecs_test, labels_test_funny)

        model_grade = nb.create_nb_model(vecs_train, labels_train_grade)
        pred_grade = nb.nb_predict(model_grade, vecs_test, labels_test_grade)

        str0 += "\n".join(["", tested_usr, ms.all_mesure_funny(pred_funny),
                           ms.all_mesure_grade(pred_grade)])
        all_usr_funny.extend(pred_funny)
        all_usr_grade.extend(pred_grade)
    str0 += "\n".join(["", "all_usr", ms.all_mesure_funny(all_usr_funny),
                       ms.all_mesure_grade(all_usr_grade)])
    print(str0)


if __name__ == '__main__':
    main()
