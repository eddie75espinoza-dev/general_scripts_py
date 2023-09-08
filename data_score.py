import sys
import json
import random

data_score ={
    "num_records": random.randint(9000,10000),
    "num_coordinates": random.randint(7000,9000),
    "percent_accuracy": round(random.random(),2),
    "percent_approximate": round(random.random(),2),
    "percent_inaccurate": round(random.random(),2),
    "response_rate": round(random.random()*100,2),
    "accuracy_rate": round(random.random()*100,2),
    "value_score": round(random.random()*100,2)
}

sys.stdout.write(f"{json.dumps(data_score)} \n")

