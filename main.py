from requests_html import HTMLSession
from torrentParser import findEntries, fullDisclosure
from pprint import pprint
from utils import *
from operator import itemgetter


def main():
  print_logo()

  options = prompt_start()
  path, term = itemgetter('path', 'term')(options)

  # create_folder(path)

  session = HTMLSession()
  entries = findEntries(session, term)

  selected_index = prompt_entries(entries)
  entry = entries[selected_index]

  disclosure = fullDisclosure(session, entry)
  download_links = prompt_links(disclosure)

  download(download_links, path)


if __name__ == '__main__':
    main()