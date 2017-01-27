import pysumo
from tqdm import tqdm
import random
from time import time
cmd = ['sumo', 
  '--net-file', 'simple/traffic.net.xml', 
  '--route-files', 'simple/traffic.rou.xml',
  '--additional-files', 'simple/traffic.add.xml',
  '--end', '500']
actions = ['rGrG','ryry','GrGr','yryr']
def random_action():
	return random.choice(actions)
  
time_start = time()
for i in tqdm(range(500)):
	pysumo.simulation_start(cmd)
	for j in range(1000):
		pysumo.tls_setstate("0",random_action())
		pysumo.simulation_step()
		ids = pysumo.vehicle_list()
		for vid in ids:
			print pysumo.vehicle_lane_position(vid)	
	pysumo.simulation_stop()
time_end = time()
print "pysumo time elapsed: {}".format(time_end-time_start)
