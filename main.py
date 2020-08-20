import random


class GuessGame:

    # Array for mathematical operations
    calcType = ["+", "-", "*", "/", "%"]

#   prints an hint
#   Too small or too high
#   calculates randomnumber and guessednumber with an random operator
    def hints(self, randomnumber, guessednumber, bigorsmall):
        print("Too " + bigorsmall)
        evalString = eval(str(randomnumber) + str(random.choice(self.calcType)) + str(guessednumber))
        print("Tip: ", evalString)

#   starts the game
    def start(self):
        playagain = True

        while playagain:
            count = 0
            randomnumber = random.randint(1, 100)
            boolean = True

            while boolean:
                try:
                    number = input("Take a Guess: ")
                    number = int(number)
                    count += 1
                    if randomnumber == number:
                        print("Nice - You needed: " + str(count) + " guesses")
                        boolean = False

                        try:
                            suggest = input("Wanna try again? Y / n")[:1].lower()
                            if suggest != "y":
                                playagain = False
                                print("Thanks for the game!")
                        except:
                            print("You wanna fight me?")

                    elif randomnumber < number:
                        self.hints(randomnumber, number, "big")
                    elif randomnumber > number:
                        self.hints(randomnumber, number, "small")

                except ValueError:
                    print("thats not a number, punk")


my_object = GuessGame()
my_object.start()
