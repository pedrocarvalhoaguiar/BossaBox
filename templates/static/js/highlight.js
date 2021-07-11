var se = document.getElementById('search')
doSearch(se.value, 'yellow')

function doSearch(text, backgroundColor) {

    console.log('1')
    if (window.find && window.getSelection) {
        document.designMode = "on";
        var sel = window.getSelection();
        sel.collapse(document.body, 0);

        while (window.find(text)) {
            document.execCommand("HiliteColor", false, backgroundColor);
            sel.collapseToEnd();
        }
        document.designMode = "off";
    }
}

