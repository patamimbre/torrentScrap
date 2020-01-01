from requests_html import HTMLSession
from torrentParser import findEntries, fullDisclosure
from pprint import pprint
from utils import *
from operator import itemgetter


def main():
  print_logo()

  options = prompt_start()
  path, term = itemgetter('path', 'term')(options)

  create_folder(path)

  session = HTMLSession()
  entries = findEntries(session, term)

  selected_index = prompt_entries(entries)
  entry = entries[selected_index]

  # hacer full disclosure del elegido
  full = fullDisclosure(session, entry)

  pprint(full)

  # pintar todos los enlaces

  # marcar los que se quieran descargar (1 a 1 o todos)

  # descargar en la carpeta indicada


if __name__ == '__main__':
    main()