
import unittest


""" This class is responsible for the unit testing of the
    function 'getAndSaveFromCsv'
"""
    
class TestMyParsingFunction(unittest.TestCase):

    """ Setting up initial conditions for testing
        Creating a testing file and upon which function
        'getAndSaveFromCsv' will be tested
    """
    def setUp(self):
        global testFileName
        global testResultFileName
        global testFileString
        global resultString
        
        testFileName='testFile.csv'
        testResultFileName='testResultFile.txt'
        testFileString='Year,Month,Company A,Company B,Company C,Company D\n1990,Jan,10,15,20,30\n1990,Feb,15,5,5,35'
        resultString='Company A : Feb 1990\nCompany B : Jan 1990\nCompany C : Jan 1990\nCompany D : Feb 1990'

        testFile=open(testFileName,'w') ## Creating a testing file
        testFile.write(testFileString) ## Adding testing data in created file
        testFile.close();
        
    def test_getAndSaveFromCsv(self):
        getAndSaveFromCsv(testFileName,testResultFileName)
        resulttext=open(testResultFileName).read()
        
        ## Comparing result generated by the function and predefined result string
        self.assertTrue(resulttext==resultString) 



if __name__=='__main__':
   unittest.main()
