#======================= DO NOT ADD ANY THING HERE - START ====================
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir  = os.path.dirname(currentdir)
sys.path.append(parentdir)
#======================= DO NOT ADD ANY THING HERE - END ======================
from testCases.setup import testSetup
from testCases.setup import apiTestSetup

class testApisnc(testSetup):
    def test_api_1(self):
        test = {
            "id"       : "snc-001",             # test case id - aio
            "status"   : "active",              # depricated? what to do for aio?
            "dataFile" : r"C:\Users\sesa426398\Documents\snc\CM.xlsx",
            "sheetName": "startConfig"
        }
        # apiTestSetup.apitests().executor(**test)
        apiTestSetup.executeTest(self=self, **test)

    # def test_api_idno2(self):
    #     test = {
    #         "id"       : "tc-002",  #test case id - aio
    #         "dataFile" : r"filename.xlsx",
    #         "sheetName": "...",
    #         "status"   : "depricated"
    #     }
    #     apiTestSetup.
    #     apiTestSetup.executeTest(reporterObj=self.testReporterObj, **test)