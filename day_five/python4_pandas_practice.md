# Homework 4 - pandas (YOUR NAME HERE)
### due 03/10/2021, to be turned on github  

<br>

Use this notebook and prompts to complete the homework. Throughout there will be hints and code provided to

### Things you will need:
- Install os, NumPy, pandas
- states_covid.csv
- Bloom_etal_2018_Reduced_Dataset.csv
- logfiles.tgz (or some other multiple file dataset)

**hint:** change your working directory to a directory for just this homework. Edit path below and run.


```python
hw_dir = "your/homework/path/here"
```


```python
cd $hw_dir
```

**import packages & check required datasets**


```python
import os
import numpy as np
import pandas as pd
```


```python
assert os.path.exists(os.path.join(hw_dir,'states_covid.csv')), 'states_covid.csv does not exist' 
```


```python
assert os.path.exists(os.path.join(hw_dir,'Bloom_etal_2018_Reduced_Dataset.csv')), 'Bloom_etal_2018_Reduced_Dataset.csv does not exist'
```


```python
!tar -xvzf logfiles.tgz
log_dir = os.path.join(hw_dir,'logfiles')
assert os.path.exists(log_dir), 'log_dir does not exist' 
```


```python

```

### Task 1 - DataFrame manipulation

Using **states_covid.csv**, we are going to read the data in as a DataFrame to manipulate, subset, and filter in various ways. 

**1.1 Read in states_covid.csv with date as a "date" dtype, and only columns consisting of the hospitalization (4 col), ICU (2 col), and Ventilators (2 col)**


```python

```

**1.2 List, in order, the 5 states with the highest numbers of people *currently* hospitalized, in the ICU, and on ventilation**  
hint: sort_values, uniqie


```python

```

**1.3 Identify the date for each state where the cumulative hosipitalized was greater than or equal to 1000**


```python

```

## Task 2 - DataFrame summarizing

Using **Bloom_etal_2018_Reduced_Dataset.csv**, we are going to do more dataframe manipulation and subsetting and summarizing  

**2.1 Read in Bloom_etal_2018_Reduced_Dataset.csv and create two new columns ('genus','species') that consists of the column *taxa* split at the underscore. Print out the head of this new dataframe and the number of unique genera**   

*hint:* pd.str.split(,expand=True)

for example:

| taxa | genus | species 
| :------ | :-- | :--- 
| Alosa_alabamae | Alosa | alabamae


```python

```

**2.2 Create a new dataframe with the mean *logbodysize* and *trophicposition* of each genera. Sort this data frame by the largest body size. Print the head of this dataframe. Which genera is the smallest and largest? What is the trophic position of the smallest and largest?**


```python

```

## Task 3 - Read in muliple files to a dictionary and make a DataFrame

### This is not an easy excersize. You will have some example code to start but the rest is up to you. You have done all these parts before so should just be linking them together

Using **logfiles**: we are going to do read in each file, get some data, append it to a dictionary to later make into a dataframe. 

First step is to find the necessary files. The number of files in the log files is 36, make sure you have that many as well


```python
!ls -l logfiles/*txt | wc -l 
```

    36



```python
logfiles = !find ./logfiles -name *txt #unix command to find files
logfiles = [os.path.abspath(x) for x in logfiles] #this finds the full path to the file
print(logfiles[0])
```


```python
assert(len(logfiles)==36), 'Do not have correct number of logfiles'
```

### Getting a little tricky here

Read in each of the logfiles, for each file extract:
- minimum temperature
- maximum temperature
- date of minimum temp 
- date of maximum temp 
- mean temp for each file. 

This data should all be appended for a dictionary within a for loop:    
Key should be the file name without the path or .txt extension  
Values should be (minTemp,maxTemp,minDate,maxDate,meanTemp)

I recommend making this work for one file first, then putting the rest in a for loop to do the rest.  

Below is an example of how to read in one file

*hint:* do not read date in as date object


```python
### set up data frame as you read in each file
infile = pd.read_csv(logfiles[0],sep='\t',engine='python')
infile.columns = ['Index','Date','Time','Temp','Type']
infile = infile[['Date','Time','Temp']]
infile.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Time</th>
      <th>Temp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9/29/2013</td>
      <td>8:00:00 AM</td>
      <td>34.7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9/29/2013</td>
      <td>8:35:00 AM</td>
      <td>34.8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9/29/2013</td>
      <td>9:10:00 AM</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9/29/2013</td>
      <td>9:45:00 AM</td>
      <td>35.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9/29/2013</td>
      <td>10:20:00 AM</td>
      <td>37.0</td>
    </tr>
  </tbody>
</table>
</div>



Do everything in steps, make sure it works. Calculate summaries with this one infile:

`minTemp =   
maxTemp =  
minDate = infile['Date'][infile['Temp'] == infile['Temp'].min()].unique()[0] #use this for minDate,maxDate  
maxDate =   
meanTemp =   `

To get you started, I suggest writing some dummy code in plain words to help outline your for loop:


```python
logfiles_dict = {}  
for f in logfiles:  
    #do something   
    #do not read date in as date object  
    #do more something   
    #do other stuff  
    #make print statements EVERYWHERE  
    #append to dict  
    #blahbahblah
```

Then do the real code below here. You don't need to turnin your thoughts. Just put it in there as a help reminder. Most people all still do this, no matter how advanced they are


```python

```

**Once you have created a DataFrame with all the logfiles, print the head and save it to an outfile using pd.to_csv() as logfiles_df.csv** 


```python

```
