

class Farm:
    numFarms = 0
    def __init__(self, location='Tatuin', animals=7, power=2929):
        self.location = location
        self.animals = animals
        self.power = power
        Farm.numFarms+=1

    def __del__(self):
        Farm.numFarms-=1

    def __str__(self):
        return 'Location: ' + self.location + ';\tAnimals: ' + str(self.animals) + ';\tPower: ' + str(self.power)

    @staticmethod
    def printNumFarms():
        print("Number of farms is: %s" % Farm.numFarms)


def main():
    farm1 = Farm('Cadath', 12, 1111)
    farm2 = Farm('Saskachevan', 5)
    farm3 = Farm(animals=121)
    print(str(farm1))
    print(str(farm2))
    print(str(farm3))
    Farm.printNumFarms()


if __name__ == '__main__':
    main()