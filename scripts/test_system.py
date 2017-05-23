#!/usr/bin/env python3
import utils.datasets as ds
import machine_learning.naivebayes as nb


def main():
    usr_vid, vid_usr, lusr, lvid = ds.combine_datas()
    del vid_usr
    test_system = ds.usr_specific(usr_vid, lvid, 10)
    for tested_usr in lusr:
        print(tested_usr)
        vecs_test = ds.list_features(
            test_system, [tested_usr], "test", lvid, "vec")
        labels_test = ds.list_features(
            test_system, [tested_usr], "test", lvid, "funny")
        vecs_train = ds.list_features(
            test_system, [tested_usr], "train", lvid, "vec")
        labels_train = ds.list_features(
            test_system, [tested_usr], "train", lvid, "funny")

        clf = nb.create_nb_model(vecs_train, labels_train)
        pred = nb.nb_predict(clf, vecs_test, labels_test)


if __name__ == '__main__':
    main()
