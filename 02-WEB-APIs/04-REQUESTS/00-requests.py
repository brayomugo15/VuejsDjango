import requests

def main():
    response = requests.get("http://www.google.com")
    # response = requests.get("http://www.google.com/random-page/")
    print("Status code : ", response.status_code)
    print("Header Date: ", response.headers['Date'])

if __name__ == "__main__":
    main()