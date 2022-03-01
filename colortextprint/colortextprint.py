import sys

def cprint(*values: object, sep: str = ' ', end: str | None = '\n',fg: str = '',bg: str = '',style: str = '',file=sys.stdout,flush: bool=False):
    values = [str(val) for val in values]
    fg_colors = {'black':30,'red':31, 'green':32, 'yellow':33, 'blue':34, 'purple':35,'cyan':36, 'gray':39,  'white':37}
    bg_colors = {'black':40,'red':41, 'green':42, 'yellow':43, 'blue':44, 'purple':45,'cyan':46, 'gray':49,  'white':47}
    styles = {'bold':1,'faint':2,'italic':3,'underline':4,'slow_blink':5,'fast_blink':6,'negative':7,'conceal':8,'strike':9}
    # fsb
    codelist = []
    if fg.lower() in fg_colors:
        f_color = str(fg_colors[fg.lower()])
        codelist.append(f_color)
    else:
        f_color =''
    if bg.lower() in bg_colors:
        b_color = str(bg_colors[bg.lower()])
        codelist.append(b_color)
    else:
        b_color =''
    if style.lower() in styles:
        s_color = str(styles[style.lower()])
        codelist.append(s_color)
    else:
        s_color =''
        
    data = str(f'\033[{";".join(codelist)}m') + sep.join((values)) + "\033[0m" + end
    file.write(data)
    if flush:
        file.flush()
    return None

if __name__=='__main__':
    cprint("my ", 'name', 'is rohit', fg='red')
    # cprint("sample text",fg='reD',bg='CYan',style='bold')
