#class unit:
#    def __init__(self):
#        print("unit 생성자")

#class flyable:
#    def __init__(self):
#        print("flyable 생성자")

#class flyableunit(flyable,unit):
#    def __init__(self):
#        #super().__init__()
#        unit.__init__(self)
#        flyable.__init__(self)


#dropship = flyableunit()


class Email :
    sender = ""
    def send_mail(self,recv,title,content):
        print("From:\t" + self.sender)
        print("TO:\t" + recv)
        print("Title" + title)
        print("Content\n",content)
        print("-"*20)

