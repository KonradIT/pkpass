from zipfile import ZipFile
import json
from pprint import pprint
import magic
import datetime

class Pkpass:
    def __init__(self, pkpass):

        # house keeping
        self.mimeHelper = magic.open(magic.MAGIC_MIME)
        self.mimeHelper.load()
        self.file = pkpass
        self.fileStruct = {
            "info": "pass.json",
            "sig": "signature",
            "manifest": "manifest.json"
        }

    def isValid(self):
        # is a valid pkpass
        return "application/zip" in self.mimeHelper.file(self.file)

    def read(self):
        if self.isValid():
            with ZipFile(self.file, 'r') as zipfile:
                self.data = zipfile.read(self.fileStruct.get("info"))
                return json.loads(self.data)
        return {}

    def print(self):
        pprint(self.read())


class Airline:
    def __init__(self, data):
        self.data = data

    def getFlightInfo(self):
        return self.data.get("boardingPass").get("auxiliaryFields")

    def getPrimaryFields(self):
        return self.data.get("boardingPass").get("primaryFields")

    def getBoardingTime(self, parse=False):
        for item in self.getFlightInfo():
            if item.get("key") == "boardingTime":
                if parse:
                    return datetime.datetime.strptime("%s/%s" % ( datetime.date.today().year, item.get("value")), '%Y/%d/%m %H:%M')
                return item.get("value")

    def getDepartureTime(self, parse=False):
        for item in self.getFlightInfo():
            if item.get("key") == "departureTime":
                if parse:
                    return datetime.datetime.strptime("%s/%s" % ( datetime.date.today().year, item.get("value")), '%Y/%d/%m %H:%M')
                return item.get("value")

    def getGate(self):
        for item in self.getFlightInfo():
            if item.get("key") == "term-gate":
                return item.get("value")

    def getFlightNumber(self):
        for item in self.getFlightInfo():
            if item.get("key") == "flightNumber":
                return item.get("value")

    def getSecondaryFields(self):
        return self.data.get("boardingPass").get("secondaryFields")

    def getMetadata(self):
        return {
            "desc": self.data.get("description"),
            "airline": self.data.get("organizationName"),
            "serial": self.data.get("serialNumber"),
            "locations": self.data.get("locations")
        }

    def getUserInfo(self):
        return self.data.get("userInfo")
