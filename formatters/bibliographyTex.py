def articleTex(inlist):
    outlist = []
    outlist.append("\n\\begin{etaremune}")
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
    return "\n\\item ".join(outlist) + "\n\\end{etaremune}\n"

def proceedingsTex(inlist):
    outlist = []
    outlist.append("\n\\begin{etaremune}")
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
    return "\n\\item ".join(outlist) + "\n\\end{etaremune}\n"

def techreportTex(inlist):
    outlist = []
    outlist.append("\n\\begin{etaremune}")
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'author' in item.keys():
            outstr = outstr + f"{item['author']}. "
        if 'title' in item.keys():
            outstr = outstr + "{\\sl " + f"{item['title']}" + "}. "
        if 'booktitle' in item.keys():
            outstr = outstr + f"In {item['booktitle']}"
            if 'volume' in item.keys():
                outstr = outstr + f" vol.\\ {item['volume']}"
            if 'number' not in item.keys():
                outstr = outstr + ". "
            else:
                outstr = outstr + ", "
        elif 'type' in item.keys():
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
    return "\n\\item ".join(outlist) + "\n\\end{etaremune}\n"

def talkTex(inlist):
    outlist = []
    outlist.append("\n\\begin{etaremune}")
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
    return "\n\\item ".join(outlist) + "\n\\end{etaremune}\n"

def miscPubTex(inlist):
    outlist = []
    outlist.append("\n\\begin{etaremune}")
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
        if 'doi' in item.keys():
            outstr = (outstr + "{\\tt doi:} \\href{https://doi.org/" +
                      f"{item['doi']}" + "}{" + f"{item['doi']}" + "}")
        elif 'url' in item.keys():
            outstr = outstr + "{\\tt url:} \\url{" + f"{item['url']}" + "}"
        elif 'isbn' in item.keys():
            outstr = outstr + "In {\\tt isbn:} " + f"{item['isbn']}"
        outlist.append(outstr)
    return "\n\\item ".join(outlist) + "\n\\end{etaremune}\n"

def softwareTex(inlist):
    outlist = []
    outlist.append("\n\\begin{etaremune}")
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        if 'title' in item.keys():
            outstr = outstr + "{ " + f"{item['title']}" + "}"
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
    return "\n\\item ".join(outlist) + "\n\\end{etaremune}\n"

def proposalTex(inlist):
    outlist = []
    outlist.append("\n\\begin{etaremune}")
    for item in inlist:
        outstr = ""
        if 'year' in item.keys():
            outstr = outstr + f"{item['year']}. "
        elif 'start' in item.keys():
            outstr = outstr + f"{item['start']} - "
            if 'end' in item.keys():
                outstr = outstr + f"{item['end']}. "
            else:
                outstr = outstr + "Present. "
        if 'role' in item.keys():
            outstr = (outstr + "{\\bf " +
                      f"{item['role']}" + "}")
            if 'collaborators' in item.keys():
                outstr = outstr + " ("
                for ki, collab in enumerate(item['collaborators']):
                    for key in collab.keys():
                        if ki > 0:
                            outstr = (outstr + f", {key}: {collab[key]}")
                        else:
                            outstr = (outstr + f"{key}: {collab[key]}")
                outstr = outstr + "), "
            else:
                outstr = outstr + ", "
        if 'budget' in item.keys():
            outstr = (outstr + f"{item['budget']}")
            if 'share' in item.keys():
                outstr = outstr + f" (my share: {item['share']})"
        if 'length' in item.keys():
            if 'budget' in item.keys():
                outstr = outstr + " for "
            outstr = (outstr + f"{item['length']}")
        if 'role' in item.keys() or 'budget' in item.keys() or 'length' in item.keys():
            outstr = outstr + ". "
        if 'title' in item.keys():
            outstr = outstr + f"{{\\sl {item['title']}"
            if 'subtitle' in item.keys():
                outstr = outstr + f": {item['subtitle']}}}, "
            else:
                outstr = outstr + "}, "
        if 'type' in item.keys():
            outstr = (outstr + f"{item['type']}")
        if 'numpages' in item.keys():
            outstr = (outstr + f" ({item['numpages']})")
        if 'type' in item.keys() or 'numpages' in item.keys():
            outstr = outstr + ". "
        if 'agency' in item.keys():
            outstr = outstr + f"{item['agency']}"
        if 'foa' in item.keys():
            if 'agency' in item.keys():
                outstr = outstr + ": "
            outstr = outstr + f"{item['foa']}"
        if 'number' in item.keys():
            if 'foa' in item.keys():
                outstr = outstr + f" ({item['number']})"
            else:
                outstr = outstr + f" {item['number']}"
        if 'agency' in item.keys() or 'foa' in item.keys() or 'number' in item.keys():
            outstr = outstr + ". "
        if 'note' in item.keys():
            outstr = outstr + f"{item['note']} "
        if 'doi' in item.keys():
            outstr = (outstr + "{\\tt doi:} " +
                      "\\href{https://doi.org/" +
                      f"{item['doi']}" + "}{" + f"{item['doi']}" + "}")
        if 'git' in item.keys():
            outstr = (outstr + "{\\tt git:} "+
                      "\\url{" +
                      f"{item['git']}" + "}")
        if 'url' in item.keys():
            outstr = (outstr + "{\\tt url}: " +
                      "\\url{" + f"{item['url']}" + "}")
        outlist.append(outstr)
    return "\n\\item ".join(outlist) + "\n\\end{etaremune}\n"

def anypubTex(inlist):
    outlist = []
    outlist.append("\n\\begin{etaremune}")
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
    return "\n\\item ".join(outlist) + "\n\\end{etaremune}\n"
