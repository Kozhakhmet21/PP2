import json
game_state={
    "position":{
        "x":100,
        "y":150
    }
}
game_state["name"]="Kozhakhmet"
game_state["enemy"]={
    "x":200,
    "y":300
}
f=open("file1.json","w")
f.write(json.dumps(game_state))
f.close()