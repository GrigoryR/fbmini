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
    def __init__(self, fname, lname, mname, hm, wk, mn):
        self._First_Name = fname
        self._Last_Name = lname
        self._Middle_Name = mname
        self._Home_Number = hm
        self._Work_Phone = wk
        self.Mobile_Number = mn
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

    @property
    def Middle_Name(self, mname):
        return mname

    @Home_Number.setter
    def Home_Number(self, hm):
        self._Home_Number = hm   @property
    def Home_Number(self, hm):
        return hm

    @property
    def Work_Number(self, wk):
        return hm    @Home_Number.setter
    def Work_Number(self, wk):
        self._Work_Number = wk   @property
    def Work_Number(self, wk):
        return wk

    @property
    def Mobile_Number(self, mn):
        return wk    @Home_Number.setter
    def Mobile_Number(self, mn):
        self._Middle_Name =    @property
    def Mobile_Number(self, mn):
        return hm

    @property
    def Mobile_Number(self, mn):
        return mn
