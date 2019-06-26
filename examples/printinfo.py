from pkpass import Pkpass, Airline
madridToBarcelona = Pkpass("../samples/AirEuropaPassbook.pkpass")

flight = Airline(madridToBarcelona.read())
print("Boarding time: ", flight.getBoardingTime(parse=True))
print("Departure time: ", flight.getDepartureTime(parse=True))
print("Gate: ", flight.getGate())
print("Info: ", flight.getUserInfo())
