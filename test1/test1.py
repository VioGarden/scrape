import requests
import datetime

from requests_html import HTML

now = datetime.datetime.now()

second = now.second
micro = now.microsecond


def url_to_txt(url, filename=f"test.html", save=False):
    """
    input : url from google sheets
    output : html of google sheets link
    """
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"file-{second}-{micro}", 'w') as f:
                f.write(html_text)
        return html_text
    return ""

url = "https://gist.github.com/blissfulyoshi/586f173ba9afa45c64a7cb7c47ce7d1c"


html_text = url_to_txt(url)

def find_raw_link(html_text):
    """
    input : html of google sheets link
    output : the specified raw json data link
    """
    r_html = HTML(html=html_text)
    table_class = ".file-actions"
    r_table = r_html.find(table_class)
    try:
        if r_table:
            element = r_table[0]
        try:
            if element.links:
                x = element.links
                y = x.pop()
                z = 'https://gist.githubusercontent.com' + y
        except:
            print(".file-actions class found, link mia")
            z = ""
    except:
        print(".file-actions class not found")
        z = ""
    return z

print(find_raw_link(html_text))






