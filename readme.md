Overall Approach: Here we were dealing with two sets data--one from the .csv file and one fromt he json file. The first objective was to pull both sets of data and get them into a workable format--in this case a list of dictionaries. From there it was easy to itrate through the data, put what I needed into a new dictionary, and creat a csv file with that data. 

How to run: Run the Assignment.py file. Once you run the file it prompt you for the location of the csv data. The csv file is included and typing "sales_data.csv" in response to the prompt is all that is needed. You will see that a new file in teh directory called "aggregated_report.csv" has been created in the directory.

Room for improvement: This script does assume there will only be 2 categories: gadgets and tools. Ideally in the future it would look through the CSV file and account for every category on it. 
