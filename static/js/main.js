

function toggle(id) {
    var state = document.getElementById(id).style.display;
        if (state == 'block') {
            document.getElementById(id).style.display = 'none';
        } else {
            document.getElementById(id).style.display = 'block';
        }
    }

var timeOutId;

function stopSpinner() {
        document.getElementById('spinner').style.display = 'none';
        clearTimeout(timeOutId);
    }

function startSpinner(tt) {
        document.getElementById('spinner').style.display = 'block';
        timeOutId = setTimeout(stopSpinner, tt);
    }

function dosyaOku() {
    const fs = require('fs');
    // First I want to read the file
    fs.readFile('./temp/sevkiyat_excel_kontrol.cssx', function read(err, data) {
        if (err) {
            throw err;
        }
        const content = data;

        // Invoke the next step here however you like
        console.log(content);   // Put all of the code here (not the best solution)
        processFile(content);   // Or put the next step in a function and invoke it
    });

    function processFile(content) {
        console.log(content);
    }
}

function dosyaOku2() {
        var httpRequest = null;

        function SendRequest () {
            if (!httpRequest) {
                httpRequest = CreateHTTPRequestObject ();   // defined in ajax.js
            }
            if (httpRequest) {
                    // The requested file must be in the same domain that the page is served from.
                var url = "./temp/sevkiyat_excel_kontrol.cssx";
                httpRequest.open ("GET", url, true);    // async
                httpRequest.onreadystatechange = OnStateChange;
                httpRequest.send (null);
            }
        }
}