import geopandas as gpd

# Load the shapefile
data = gpd.read_file('OSMData/lines.shp')

# Print column names
print(data.columns)

# Filter the data for Indonesia
# Replace 'name' with the correct column name
indonesia_data = data[data['<correct_column_name>'] == 'Indonesia']

# Extract the coordinates
indonesia_coords = indonesia_data.geometry.apply(lambda geom: list(geom.coords))

# Print the coordinates
for coords in indonesia_coords:
    print(coords)