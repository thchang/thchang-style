def experienceShortTex(inlist):
    outlist = []
    for item in inlist:
        size = "small"
        if 'year' not in item.keys() and 'start' not in item.keys():
            raise ValueError("'year' or 'start' key is required for experience formatter")
        if 'start' in item.keys():
            size = "med"
            if 'end' in item.keys():
                if isinstance(item['start'], list):
                    years = [f"{si} - {ei}" for si, ei in zip(item['start'],
                                                              item['end'])]
                else:
                    years = f"{item['start']} - {item['end']}"
            else:
                if isinstance(item['start'], list):
                    years = [f"{si} - Present" for si in item['start']]
                else:
                    years = f"{item['start']} - Present"
        else:
            if isinstance(item['year'], list):
                years = [f"{yi}" for yi in item['year']]
            else:
                years = f"{item['year']}"
        if isinstance(years, list):
            for i, year in enumerate(years):
                outstr = f"\\tabbox{size}{{{year}.}}{{\\bf "
                if 'title' in item.keys():
                    if isinstance(item['title'], list):
                        outstr = outstr + f"{item['title'][i]}"
                    else:
                        outstr = outstr + f"{item['title']}"
                if 'institution' in item.keys():
                    if isinstance(item['institution'], list):
                        outstr = outstr + f": {item['institution'][i]}"
                    else:
                        outstr = outstr + f": {item['institution']}"
                outstr = outstr + "}"
                if 'department' in item.keys():
                    if isinstance(item['department'], list):
                        outstr = outstr + f", {item['department'][i]}"
                    else:
                        outstr = outstr + f", {item['department']}"
                if 'subtitle' in item.keys():
                    if isinstance(item['subtitle'], list):
                        outstr = outstr + f" ({item['subtitle'][i]})"
                    else:
                        outstr = outstr + f" ({item['subtitle']})"
                outlist.append(outstr)
        else:
            outstr = f"\\tabbox{size}{{{years}.}}{{\\bf "
            if 'title' in item.keys():
                outstr = outstr + f"{item['title']}"
            if 'institution' in item.keys():
                outstr = outstr + f": {item['institution']}"
            outstr = outstr + "}"
            if 'department' in item.keys():
                outstr = outstr + f", {item['department']}"
            if 'subtitle' in item.keys():
                outstr = outstr + f" ({item['subtitle']})"
            outlist.append(outstr)
    return "\n\n\\smallskip\n\n".join(outlist)

def experienceLongTex(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'year' not in item.keys() and 'start' not in item.keys():
            raise ValueError("'year' or 'start' key is required for experience formatter")
        if 'start' in item.keys():
            if 'end' in item.keys():
                if isinstance(item['start'], list):
                    years = [f"{si} - {ei}" for si, ei in zip(item['start'],
                                                              item['end'])]
                else:
                    years = f"{item['start']} - {item['end']}"
            else:
                if isinstance(item['start'], list):
                    years = [f"{si} - Present" for si in item['start']]
                else:
                    years = f"{item['start']} - Present"
        else:
            if isinstance(item['year'], list):
                years = [f"{yi}" for yi in item['year']]
            else:
                years = f"{item['year']}"
        if isinstance(years, list):
            for i, year in enumerate(years):
                if i > 0:
                    outstr = outstr + "\\\\\n \\tabboxmed{" + f"{year}" + ".} "
                else:
                    outstr = outstr + "\\tabboxmed{" + f"{year}" + ".} "
                outstr = outstr + "{\\bf "
                if 'title' in item.keys():
                    if isinstance(item['title'], list):
                        outstr = outstr + f"{item['title'][i]}"
                    else:
                        outstr = outstr + f"{item['title']}"
                if 'institution' in item.keys():
                    if isinstance(item['institution'], list):
                        outstr = outstr + f": {item['institution'][i]}"
                    else:
                        outstr = outstr + f": {item['institution']}"
                outstr = outstr + "}"
                if 'department' in item.keys():
                    if isinstance(item['department'], list):
                        outstr = outstr + f", {item['department'][i]}"
                    else:
                        outstr = outstr + f", {item['department']}"
        else:
            outstr = outstr + "\\tabboxmed{" + f"{years}" + ".} "
            outstr = outstr + "{\\bf "
            if 'title' in item.keys():
                outstr = outstr + f"{item['title']}"
            if 'institution' in item.keys():
                outstr = outstr + f": {item['institution']}"
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
    return "\n\n\\medskip\n\n".join(outlist)

def degreeLongTex(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'title' not in item.keys() or 'institution' not in item.keys() \
           or 'subtitle' not in item.keys():
            raise ValueError("'title', 'subtitle', and 'institution'"
                             + " are required keys for degree formatter")
        if 'year' not in item.keys() and 'start' not in item.keys():
            raise ValueError("'year' or 'start' key is required for degree formatter")
        if 'start' in item.keys():
            if 'end' in item.keys():
                if isinstance(item['start'], list):
                    years = [f"{si} - {ei}" for si, ei in zip(item['start'],
                                                              item['end'])]
                else:
                    years = f"{item['start']} - {item['end']}"
            else:
                if isinstance(item['start'], list):
                    years = [f"{si} - Present" for si in item['start']]
                else:
                    years = f"{item['start']} - Present"
        else:
            if isinstance(item['year'], list):
                years = [f"{yi}" for yi in item['year']]
            else:
                years = f"{item['year']}"
        outstr = outstr + (f"{item['title']}, {years}, " +
                           f"{item['subtitle']}, {item['institution']}\n")
        if 'description' in item.keys():
            if isinstance(item['description'], str):
                outstr = outstr + "\n\\bullitem { "
                outstr = outstr + f"{item['description']}" + "}\n"
            elif isinstance(item['description'], list):
                for i2 in item['description']:
                    outstr = outstr + "\n\\bullitem { "
                    outstr = outstr + f"{i2}" + "}\n"
        outlist.append(outstr)
    return "\n\n\\medskip\n\n".join(outlist)

def degreeShortTex(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'title' not in item.keys() or 'institution' not in item.keys() \
           or 'subtitle' not in item.keys():
            raise ValueError("'title', 'subtitle', and 'institution'"
                             + " are required keys for degree formatter")
        if 'year' not in item.keys() and 'start' not in item.keys():
            raise ValueError("'year' or 'start' key is required for degree formatter")
        if 'start' in item.keys():
            if 'end' in item.keys():
                if isinstance(item['start'], list):
                    years = [f"{si} - {ei}" for si, ei in zip(item['start'],
                                                              item['end'])]
                else:
                    years = f"{item['start']} - {item['end']}"
            else:
                if isinstance(item['start'], list):
                    years = [f"{si} - Present" for si in item['start']]
                else:
                    years = f"{item['start']} - Present"
        else:
            if isinstance(item['year'], list):
                years = [f"{yi}" for yi in item['year']]
            else:
                years = f"{item['year']}"
        outstr = outstr + (f"{item['title']}, {years}, " +
                           f"{item['subtitle']}, {item['institution']}\n")
        if 'honors' in item.keys():
            outstr = outstr + f", {{\\sl {item['honors']}}}"
        outlist.append(outstr)
    return "\n\n\\smallskip\n\n".join(outlist)
