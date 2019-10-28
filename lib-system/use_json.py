import json

if __name__ == '__main__':
    office_worker = '''
    [{
        "name":"jack",
        "gender":"male",
        "birthday":"1966-06-06",
        "company":"Alibaba"
    },
    {
        "name":"rose",
        "gender":"female",
        "birthday":"1988-08-26",
        "company":"Alibaba"
    }
    ]
    '''
    data = json.loads(office_worker)
    for item in data:
        print(item)

    x = json.dumps(data,
                   sort_keys=True,
                   indent=4,
                   separators=(',', ':'))
    print(x)
