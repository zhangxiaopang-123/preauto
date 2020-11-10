

import yaml
import os
import json
from WbfServices import wbf_config


def read():
    basedir = wbf_config.basedir
    data_path = os.path.join(basedir, 'WbfConfig/wbf.yaml')
    with open(data_path, 'r', encoding='utf-8') as f:
        d = yaml.safe_load(f.read())
        return d
        # print(json.dumps(d['user'],indent=2,sort_keys=True,separators=(',',':')))
        # print(d['test-5']['user'].split(',')[0])


if __name__ == '__main__':
    read()

