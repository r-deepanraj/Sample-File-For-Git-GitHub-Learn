from deepanproject1 import student

class student(student):
    def __init__(self,name,age,study,score):
        super().__init__(name,age,study)
        self.score=score
    def view(self):
        print(self.name)
        print(self.age)
        print(self.study)
        print(self.score)


s1=student("Deepan",20,"MCA with Gen Ai",98)
s1.view()