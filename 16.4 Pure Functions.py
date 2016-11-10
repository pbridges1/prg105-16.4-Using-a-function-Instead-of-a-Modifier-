class Time:
    def __init__(self):
        self.minute = None
        self.second = None
        self.hour = None
    """Represents the time of day
    attributes: hour, minute, second
    """
time = Time()
time.hour = 10
time.minute = 10
time.second = 10


def time_to_sec(hr, mt):
    hr == 0
    mt == 0
    hr = time.hour * 60 * 60
    mt = time.minute * 60
    sec = time.second + hr + mt
    return sec
time_to_sec(time.hour, time.minute)
print ("Current time is " + '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second) + "\n")


def adjust(t, inc):
    t1 = t
    t1 = (t1 + inc)
    return t1

user = raw_input("Enter how many seconds you would like to adjust: \n")
new_time = adjust(time_to_sec(time.hour, time.minute), int(user))
print ("\nYou entered " + str(user) + " seconds")

answer = raw_input("Is this correct? \n")
while answer != "yes":
    user = raw_input("Please Re-enter how many seconds you would like to adjust: \n")
    print ("\nYou entered " + str(user) + " seconds")
    answer = raw_input("Is this correct? \n")


def int_to_time(seconds):
    t = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return t
times = int_to_time(new_time)
if time.second > 60:
    time.second -= 60
    time.minute += 1
if time.minute > 60:
    time.minute -= 60
    time.hour += 1
if time.hour > 12:
    time.hour -= 12

print ('\nThe new incremented time is ' + '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))
