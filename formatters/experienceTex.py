def experienceShortTex(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        outstr = outstr + "{\\bf "
        if 'title' in item.keys():
            outstr = outstr + f"{item['title']}: "
        if 'institution' in item.keys():
            outstr = outstr + f"{item['institution']}"
        outstr = outstr + "}"
        if 'department' in item.keys():
            outstr = outstr + f", {item['department']}"
        outlist.append(outstr)
    return "\n\n\\bigskip\n\n".join(outlist)

def experienceLongTex(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        outstr = outstr + "{\\bf "
        if 'title' in item.keys():
            outstr = outstr + f"{item['title']}: "
        if 'institution' in item.keys():
            outstr = outstr + f"{item['institution']}"
        outstr = outstr + "}"
        if 'department' in item.keys():
            outstr = outstr + f", {item['department']}"
        if 'description' in item.keys():
            if isinstance(item['description'], str):
                outstr = outstr + "\n\\bullitem "
                outstr = outstr + f"{item['description']}"
            elif isinstance(item['description'], list):
                for i2 in item['description']:
                    outstr = outstr + "\n\\bullitem "
                    outstr = outstr + f"{i2}"
        outlist.append(outstr)
    return "\n\n\\bigskip\n\n".join(outlist)
