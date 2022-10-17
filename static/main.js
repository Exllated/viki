richText = document.getElementById('richText')
primaryCaret = document.getElementById('primaryCaret')

document.addEventListener("keydown", dockeydown);

async function dockeydown(e) {
    e.preventDefault();
    jsonResp = JSON.parse(await fetchAsync('/viki/api/on_key_pressed?k=' + e.key + '&alt=' + (e.altKey ? '1' : '0') + '&ctrl=' + (e.ctrlKey ? '1' : '0')));
    richText.innerHTML = jsonResp.html;
    primaryCaret.style = 'top: ' + letter_height * jsonResp.caret_position[0] + 'px; left: ' + letter_width * jsonResp.caret_position[1] + 'px;';

    primaryCaret.style.animation = 'none';
    primaryCaret.offsetHeight; /* trigger reflow */
    primaryCaret.style.animation = null;
}

async function fetchAsync(url) {
    let response = await fetch(url);
    let data = await response.text();
    return data;
}

richText.innerHTML = 'Some Really Long Text CAPS TEXT non-caps text 1234567890'
richText.style = 'position: absolute; height: auto; width: auto; white-space: nowrap;'

letter_width = richText.clientWidth/56;
letter_height = richText.clientHeight;

richText.innerHTML = ''
richText.style = ''
