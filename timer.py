# 7/11/2021
# Muath Alsubhi
import time


class Clock:
    def timer(self):
        print("Enter time:")
        try:
            t = int(input(">"))
            while t:
                mins, secs = divmod(t, 60)
                display = "{:02d}:{:02d}".format(mins, secs)
                print(display)
                time.sleep(1)
                t -= 1
            print("Time is up!")
        except ValueError:
            print("Please enter an integer value")
        except NameError:
            print("Please enter an integer value")


c = Clock()
c.timer()
