import random

class my_class():

    maths = ["+", "-", "*", "/", "%"]

    def hints(self, randomNumber, guessedNumber, somethingStupid):
        print("Too " + somethingStupid + " " + str(randomNumber))
        evalString = eval(str(randomNumber) + str(random.choice(self.maths)) + str(guessedNumber))
        print("Tip: ", evalString)

    def tipIn(self):
        playagain = True

        while playagain:
            count = 0
            randomNumber = random.randint(1, 100)
            boolean = True

            while boolean:
                try:
                    number = input("Errate die Zahl ")
                    number = int(number)
                    count += 1
                    if randomNumber == number:
                        print("Nice - Your Tries: " + str(count))
                        boolean = False

                        try:
                            suggest = input("Wanna try again? Y / n")[:1].lower()
                            if suggest != "y":
                                playagain = False
                                print("Thanks for the game!")
                        except:
                            print("You wanna fight me?")

                    elif randomNumber < number:
                        self.hints(randomNumber, number, "big")
                    elif randomNumber > number:
                        self.hints(randomNumber, number, "small")

                except:
                    print("thats not a number, punk")


my_object=my_class()
my_object.tipIn()
