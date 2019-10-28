import requests

if __name__ == '__main__':
    response = requests.get('http://httpbin.org/get')
    print(f"response.status_code:{response.status_code}\n")
    print(f"response.apparent_encoding:{response.apparent_encoding}\n")
    print(f"response.headers:{response.headers}\n")
    print(f"response.content:{response.content}\n")
    print("response.text:\n"+response.text)
