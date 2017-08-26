#narrow down our data
#for each GSM file, reduce to id (0), log_rat2n_mean (17), and subtype


import os
import numpy as np

directory = "/Users/nataliacarignano/Desktop/lsds/project/data/GSE10886_family.xml/"
shortDirectory = "/Users/nataliacarignano/Desktop/lsds/project/shortData/"

def importData(file):
	dt = {'names':["id","log_rat2n_mean"], 'formats':[np.int, np.float_]}
	info = np.genfromtxt(file, usecols = (0,17)) #, names=["id","log_rat2n_mean"])
	return info
	
def writeData(info,fname):
	#create new file, write reduced data to new file
	newf = shortDirectory+"short"+fname[:-4]+".txt"
	
	np.savetxt(newf,info, header= "id	log_rat2n_mean", fmt = ['%i', '%1.3f']) #, fmt= ['%f', '%1.4f'])



def main():

		
	#loop to load GSE10886 
	#for f in os.listdir(directory):
		
		#for each GSM file in folder:
	#	if f.startswith("GSM"):
	
	f = "GSM34464-tbl-1.txt"
	
	d = importData(directory+f)
	writeData(d,f)		
			
		
main()
	
