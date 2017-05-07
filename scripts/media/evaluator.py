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
        output = "user_id;video_name;grade\n"
        for e in self.evaluations:
            output += e + "\n"
        open(file_path, mode="w+").write(output)
        print("evaluation saved in " + file_path)
