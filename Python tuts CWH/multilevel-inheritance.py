class Electronic_gadgets:
    def accept_elec(self,data1):
        self.data1 = data1
        return f"{self.data1} is an electronic device"
    
class Pocket_gadgets(Electronic_gadgets):
    def accept_pocket(self,data2):
        self.data2 = data2
        return f"{self.data2} is an electronic device as well as pocket gadget"
    
class Mobile_devices(Pocket_gadgets):
    def accept_mobile(self,data3):
        self.data3 = data3
        return f"{self.data3} is an electronic device as well as pocket gadget as well as mobile device"
mobile = Mobile_devices()
print(mobile.accept_elec("mobile"))
print(mobile.accept_pocket("mobile"))
print(mobile.accept_mobile("mobile"))
    