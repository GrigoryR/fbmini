"""
Contact object should have the following data points:
  First Name
  Last Name
  Middle Initial
  Home Phone Number
  Mobile Phone Number
  Work Phone Number
  Street Address
  City
  State
  Zip Code
  Country
  Email Address
  Notes
  Pictures
 All data points except First Name and Last Name are optional

 class Apartment(House): #Apartment inherits from House
    def __init__(self, pID, aptNo, rent, isVacant = False):
        self._pID = pID
        self._aptNo = aptNo
        self._rent = rent
        self._isVacant = isVacant

    @property
    def pID(self):
        return self._pID

    @setter.pID
    def pID(self, pID):
        self._pID = pID

"""


class Contact:
    def __init__(self, fname, lname):
        self._First_Name = fname
        self._Last_Name = lname

    @property
    def First_Name(self, fname):
        return fname

    @First_Name.setter
    def First_Name(self, fname):
        self._First_Name = fname

    @property
    def Last_Name(self, lname):
        return lname

    @Last_Name.setter
    def Last_Name(self, lname):
        self._Last_Name = lname
