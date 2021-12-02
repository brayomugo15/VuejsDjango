import requests

def main():
    response = requests.get("https://api.exchangeratesapi.io/latest")
    print("Status code : ", response.status_code)
    print("Content Type: ", response.headers["Content-Type"])


if __name__ == "__main__":
    main()