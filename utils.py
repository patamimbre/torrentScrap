import wget
import requests
from PyInquirer import prompt, Token
from pprint import pprint
from operator import itemgetter
from os.path import expanduser

def print_logo():
  print(
    """
  _                            _    _____                      
 | |                          | |  / ____|                     
 | |_ ___  _ __ _ __ ___ _ __ | |_| (___   ___ _ __ __ _ _ __  
 | __/ _ \| '__| '__/ _ \ '_ \| __|\___ \ / __| '__/ _` | '_ \ 
 | || (_) | |  | | |  __/ | | | |_ ____) | (__| | | (_| | |_) |
  \__\___/|_|  |_|  \___|_| |_|\__|_____/ \___|_|  \__,_| .__/ 
                                                        | |    
                                                        |_|    

    """
  )

def prompt_start():
  questions = [
    {
      'type': 'input',
      'name': 'path',
      'message': 'Carpeta de descarga: ',
      'default': F'{expanduser("~")}/torrentScrap',
    },
    {
      'type': 'input',
      'name': 'term',
      'message': 'Término a buscar: ',
    },
  ]

  answers = prompt(questions)
  return answers

def create_folder(path):
  if not path:
    raise "A path is required"

  # check if the path exist
    # create the path

def entries_questions(entries):
    choices = []
    for idx, entry in enumerate(entries):
        name = entry.get('name', '').replace('\n', ' ')
        quality = entry.get('quality', '')
        entry_type = entry.get('type', '')

        choices.append({
            'name': F"{name} ({quality}) - {entry_type}",
            'value': idx,
        })

    return [
        {
            'type': 'list',
            'name': 'entries',
            'message': 'Selecciona el elemento',
            'choices': choices,
        }
    ]

def prompt_entries(entries):
    answers = prompt(entries_questions(entries))
    return int(answers.get('entries', '0'))



def links_questions(entry):
    name, download = itemgetter('name', 'download')(entry)
    choices = []

    for entry in download:
        link = entry.get('link', '')
        if (link):
            choices.append({
                'name': entry.get('name', ''),
                'value': link,
            })

    return [
        {
            'type': 'checkbox',
            'message': 'Selecciona los enlaces',
            'name': 'links',
            'choices': sorted(choices, key=itemgetter('name')) ,
            'validate': lambda answer: 'You must choose at least one link' \
                if len(answer) == 0 else True
        }
    ]

def prompt_links(entry):
    download = itemgetter('download')(entry)

    if (len(download) == 1):
        return [download[0]['link']]
    
    if (len(download) > 1):
        answers = prompt(links_questions(entry))
        return answers.get('links', None)

def download(links, path):
    print(F'Descargando {len(links)} elementos')
    for url in links:
        filename = url.split('/')[-1]
        myfile = requests.get(url)
        open(F'{path}/{filename}', 'wb').write(myfile.content)

        # wget.download(url, F'{path}/{filename}')

    print(F'Elementos descargados en {path}')



