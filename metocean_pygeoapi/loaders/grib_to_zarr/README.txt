GRIB TO ZARR Ingest Example:

Summary:

In this example, the gfs_GRIB_to_ZARR.sh script will download the GFS 1.00 Degree data for the 00z run
and store it in the test_data directory using the gfs_download_data.py script. Then, the create_collections.py 
script will concatenate the GRIB files within the test_data directory. Using that concatenated GRIB file,
the data is loaded into xarray using pynio as an engine. The weather parameters within the xarray object 
are then grouped by common dimensions and level type into "collections". All of the collections are stored 
in a dictionary with the key being the name of the collection and the value being the associated xarray object.

Using multiprocessing, the collection xarray objects are then chunked and converted to zarr. The zarr datastores 
are then stored in the ./zarr directory.


Installing dependencies:

Xarray uses pynio to open the GRIB file. pynio is only distributed on conda. To install,
conda create --name pygeomo --file requirements.txt python=3.8


How to run:

Simply run the gfs_GRIB_to_ZARR.sh script. This will download the gfs data locally and convert to zarr.


Testing other GRIB data outside of the GFS:

This has not been tested yet. My first step would be to concatenate the grib files together into one 
grib file so that pynio can read it directly.



