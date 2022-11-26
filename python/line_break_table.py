import pandas as pd

def parse_line_breaks_line(line):
    '''
    parse the "line breaks" line
    '''
    elems = line.split(' ')
    num = elems[0]
    name = ' '.join(elems[1: -18])
    stats = elems[-18:]
    return [num, name, *stats]

def get_line_breaks_columns():
    return [
        "#",
        "Player",
        "Line Breaks Attempted",
        "Line Breaks Completed",
        "Line Break Completion %",
        "Attacking Line/4",
        "Attacking Midﬁeld Line/4",
        "Midﬁeld Line/4",
        "Defensive Line/4",
        "Attacking Line/3",
        "Midﬁeld Line/3",
        "Defensive Line/3",
        "Midﬁeld Line/2",
        "Defensive Line/2",
        "Through/Direction",
        "Around/Direction",
        "Over/Direction",
        "Pass/Distribution",
        "Cross/Distribution",
        "Ball Progression/Distribution"
    ]
def parse_line_breaks_table(text):
    lines = text.split('\n')
    team = ' '.join(lines[0].split(' ')[2:])
    data = list(map(parse_line_breaks_line, lines[20:-1]))
    df = pd.DataFrame(data, columns=get_line_breaks_columns())
    return df