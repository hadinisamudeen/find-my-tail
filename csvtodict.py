#This snippet shows how to read a CSV file, and make separate dictionaries for 8 different outlets available in the UK, with their pricings.

import csv

with open('Price List_2.csv') as file:
    reader = csv.reader(file)
   
    def_dict = {}
    count = 0
    lista = []
    listb = []
    listc = []
    listd = []
    liste = []
    listf = []
    listg = []
    listh = []
    #Creating a list of lists.
    listoflists = [lista,listb,listc,listd,liste,listf,listg,listh]
    #Here, the csv file is being read, the necessary values are added into each list,
    #and a dummy dictionary is created so as to be used later on.
    for row in reader:
        for i in range (0,8):
            #adds in the column values to each of the lists.
            listoflists[i].append(row[i+3])
       
        #print(row[5])
        def_dict[row[0]] = 'X'
       
        if count>34:
            break
       
        count += 1
#creating a list of the keys of the dictionary.
#This is useful as they would be used to update the dictionary values,
# when each of them are singularly created
    dictlist = list(def_dict.keys())
    
    del def_dict["ï»¿Product"]
    coop_dict = def_dict.copy()
    for i in range(0,len(lista)):
        coop_dict.update({(dictlist[i]): lista[i]})
   
#creating specific dictionaries: The dummy dict is copied, 
# and the values are updated.   
    tesco_dict = def_dict.copy()
    for i in range(0,len(listb)):
        tesco_dict.update({(dictlist[i]): listb[i]})
   

    saints_dict = def_dict.copy()
    for i in range(0,len(listc)):
        saints_dict.update({(dictlist[i]): listc[i]})
     
    asda_dict = def_dict.copy()
    for i in range(0,len(listd)):
        asda_dict.update({(dictlist[i]): listd[i]})
   
    morrisons_dict = def_dict.copy()
    for i in range(0,len(liste)):
        morrisons_dict.update({(dictlist[i]): liste[i]})

   
    aldi_dict = def_dict.copy()
    for i in range(0,len(listf)):
        aldi_dict.update({(dictlist[i]): listf[i]})
   
 
    waitrose_dict = def_dict.copy()
    for i in range(0,len(listg)):
        waitrose_dict.update({(dictlist[i]): listg[i]})
   
     
    iceland_dict = def_dict.copy()
    for i in range(0,len(listh)):
        iceland_dict.update({(dictlist[i]): listh[i]}) 
