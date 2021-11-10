class student:
    def __init__(self, scores):
        self.scores = scores

    def avg(self):
        return sum(self.scores) / len(self.scores)
# objec t / instance
louis = student (scores= [2,3,4,5,6,7,8,9])
lisa = student(scores =[1,2,3,4,5,6,66,8])

print(louis.avg())
print(lisa.avg())