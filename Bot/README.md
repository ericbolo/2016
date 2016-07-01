# Hackatal Recast.ai bot

## Creating intents and expressions

For training, use developer token.

### Create an intent

#### curl

    curl -X POST -H "Content-Type: application/json" -H "Authorization: Token a717af48bbb2eeded81abdd61e482dd5" -H "Cache-Control: no-cache" -H "Postman-Token: 87f3d789-9905-5359-14ed-91421de9547d" -d '{"name":"Follow a game"
    }' "https://api.recast.ai/v1/users/ericbolo/bots/hackatal/intents"

#### nodeJS

    var http = require("https");
    
    var options = {
      "method": "POST",
      "hostname": "api.recast.ai",
      "port": null,
      "path": "/v1/users/ericbolo/bots/hackatal/intents",
      "headers": {
        "content-type": "application/json",
        "authorization": "Token a717af48bbb2eeded81abdd61e482dd5",
        "cache-control": "no-cache",
        "postman-token": "e2bab823-c3ea-fb37-1ac6-aceba287e8fa"
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
    
    req.write(JSON.stringify({ name: 'Follow a game' }));
    req.end();

### Create an expression for that intent

#### curl

    curl -X POST -H "Content-Type: application/json" -H "Authorization: Token a717af48bbb2eeded81abdd61e482dd5" -H "Cache-Control: no-cache" -H "Postman-Token: 13ba807b-0811-7082-ee03-1f83cee1ff99" -d '{"source": "I want to follow England's next game"
    }' "https://api.recast.ai/v1/users/ericbolo/bots/hackatal/intents/follow-a-game-1/expressions"

#### nodeJS

    var http = require("https");
    
    var options = {
      "method": "POST",
      "hostname": "api.recast.ai",
      "port": null,
      "path": "/v1/users/ericbolo/bots/hackatal/intents/follow-a-game-1/expressions",
      "headers": {
        "content-type": "application/json",
        "authorization": "Token a717af48bbb2eeded81abdd61e482dd5",
        "cache-control": "no-cache",
        "postman-token": "6fea5ffb-b5cf-a05b-3ea4-d72584f96ec5"
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
    
    req.write(JSON.stringify({ source: 'I want to follow England\'s next game' }));
    req.end();

### Bulk-create expressions for an intent

#### curl

    curl -X POST -H "Content-Type: application/json" -H "Authorization: Token a717af48bbb2eeded81abdd61e482dd5" -H "Cache-Control: no-cache" -H "Postman-Token: aa00191a-9a3c-b3fd-a2c4-52cd4b27fdae" -d '[{"source": "France vs. England"
    },
    {"source": "Ireland against Germany"}]' "https://api.recast.ai/v1/users/ericbolo/bots/hackatal/intents/follow-a-game-1/expressions/bulk_create"

#### nodeJS

    var http = require("https");
    
    var options = {
      "method": "POST",
      "hostname": "api.recast.ai",
      "port": null,
      "path": "/v1/users/ericbolo/bots/hackatal/intents/follow-a-game-1/expressions/bulk_create",
      "headers": {
        "content-type": "application/json",
        "authorization": "Token a717af48bbb2eeded81abdd61e482dd5",
        "cache-control": "no-cache",
        "postman-token": "6ec7fb40-f273-5b29-e8ee-490ec0bb84b5"
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
    
    req.write(JSON.stringify([ { source: 'France vs. England' },
      { source: 'Ireland against Germany' } ]));
    req.end();
    
## Making requests to the bot

For requesting to bot, use access token.

### curl

    curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -H "Authorization: Token 3d1dc97e4c05504e077542f82fd4f9fe" -H "Cache-Control: no-cache" -H "Postman-Token: 092a2496-0de0-046e-b2fd-78acffe65d02" -d 'text=I want to follow England's next game' "https://api.recast.ai/v1/request"
    
### nodeJS

    var qs = require("querystring");
    var http = require("https");
    
    var options = {
      "method": "POST",
      "hostname": "api.recast.ai",
      "port": null,
      "path": "/v1/request",
      "headers": {
        "content-type": "application/x-www-form-urlencoded",
        "authorization": "Token 3d1dc97e4c05504e077542f82fd4f9fe",
        "cache-control": "no-cache",
        "postman-token": "3c14cb97-6c71-ccca-7c72-4b21aaadd2da"
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