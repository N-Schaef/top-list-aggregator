#!/usr/bin/python3

import argparse
import requests
from bs4 import BeautifulSoup as Soup
import re


def parse_list(page, selector):
    sauce = requests.get(page)
    soup = Soup(sauce.content, features="html5lib")
    results = soup.select(selector)
    entries = list(map(lambda x: preprocess(x.getText()), results))
    print(f'"{page}": "{selector}" found {len(entries)} entries')
    return entries


def merge_list(previous, new):
    for entry in new:
        found = False
        for p in previous:
            if p[0] == entry:
                found = True
                p[1] += 1
        if not found:
            previous.append([entry, 1])
    return previous


def preprocess(entry):
    entry = entry.strip()
    entry = re.sub('^\d+\.\s*', '', entry)
    entry = re.sub('^Best(?:.+):\s', '', entry)
    return entry


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Aggregates multiple Top-X lists.')
    parser.add_argument('-l', '--list', dest='list', action="append", type=str, nargs='+',
                        help='a URL to a Top-X list.')
    parser.add_argument('-s', '--selector', dest='selector', action="append", type=str, nargs='+',
                        help='selector for the list. (See BeautifulSoup selector reference for syntax)')

    args = parser.parse_args()
    if args.list is None or args.selector is None:
        print("You need at least one selector and list.")
        exit(-1)

    if len(args.list) != len(args.selector):
        print("You need one selector per list.")
        exit(-1)

    all_entries = []
    for i in range(0, len(args.list)):
        entries = parse_list(args.list[i][0], args.selector[i][0])
        merge_list(all_entries, entries)
    all_entries.sort(key=(lambda x: x[1]), reverse=True)
    print("======= Results =======")
    for i in range(len(all_entries)):
        entry = all_entries[i]
        print(f'{i + 1}.: {entry[0]} ({entry[1]} mentions)')
