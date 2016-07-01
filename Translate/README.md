# Translating with Google Translate

You can obtain your own Google Translate credentials at: https://console.cloud.google.com

Depending on the context, use a browser key or a server key.

## curl

    curl -X GET -H "Cache-Control: no-cache" -H "Postman-Token: 4379fd24-ab5c-968f-a8af-0199b0bafb08" "https://www.googleapis.com/language/translate/v2?key=AIzaSyC-tAIXhMDaip4B29Q8WxSDk34vVkHJ_1c&q=hello%20world&source=en&target=de"

## nodeJS

    var qs = require("querystring");
    var http = require("https");
    
    var options = {
      "method": "GET",
      "hostname": "www.googleapis.com",
      "port": null,
      "path": "/language/translate/v2?key=AIzaSyC-tAIXhMDaip4B29Q8WxSDk34vVkHJ_1c&q=hello%2520world&source=en&target=de",
      "headers": {
        "cache-control": "no-cache",
        "postman-token": "3e8fa0dd-7a59-efa8-a073-111d44e69386"
      }
    };
    
    var req = http.request(options, function (res) {
      var chunks = [];
    
      res.on("data", function (chunk) {
        chunks.push(chunk);
      });
    
      res.on("end", function () {
        var body = Buffer.concat(chunks);
        console.log(body.toString());
      });
    });
    
    req.write(qs.stringify({ text: 'I want to follow England\'s next game' }));
    req.end();