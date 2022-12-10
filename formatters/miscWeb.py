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
        if 'name' in item.keys():
            newstr = newstr + f" {item['name']}"
        if 'institution' in item.keys():
            newstr = newstr + f" ({item['institution']})"
        if 'type' in item.keys():
            newstr = newstr + f", {item['type']}"
        if 'description' in item.keys():
            newstr = newstr + "<ul>\n"
            for desc in item['description']:
                newstr = newstr + f"<li>{desc}</li>\n"
            newstr = newstr + "</ul>\n"
        outlist.append(newstr)
    return "\n<br>\n".join(outlist) + "\n"

def peopleShortWeb(inlist):
    outlist = []
    for item in inlist:
        newstr = ""
        if 'year' in item.keys():
            newstr = newstr + f"{item['year']}. "
        if 'name' in item.keys():
            newstr = newstr + f" {item['name']}"
        if 'institution' in item.keys():
            newstr = newstr + f" ({item['institution']})"
        if 'type' in item.keys():
            newstr = newstr + f", {item['type']}"
        outlist.append(newstr)
    return "\n<br>\n".join(outlist) + "\n"
