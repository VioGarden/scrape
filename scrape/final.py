import datetime, json, requests, sqlite3, time, urllib.request
from requests_html import HTML

from lists import farr

print(farr)

full = len(farr)
for i in range(full):
    start = time.time()

    print(f"starting: {i}/{full}")

    now = datetime.datetime.now()
    second = now.second
    micro = now.microsecond

    print(1)

    url = farr[i]

    def url_to_txt(url, filename=f"test.html", save=False):
        """
        input : url from google sheets
        output : html/text of google sheets link
        """
        print(2)
        r = requests.get(url)
        if r.status_code == 200:
            print(3)
            html_text = r.text
            # if save:
            #     with open(f"file-{second}-{micro}", 'w') as f:
            #         f.write(html_text)
            return html_text
        print("????")
        return ""

    html_text = url_to_txt(url) 
    # print(html_text)
    if not html_text:
        print("wat")
        break

    def find_raw_link(html_text):
        """
        input : html of google sheets link
        output : the specified raw json data link
        """
        print(4)
        r_html = HTML(html=html_text)
        table_class = ".file-actions"
        r_table = r_html.find(table_class)
        try:
            if r_table:
                element = r_table[0]
            try:
                if element.links:
                    print(5)
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

    json_link = find_raw_link(html_text)
    print(6)
    print(json_link)

    # gets json data from website
    with urllib.request.urlopen(json_link) as url:
        try:
            data = json.load(url)
        except:
            data = ""
            print("-----------json.decoder.JSONDecodeError----------")
            print("for list index: ", i)
    print(7)
    if not data:
        print("no data no data no data no data no data no data no data no data")
        continue

    final = []
    for i in range(len(data)):
        temp_dict = {}
        curr = data[i]
        if 'animeEng' in curr:
            temp_dict["title"] = curr['animeEng']
        else:
            temp_dict["title"] = ''

        if 'animeRomaji' in curr:
            temp_dict['titleRom'] = curr['animeRomaji']
        else:
            temp_dict['titleRom'] = ''

        # if 'annId' in curr:
        #     temp_dict['annid'] = curr['annId']
        # else:
        #     temp_dict['annid'] = None

        if 'songName' in curr:
            temp_dict['song'] = curr['songName']
        else:
            temp_dict['song'] = ''

        if 'artist' in curr:
            temp_dict['artist'] = curr['artist']
        else:
            temp_dict['artist'] = ''

        if 'type' in curr:
            temp_dict['opedin'] = curr['type']
        else:
            temp_dict['opedin'] = ''

        if 'LinkVideo' in curr:
            temp_dict['video'] = curr['LinkVideo']
        else:
            temp_dict['video'] = ''

        if 'LinkMp3' in curr:
            temp_dict['audio'] = curr['LinkMp3']
        else:
            temp_dict['audio'] = ''
        final.append(temp_dict)
    print(8)

    final2 = []
    for i in range(len(final)):
        final2.append(tuple(final[i].values()))
    print(9)

    conn = sqlite3.connect('base.db') # connection (creates) to database
    print(10)

    c = conn.cursor() # to start sql commands

    # c.execute("""
    #     CREATE TABLE AMQ (
    #     title VARCHAR,
    #     titleRom VARCHAR, 
    #     song VARCHAR,
    #     artist VARCHAR,
    #     opedin VARCHAR,
    #     video VARCHAR,
    #     audio VARCHAR,
    #     un_min text GENERATED ALWAYS AS (MIN(title, song, artist, opedin)),
    #     un_max text GENERATED ALWAYS AS (MAX(title, song, artist, opedin)),
    #     UNIQUE(un_min, un_max));
    # """)


    sql = """INSERT OR IGNORE INTO amq
    (title, titleRom, song, artist, opedin, video, audio) 
    VALUES (?, ?, ?, ?, ?, ?, ?);"""

    c.executemany(sql, final2)
    print(11)

    conn.commit()

    conn.close()
    print("------------------------------------")
    end = time.time()
    print(end - start)
    print("------------------------------------")

# conn = sqlite3.connect('base.db') # connection (creates) to database

# c = conn.cursor() # to start sql commands

# c.execute("""
#     CREATE TABLE AMQ (
#     title VARCHAR,
#     titleRom VARCHAR, 
#     song VARCHAR,
#     artist VARCHAR,
#     opedin VARCHAR,
#     video VARCHAR,
#     audio VARCHAR,
#     un_min text GENERATED ALWAYS AS (MIN(title, song, artist, opedin)),
#     un_max text GENERATED ALWAYS AS (MAX(title, song, artist, opedin)),
#     UNIQUE(un_min, un_max));
# """)

# conn.commit()

# conn.close()
# print("------------------------------------")