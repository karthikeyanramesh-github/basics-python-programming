class bike:
    # class attributes
    type="motorcycles"

    #constructor
    def __init__(self,brand,model,regno):
        self.brand=brand
        self.model=model
        self.regno=regno
        self.batt=0

    def start(self):
        print("Vrrmmmmm.....Engine is Online!")
        print("{} {} is Ready to Drive!".format(self.brand,self.model))

    def battery(self):
        print("{} {} Battery Percentage is {}%".format(self.brand,self.model,self.batt))
        self.start()
    
    @classmethod
    def types(cls):
        print(cls.type)
        g=cls("Yamaha","R15"," ")
        g.start()

    @classmethod
    def build_bike():
        pass

    # @staticmethod
    # def anything():
    #     print("Iam @staticmethod")

    @staticmethod
    def derive_max_speed():
        print("Iam All Independent! @staticmethod")

# def fm(x):
#     print("Iam {}".format(x))