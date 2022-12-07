def parseAuthors(authorstr):
    """ Parse the given bibtex-style author string and format the author list.

    Args:
        authorstr (str): Author list in the style:
            Last, First MI and Last, First MI and Last, First MI

    Returns:
        str: Author list in the style:
        FI. MI. Last, FI. MI. Last, and FI. MI. Last

    """

    # Split author list on " and "
    authorlist = authorstr.split(" and ")
    nameout = []
    # Reformat each individual author
    for author in authorlist:
        namelist = author.strip().split(",")
        lastname = namelist[0].strip()
        firstname = namelist[1]
        nameout.append(". ".join([f.strip()[0] for f in firstname.split()])
                       + ". " + lastname)
    # Join output string using special rule for lists less than 3 in length
    if len(nameout) < 3:
        nameoutstr = " and ".join(nameout)
    else:
        nameoutstr = " and ".join([", ".join(nameout[:-1]), nameout[-1]])
    return nameoutstr

def parseTitle(titlestr):
    """ Parse the given bibtex-style title and reformat.

    Args:
        titlestr (str): Title string in the style:
            Title WiTh WeIrd Capitalization {BRACKETS} UsEd to KEEP pArts

    Returns:
        titlestr (str): Title string lower-cased, except between brackets and
        first letter:
        Title with weird capitalization BRACKETS used to keep parts

    """

    # Split on brackets
    titlelist = titlestr.replace("{", "|SPLIT|").replace("}", "|SPLIT|").split("|SPLIT|")
    titleout = []
    # Reformat first and other even entries
    for i, tpart in enumerate(titlelist):
        if i == 0 and len(tpart) >= 1:
            titleout.append(tpart[0] + tpart[1:].lower())
        elif i % 2 == 1:
            titleout.append(tpart)
        else:
            titleout.append(tpart.lower())
    # Rejoin to form output
    return "".join(titleout)


if __name__ == "__main__":
    " Some unit tests "

    import sys

    namestr = "Chang, Tyler H. and Watson, Layne T. and Lux, Thomas C. H. and Larson, Jeffrey"
    titlestr = "Algorithm 1028: {VTMOP}: {S}olver for Blackbox Optimization Problems"

    print(parseAuthors(namestr))
    print(parseTitle(titlestr))
