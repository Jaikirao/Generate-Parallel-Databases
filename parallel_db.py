print("i start this project I will complete this project soon")
#try here
import torch

# the number of entries in our database
num_entries = 5000

db = torch.rand(num_entries) > 0.5
db
#create a fuction of parallel database
def get_parallel_db(db , remove_index):       #remove_index to remove the entry
  return torch.cat((db[0:remove_index],
                    db[remove_index+1:]))
#now call this fuction
get_parallel_db(db,2)
#now we create a another fuction get_parralle_dbs after making create we combine both the fuction
