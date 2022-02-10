import farmacia

p = farmacia.Prescription_items
print("")
print("")
for attr in p.__dict__:
    print("\t def get_"+attr+"(self):")
    print("\t\t return self."+attr)
    print("\t def set_"+attr+"(self,"+attr+"):")
    print("\t\tself."+attr+" = "+attr)
    print("\n")

from datetime import datetime
import time


def time_stamp(self):
    ts = time.time()

    # print the current timestamp
    print(ts)
    timestamp = ts
    dt_object = datetime.fromtimestamp(timestamp)
    return dt_object