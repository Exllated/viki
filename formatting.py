
def ide_text_list_to_html(text_list):
    html = ''
    for i, line in enumerate(text_list):
        if line == '':
            html += '<br>'
        else:
            html += f'<p>{line}</p>'
    return html
