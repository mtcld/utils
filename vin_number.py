import urllib
import re
links = [
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/protestlex001/vin_number/331/original/IMG_20170414_110850.jpg?1513594791", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/protestlex001/vin_number/339/original/AI-potential-in-claims-automation-motionscloud.jpg?1513595112", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R3917/vin_number/348/original/image.jpg?1513610358", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017a0000/vin_number/351/original/image.jpg?1513620180", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/TestLex007/vin_number/362/original/AI-potential-in-claims-automation-motionscloud.jpg?1513629682", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/TestLex007/vin_number/371/original/1498514740463.jpg?1513629728", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/Lextest007/vin_number/379/original/1498514740463.jpg?1513632738", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R3963/vin_number/388/original/image.jpg?1513690329", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R3891/vin_number/419/original/Resized952017121595163637.jpg?1513719489", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4152/vin_number/455/original/025.JPG?1513722043", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4338/vin_number/466/original/image.jpg?1513783009", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R3551/vin_number/488/original/image.jpg?1513787257", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4362/vin_number/491/original/image.jpg?1513863963", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4390/vin_number/501/original/20171221_151933.jpg?1513891361", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4471/vin_number/530/original/image.jpg?1513973132", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4384/vin_number/539/original/IMG_20171222_142053805.jpg?1513974227", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4568/vin_number/559/original/image.jpg?1514151759", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4568/vin_number/567/original/image.jpg?1514152002", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4713/vin_number/587/original/image.jpg?1514391931", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4373/vin_number/599/original/image.jpg?1514402407", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4650/vin_number/607/original/image.jpg?1514410746", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4683/vin_number/617/original/image.jpg?1514412150", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4763/vin_number/633/original/1514413465914-105710778.jpg?1514413491", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4687/vin_number/636/original/image.jpg?1514416703", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4743/vin_number/647/original/image.jpg?1514480518", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4837/vin_number/654/original/image.jpg?1514557013", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4568/vin_number/662/original/1514570740546769377447.jpg?1514570782", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4905/vin_number/672/original/20171229_142404.jpg?1514579694", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4721/vin_number/681/original/IMG_1425.JPG?1514585968", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4775/vin_number/712/original/15150184408591588812235.jpg?1515018525", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4936/vin_number/733/original/image.jpg?1515021989", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4936/vin_number/734/original/image.jpg?1515022054", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R4839/vin_number/735/original/image.jpg?1515078223", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018R5438/vin_number/754/original/image.jpg?1515170769", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018R5242/vin_number/780/original/1515451374097-577217375.jpg?1515451555", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R3551/vin_number/789/original/image.jpg?1515461152", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2017R3894/vin_number/803/original/20180108_155442.jpg?1515464009", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018R5465/vin_number/806/original/151550720472256232950.jpg?1515507236", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018R5450/vin_number/829/original/1515515019090108394758.jpg?1515514993", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018R5525/vin_number/834/original/20180109_131755.jpg?1515525528", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018R5766/vin_number/845/original/20180109_153013.jpg?1515533702", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018R5471/vin_number/858/original/image.jpg?1515595312", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018R5873/vin_number/876/original/image.jpg?1515624430", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018R5650/vin_number/885/original/IMG_8581.jpg?1515687814", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018R6019/vin_number/893/original/15157751239502077346635.jpg?1515775151", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018R5633/vin_number/902/original/15159594293561183672288.jpg?1515959455", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018R6019/vin_number/909/original/15159635262741953975071.jpg?1515963550", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018R5042/vin_number/917/original/Photo.jpg?1516047417", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018R6049/vin_number/920/original/20180115_145831.jpg?1516050089", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018R6192/vin_number/930/original/FA22FAD7-3545-43E5-A2E0-8378D436D1DD.jpeg?1516122139", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018R5547/vin_number/959/original/image.jpg?1516128994", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018r6263/vin_number/967/original/image.jpg?1516132869", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018r6263/vin_number/977/original/15161322736501519333385.jpg?1516133212", 
"https://motionscloudstorage.blob.core.windows.net/imt/vehicle/2018R5967/vin_number/983/original/15161361495981054602394.jpg?1516136329"
]
pattern = "(.*)/vin_number/(\d+)/original/(.*)"
p = re.compile(pattern)
for i in links:
    g = p.match(i)
    print g.group(2)
    urllib.urlretrieve(i, g.group(2)+".jpg")




