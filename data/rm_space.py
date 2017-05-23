# ! /usr/bin/python3
import os

source = ["au_matrix/usr/", "au_matrix/resize/"]

for s in source:
    for path_id_usr in os.listdir(s):
        for vid_yt in os.listdir(s + path_id_usr):
            with open(s + path_id_usr + "/" + vid_yt, 'r') as stream:
                new = stream.read().replace(" ", "")
            with open(s + path_id_usr + "/" + vid_yt, 'w') as stream:
                stream.write(new)
