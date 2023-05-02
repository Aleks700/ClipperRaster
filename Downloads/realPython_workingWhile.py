import os
import processing
wayToTIFSource = 'F:\Prokurotura'
maskLayer=r'C:\Users\A.Agadilov\Downloads\NewJoin.kml'
output_Path = wayToTIFSource+'_Cliper'

if not os.path.exists(output_Path):
    os.mkdir(output_Path)



# testLayer = 'F:\Prokurotura\HR_2304271126241\DZZ-HR_20200326065102_000526_E065N44_2A_PAN_HR_2304271126241\DZZ-HR_20200326065102_000526_E065N44_2A_PAN_HR_2304271126241\IMAGERY.TIF'
# testwayName = (testLayer.split('\\'))
# print(testwayName[-2]+'_'+testwayName[-1])
# newName = testwayName[-2].split('_')
# print(newName[-3]+"_"+newName[-2]+"_"+newName[-1])
tree = os.walk(wayToTIFSource)
print(tree)
tif = []

for address,dirs,files in tree:
    for name in files:
        if('.TIF' in name):
            print(os.path.join(address,name))
            tif.append(os.path.join(address,name))
            


for i in tif:
    testwayName = (i.split('\\'))
    #print(testwayName[-2]+'_'+testwayName[-1])
    newName = testwayName[-2].split('_')
    newToSaveName = newName[-3]+"_"+newName[-2]+"_"+newName[-1]+"_"+testwayName[-1]
    print(newToSaveName)
    output =os.path.join(output_Path,newToSaveName)
    print(output)
    processing.run("gdal:cliprasterbymasklayer", {'INPUT':i,'MASK':maskLayer,'OUTPUT':output})
print('its done')