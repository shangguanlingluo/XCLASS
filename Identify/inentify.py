#data
FreqMin = 9.758782812500e+04
FreqMax = 9.946144531250e+04
#data off
#FreqMin = 219345
#FreqMax = 221323

FreqStep = 0.25
#######################
TelescopeSize = 1.8 
######################
Inter_Flag = True

t_back_flag = False
#tBack = 0
#tslope = 0.0000000000E+00

nH_flag = False
#N_H = 3.0000000000E+24
#beta_dust = 2.0
#kappa_1300 = 0.02

#MolfitsFileName = "C2H5C-13-N.molfit"
#MolfitsFileName = "CH3OH.molfit"
#MolfitsFileName = "CH3OCHO.molfit"
#MolfitsFileName = "C2H5CN.molfit"
MolfitsFileName = "C2H5OH.molfit"
iso_flag = False
#IsoTableFileName = " "

RestFreq = 0.0
vLSR = 0.0
modeldata,log,TransEnergies,IntOptical,jobDir = myXCLASS ()



FileName = "I17016_37.txt"
NumHeaderLines = 0
expdata = LoadASCIIFile()




MinTransEnergy = 0.0
#data
xLowerLimit = 9.758782812500e+04
xUpperLimit = 9.946144531250e+04
#data off
#xLowerLimit = 219345
#xUpperLimit = 221323

yLowerLimit =-3
yUpperLimit =35
PlotTitle = "I17016_37"
LegendFlag = True
SaveFigureFile = " "
#OutputDevice = " "
myXCLASSPlot()

