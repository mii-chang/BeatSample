var SERVER_URL = "http://192.168.0.20:8080/"

setInterval(getButton, 200)

function setLed(num, onoff) {
  callApi(
    SERVER_URL + "setLed", {
      "num": num,
      "onoff": onoff
    },
    function(o) {});
}

function callApi(url, jsonObj, callback) {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', url);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.setRequestHeader('Accept', 'application/json');
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.setRequestHeader('Accept', 'application/json');

  xhr.onreadystatechange = (function(myxhr) {
    return function() {
      if (xhr.readyState == 4 && xhr.status == 200) {
        callback(myxhr);
      }
    }
  })(xhr);

  xhr.send(JSON.stringify(jsonObj));
}
