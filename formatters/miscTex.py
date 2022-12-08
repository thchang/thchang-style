def singlelineTex(inlist):
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

def multilineTex(inlist):
    outlist = []
    for item1 in inlist:
        if isinstance(item1, list):
            for item2 in item1:
                outlist.append(str(item2).strip())
        elif isinstance(item1, dict):
            if 'year' in item1.keys():
                outstr = "\\tabboxsmall{ " + f"{item1['year']}" + ".}"
            else:
                outstr = ""
            if 'title' in item1.keys():
                outstr = outstr + "{\\sl " + f"{item1['title']}" + "}"
            for key2 in item1.keys():
                if key2 not in ('year', 'title'):
                    outstr = outstr + f", {item1[key2]}".strip()
            outlist.append(outstr)
        elif isinstance(item1, str):
            outlist.append(item1.strip())
    if len(outlist) == 0:
        return ""
    else:
        return "\n\n".join(outlist) + "\n\n"

def bulletDateTex(inlist):
    outlist = []
    for item in inlist:
        newstr = ""
        if 'title' in item.keys():
            newstr = newstr + f"\\bullitem {item['title']}"
        else:
            raise ValueError(f"cannot format {item}; missing 'title' field")
        if 'year' in item.keys():
            newstr = newstr + f" ({item['year']})"
        outlist.append(newstr)
    return "\n".join(outlist) + "\n\n"

def bulletNoDateTex(inlist):
    outlist = []
    for item in inlist:
        newstr = ""
        if 'title' in item.keys():
            newstr = newstr + f"\\bullitem {item['title']}"
        else:
            raise ValueError(f"cannot format {item}; missing 'title' field")
        outlist.append(newstr)
    return "\n".join(outlist) + "\n\n"

def peopleTex(inlist):
    outlist = []
    for item in inlist:
        newstr = ""
        if 'year' in item.keys():
            newstr = newstr + "\\tabboxmed{ " + f"{item['year']}." + "}"
        if 'name' in item.keys():
            newstr = newstr + f" {item['name']}"
        if 'institution' in item.keys():
            newstr = newstr + f" ({item['institution']})"
        if 'type' in item.keys():
            newstr = newstr + f", {item['type']}"
        newstr = newstr + "\n"
        if 'description' in item.keys():
            for desc in item['description']:
                newstr = newstr + f"\\bullitem {desc}\n"
        outlist.append(newstr)
    return "\n\n\\bigskip\n\n".join(outlist) + "\n\n"

def peopleShortTex(inlist):
    outlist = []
    for item in inlist:
        newstr = ""
        if 'year' in item.keys():
            newstr = newstr + "\\tabboxsmall{ " + f"{item['year']}." + "}"
        if 'name' in item.keys():
            newstr = newstr + f" {item['name']}"
        if 'institution' in item.keys():
            newstr = newstr + f" ({item['institution']})"
        if 'type' in item.keys():
            newstr = newstr + f", {item['type']}"
        outlist.append(newstr)
    return "\n\n\\bigskip\n\n".join(outlist) + "\n\n"