def experienceShortWeb(inlist):
    outlist = []
    for item in inlist:
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
        outstr = "<li>"
        if isinstance(years, list):
            for i, year in enumerate(years):
                if i > 0:
                    outstr = outstr + f"\n<br>{year}"
                else:
                    outstr = outstr + f"{year}"
                outstr = outstr + ". <b>"
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
            outstr = outstr + f"{years}"
            outstr = outstr + ". <b>"
            if 'title' in item.keys():
                outstr = outstr + f"{item['title']}"
            if 'subtitle' in item.keys():
                outstr = outstr + f", {item['subtitle']}"
            if 'institution' in item.keys():
                outstr = outstr + f": {item['institution']}"
            outstr = outstr + "</b>"
            if 'department' in item.keys():
                outstr = outstr + f", {item['department']}"
        outstr = outstr + "</li>\n"
        outlist.append(outstr)
    return "<ul>\n" + "".join(outlist) + "</ul>\n"

def experienceLongWeb(inlist):
    outlist = []
    for item in inlist:
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
        outstr = "<li>"
        if isinstance(years, list):
            for i, year in enumerate(years):
                if i > 0:
                    outstr = outstr + f"\n<br>{year}"
                else:
                    outstr = outstr + f"{year}"
                outstr = outstr + ". <b>"
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
            outstr = outstr + f"{years}"
            outstr = outstr + ". <b>"
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
            outstr = outstr + "    <ul>"
            if isinstance(item['description'], str):
                outstr = outstr + "\n    <li>"
                outstr = outstr + f"{item['description']}"
                outstr = outstr + "</li>"
            elif isinstance(item['description'], list):
                for i2 in item['description']:
                    outstr = outstr + "\n    <li>"
                    outstr = outstr + f"{i2}"
                    outstr = outstr + "</li>"
            outstr = outstr + "\n    </ul>\n"
        outstr = outstr + "</li>\n"
        outlist.append(outstr)
    return "<ul>\n" + "".join(outlist) + "</ul>\n"

def degreeLongWeb(inlist):
    outlist = []
    for item in inlist:
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
        outstr = "<li>"
        outstr = outstr + (f"{item['title']}, {years}, " +
                           f"{item['subtitle']}, {item['institution']}")
        if 'description' in item.keys():
            if isinstance(item['description'], str):
                outstr = outstr + "\n    <ul>\n    <li><i>"
                outstr = outstr + f"{item['description']}</i></li>"
                outstr = outstr + "\n    </ul>\n"
            elif isinstance(item['description'], list):
                for i2 in item['description']:
                    outstr = outstr + "\n    <ul>\n    <li><i>"
                    outstr = outstr + f"{i2}</i></li>"
                    outstr = outstr + "\n    </ul>\n"
        outstr = outstr + "</li>\n"
        outlist.append(outstr)
    return "<ul>\n" + "".join(outlist) + "</ul>"

def degreeShortWeb(inlist):
    outlist = []
    for item in inlist:
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
        outstr = "<li>"
        outstr = outstr + (f"{item['title']}, {years}, " +
                           f"{item['subtitle']}, {item['institution']}</li>\n")
        outlist.append(outstr)
    return "<ul>\n" + "".join(outlist) + "</ul>"

