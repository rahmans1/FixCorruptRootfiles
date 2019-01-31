import sys
import ROOT as R
import os


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
	maptype="R"
else:
	maptype=sys.argv[4]
	
if not sys.argv[5]:
	mapvalue="0.0"
else:
	mapvalue=sys.argv[5]
	




generator = ["moller", "elastic", "inelastic"]
runrange= range(1,501)

output=output+"/"+spectrometer+maptype+mapvalue
jsub=jsub+"/"+spectrometer+maptype+mapvalue


for gen in generator:
	count=0
	for i in runrange:
		filepath = output+"/"+gen+"/"+gen+"_"+str(i)+".root"
		if os.path.exists(filepath):
                	corrupt=False  	
			f=R.TFile(filepath)
                	if(f.IsZombie()):
				print(f.GetName()+" is jombie \n")
				corrupt=True
			if(f.TestBit(R.TFile.kRecovered)):
				print(f.GetName()+" is recovered \n")
				corrupt=True
			if corrupt:
				os.system("qsub -l procs=1,pmem=3gb,walltime=0:10:00 "+jsub+"/"+gen+"/"+gen+"_"+ str(i)+ ".pbs")
				print(f.GetName()+" is corrupt. Deleting file. \n")	
			else:
				count=count+1
		else:
			print(filepath+" does not exist")
			os.system("qsub -l procs=1,pmem=3gb,walltime=0:10:00 "+jsub+"/"+gen+"/"+gen+"_"+ str(i)+ ".pbs")
	
	print(filepath+" "+str(count))
	
