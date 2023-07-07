class Automobile:

    #constructor
    def __init__(self,brand,model,regno):
        # Instance Attribute
        self.brand=brand
        self.model=model
        self.regno=regno
    
    @property
    def make(self):
        return self.brand
    
    @make.getter
    def make(self):
        return self.brand
    
    @make.setter
    def make(self,brand):
        self.brand=brand

    @make.deleter
    def make(self):
        del self.brand