# %%
import osmnx as ox

# %%
# CASE 1 - download for Greece
# Download the boundaries for Greece
# This will return a GeoPandas DataFrame
greece_extents_gdf = ox.geocode_to_gdf(
    ["Greece", "British Sovereign Base Areas", "Northern Cyprus"]
)
# dissolve the boundaries into a single boundary
greece_dissolved_gdf = greece_extents_gdf.dissolve()
# preferably simplify - units are degrees from WGS84 - optionally take the convex hull
greece_dissolved_gdf.geometry = greece_dissolved_gdf.geometry.simplify(0.0001)
# then save to a file
greece_dissolved_gdf.to_file(f"../temp/greece_boundary.gpkg")

# %%
# CASE 2 - download for Athens
# in this case the query directly requests the polygon from the OSM id relation
athens_extents_gdf = ox.geocode_to_gdf("R2628520", by_osmid=True, which_result=2)
# preferably simplify - units are degrees from WGS84 - optionally take the convex hull
athens_extents_gdf.geometry = athens_extents_gdf.geometry.simplify(0.0001)
# then save to a file
athens_extents_gdf.to_file(f"../temp/athens_boundary.gpkg")
