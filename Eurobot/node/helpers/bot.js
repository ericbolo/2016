module.exports = {
    answer: function(text, access_token){

        console.log("sending request to bot")

        var Q = require('q');
        var qs = require("querystring");
        var http = require("https");

        var deferred = Q.defer();

        var options = {
            "method": "POST",
            "hostname": "api.recast.ai",
            "port": null,
            "path": "/v1/request",
            "headers": {
                "content-type": "application/x-www-form-urlencoded",
                "authorization": "Token "+access_token,
                "cache-control": "no-cache"
            }
        };

        var req = http.request(options, function (res) {
            var chunks = [];

            res.on("data", function (chunk) {
                chunks.push(chunk);
            });

            res.on("end", function () {
                var body = Buffer.concat(chunks);

                body = JSON.parse(body.toString());

                if(body.results.intents.length > 0){
                    var intent = body.results.intents[0];
                    if(intent == 'follow-a-game-1'){
                        var country = body.results.sentences[0].entities.location[0].raw;
                        deferred.resolve({
                            text: "Ok, I'll look for "+country+"'s next game"
                        })
                    }
                }else{
                    deferred.resolve(); //Resolve with empty
                }
            });
        });

        req.write(qs.stringify({ text: text }));
        req.end();

        return deferred.promise;

    }
}