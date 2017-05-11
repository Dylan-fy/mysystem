import json
def get_user_config(computername):
    return 'VBoxManage showvminfo '+ computername

def format_config(origin_config):
    config = origin_config.split('\n')
    config_dict = {}
    for config_line in config:
        line = config_line.split(':')

        try:
            key = line[0].strip()
            key = key.replace(' ','_')
            value = line[1]
            if key == 'State':
                value = line[1].split('(')
                value = value[0]
            config_dict[key] = value.strip()
        except:
            continue
    return json.dumps(config_dict)