# importing 'csv' and 'glob' library to be able to read .csv files and use file system
import csv
import glob

path = "C:/Users/khamz/Downloads/*.csv"

result = []
for files in glob.glob(path):
#TEST    
#    print(files)
# reading the .csv file starting from the third line
    with open(files) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        linecount = 0
        for row in csv_reader:
# counting the values in lines

#           print row
            if (linecount < 2):
                linecount=linecount+1
                continue
# assigning a variable for rows         
            BLOCK_ID = row[1]
            UNIT_ID = 0
#TEST
#        print row
            columncount = 0
            for column in row:
# counting columns starting from the third             
                if (columncount < 2):
                    columncount=columncount+1
                    continue
#TEST            
#            print "clo"+str(columncount)
# assigning the third variable 
                CODE = columncount-1
#TEST
#            print column
#            print "----------"
# finally creating final table with three columns, where UNIT_ID column uses
# last 9 digits of BLOCK_ID values and adds unique 4 integer values like (0001).
# The code generates the N number of lines from the N number of values in the cells.
# Each line has unique UNIT_ID and assigned CODE
                for number in range(1, int(column)+1):
                    result_row = [BLOCK_ID, str(BLOCK_ID[4:15])+str(UNIT_ID).zfill(4), CODE]
                    UNIT_ID = UNIT_ID+1
# TEST
#                print result_row
                    result.append(result_row)

                
                columncount=columncount+1
# writing the output to new .csv file
with open('Urbansim_RU_final100.csv', "ab") as csv_output:
    csv_writer = csv.writer(csv_output)
    csv_writer.writerows(result)

## Basically this code was created for data cleaning, table structure change,
## data preparation for UrbanSim cloud-based platform for urban planners
## that requires strict format of CSVs and unique codes for each household unit.
## Based on the data provided by (me) UrbanSim creates reports and forecasts
## for future urban development.
## For full understanding you can find input and output files in repository.
                    
                    
            
