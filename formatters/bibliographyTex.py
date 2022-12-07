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
            outstr = (outstr + "{\\tt doi:~\\href{https://doi.org/" +
                      f"{item['doi']}" + "}{" + f"{item['doi']}" + "}}")
        elif 'url' in item.keys():
            outstr = outstr + "{\\tt url:~\\url{" + f"{item['url']}" + "}}"
        elif 'isbn' in item.keys():
            outstr = outstr + "In ISBN:~{\\tt " + f"{item['isbn']}" + "}"
        outlist.append(outstr)
    return "\n\n\\bigskip\n\n".join(outlist)

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
            outstr = (outstr + "{\\tt doi:~\\href{https://doi.org/" +
                      f"{item['doi']}" + "}{" + f"{item['doi']}" + "}}")
        elif 'url' in item.keys():
            outstr = outstr + "{\\tt url:~\\url{" + f"{item['url']}" + "}}"
        elif 'isbn' in item.keys():
            outstr = outstr + "In ISBN:~{\\tt " + f"{item['isbn']}" + "}"
        outlist.append(outstr)
    return "\n\n\\bigskip\n\n".join(outlist)

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
            outstr = (outstr + "{\\tt doi:~\\href{https://doi.org/" +
                      f"{item['doi']}" + "}{" + f"{item['doi']}" + "}}")
        elif 'url' in item.keys():
            outstr = outstr + "{\\tt url:~\\url{" + f"{item['url']}" + "}}"
        elif 'isbn' in item.keys():
            outstr = outstr + "In ISBN:~{\\tt " + f"{item['isbn']}" + "}"
        outlist.append(outstr)
    return "\n\n\\bigskip\n\n".join(outlist)

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
    return "\n\n\\bigskip\n\n".join(outlist)

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
    return "\n\n\\bigskip\n\n".join(outlist)

