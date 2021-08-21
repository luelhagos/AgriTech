import numpy as np
from laspy.file import File
from pandas import DataFrame
from geopandas import GeoDataFrame
from shapely.geometry import Point

#Read LAS file
inFile = File("s428_7568.las", mode = "r")

#Import LAS into numpy array (X=raw integer value x=scaled float value)
lidar_points = np.array((inFile.x,inFile.y,inFile.z,inFile.intensity,
               inFile.raw_classification,inFile.scan_angle_rank)).transpose()

#Transform to pandas DataFrame
lidar_df=DataFrame(lidar_points)

#Transform to geopandas GeoDataFrame
crs = None
geometry = [Point(xyz) for xyz in zip(inFile.x,inFile.y,inFile.z)]
lidar_geodf = GeoDataFrame(lidar_df, crs=crs, geometry=geometry)
lidar_geodf.crs = {'init' :'epsg:2959'} # set correct spatial reference
