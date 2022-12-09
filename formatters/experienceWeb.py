def experienceShortWeb(inlist):
    outlist = []
    for item in inlist:
        if 'year' not in item.keys():
            raise ValueError("'year' key is required for experience formatter")
        outstr = "<li>"
        if isinstance(item['year'], list):
            for i, year in enumerate(item['year']):
                if i > 0:
                    outstr = outstr + f"</li>\n<li>{year}. "
                else:
                    outstr = outstr + f"{year}. "
                outstr = outstr + "<b>"
                if 'title' in item.keys():
                    if isinstance(item['title'], list):
                        outstr = outstr + f"{item['title'][i]}"
                    else:
                        outstr = outstr + f"{item['title']}"
                if 'subtitle' in item.keys():
                    if isinstance(item['subtitle'], list):
                        outstr = outstr + f", {item['subtitle'][i]}"
                    else:
                        outstr = outstr + f", {item['subtitle']}"
                if 'institution' in item.keys():
                    if isinstance(item['institution'], list):
                        outstr = outstr + f": {item['institution'][i]}"
                    else:
                        outstr = outstr + f": {item['institution']}"
                outstr = outstr + "</b>"
                if 'department' in item.keys():
                    if isinstance(item['department'], list):
                        outstr = outstr + f", {item['department'][i]}"
                    else:
                        outstr = outstr + f", {item['department']}"
        else:
            outstr = outstr + f"{item['year']}. "
            outstr = outstr + "<b> "
            if 'title' in item.keys():
                outstr = outstr + f"{item['title']}"
            if 'subtitle' in item.keys():
                outstr = outstr + f", {item['title']}"
            if 'institution' in item.keys():
                outstr = outstr + f": {item['institution']}"
            outstr = outstr + "</b>"
            if 'department' in item.keys():
                outstr = outstr + f", {item['department']}"
        outstr = outstr + "</li>\n"
        outlist.append(outstr)
    return "<ul>\n" + "".join(outlist) + "</ul>"

def experienceLongWeb(inlist):
    outlist = []
    for item in inlist:
        if 'year' not in item.keys():
            raise ValueError("'year' key is required for experience formatter")
        outstr = "<li>"
        if isinstance(item['year'], list):
            for i, year in enumerate(item['year']):
                if i > 0:
                    outstr = outstr + f"\n    <br>{year}. "
                else:
                    outstr = outstr + f"{year}. "
                outstr = outstr + "<b>"
                if 'title' in item.keys():
                    if isinstance(item['title'], list):
                        outstr = outstr + f"{item['title'][i]}"
                    else:
                        outstr = outstr + f"{item['title']}"
                if 'subtitle' in item.keys():
                    if isinstance(item['subtitle'], list):
                        outstr = outstr + f", {item['subtitle'][i]}"
                    else:
                        outstr = outstr + f", {item['subtitle']}"
                if 'institution' in item.keys():
                    if isinstance(item['institution'], list):
                        outstr = outstr + f": {item['institution'][i]}"
                    else:
                        outstr = outstr + f": {item['institution']}"
                outstr = outstr + "</b>"
                if 'department' in item.keys():
                    if isinstance(item['department'], list):
                        outstr = outstr + f", {item['department'][i]}"
                    else:
                        outstr = outstr + f", {item['department']}"
        else:
            outstr = outstr + f"{item['year']}. "
            outstr = outstr + "<b> "
            if 'title' in item.keys():
                outstr = outstr + f"{item['title']}"
            if 'subtitle' in item.keys():
                outstr = outstr + f", {item['subtitle']}"
            if 'institution' in item.keys():
                outstr = outstr + f": {item['institution']}"
            outstr = outstr + "</b>"
            if 'department' in item.keys():
                outstr = outstr + f", {item['department']}"
        if 'description' in item.keys():
            outstr = outstr + "\n    <ul>"
            if isinstance(item['description'], str):
                outstr = outstr + "\n    <li>"
                outstr = outstr + f"{item['description']}</li>\n"
            elif isinstance(item['description'], list):
                for i2 in item['description']:
                    outstr = outstr + "\n    <li>"
                    outstr = outstr + f"{i2}</li>\n"
            outstr = outstr + "    </ul>\n"
        outstr = outstr + "</li>\n"
        outlist.append(outstr)
    return "<ul>\n" + "".join(outlist) + "</ul>"

def degreeLongWeb(inlist):
    outlist = []
    for item in inlist:
        outstr = "<li>"
        if 'year' not in item.keys() or 'title' not in item.keys() or \
           'institution' not in item.keys() or 'subtitle' not in item.keys():
            raise ValueError("'year', 'title', 'subtitle', and 'institution'"
                             + " are required keys for degree formatter")
        outstr = outstr + (f"{item['title']}, {item['year']}, " +
                           f"{item['subtitle']}, {item['institution']}\n")
        if 'description' in item.keys():
            outstr = outstr + "\n    <ul>"
            if isinstance(item['description'], str):
                outstr = outstr + "\n    <li>"
                outstr = outstr + f"<i>{item['description']}</i></li>\n"
            elif isinstance(item['description'], list):
                for i2 in item['description']:
                    outstr = outstr + "\n    <li>"
                    outstr = outstr + f"<i>{i2}</i></li>\n"
            outstr = outstr + "    </ul>\n"
        outstr = outstr + "</li>\n"
        outlist.append(outstr)
    return "<ul>\n" + "".join(outlist) + "</ul>"

def degreeShortWeb(inlist):
    outlist = []
    for item in inlist:
        outstr = "<li>"
        if 'year' not in item.keys() or 'title' not in item.keys() or \
           'institution' not in item.keys() or 'subtitle' not in item.keys():
            raise ValueError("'year', 'title', 'subtitle', and 'institution'"
                             + " are required keys for degree formatter")
        outstr = outstr + (f"{item['title']}, {item['year']}, " +
                           f"{item['subtitle']}, {item['institution']}\n")
        outstr = outstr + "</li>\n"
    return "<ul>\n" + "".join(outlist) + "</ul>"
