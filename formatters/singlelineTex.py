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
