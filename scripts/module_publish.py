#!/usr/local/bin/python
import requests
import os
import json
import sys
import hcl

def sanitize_path(config):
    path = os.path.expanduser(config)
    path = os.path.expandvars(path)
    path = os.path.abspath(path)
    return path

def tfe_token(tfe_api, config):
    with open(sanitize_path(config), 'r') as fp:
        obj = hcl.load(fp)
    return obj.get('credentials').get(tfe_api).get('token')


def main(opt):
    
    with open(opt.config, 'r') as module_config:
        data = json.loads(module_config.read())

    atlas_token = opt.token
    headers = {"Authorization": "Bearer {0}".format(atlas_token),
               "Content-Type": "application/vnd.api+json"}

    resp = requests.post("https://{0}/api/v2/registry-modules".format(opt.api), 
                    headers=headers,
                    data=json.dumps(data))


    data = json.dumps(resp.json(), separators=(',', ':'), indent=4, sort_keys=True)

    if resp.status_code not in [200, 201]:
        sys.stderr.write(str(resp.status_code))
        sys.stderr.write(resp.text)
        sys.exit(1)

    print json.dumps(dict(status=str(resp.status_code)), 
                        separators=(',', ':'), 
                        indent=4, 
                        sort_keys=True)

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--token")
    parser.add_option("--org")
    parser.add_option("--api")
    parser.add_option("--config")
    opt, args = parser.parse_args()
    main(opt)
