#narrow down our data
#for each GSM file, reduce to id (0), log_rat2n_mean (17), and subtype


import os
import numpy as np

directory = "/Users/nataliacarignano/Desktop/lsds/project/data/GSE10886_family.xml/"
shortDirectory = "/Users/nataliacarignano/Desktop/lsds/project/shortData/"
subtypeFile = "/Users/nataliacarignano/Desktop/lsds/project/data/226subtypes.csv"

def importData(file, cols):
	info = np.genfromtxt(file, usecols = cols) 
	return info
	
def getSubtype(file):
	
	return subtype
	
	
def writeData(info,fname):
	#create new file, write reduced data to new file
	newf = shortDirectory+"short"+fname[:-4]+".txt"
	
	np.savetxt(newf,info, header= "id	log_rat2n_mean", fmt = ['%i', '%1.3f'])



def main():

		
	#loop to load GSE10886 
	#for f in os.listdir(directory):
		
		#for each GSM file in folder:
	#	if f.startswith("GSM"):
	
	f = "GSM34464-tbl-1.txt"
	
	d = importData(directory+f, (0,17))
	writeData(d,f)		
			
		
main()
	