def timelineWeb(inlist):
    from matplotlib import pyplot as plt
    import datetime
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
              'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    yearlist = []
    titlelist = []
    for item in inlist:
        if 'title' not in item.keys():
            raise ValueError("'title' is required by timeline formatter")
        if 'year' not in item.keys() and 'start' not in item.keys():
            raise ValueError("'year' or 'start' key is required for degree formatter")
        if 'start' in item.keys():
            if isinstance(item['start'], list):
                starts = item['start']
                if 'end' in item.keys():
                    ends = item['end']
                else:
                    ends = f"Dec {datetime.date.today().year}"
            else:
                starts = [item['start']]
                if 'end' in item.keys():
                    ends = [item['end']]
                else:
                    ends = [f"Dec {datetime.date.today().year}"]
            for start, end in zip(starts, ends):
                thisdate = []
                if len(str(start).strip().split()) > 1:
                    year = float(str(start).strip().split()[1])
                    try:
                        month = months.index(str(start).strip().split()[0].lower()[:3])
                        assert(month in range(12))
                    except BaseException:
                        raise ValueError("Could not parse start month")
                    year = year + (month / 12)
                else:
                    year = float(str(start).strip()) + 0.5
                thisdate.append(year)
                if len(str(end).strip().split()) > 1:
                    year = float(str(end).strip().split()[1])
                    try:
                        month = months.index(str(end).strip().split()[0].lower()[:3])
                        assert(month in range(12))
                    except BaseException:
                        raise ValueError("Could not parse end month")
                    year = year + (month / 12)
                else:
                    year = float(str(end).strip()) + 0.5
                thisdate.append(year)
                yearlist.append(thisdate)
        else:
            if isinstance(item['year'], list):
                years = item['year']
            else:
                years = [item['year']]
            for year in years:
                if len(str(year).strip().split()) > 1:
                    year_exact = float(str(year).strip().split()[1])
                    try:
                        month = months.index(str(year).strip().split()[0].lower()[:3])
                        assert(month in range(12))
                    except BaseException:
                        raise ValueError("Could not parse year's month")
                    year_exact = year_exact + (month / 12)
                else:
                    year_exact = float(str(year).strip()) + 0.5
            yearlist.append(year_exact)
        if isinstance(item['title'], list):
            for i in range(len(item['title'])):
                titlestr = f"{item['title'][i]}"
                if 'subtitle' in item.keys():
                    titlestr = titlestr + f", {item['subtitle'][i]}"
                if 'institution' in item.keys():
                    titlestr = titlestr + f": {item['institution'][i]}"
                titlelist.append(titlestr)
        else:
            titlestr = f"{item['title']}"
            if 'subtitle' in item.keys():
                titlestr = titlestr + f", {item['subtitle']}"
            if 'institution' in item.keys():
                titlestr = titlestr + f": {item['institution']}"
            titlelist.append(titlestr)
    # build timeline plot
    pallet = [['b', 'r', 'g'], ['b', 'r', 'g']]
    lines = []
    x_ticks = []
    y_ticks = []
    y_ticks_adjusted = []
    x_labels = []
    y_labels = []
    max_level = 1.0
    ytop = 0
    ybot = 0
    y_dots = []
    order = []
    for title, year in zip(titlelist, yearlist):
        if isinstance(year, list):
            level = 1.0
            index = 0
            for li in lines:
                if year[1] > li[0] + 1.0e-2:
                    index = 0
                    level = max(level, li[2] + 1.0)
                    max_level = max(level, max_level)
                elif abs(li[2] - level) < 0.5:
                    index = index + 1
            color = pallet[round(level) % 2][(round(level + index) % 3 + index) % 3]
            lines.append([year[0], year[1], level, index, title, color])
            order.append('l')
            if all([abs(yi - year[0]) > 0.01 for yi in y_ticks]):
                y_ticks.append(year[0])
                y_labels.append(f"{months[round(12 * (year[0] % 1.0))]} {int(year[0])}")
                tick_spot = 0
                for i in range(len(y_ticks_adjusted)):
                    if y_ticks[i] > year[0]:
                        tick_spot -= 0.3
                    else:
                        y_ticks_adjusted[i] -= 0.3
                y_ticks_adjusted.append(tick_spot)
            if all([abs(yi - year[1]) > 0.01 for yi in y_ticks]):
                y_ticks.append(year[1])
                y_labels.append(f"{months[round(12 * (year[1] % 1.0))]} {int(year[1])}")
                tick_spot = 0
                for i in range(len(y_ticks_adjusted)):
                    if y_ticks[i] > year[1]:
                        tick_spot -= 0.3
                    else:
                        y_ticks_adjusted[i] -= 0.3
                y_ticks_adjusted.append(tick_spot)
        elif isinstance(year, float):
            y_dots.append([year, 1.0, title, 'k'])
            order.append('d')
            if all([abs(yi - year) > 0.01 for yi in y_ticks]):
                y_ticks.append(year)
                y_labels.append(f"{months[round(12 * (year % 1.0))]} {int(year)}")
                tick_spot = 0
                for i in range(len(y_ticks_adjusted)):
                    if y_ticks[i] > year:
                        tick_spot -= 0.3
                    else:
                        y_ticks_adjusted[i] -= 0.3
                y_ticks_adjusted.append(tick_spot)
    ybot = min(y_ticks_adjusted)
    plt.figure(figsize = (max_level+5, (ytop - ybot + 0.1)))
    ax = plt.axes()
    last = ytop + 0.3
    linecount = 0
    dotcount = 0
    for oi in order:
        if oi == 'l':
            line = lines[linecount]
            i1 = y_ticks.index(line[0])
            i2 = y_ticks.index(line[1])
            plt.vlines(ymin=y_ticks_adjusted[i1], ymax=y_ticks_adjusted[i2],
                       x=line[2], color=line[5], linewidth=5)
            ycoord = min(last - 0.3, y_ticks_adjusted[i2])
            plt.text(max_level + 0.5, ycoord - 0.1, line[4],
                     fontsize="12", color=line[5])
            plt.plot([line[2], max_level + 0.25],
                     [y_ticks_adjusted[i2], ycoord],
                     color=line[5], linestyle='dashed')
            last = ycoord
            linecount = linecount + 1
        elif oi == 'd':
            dot = y_dots[dotcount]
            i1 = y_ticks.index(dot[0])
            ycoord = min(last - 0.3, y_ticks_adjusted[i1])
            plt.text(max_level + 0.5, ycoord - 0.1, dot[2],
                     fontsize="12", color=dot[3])
            plt.plot([dot[1], max_level + 0.25], [y_ticks_adjusted[i1], ycoord],
                     color=dot[3], linestyle='dashed')
            last = ycoord
            dotcount = dotcount + 1
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks_adjusted)
    for i in range(len(y_labels)):
        thisyear = datetime.date.today().year
        if y_labels[i].split()[0] == "dec" and y_labels[i].split()[1] == f"{thisyear}":
            y_labels[i] = "present"
    ax.set_xticklabels(x_labels)
    ax.set_yticklabels(y_labels)
    plt.xlim([0.9, max_level+10])
    plt.ylim([ybot, ytop + 0.1])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.savefig("timeline.svg", format='svg', bbox_inches='tight')
    return '<br><img src="timeline.svg" alt="timeline" width="100%">'

scroller = """<br>\n<div style="height: 20em;
              padding-top: 0em;
              padding-bottom: 0em;
              text-align: justify;
              text-justify: inter-word;
              border: 0px solid black;
              overflow:scroll;">\n<img src="timeline.svg" alt="timeline" width="100%">\n</div>"""
