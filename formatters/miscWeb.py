def singlelineWeb(inlist):
    outlist = []
    for item1 in inlist:
        if isinstance(item1, list):
            for item2 in item1:
                outlist.append(str(item2).strip())
        elif isinstance(item1, dict):
            for key2 in item1.keys():
                outlist.append(f"{key2}: {item1[key2]}".strip())
        elif isinstance(item1, str):
            outlist.append(item1.strip())
    if len(outlist) == 0:
        outstr = ""
    elif len(outlist) == 1:
        outstr = outlist[0][0].upper() + outlist[0][1:]
    elif len(outlist) == 1:
        outstr = outlist[0][0].upper() + outlist[0][1:] + " and " + outlist[1]
    elif len(outlist) > 1:
        outstr = outlist[0][0].upper() + outlist[0][1:] + ", " + ", ".join(outlist[1:-1]) + ", and " + outlist[-1]
    return outstr

def multilineWeb(inlist):
    outlist = []
    for item1 in inlist:
        if isinstance(item1, list):
            for item2 in item1:
                outlist.append(str(item2).strip())
        elif isinstance(item1, dict):
            if 'year' in item1.keys():
                outstr = f"{item1['year']}. "
            else:
                outstr = ""
            if 'title' in item1.keys():
                outstr = outstr + f"<i>{item1['title']}</i>"
            for key2 in item1.keys():
                if key2 not in ('year', 'title'):
                    outstr = outstr + f", {item1[key2]}".strip()
            outlist.append(outstr)
        elif isinstance(item1, str):
            outlist.append(item1.strip())
    if len(outlist) == 0:
        return ""
    else:
        return "\n<br>\n".join(outlist) + "\n<br>\n"

def bulletDateWeb(inlist):
    outlist = []
    for item in inlist:
        newstr = "<li>"
        if 'title' in item.keys():
            newstr = newstr + f"{item['title']}"
        else:
            raise ValueError(f"cannot format {item}; missing 'title' field")
        if 'year' in item.keys():
            newstr = newstr + f" ({item['year']})"
        newstr = newstr + "</li>"
        outlist.append(newstr)
    return "<ul>\n" + "\n".join(outlist) + "\n</ul>\n"

def bulletNoDateWeb(inlist):
    outlist = []
    for item in inlist:
        newstr = "<li>"
        if 'title' in item.keys():
            newstr = newstr + f"{item['title']}"
        else:
            raise ValueError(f"cannot format {item}; missing 'title' field")
        newstr = newstr + "</li>"
        outlist.append(newstr)
    return "<ul>\n" + "\n".join(outlist) + "\n</ul>\n"

def peopleWeb(inlist):
    outlist = []
    for item in inlist:
        newstr = ""
        if 'year' in item.keys():
            newstr = newstr + f"{item['year']}. "
        elif 'start' in item.keys():
            if 'end' in item.keys():
                end = item['end']
            else:
                end = "Present"
            newstr = newstr + f"{item['start']} - {end}. "
        if 'name' in item.keys():
            if 'website' in item.keys():
                newstr = (newstr + f""" <a href="{item['website']}">""" +
                          f"""{item['name']}""")
            else:
                newstr = newstr + f" {item['name']}"
        if 'institution' in item.keys():
            newstr = newstr + f" ({item['institution']})"
        if 'website' in item.keys():
            newstr = newstr + "</a>"
        if 'type' in item.keys():
            newstr = newstr + f", {item['type']}"
        if 'description' in item.keys():
            newstr = newstr + "<ul>\n"
            for desc in item['description']:
                newstr = newstr + f"<li>{desc}</li>\n"
            newstr = newstr + "</ul>\n"
        outlist.append(newstr)
    return "<br>\n" + "\n<br>\n".join(outlist) + "\n"

