def experienceShortTex(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'year' not in item.keys():
            raise ValueError("'year' key is required for experience formatter")
        if isinstance(item['year'], list):
            for i, year in enumerate(item['year']):
                if i > 0:
                    outstr = outstr + "\\\\\n \\tabboxsmall{" + f"{year}" + ".} "
                else:
                    outstr = outstr + "\\tabboxsmall{" + f"{year}" + ".} "
                outstr = outstr + "{\\bf "
                if 'title' in item.keys():
                    if isinstance(item['title'], list):
                        outstr = outstr + f"{item['title'][i]}: "
                    else:
                        outstr = outstr + f"{item['title']}: "
                if 'institution' in item.keys():
                    if isinstance(item['institution'], list):
                        outstr = outstr + f"{item['institution'][i]}"
                    else:
                        outstr = outstr + f"{item['institution']}"
                outstr = outstr + "}"
                if 'department' in item.keys():
                    if isinstance(item['department'], list):
                        outstr = outstr + f", {item['department'][i]}"
                    else:
                        outstr = outstr + f", {item['department']}"
        else:
            outstr = outstr + "\\tabboxsmall{" + f"{item['year']}" + ".} "
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
        if 'year' not in item.keys():
            raise ValueError("'year' key is required for experience formatter")
        if isinstance(item['year'], list):
            for i, year in enumerate(item['year']):
                if i > 0:
                    outstr = outstr + "\\\\\n \\tabboxmed{" + f"{year}" + ".} "
                else:
                    outstr = outstr + "\\tabboxmed{" + f"{year}" + ".} "
                outstr = outstr + "{\\bf "
                if 'title' in item.keys():
                    if isinstance(item['title'], list):
                        outstr = outstr + f"{item['title'][i]}: "
                    else:
                        outstr = outstr + f"{item['title']}: "
                if 'institution' in item.keys():
                    if isinstance(item['institution'], list):
                        outstr = outstr + f"{item['institution'][i]}"
                    else:
                        outstr = outstr + f"{item['institution']}"
                outstr = outstr + "}"
                if 'department' in item.keys():
                    if isinstance(item['department'], list):
                        outstr = outstr + f", {item['department'][i]}"
                    else:
                        outstr = outstr + f", {item['department']}"
        else:
            outstr = outstr + "\\tabboxmed{" + f"{item['year']}" + ".} "
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
