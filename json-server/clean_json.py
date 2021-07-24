import json

data = {
    "apis": [],
    "trades": [],
}

with open('gtt_api_data.json') as f:
    for line in f.readlines():
        line_dict = json.loads(line)
        # for k, v in line_dict.items():
        #     data["apis"][k] = v
        data["apis"].append(line_dict)



with open('gtt_trade_data.json') as f:
    for line in f.readlines():
        line_dict = json.loads(line)
        # for k, v in line_dict.items():
            # data[k] = v
        data["trades"].append(line_dict)


with open('gtt_merged_data.json', 'w+') as f_cleaned:
    json.dump(data, f_cleaned, indent=4)