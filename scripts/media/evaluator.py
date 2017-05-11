#! /usr/bin/python3


class Evaluator:
    """
    A simple class to store user's evaluation
    @Djavan Sergent
    """
    def __init__(self, params):
        self.evaluations = []
        self.par = params

    def add(self, evaluation):
        self.evaluations.append(evaluation)

    def write(self):
        file_path = self.par.eval_path + self.par.user + ".csv"
        output = "user_id,video_name,grade,funny\n"
        for e in self.evaluations:
            output += str(e.user) + "," + e.video+"," + str(e.grade) + "," +str(e.funny) + "\n"
        open(file_path, mode="w+").write(output)
        print("evaluation saved in " + file_path)


class Evaluation:
    def __init__(self, evaluator, user="", video="", grade="", funny=""):
        self.master = evaluator
        self.user = user
        self.video = video
        self.grade = grade
        self.funny = funny

    def add(self):
        self.master.add(self)
