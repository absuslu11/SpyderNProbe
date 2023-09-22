import sys
import requests

def probe(out_file):
    url2 = sys.stdin.read().splitlines()

    goodUrls = []
    badUrls = []

    for url in url2:

        try:
            response = requests.head(url)

            if response.status_code == 200:
                goodUrls.append()
        except requests.exceptions.MissingSchema:
            badUrls.append(url)
            continue
    with open(out_file, "w") as file:
        file.write("\n".join(goodUrls))
    
    print(f"saved URL's {out_file}")


out_file = "url.txt"
probe(out_file)
