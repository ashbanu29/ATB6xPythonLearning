response_time_s = [1200,1500,1700]

def mil_sec(x):
    return x / 1000

#response_time_s = list(map(mil_sec, response_time_s))
response_time_s = list(map(lambda x: x/1000, response_time_s))
print(response_time_s)