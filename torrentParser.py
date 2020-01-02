import demjson
import re

base = 'http://www.mejortorrentt.org'
download_base = '/uploads/torrents/'



def extractEntry(entry):
  a = entry.find('a', first=True)
  q = entry.find('span', first=True)
  l = a.links.pop()

  return {
    'name': a.text,
    'link': base + l,
    'quality': q.text.strip('()') if q else '',
    'type': entry.find('td[align="right"]', first=True).text,
  }

def findEntries(session, term):
  t = term.replace(' ', '+')
  url = F'{base}/secciones.php?sec=buscador&valor={t}'

  r = session.get(url)
  r.html.render()
  entries = r.html.find('tr[height="22"]')
  return [extractEntry(e) for e in entries]


def getFinalLinks(session, table):
  links = list(table.absolute_links)
  result = []

  for link in links:
    r = session.get(link)
    l = r.html.find('a[style="font-size:12px;"]', first=True).absolute_links.pop()
    result.append(l)

  return result


def getDownloadLink(session, link):
  link_regex = '\/uploads/\w+/\w+'
  
  r = session.get(link)
  l = r.html.find('a[href="#"]', first=True)
  attr = l.attrs['onclick']

  ty = re.search(link_regex, attr).group(0).split('/')[3]
  obj = demjson.decode(attr.split(',', 1)[1][0:-2])
  name = obj['name'].replace(' ', '%20')

  return {
    'name': name,
    'link': F'{base}{download_base}{ty}/{name}',
  }


def fullDisclosure(session, entry):
  url = entry['link']

  r = session.get(url)
  r.html.render()

  founds = r.html.find('td[style="border-top: 1px solid black; border-left: 1px solid black; border-right: 1px solid black;"]', first=True)
  finalLinks = []

  if founds:
    finalLinks = getFinalLinks(session, founds)
  else:
    finalLinks = [
      r.html.find('a[style="font-size:12px;"]', first=True).absolute_links.pop()
    ]



  downloadLinks = [getDownloadLink(session, l) for l in finalLinks]
  return {
    **entry,
    'download': downloadLinks,
  }



