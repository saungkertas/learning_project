# Day 6: Zonal Statistics (Raster + Vector)

## Overview
This script demonstrates zonal statistics using `rasterstats` to compute average elevation (or other stats) within GeoJSON polygons masked against a raster file (e.g., DEM).

### Goal
Integrate satellite/grid data with boundaries to find stats like mean elevation or temperature for specific regions.

### Usage
1. Update paths in `zonal_stats.py`:
   - `vector_path`: GeoJSON with polygons (e.g., regions.geojson)
   - `raster_path`: Raster file (e.g., elevation_dem.tif)

2. Install dependencies: `pip install -r requirements.txt`

3. Run: `python zonal_stats.py`

### Output
- Updated GeoJSON (`regions_with_elev.geojson`) with `mean_elevation` property per polygon.
- Console preview of results.

### Notes
- Ensure CRS alignment between raster and vector.
- For temperature, swap raster and rename column.
- Example data: SRTM DEM from USGS, GADM boundaries.

See `zonal_stats.py` for details.