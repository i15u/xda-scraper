import json
import os
from typing import Callable
from urllib.parse import urljoin

import requests
from bs4 import Tag, BeautifulSoup

from Entity import Entity


def resolve_url(path: str) -> str:
    return urljoin('https://xdaforums.com/all-forums-by-manufacturer', path)


def get_page(path: str) -> Tag:
    return BeautifulSoup(requests.get(resolve_url(path)).text, 'html.parser')


def format_num(num: str) -> int:
    for key, value in {
        'K': 1_000,
        'M': 1_000_000,
    }.items():
        num = num.replace(key, f' * {value}')

    return int(eval(num))


def to_json(obj):
    return json.dumps(obj, indent=4, default=lambda o: vars(o))


def safe_value(callback: Callable):
    try:
        return callback()
    except:
        return None


def write_to(path: str, entities: list[Entity]) -> str:
    brands_dir = './items'
    os.makedirs(brands_dir, exist_ok=True)

    path = os.path.abspath(os.path.join(brands_dir, path))

    with open(path, 'w+') as brands_file:
        brands_file.write(to_json(entities))

    return path
