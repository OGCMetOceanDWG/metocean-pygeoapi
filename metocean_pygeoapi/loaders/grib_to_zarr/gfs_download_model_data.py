import argparse
import os
from multiprocessing import Pool
from datetime import date



def sys_request(i):
   try:
      os.system('perl get_gfs.pl data '+d+' ' +str(i)+' '+str(i)+' '+str(i)+' all all test_data')
   except: 
      pass
   return



def multi_process_loop(model_run):
   today=date.today()
   today=today.strftime("%Y%m%d")
   d=today+model_run
   hour_list=list()
   for i in range(0, 387,3):
      hour_list.append(i)
   pool=Pool()
   pool.map(sys_request,hour_list)
   return




if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='Ingest Model')
   parser.add_argument('model_run', type = str, help = 'Enter model run (ie. 00 for 00z)')
   args=parser.parse_args()
   model_run=args.model_run
   today=date.today()
   today=today.strftime("%Y%m%d")
   d=today+model_run
   multi_process_loop(model_run)
