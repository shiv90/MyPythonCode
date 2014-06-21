
import unittest
import sys

"""This function will create a result file by name provided in parameter
    sourcefilename : source csv file
    resultfilename : result txt file
"""
def getAndSaveFromCsv(sourcefilename,resultfilename):
    file=open(sourcefilename)
    firstLine=file.readline().replace('\n','').split(',') ## Getting all company names
    firstLine.pop(0) ## Popping out year from list
    firstLine.pop(0) ## Popping out month from list
    secondline=file.readline()
    secondlinelist=secondline.split(',')
    
    ## Save value, year and month in Hahmap for better speed and less code
    mapForMaxValue={}

    ## Populating map with first row value for comparison
    for k in range(0,len(secondlinelist)-2):
        mapForMaxValue[k]=(secondlinelist[k+2],secondlinelist[0],secondlinelist[1])
    for i, line in enumerate(file):
        newLine=line.split(',')
        for k in range(0,len(newLine)-2):
            if int(newLine[k+2])>int(mapForMaxValue[k][0]):
                mapForMaxValue[k]=(newLine[k+2],newLine[0],newLine[1])
                
    ## Creating and saving result in result file
    newFile=open(resultfilename,'w')
    
    for k in range(len(mapForMaxValue)-1):
        newFile.write(firstLine[k] +' : '+mapForMaxValue[k][2]+' '+mapForMaxValue[k][1]+"\n")
        
    newFile.write(firstLine[len(mapForMaxValue)-1] +' : '+mapForMaxValue[len(mapForMaxValue)-1][2]+' '+mapForMaxValue[len(mapForMaxValue)-1][1])
    newFile.close()
    

##def main():
  ##  getAndSaveFromCsv(sys.argv[1],sys.argv[2])


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