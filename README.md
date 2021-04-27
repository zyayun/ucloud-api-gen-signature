# ucloud-api-gen-signature
根据请求api生成签名(Signature)并打印出response信息


## 配置
``` python
`修改为你要请求的api`
ucloud_request_data = {
    'Action': 'DescribeUHostInstance',
    'Region': 'xxx',
    'Zone': 'xxx',
    'ProjectId': 'xxx',
    'PublicKey': 'YOUR_ACCESS_PUBLIC_KEY',
    'Tag': 'xxx'
}
```
```python
if __name__ == '__main__':
    api_url = 'https://api.ucloud.cn'
    privite_key = 'YOU_PRIVITE_KEY'   # 修改为你的ACCESS_PRIVITE_KEY
    show_info(api_url, ucloud_request_data, privite_key)
```

## 测试

```python
~/workspace/ucloud-api-signature(master) » python gen_signature.py 
请求参数拼接:
xxxx
签名:
xxx
请求JSON:
{
    "Action": "DescribeUHostInstance",
    "ProjectId": "xxx",
    "PublicKey": "xxx",
    "Region": "xxx",
    "Signature": "xxx",
    "Tag": "xxx",
    "Zone": "xxx"
}
RESP:
 {
    "RetCode": 0,
    "Action": "DescribeUHostInstanceResponse",
    "UHostSet": [
        {
            "UHostId": "xxx",
        ...
```