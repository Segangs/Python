import requests

def fetch(url):
    response = requests.get(url)
    return response.text

def main():
    html = fetch("http://yahoo.jp")
    print(html)
    

if __name__ == "__main__":
    main()