def peopleShortWeb(inlist):
    outlist = []
    for item in inlist:
        newstr = ""
        if 'year' in item.keys():
            newstr = newstr + f"{item['year']}. "
        elif 'start' in item.keys():
            if 'end' in item.keys():
                end = item['end']
            else:
                end = "Present"
            newstr = newstr + f"{item['start']} - {end}. "
        if 'name' in item.keys():
            if 'website' in item.keys():
                newstr = (newstr + f""" <a href="{item['website']}">""" +
                          f"""{item['name']}</a>""")
            else:
                newstr = newstr + f" {item['name']}"
        if 'institution' in item.keys():
            newstr = newstr + f" ({item['institution']})"
        if 'type' in item.keys():
            newstr = newstr + f", {item['type']}"
        outlist.append(newstr)
    return "<br>\n" + "\n<br>\n".join(outlist) + "\n"

def paragraphWeb(inlist):
    outlist = []
    for item1 in inlist:
        if isinstance(item1, str):
            outlist.append(f"{str(item1)}")
        elif isinstance(item1, dict):
            for key in item1.keys():
                if isinstance(item1[key], str):
                    outlist.append(f"{str(item1[key])}")
                elif isinstance(item1[key], list):
                    outstr = "<ul>\n"
                    for item2 in item1[key]:
                        outstr = outstr + f"<li>{str(item2)}</li>\n"
                    outstr = outstr + "</ul>"
                    outlist.append(outstr)
    return "\n</p>\n<p>\n".join(outlist)

def linktreeWeb(inlist):
    outlist = []
    for item in inlist:
        newstr = ""
        if isinstance(item, dict):
            for key in item.keys():
                newstr = (newstr + '<li><a target="_blank"' +
                          f'href="{item[key]}">{key}</a></li>\n')
        elif isinstance(item, list):
            for itemi in item:
                newstr = (newstr + '<li><a target="_blank"' +
                          f'href="{itemi}">{itemi}</a></li>\n')
        elif isinstance(item, str):
            newstr = ('<li><a target="_blank"' +
                      f'href="{item}">{item}</a></li>\n')
        outlist.append(newstr)
    return "<ul>\n" + "".join(outlist) + "\n</ul>\n"

def skillsWeb(inlist):
    outlist = []
    for item1 in inlist:
        if isinstance(item1, list):
            outlist.append(", ".join([str(item2).strip() for item2 in item1]))
        elif isinstance(item1, dict):
            for key2 in item1.keys():
                outstr = (f"<b>{key2}:</b> " +
                          ", ".join([str(i2).strip() for i2 in item1[key2]]))
                outlist.append(outstr)
        elif isinstance(item1, str):
            outlist.append(item1.strip())
    return "\n<br>\n".join(outlist)

def contactRowWeb(inlist):
    outlist = []
    for item in inlist:
        linklist = []
        if isinstance(item, dict):
            if "email" in item.keys():
                linklist.append(["email", f"mailto:{item['email']}"])
            if "links" in item.keys():
                for key in item["links"].keys():
                    linklist.append([key, item["links"][key]])
            if "images" in item.keys():
                for i in range(len(linklist)):
                    if linklist[i][0] in item["images"].keys():
                        linklist[i][0] = f"""<img src="{item['images'][linklist[i][0]]}" width="25em" hspace="5em" vspace="5em">"""
    for link in linklist:
        outlist.append(f"""<a href="{link[1]}">{link[0]}</a>""")
    return "\n".join(outlist)
    #return '<ul class="nav nav-pills">\n' + "\n".join(outlist) + "\n</ul>"

def newsWeb(inlist):
    maxlen = 6
    outlist = []
    for item in inlist:
        outstr = ""
        if "year" in item.keys():
            outstr = outstr + f"<b>{item['year']}: </b>"
        if "title" in item.keys():
            outstr = outstr + f"<i>{item['title']}</i>"
        if "booktitle" in item.keys():
            outstr = outstr + f" at {item['booktitle']}"
        if len(outlist) < maxlen:
            outlist.append(outstr)
    return '\n<div style="background-color:rgb(240,240,240);padding-top:30px;padding-right:30px;padding-bottom:30px;padding-left:30px;">\n' + "\n<br><br>\n".join(outlist) + "\n</div>"
