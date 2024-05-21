import introduce

class IntroFam(introduce.Intro):

    def __init__(self,name,age,pet_name):
        super().__init__(name,age)
        self.pet_name = pet_name

    def cat_out(self):
        pettxt= "飼い猫の名前は、" + self.pet_name + "です"
        return pettxt

    
