from .automobile import Automobile

class Car(Automobile):

    def __init__(self,brand,model,regno):
        super().__init__(brand,model,regno)

    def start(self):
        print("Vrrmmmmm.....Engine is Online!")
        print("{} {} {} is Ready to Drive!".format(self.brand,self.model,self.regno))

    def battery(self):
        print("{} {} Battery Percentage is {}%".format(self.brand,self.model,self.batt))
        self.start()

    @classmethod
    def bajaj(cls,regno):
        g=cls("jaquer","n4",regno)
        g.start()

    @staticmethod
    def tvs(regno):
        cls = Car
        g=cls("swift","x1",regno)
        g.start()