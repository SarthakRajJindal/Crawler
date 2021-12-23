# Crawler

This is a python based web crawler made for IEEE papers.
It uses https://ieeexplore.ieee.org/document/8301529 as the start point and recursively traverses through the reference papers and extracts abstract data from them until it obtains a prespecified number of papers.

# Running Instructions

1. Run the main.py file using python : "python main.py"
2. Enter the number of papers that are needed to be scrapped.
3. Wait for the scaping process, it can take a couple of minutes.

Program will print the traversed document links of the papers.  
Also you can find the details of these paper in a csv file "papers.csv".  
It will have the information regarding the document link, title and abstract of the paper.

Sample run is shown below :

![174bfe57-b6c9-40a7-8ea2-a5f0ff2b25c2](https://user-images.githubusercontent.com/58340535/147193341-8f1e9fab-b259-417b-bcf1-df6d9f42bcea.jpg)

An output CSV file will be generated containing the details of all the papers. 
