import folium
import os
import geopandas as gpd
import pandas as pd


def generateBaseMap(default_location = [41.8600, -87.6298], default_zoom_start = 10):
    '''
    generates a map for the correct area
    
    Parameters
    ----------
    default_location: list of floats
        location of where the map is going to be
    
    default_zoom_start: int
        the amount of zoom on the map in beginning
    
    '''
    base_map = folium.Map(location=default_location, control_scale = True, zoom_start = default_zoom_start)
    return base_map


def geodataframe(df):
    '''
    converts a dataframe into a geodataframe
    
    Parameters
    ----------
    df: pandas.dataframe
    
    Returns
    -------
    gdf: geopandas.dataframe
    '''

    # path to geoJson file 
    geo = os.path.join('data/Boundaries-ZIPCodes.geojson')

    # creation of a geodataframe using geopandas
    gdf = gpd.read_file(geo)

    # add a column with the x-coordinate of the multipolygon
    gdf['centroid_lon'] = gdf['geometry'].centroid.x

    # add a column with the y-coordinate of the multipolygon
    gdf['centroid_lat'] = gdf['geometry'].centroid.y

    # setting a projection  by assigning the WGS84 latitude-longitude CRS to the crs attribute
    gdf.crs = {'init' :'epsg:4326'}
    
    # counting the number of facilities per zip 
    facility_number_per_zip = pd.DataFrame(df.groupby('zip')['license'].count()).reset_index()
    
    if (type(df.zip) is not str):
        # convert the zip column into an str
        facility_number_per_zip.zip = facility_number_per_zip.zip.astype(str)
    
        # reformat the zip code writing in order to compare it with the zip code in geojson file (for vizualisation step)
        facility_number_per_zip['zip'] = facility_number_per_zip['zip'].apply(lambda x : x.split('.')[0])
    
    # merge with the geodataframe
    gdf = pd.merge(gdf,facility_number_per_zip, on = 'zip')
    gdf.rename(columns = {'license': 'facility_number_per_zip'}, inplace = True)
    
    return gdf


def chlorepleth_map (name,gdf,columns,legend_name,color):
    '''
    mapping cloropleth map
    
    Parameters
    ----------
    name: str 
        name of map
    
    gdf: geopandas.dataframe
        dataframe with data for mapping
    
    columns: list
        columns with data for mapping
    
    legend_name: str
        name on scale 
    
    color: str
        color scheme for map
        
    Returns
    -------
    map_: folium.folium.Map
    '''

    #creating a basic map of Chicago
    map_ = folium.Map(location=[41.8600, -87.6298], control_scale=True, zoom_start=10)
    
    #geoJson file path
    geo = os.path.join('data/Boundaries-ZIPCodes.geojson')
    
    folium.Choropleth(
        geo_data=geo,
        name=name,
        data=gdf,
        columns=columns,
        key_on='feature.properties.zip',
        fill_color=color,
        fill_opacity=0.8,
        line_opacity=1,
        legend_name=legend_name
    ).add_to(map_)
    
    #if (markers==True):
        #add_markers(map)
    
    return map_


def adding_Marker(map_, longitude, latitude, popup, colour):
    '''
    adds a marker which locates a facility on the map
    
    Parameters
    ----------
    map_: folium.folium.Map
        basic map
    
    longitude: numpy.float64
    
    latitude: numpy.float64
    
    popup: str
        beach name and count of e-coli consentration higher than limit
    
    colour: str
    '''
    folium.Marker(
        location = [latitude,longitude], # coordinates for the marker 
        popup = popup ,  # pop-up label for the marker
        icon = folium.Icon(color = colour)
    ).add_to(map_)

    
def adding_CircleMarker(map_, longitude, latitude, color,r):
    '''
    adds a marker which locates a facility on the map
    
    map_: folium.folium.Map
        basic map
    
    longitude: numpy.float64
    
    latitude: numpy.float64
    
    popup: str
        beach name and count of e-coli consentration higher than limit
    
    colour: str
   '''
    
    
    folium.CircleMarker(
        location = [latitude,longitude], # coordinates for the marker 
        color = color ,  # pop-up label for the marker
        fill=True,
        radius = r,
    ).add_to(map_)
