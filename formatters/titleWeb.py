TITLETEMPLATE = """
<!-- Title row -->
<div class"row">
  <div class="col-xs-12 col-md-10 col-md-offset-1 
    col-lg-8 col-lg-offset-2 panel panel-default">
  <div class="col-xs-12 col-md-10 col-md-offset-1 
    col-lg-8 col-lg-offset-2 panel-top panel-default">

    <!-- Profile image, name, dept, etc. -->
    <div class="row">

    <!-- Profile image -->
    $PROFILEIMAGE

    <!-- General info -->
    <h1 class="margin-base-vertical">
    <b> $NAME </b>
    <font size="-5">
    <br><br>
    </font>
    <font size="+1">
    $INSTITUTION
    </font>
    </h1>
    </div>

    <!-- Navigation pill menu -->
    <div class = "row">
    <ul class="nav nav-pills">
    $SECTIONS
    </ul>
    </div>
  </div>
  </div>
</div>
"""

def titleWeb(inlist):
    outstr = []
    for item in inlist:
        if 'name' not in item.keys():
            raise ValueError(f"title data does not contain a name field")
        if 'institution' not in item.keys():
            raise ValueError(f"title data does not contain an institution field")
        NAME = item['name']
        INSTITUTION = item['institution']
        if 'department' in item.keys():
            INSTITUTION = INSTITUTION + f",\n<br>{item['department']}\n"
        if 'image' in item.keys():
            PROFILEIMAGE = '<img src="' + f'{item["image"]}' + '" class="img-responsive" align="left" width="20%" hspace="15em" vspace="30em">'
        try:
            with open("targets.temp", "r") as fp:
                targets = fp.readlines()
        except BaseException:
            targets = []
    if len(targets) > 0:
        SECTIONS = '<ul class="nav nav-pills">\n'
        for ti in targets:
            SECTIONS = SECTIONS + f'<li><a href="#{ti}">{ti}</a></li>'
        SECTIONS = SECTIONS + '</ul>'
    else:
        SECTIONS = ""
    return TITLETEMPLATE.replace("$NAME", NAME).replace("$INSTITUTION", INSTITUTION).replace("$PROFILEIMAGE", PROFILEIMAGE).replace("$SECTIONS", SECTIONS)
