from .automobile import Automobile

class Bike(Automobile):
    # class attributes
    type="superbikes"

    #constructor
    def __init__(self,brand,model,regno):
        # Instance Attribute
        super().__init__(brand,model,regno)
        self.batt=0

    def start(self):
        print("Vrrmmmmm.....Engine is Online!")
        print("{} {} {} is Ready to Drive!".format(self.brand,self.model,self.regno))

    def battery(self):
        print("{} {} Battery Percentage is {}%".format(self.brand,self.model,self.batt))
        self.start()

    @classmethod
    def bajaj(cls,regno):
        g=cls("pulsar","ns200",regno)
        g.start()

    @staticmethod
    def tvs(regno):
        cls = Bike
        g=cls("apache RTR","180",regno)
        g.start()

    @classmethod
    def build_from_automobile(cls,d:Automobile):
        c=cls(d.brand,d.model,d.regno)
        return c

    @staticmethod
    def anything():
        print("Iam @staticmethod")

    @staticmethod
    def derive_max_speed():
        print("Iam All Independent! @staticmethod")

def fm(x):
    print("Iam {}".format(x))