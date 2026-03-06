# Day 7: Spatial Clustering (Unsupervised Learning)

## Overview
This script uses scikit-learn's DBSCAN for density-based spatial clustering on point coordinates to identify "hotspots" without predefined boundaries. K-Means alternative available (commented).

### Goal
Apply ML to find patterns in location data, revealing high-density activity areas.

### Usage
1. Prepare input: GeoJSON or CSV with points (lon/lat columns or geometry).
   - Sample: Generate random points or use real data (e.g., crime incidents, tweets).

2. Install: `pip install -r requirements.txt`

3. Update paths in `spatial_clustering.py`:
   - `input_path`: Your points data.
   - `output_path`: Clustered GeoJSON.

4. Run: `python spatial_clustering.py`

### Output
- `clustered_points.geojson`: Each point with `cluster` property (-1 for noise).
- Console: Cluster counts and sample.

### Notes
- DBSCAN params: `eps=0.01` (~1km in degrees), `min_samples=5`. Tune for your data.
- For K-Means (equal-sized clusters): Uncomment and set `n_clusters=5`.
- CRS: Project to metric (e.g., UTM) for accurate distance-based clustering: `gdf = gdf.to_crs('EPSG:3857')`.
- Visualization: Load in QGIS (style by 'cluster') or Folium: `folium.GeoJson(gdf, style_function=... )`.
- Data example: Random points around London for testing.

To test, add sample points GeoJSON with generated coords.

See `spatial_clustering.py` for details.