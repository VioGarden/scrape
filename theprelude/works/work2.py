import json

with open("test.json", "r") as readjson:
    data = json.load(readjson)

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

file = open('test2.json', 'a')
file.write(json.dumps(final, indent=2))
file.close()

