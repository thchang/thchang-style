def articleTex(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'author' in item.keys():
            outstr = outstr + f"{item['author']}. "
        if 'title' in item.keys():
            outstr = outstr + f"{item['title']}. "
        if 'journal' in item.keys():
            outstr = outstr + "{\\sl " + f"{item['journal']}" + "}"
            if 'volume' in item.keys():
                outstr = outstr + f" {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f"({item['number']})"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ". "
        if 'note' in item.keys():
            outstr = outstr + f"{item['note']}. "
        if 'doi' in item.keys():
            outstr = (outstr + "{\\tt doi:} \\href{https://doi.org/" +
                      f"{item['doi']}" + "}{" + f"{item['doi']}" + "}")
        elif 'url' in item.keys():
            outstr = outstr + "{\\tt url:} \\url{" + f"{item['url']}" + "}"
        elif 'isbn' in item.keys():
            outstr = outstr + "In {\\tt isbn:} " + f"{item['isbn']}"
        outlist.append(outstr)
    return "\n\n\\medskip\n\n".join(outlist)

def proceedingsTex(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'author' in item.keys():
            outstr = outstr + f"{item['author']}. "
        if 'title' in item.keys():
            outstr = outstr + f"{item['title']}. "
        if 'booktitle' in item.keys():
            outstr = outstr + "{\\sl In " + f"{item['booktitle']}"
            if 'volume' in item.keys():
                outstr = outstr + f" Vol. {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f", No. {item['number']}"
            outstr = outstr  + "}"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ". "
        if 'location' in item.keys():
            outstr = outstr + f"{item['location']}. "
        if 'note' in item.keys():
            outstr = outstr + f"{item['note']}. "
        if 'doi' in item.keys():
            outstr = (outstr + "{\\tt doi:} \\href{https://doi.org/" +
                      f"{item['doi']}" + "}{" + f"{item['doi']}" + "}")
        elif 'url' in item.keys():
            outstr = outstr + "{\\tt url:} \\url{" + f"{item['url']}" + "}"
        elif 'isbn' in item.keys():
            outstr = outstr + "In {\\tt isbn:} " + f"{item['isbn']}"
        outlist.append(outstr)
    return "\n\n\\medskip\n\n".join(outlist)

def techreportTex(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'author' in item.keys():
            outstr = outstr + f"{item['author']}. "
        if 'title' in item.keys():
            outstr = outstr + "{\\sl " + f"{item['title']}" + "}. "
        if 'type' in item.keys():
            outstr = outstr + f"{item['type']}"
            if 'number' not in item.keys():
                outstr = outstr + ". "
        if 'number' in item.keys():
            outstr = outstr + f" {item['number']}. "
        if 'organization' in item.keys():
            outstr = outstr + f"{item['organization']}"
            if 'location' in item.keys():
                outstr = outstr + ", " + f"{item['location']}"
            outstr = outstr + ". "
        if 'note' in item.keys():
            outstr = outstr + f"{item['note']}. "
        if 'doi' in item.keys():
            outstr = (outstr + "{\\tt doi:} \\href{https://doi.org/" +
                      f"{item['doi']}" + "}{" + f"{item['doi']}" + "}")
        elif 'url' in item.keys():
            outstr = outstr + "{\\tt url:} \\url{" + f"{item['url']}" + "}"
        elif 'isbn' in item.keys():
            outstr = outstr + "In {\\tt isbn:} " + f"{item['isbn']}"
        outlist.append(outstr)
    return "\n\n\\medskip\n\n".join(outlist)

def talkTex(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'month' in item.keys():
            outstr = outstr + f"{item['month']} "
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'author' in item.keys():
            outstr = outstr + f"{item['author']}. "
        if 'title' in item.keys():
            outstr = outstr + f"{item['title']}. "
        if 'booktitle' in item.keys():
            outstr = outstr + "{\\sl " + f"{item['booktitle']}"
            if 'volume' in item.keys():
                outstr = outstr + f" Vol. {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f", No. {item['number']}"
            outstr = outstr  + "}"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ", "
        if 'location' in item.keys():
            outstr = outstr + f"{item['location']}. "
        if 'note' in item.keys():
            outstr = outstr + f"{item['note']}. "
        outlist.append(outstr)
    return "\n\n\\medskip\n\n".join(outlist)

def miscPubTex(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'author' in item.keys():
            outstr = outstr + f"{item['author']}. "
        if 'title' in item.keys():
            outstr = outstr + f"{item['title']}. "
        if 'journal' in item.keys():
            outstr = outstr + "{\\sl " + f"{item['journal']}" + "}"
            if 'volume' in item.keys():
                outstr = outstr + f" {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f"({item['number']})"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ". "
        if 'booktitle' in item.keys():
            outstr = outstr + "{\\sl " + f"{item['booktitle']}"
            if 'volume' in item.keys():
                outstr = outstr + f" Vol. {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f", No. {item['number']}"
            outstr = outstr  + "}"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ". "
        if 'location' in item.keys():
            outstr = outstr + f"{item['location']}. "
        if 'note' in item.keys():
            outstr = outstr + f"{item['note']}. "
        outlist.append(outstr)
    return "\n\n\\medskip\n\n".join(outlist)

def softwareTex(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'title' in item.keys():
            outstr = outstr + "{\\bf " + f"{item['title']}" + "}"
            if 'subtitle' in item.keys():
                outstr = outstr + f": {item['subtitle']}. "
            else:
                outstr = outstr + ". "
            if 'version' in item.keys():
                outstr = outstr + f"Release: {item['version']}"
        outstr = outstr + "\\\\\n"
        if 'author' in item.keys():
            outstr = outstr + f"Devs: {item['author']} \\hskip 2em"
        if 'language' in item.keys():
            outstr = (outstr + "Primary Prog. Lang: {\\tt " +
                      f"{item['language']}" + "}")
        if 'note' in item.keys():
            outstr = outstr + f"\\\\\n{item['note']}"
        if 'doi' in item.keys():
            outstr = (outstr + "\\\\\n{\\tt doi:} \\href{https://doi.org/" +
                      f"{item['doi']}" + "}{" + f"{item['doi']}" + "}")
        if 'git' in item.keys():
            outstr = (outstr + "\\\\\n{\\tt git:} \\url{" +
                      f"{item['git']}" + "}")
        if 'url' in item.keys():
            outstr = outstr + "\\\\\n{\\tt url:} \\url{" + f"{item['url']}" + "}"
        outlist.append(outstr)
    return "\n\n\\medskip\n\n".join(outlist)

def proposalTex(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + "\\tabboxsmall{" f"{item['year']}." + "} "
        elif 'start' in item.keys():
            outstr = outstr + "\\tabboxmed{" f"{item['start']} - "
            if 'end' in item.keys():
                outstr = outstr + f"{item['end']}.}} "
            else:
                outstr = outstr + "Present.} "
        if 'title' in item.keys():
            outstr = outstr + f"{item['title']}"
            if 'subtitle' in item.keys():
                outstr = outstr + f": {item['subtitle']}. "
            else:
                outstr = outstr + ". "
        outstr = outstr + "\\\\\n"
        if 'role' in item.keys():
            outstr = (outstr + "\\tabboxmed{{\\bf Role: " +
                      f"{item['role']}." + "}}")
            if 'collaborators' in item.keys():
                for collab in item['collaborators']:
                    for key in collab.keys():
                        outstr = (outstr + "\\tabboxmed{" +
                                  f" {key}: {collab[key]}." + "}")
        outstr = outstr + "\\\\\n"
        if 'agency' in item.keys():
            outstr = outstr + f"{item['agency']}"
        if 'foa' in item.keys():
            if 'agency' in item.keys():
                outstr = outstr + ": "
            outstr = outstr + "{\\it " + f"{item['foa']}" + "}"
        if 'number' in item.keys():
            if 'foa' in item.keys():
                outstr = outstr + f" ({item['number']})"
            else:
                outstr = outstr + f" {item['number']}"
        outstr = outstr + ".\\\\\n"
        if 'type' in item.keys():
            outstr = (outstr + f"Type: {item['type']}")
        if 'numpages' in item.keys():
            outstr = (outstr + f" ({item['numpages']})")
        if 'budget' in item.keys():
            outstr = (outstr + f".\\hskip 2em Budget: {item['budget']}")
        if 'length' in item.keys():
            outstr = (outstr + f".\\hskip 2em Length: {item['length']}")
        outstr = outstr + "."
        if 'note' in item.keys():
            outstr = outstr + f"\\\\\n{item['note']}"
        if 'doi' in item.keys():
            outstr = (outstr + "\\\\\n{\\tt doi:} \\href{https://doi.org/" +
                      f"{item['doi']}" + "}{" + f"{item['doi']}" + "}")
        if 'git' in item.keys():
            outstr = (outstr + "\\\\\n{\\tt git:} \\url{" +
                      f"{item['git']}" + "}")
        if 'url' in item.keys():
            outstr = outstr + "\\\\\n{\\tt url: \\url{" + f"{item['url']}" + "}"
        outlist.append(outstr)
    return "\n\n\\bigskip\n\n".join(outlist)

def anypubTex(inlist):
    outlist = []
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'author' in item.keys():
            outstr = outstr + f"{item['author']}. "
        if 'journal' not in item.keys() and 'booktitle' not in item.keys():
            if 'title' in item.keys():
                outstr = outstr + "{\\sl " + f"{item['title']}" + "}. "
        else:
            if 'title' in item.keys():
                outstr = outstr + f"{item['title']}. "
        if 'journal' in item.keys():
            outstr = outstr + "{\\sl " + f"{item['journal']}" + "}"
            if 'volume' in item.keys():
                outstr = outstr + f" {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f"({item['number']})"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ". "
        elif 'booktitle' in item.keys():
            if 'chapter' in item.keys():
                outstr = outstr + f"Ch. {item['chapter']} "
            outstr = outstr + "{\\sl In " + f"{item['booktitle']}"
            if 'volume' in item.keys():
                outstr = outstr + f" Vol. {item['volume']}"
            if 'number' in item.keys():
                outstr = outstr + f", No. {item['number']}"
            outstr = outstr  + "}"
            if 'articleno' in item.keys():
                outstr = outstr + f", Article {item['articleno']}"
            if 'pages' in item.keys():
                outstr = outstr + f", {item['pages']}"
            outstr = outstr + ". "
        elif 'type' in item.keys():
            outstr = outstr + f"{item['type']}"
            if 'number' in item.keys():
                outstr = outstr + f" {item['number']}"
                outstr = outstr + ". "
            if 'organization' in item.keys():
                outstr = outstr + f"{item['organization']}"
                if 'location' in item.keys():
                    outstr = outstr + ", " + f"{item['location']}"
                outstr = outstr + ". "
        else:
            if 'number' in item.keys():
                outstr = outstr + f"{item['number']}. "
            if 'organization' in item.keys():
                outstr = outstr + f"{item['organization']}"
                if 'location' in item.keys():
                    outstr = outstr + ", " + f"{item['location']}"
            outstr = outstr + ". "
        if 'note' in item.keys():
            outstr = outstr + f"{item['note']}. "
        if 'doi' in item.keys():
            outstr = (outstr + "{\\tt doi:} \\href{https://doi.org/" +
                      f"{item['doi']}" + "}{" + f"{item['doi']}" + "}")
        elif 'url' in item.keys():
            outstr = outstr + "{\\tt url:} \\url{" + f"{item['url']}" + "}"
        elif 'isbn' in item.keys():
            outstr = outstr + "In {\\tt isbn:} " + f"{item['isbn']}"
        outlist.append(outstr)
    return "\n\n\\medskip\n\n".join(outlist)
