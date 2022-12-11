# Activity1.py
# A = P(1 + rt)


# Calculate Simple Interest
def calculate(principle, rate, time):
    # Check and convert them all to floats. try & except so if the value isn't valid we just just 'catch' it.
    if not isinstance(principle, float):
        try:
            principle = float(principle)
        except:
            raise Exception("Value 'principle' is not valid type int or float.")
    if not isinstance(rate, float):
        try:
            rate = float(rate)
        except:
            raise Exception("Value 'rate' is not valid type int or float.")
    if not isinstance(time, float):
        try:
            time = float(time)
        except:
            raise Exception("Value 'time' is not valid type int or float.")
    if not isinstance(principle, float):
        raise Exception("Value principle in not valid type int or float.")
    if rate > 1: # Convert rate to decimal from percentage
        rate = rate * 0.01
        round(rate, 1)
    if principle < 0 or rate < 0 or time < 0: # Make sure nothing is negative
        raise Exception("Your values cannot be negative!")
    result = principle * (1 + rate * time)
    result = round(result, 2) # Round to hundreds
    print("Interest alone: " + str(result - principle))
    print("Principle with interest: " + str(result))


calculate(10000, 1.5, 5) # Valid
try:
    calculate(-21, -1, 3) # Invalid, throws
except Exception as e:
    print(str(e))

try:
    def not_a_valid():
        print("what?")
    calculate(not_a_valid, not_a_valid, not_a_valid) # Also invalid, throws
except Exception as e:
    print(str(e))
