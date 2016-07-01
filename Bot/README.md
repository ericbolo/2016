# Hackatal Recast.ai bot

## Creating intents and expressions

### Create an intent

curl -X POST -H "Content-Type: application/json" -H "Authorization: Token a717af48bbb2eeded81abdd61e482dd5" -H "Cache-Control: no-cache" -H "Postman-Token: 87f3d789-9905-5359-14ed-91421de9547d" -d '{"name":"Follow a game"
}' "https://api.recast.ai/v1/users/ericbolo/bots/hackatal/intents"

### Create an expression for that intent

curl -X POST -H "Content-Type: application/json" -H "Authorization: Token a717af48bbb2eeded81abdd61e482dd5" -H "Cache-Control: no-cache" -H "Postman-Token: 13ba807b-0811-7082-ee03-1f83cee1ff99" -d '{"source": "I want to follow England's next game"
}' "https://api.recast.ai/v1/users/ericbolo/bots/hackatal/intents/follow-a-game-1/expressions"

### Bulk create expressions for an intent

curl -X POST -H "Content-Type: application/json" -H "Authorization: Token a717af48bbb2eeded81abdd61e482dd5" -H "Cache-Control: no-cache" -H "Postman-Token: aa00191a-9a3c-b3fd-a2c4-52cd4b27fdae" -d '[{"source": "France vs. England"
},
{"source": "Ireland against Germany"}]' "https://api.recast.ai/v1/users/ericbolo/bots/hackatal/intents/follow-a-game-1/expressions/bulk_create"

