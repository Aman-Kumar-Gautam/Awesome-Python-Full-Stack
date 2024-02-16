class Fruits:           # Define a class Using Fruits name

    @staticmethod
    def fav_fruits():           # Creating a function using fav_fruits name

        fruit_bucket = ['Apple', 'Banana', 'Cherry', 'Straw-Berry', 'Orange']
        print("My Favorite fruits are\n")
        for i in fruit_bucket:
            print(i)


a = Fruits()            # initialization object with the class
a.fav_fruits()          # calling function using dot(.)notation
