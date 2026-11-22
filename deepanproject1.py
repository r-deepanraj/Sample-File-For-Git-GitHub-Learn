from deepanproject import sample

class student(sample):
    def __init__(self,name,age,study):
        super().__init__(name,age)
        self.study=study
    def view(self):
        print(self.name)
        print(self.age)
        print(self.study)


s1=student("Deepan",20,"MCA with Gen Ai")
s1.view()