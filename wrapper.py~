import sys
import os

#os.system("module load root-cern/6.14.04-gcc52")


spectrometer="\""+sys.argv[1]+"\""
field="\""+sys.argv[2]+"\""


if(field=="\"Z\"" or field=="\"R\""):
	offset=["\"0.0\"","\"0.1\"","\"0.2\"","\"0.3\"","\"0.4\"","\"0.5\"", "\"-0.1\"", "\"-0.2\"", "\"-0.3\"","\"-0.4\"", "\"-0.5\""]
else:
	offset=["\"0.0\"","\"0.01\"","\"0.02\"","\"0.03\"","\"0.04\"","\"0.05\"", "\"-0.01\"", "\"-0.02\"", "\"-0.03\"","\"-0.04\"", "\"-0.05\""]




for j in offset:
	os.system("python goodsenspl.py \"\" \"\" "+spectrometer+" "+field+" "+j)
