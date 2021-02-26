#!/bin/bash
mkdir test_data
mkdir zarr
python gfs_download_model_data.py 00
python create_collections.py
