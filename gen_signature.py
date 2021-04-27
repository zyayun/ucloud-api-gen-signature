#!/usr/bin/env python
import requests
import json
import hashlib

ucloud_request_data = {
    'Action': 'DescribeUHostInstance',
    'Region': 'cn-bj2',
    'Zone': 'cn-bj2-02',
    'ProjectId': 'org-18995',
    'PublicKey': 'YOUR_ACCESS_PUBLIC_KEY',
    'Tag': 'test'
}

def gen_sign(privite_key, parms):
    l = sorted(parms.items())
    parms_data = ""
    for k, v in l:
        parms_data = parms_data + k + v
    parms_data = parms_data + privite_key
    # 请求参数拼接
    print('请求参数拼接:\n' + parms_data)
    sha1 = hashlib.sha1()
    sha1.update(parms_data.encode('utf-8'))
    signature = sha1.hexdigest()
    print('签名:\n' + signature)
    return signature


def show_info(api_url, ucloud_request_data, privite_key):
    headers = {'Content-Type': 'application/json'}
    sign = gen_sign(privite_key, ucloud_request_data)
    ucloud_request_data['Signature'] = sign
    sort_json = json.dumps(ucloud_request_data, sort_keys=True, indent=4)
    resp = requests.post(api_url, data=sort_json, headers=headers)
    pretty_json = json.loads(resp.text)
    # 打印请求json
    print('请求JSON:\n' + sort_json)

    # resp json
    print('RESP:\n',json.dumps(pretty_json,indent=4))


if __name__ == '__main__':
    api_url = 'https://api.ucloud.cn'
    privite_key = 'YOU_PRIVITE_KEY'
    show_info(api_url, ucloud_request_data, privite_key)
