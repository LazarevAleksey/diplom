import json
with open('./stp_conf/stp_3.json', 'r') as f:
    data = json.load(f)

list_of_bmk:dict[str, str] = data['stp_names']
list_of_control_com:list[str] = data['list_of_control_com']