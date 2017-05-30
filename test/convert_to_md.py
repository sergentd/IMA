#!/usr/bin/env python3

from collections import defaultdict as dd


def convert_to_md(f):
    with open(f) as stream:
        lines = stream.readlines()
    tab = []
    add = False
    str0 = ""
    for line in lines:
        if line[:4] == "C:Pr":
            add = True
            tab.append(line)
        elif (line[:3] == "Acc" or line[:3] == "Err") and add:
            add = False
            tab.pop(1)
            tab = ["{}{}{}".format("| ", " | ".join(t.split()), " |")
                   for t in tab]
            tab.insert(
                1, "|" + "|".join([":---:"for i in tab[0].split(" | ")]) + "|")
            # str0 += "\n".join(tab) + "\n\n"
            str0 += line + "\n"
            tab = []
        elif add:
            tab.append(line)
        else:
            str0 += line + "\n"
    return str0


def get_mesure_by_X(file):
    str0 = ""
    dic = dd(lambda: dd(str))
    with open(file) as stream:
        lines = [l for l in stream.read().split("\n") if l != '']
    X = ""
    for l in lines:
        l = l.split("\t")
        if len(l) > 1:
            dic[X][l[0]] = l[-1]
        else:
            X = l[0]
    firstline = ["Mesure"] + [k for k in sorted(dic.keys())]
    str0 += "{}{}{}".format("| ", " | ".join(firstline), " |\n")
    str0 += "|" + "|".join([":---:"for i in str0.split(" | ")]) + "|\n"
    for ms in sorted(dic[firstline[1]]):
        line = [ms[:-1]]
        for X in sorted(dic):
            line.append(dic[X][ms])
        str0 += "{}{}{}".format("| ", " | ".join(line), " |\n")
    return str0 + "\n\n"


def main():
    # files = ['test_hyp1_nb.txt', 'test_hyp2_nb.txt', 'test_sys_nb.txt',
    #         'test_hyp1_nn.txt', 'test_hyp2_nn.txt', 'test_sys_nn.txt']
    # for file in files:
    #    open(file[:-4] + ".md", "x").write(convert_to_md(file))
    files = ['test_hyp1_nb.res', 'test_hyp2_nb.res', 'test_sys_nb.res',
             'test_hyp1_nn.res', 'test_hyp2_nn.res', 'test_sys_nn.res']
    str0 = ""
    for file in files:
        str0 += file[: -4] + "\n\n"
        str0 += get_mesure_by_X(file)
    open("all_res.md", "x").write(str0)


if __name__ == '__main__':
    main()
