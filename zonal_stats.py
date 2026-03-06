import geopandas as gpd
from rasterstats import zonal_stats

# Paths (update these to your files)
vector_path = '/home/pi/.openclaw/workspace/regions.geojson'  # Input GeoJSON polygons
raster_path = '/home/pi/.openclaw/workspace/elevation_dem.tif'  # Input raster (e.g., DEM)
output_path = '/home/pi/.openclaw/workspace/regions_with_elev.geojson'  # Output GeoJSON

# Load polygons
gdf = gpd.read_file(vector_path)

# Compute zonal stats: mean elevation for each polygon
# 'mean' is the statistic; add 'min', 'max', 'count' if needed
stats = zonal_stats(
    vector_path,  # Polygons
    raster_path,  # Raster
    stats=['mean'],  # Compute mean only (add more like 'min', 'max')
    affine=None,  # Auto-detects raster affine transform
    nodata=-9999,  # Ignore nodata values in raster
    geojson_out=True  # Returns GeoJSON-compatible output
)

# Add the mean elevation as a property to each polygon
# stats is a list of dicts; zip with gdf
mean_elevations = [feature['properties']['mean'] if 'mean' in feature['properties'] else None 
                   for feature in stats]
gdf['mean_elevation'] = mean_elevations

# Save updated GeoJSON
gdf.to_file(output_path, driver='GeoJSON')
print(f"Output saved: {output_path}")
print(gdf[['name', 'mean_elevation']].head())  # Preview (assuming 'name' column exists)