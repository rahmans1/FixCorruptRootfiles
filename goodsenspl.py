import sys
import ROOT as R
import os
import subprocess


if not sys.argv[1]:
	output="/global/scratch/rahmans/scratch/sensitivityStudy"
else:
	output= sys.argv[1]
if not sys.argv[2]:
	jsub="/home/rahmans/jobSubmission/sensitivityStudy/jsub"
else:
	jsub=sys.argv[2]
if not sys.argv[3]:
	spectrometer="sensUpstream"
else:
	spectrometer=sys.argv[3]

if not sys.argv[4]:
	maptype=""
else:
	maptype=sys.argv[4]
	
if not sys.argv[5]:
	mapvalue=""
else:
	mapvalue=sys.argv[5]
	




generator = ["moller", "elastic", "inelastic"]
runrange= range(1,101)

output=output+"/"+spectrometer+maptype+mapvalue
jsub=jsub+"/"+spectrometer+maptype+mapvalue


for gen in generator:
	count=0
	for i in runrange:
		filepath0 = output+"/"+gen+"/"+gen+"_"+str(i)+"_t0.root"
		filepath1 = output+"/"+gen+"/"+gen+"_"+str(i)+"_t1.root"
		filepath2 = output+"/"+gen+"/"+gen+"_"+str(i)+"_t2.root"
		filepath3 = output+"/"+gen+"/"+gen+"_"+str(i)+"_t3.root"
		filepath4 = output+"/"+gen+"/"+gen+"_"+str(i)+"_t4.root"
		
		if os.path.exists(filepath0) and os.path.exists(filepath1) and os.path.exists(filepath2) and os.path.exists(filepath3) and os.path.exists(filepath4) :
                	corrupt=False  	
			f0=R.TFile(filepath0)
			f1=R.TFile(filepath1)
			f2=R.TFile(filepath2)
			f3=R.TFile(filepath3)
			f4=R.TFile(filepath4)
                	if(f0.IsZombie() or f1.IsZombie() or f2.IsZombie() or f3.IsZombie() or f4.IsZombie()):
				print(f0.GetName()+" is jombie \n")
				corrupt=True
			if(f0.TestBit(R.TFile.kRecovered) or f1.TestBit(R.TFile.kRecovered) or f2.TestBit(R.TFile.kRecovered) or f3.TestBit(R.TFile.kRecovered) or f4.TestBit(R.TFile.kRecovered)):
				print(f0.GetName()+" is recovered \n")
				corrupt=True
			if corrupt:
				subprocess.call("qsub -l nodes=1:ppn=5,pmem=3gb,walltime=0:10:00 "+jsub+"/"+gen+"/"+gen+"_"+ str(i)+ ".pbs", shell=True)
				print(f0.GetName()+" is corrupt. Deleting file. \n")	
			else:
				count=count+5
		else:
			print(filepath0+" does not exist")
			subprocess.call("qsub -l nodes=1:ppn=5,mem=3gb,walltime=0:10:00 "+jsub+"/"+gen+"/"+gen+"_"+ str(i)+ ".pbs", shell=True)
	
	print(filepath0+" "+str(count))
	
