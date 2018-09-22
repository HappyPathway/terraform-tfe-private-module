#!/usr/local/bin/python
import requests
import os
import json
import sys

class ModulePublishException(Exception): pass

def main(opt):

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
    parser.add_option("--token", default=os.environ.get("ATLAS_TOKEN"))
    parser.add_option("--org")
    parser.add_option("--api", default="app.terraform.io")
    opt, args = parser.parse_args()

    if not opt.token:
        raise ModulePublishException("No Token Set")
    if not opt.org:
        raise ModulePublishException("No Org Set")
    main(opt)
