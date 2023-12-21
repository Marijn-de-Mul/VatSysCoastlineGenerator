import geopandas as gpd
import xml.etree.ElementTree as ET

def format_position(lat, lon):
    lat_sign = '+' if lat >= 0 else '-'
    lon_sign = '+' if lon >= 0 else '-'
    lat = abs(lat)
    lon = abs(lon)
    lat_str = f"{lat_sign}{lat:02.4f}".zfill(8)
    lon_str = f"{lon_sign}{lon:03.4f}".zfill(9)
    return f"{lat_str}{lon_str}"

data = gpd.read_file('OSMData/lines.shp')

indonesia_coastlines = data.cx[95:141, -11:6].copy()

tolerance = 0.01  
indonesia_coastlines.geometry = indonesia_coastlines.geometry.simplify(tolerance, preserve_topology=True)

coords = indonesia_coastlines.geometry.apply(lambda geom: list(geom.coords))

root = ET.Element('Maps')

map_elem = ET.SubElement(root, 'Map', {'Type': 'System', 'Name': 'COAST_ALL', 'Priority': '3'})

for i, coord_set in enumerate(coords):
    line_elem = ET.SubElement(map_elem, 'Line', {'Name': f'Line{i}'})

    line_elem.text = '/\n'.join(format_position(coord[1], coord[0]) for coord in coord_set)

tree = ET.ElementTree(root)
tree.write('COAST_ALL.xml', encoding='utf-8', xml_declaration=True)