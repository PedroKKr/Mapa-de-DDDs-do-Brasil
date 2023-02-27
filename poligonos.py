from xml.dom import minidom

xmldoc = minidom.parse('Mapa DDDs colorido simplificado.svg')
itemlist = xmldoc.getElementsByTagName('polygon')

regions = []

for s in itemlist:
    poly = []
    for i,p in enumerate(s.attributes['points'].value.split()):
        if i%2 == 0:
            poly.append([])
        poly[-1].append(float(p))
    regions.append([tuple(x) for x in poly])