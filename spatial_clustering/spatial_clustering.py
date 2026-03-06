import geopandas as gpd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# Paths (update to your files)
input_path = '/home/pi/.openclaw/workspace/points.geojson'  # Input GeoJSON or CSV with geometry/lon-lat
output_path = '/home/pi/.openclaw/workspace/clustered_points.geojson'  # Output GeoJSON with cluster labels

# Load points (assuming GeoJSON with geometry; if CSV, use gpd.read_file with driver='CSV', geometry='geometry')
gdf = gpd.read_file(input_path)

# Extract coordinates (assuming CRS is geographic; project to metric if needed for clustering, e.g., gdf.to_crs('EPSG:3857'))
coords = np.array([[point.x, point.y] for point in gdf.geometry])

# Optional: Scale features if clusters vary in scale
scaler = StandardScaler()
coords_scaled = scaler.fit_transform(coords)

# Run DBSCAN (density-based clustering for hotspots)
# eps: max distance between points in cluster (tune based on units, e.g., 0.01 for degrees ~1km)
# min_samples: min points to form a cluster (e.g., 5)
dbscan = DBSCAN(eps=0.01, min_samples=5)
cluster_labels = dbscan.fit_predict(coords_scaled)

# Add cluster labels to GeoDataFrame ('-1' for noise/outliers)
gdf['cluster'] = cluster_labels

# Save as GeoJSON (points color-coded by cluster ID)
gdf.to_file(output_path, driver='GeoJSON')
print(f"Output saved: {output_path}")
print(gdf['cluster'].value_counts())  # Preview cluster counts
print(gdf[['cluster']].head())  # Sample output