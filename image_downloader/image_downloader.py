import argparse
import requests

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("-f", metavar="f", type=str, help='file name')
parser.add_argument("-u", metavar="u", type=str, help='link')
parser.add_argument("-p", metavar="p", type=str, help='path at computer', default='')

args = parser.parse_args()


def save_foto(file_name, url, path):
    with open(f'{path}{file_name}.jpg', 'wb') as f:
        f.write(requests.get(url).content)


save_foto(args.f, args.u, args.p)
