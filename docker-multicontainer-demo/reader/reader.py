import os
import time
import requests

# refit to automatically send API request to "writer" triggering a write
# then grab the last line of log.csv (CSV) after wait
# writer should store API requests as a JSON string with timestamp and source (?)

def load_env(names):
    env_dict = { "unset": [] }
    for nm in names:
        env = os.environ.get(nm)
        
        if env == None:
            env_dict['unset'].append(nm)
            continue

        env_dict[nm] = env
    return env_dict

env = load_env(["DATA_PATH", "WAIT_TIME", "CHECKUP_FREQ", "WRITER_ENDPOINT"])

data_path = env["DATA_PATH"]
wait_time = float(env["WAIT_TIME"])
checkup_freq = int(env["CHECKUP_FREQ"])
writer_endpoint = env["WRITER_ENDPOINT"]

if len(env["unset"]) > 0:
    print ("Exit due to env variables being unset.")
    exit(0)

it = 0

with open(data_path, "a+") as f:
    #create file if it doesn't exist
    pass

while (True):
    print("Last line: ", end="")

    with open(data_path, "rb") as f:
        # get last line of file
        try: 
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)
        except OSError:
            f.seek(0)
        last_line = f.readline().decode()
        
        it = (it + 1) % checkup_freq

        if it == 0:
            requests.post(writer_endpoint,json={"source": "reader", "text": "checkup"})

    print(last_line, end="")
    time.sleep(wait_time)