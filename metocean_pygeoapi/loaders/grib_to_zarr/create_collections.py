import glob
import multiprocessing
import shutil
import xarray as xr
import re

def create_collections():
   ds_dict={}
   dims_dict={}
   ds_concat_dict={}
   all_grb=open('all.grb','wb')
   for f in glob.glob('test_data/*'):
      shutil.copyfileobj(open(f,'rb'),all_grb)
   ds=xr.open_dataset('all.grb',engine='pynio')
   for v in ds.data_vars:
      tup=ds[v].dims
      joined_string = "_".join(tup)
      if 'level_type' in ds[v].attrs:
         level_type=ds[v].level_type.replace(' ','_').lower()
         joined_string=joined_string+'_'+level_type
         joined_string=re.sub('[()]','',joined_string)
      else:
         pass
      try:
         dims_dict[joined_string].append(v)
      except:
         dims_dict[joined_string]=[]
         dims_dict[joined_string].append(v)
   for common_dims in dims_dict:
      if common_dims in ds_dict.keys():
         ds_dict[common_dims].append(ds[dims_dict[common_dims]])
      else:
         ds_dict[common_dims]=[]
         ds_dict[common_dims].append(ds[dims_dict[common_dims]])
   cpus = multiprocessing.cpu_count()
   max_pool_size = 4
   pool = multiprocessing.Pool(cpus if cpus < max_pool_size else max_pool_size)
   for collection in ds_dict:
      pool.apply_async(convert_to_zarr, args=(ds_dict,collection))
   pool.close()
   pool.join()
   return


def convert_to_zarr(ds_dict,collection):
   chunk_dict={}
   dsz=ds_dict[collection][0]
   for dim in dsz.dims:
      if 'lat_' in dim:
         chunk_dict[dim]=64
      if 'lon_0' in dim:
         chunk_dict[dim]=64  
   for data_var in dsz.data_vars:
      dsz[data_var]=dsz[data_var].chunk(chunks=chunk_dict)
   dsz.to_zarr('zarr/'+collection,mode='w',compute=True,consolidated=True)
   print(collection+' converted to zarr')
   return 'converted to zarr'

if __name__ == "__main__":
   create_collections()
