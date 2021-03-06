import os
import requests
from bs4 import BeautifulSoup
import typer

def dlimg(url, folder, filename):
    
    if not os.path.isdir(folder):
        os.makedirs(folder, exist_ok=True)
    
    filepath = os.path.join(folder, filename)
    r = requests.get(url, stream=True)
    with open(filepath, 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)
    print(f'finished downloading {filename}')
    

def dlpage(url: str, to: str = "./dl"):
    """
    Download all images from a webpage
    """
    print(f'\n\nnow downloading all images from {url}')

    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    imgl = [i['src'] for i in soup.find_all('img')]

    for i, img in enumerate(imgl):
        dlimg(img, to, f'{str(i).zfill(len(str(len(imgl))))}__{img.split("/")[-1].split("?")[0]}')

    print(f'\nfinished downloading all images in {url}')


if __name__ == '__main__':
    typer.run(dlpage)
