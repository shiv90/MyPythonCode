
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
    

def main():
	getAndSaveFromCsv(sys.argv[1],sys.argv[2])
