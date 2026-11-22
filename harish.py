from deepanproject2 import student

class HarishDetails(student):
    def __init__(self,name,age,study,score):
        super().__init__(name,age,study,score)

    def view(self):
        print(self.name)
        print(self.age)
        print(self.study)
        print(self.score)


hd=HarishDetails("Harish",20,"McaGenAi",98)
hd.view()