import requests

def main():
    response = requests.get("https://api.genderize.io?name=james")
    
    if response.status_code != 200:
        print("Status code : ", response.status_code)
        raise Exception("There was an error")
    data = response.json()
    print("Json response : ", data)


if __name__ == "__main__":
    main()