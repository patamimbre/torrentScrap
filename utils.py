from PyInquirer import prompt, Token

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
      'default': '~/torrentScrap',
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