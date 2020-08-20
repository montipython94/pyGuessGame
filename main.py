import random

class my_class():
    # Array for mathematical operations
    calcType = ["+", "-", "*", "/", "%"]

    #prints an hint
    #Too small or too high
    #calculates randomBumber and guessedNumber with an random operatior
    def hints(self, randomNumber, guessedNumber, bigOrSmall):
        print("Too " + bigOrSmall)
        evalString = eval(str(randomNumber) + str(random.choice(self.calcType)) + str(guessedNumber))
        print("Tip: ", evalString)

    #starts the game
    def start(self):
        playagain = True

        while playagain:
            count = 0
            randomNumber = random.randint(1, 100)
            boolean = True

            while boolean:
                try:
                    number = input("Take a Guess: ")
                    number = int(number)
                    count += 1
                    if randomNumber == number:
                        print("Nice - You needed: " + str(count) + " guesses")
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


my_object = my_class()
my_object.start()
