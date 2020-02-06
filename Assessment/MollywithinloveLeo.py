class PersonInLove():
    def __init__(self, personA, personB):
        self.personA = personA
        self.personB = personB

    def howDidTheyMet(self, when, where, how):
        print('{0} at {1} how {2}'.format(when ,where , how))

    def howDidTheyKnow(self, when, where, how):
        print('{0} at {1} {2}'.format(when, where, how))

    def howDidTheyPropose(self,who,where, content):
        print('{0} proposed at {1} with his heart word: {2}'.format(who, where, content))
        pass

    def toString(self):
        print(self.personA + ' is in love with ' + self.personB)

#Molly = 'Molly'
#Leo = 'Leo'
A=PersonInLove('Molly', 'Leo')
A.howDidTheyMet('2018-11-18 10:20:00',
                'Starpoint, 319 Pasir panjang road #04-00',
                'Because of Wenjia')
A.howDidTheyKnow('2019-10-10', 'NUS', 'IT 5003 due to Wenjia')
A.howDidTheyPropose('2019-10-25', 'Singapore River', 'Are you willing to give me your hand and count on me?')
A.toString()


