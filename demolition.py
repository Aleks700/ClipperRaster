import os
import processing
wayToTIFSource = 'F:\Real_chelyabinsk2023\Тункинский'
maskLayer=r'F:\Real_chelyabinsk2023\KML_AREA\Тункинский_area.kml'
folderName = maskLayer.split('\\')[-1].split('.')[0]
output_Path = os.path.join( os.path.dirname(maskLayer) ,folderName)
#wayToTIFSource = 'W:\share\Alexey\Real_chelyabinsk2023\HR_2305080829265'
#maskLayer=r'F:\Chelyabinsk\areaToClip\HR_2305080829265_Clip.kml'
#output_Path = os.path.join( os.path.dirname(maskLayer) ,'Cliper')




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
        if( name.endswith('.TIF') ):
            print(os.path.join(address,name))
            tif.append(os.path.join(address,name))
            


for i in tif:
    testwayName = (i.split('\\'))
    #print(testwayName[-2]+'_'+testwayName[-1])
    newName = testwayName[-2].split('_')
    # newToSaveName = newName[-3]+"_"+newName[-2]+"_"+newName[-1]+"_"+testwayName[-1]
    newToSaveName =testwayName[-2]+"_"+testwayName[-1]+"_"+'IMAGES.TIF'
    new_SHP_Name =testwayName[-2]+"_"+'Vector.kml'
    new_SHP_Clip =testwayName[-2]+"_"+'Clip_Vector.shp'
    # print(newToSaveName)
    output =os.path.join(output_Path,newToSaveName)
    outputSHP =os.path.join(output_Path,new_SHP_Name)
    outputSHP_Clipped =os.path.join(output_Path,new_SHP_Clip)
    # print(output)
    print('outputSHP',outputSHP)
    print('outputSHP_Clipped',outputSHP_Clipped)
    # print('i',i)
    processing.run("qgis:polygonfromlayerextent", {'INPUT':i,'OUTPUT':outputSHP})
    processing.run("qgis:clip", {'INPUT':maskLayer,'OVERLAY':outputSHP,'OUTPUT':outputSHP_Clipped})
    # processing.run("gdal:cliprasterbymasklayer", {'INPUT':i,'MASK':outputSHP_Clipped,'OUTPUT':output})
print('its done')