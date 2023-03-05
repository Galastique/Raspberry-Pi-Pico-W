const fs = require("fs");
const { format } = require("path");

//Gets song and splits it by lines
let song = fs.readFileSync("./song.txt").toString("utf-8"); //the whole song
let lines = song.split("\r\n") //the song separated by lines (which sometimes includes multiples lines of different octaves)
let finalNotesArray = []; //final output array

//Combines "groups" of "sentences" into a single line (extremely messy code but stfu, no one cares)
function combineGroup(group){
    newGroup = [];

    for(let i = 0; i < group.length; i++){
        for (let j = 0; j < group[i].length; j++) {
            if (i == 0) {
                newGroup.push(group[i][j])
            }else{
                newGroup[j] = (newGroup[j] + group[i][j]).trim();
            }
        }
    }

    for(let i = 0; i < newGroup.length; i++){
        if(newGroup[i] == ""){
            newGroup[i] = " ";
        }
    }
    finalNotesArray = finalNotesArray.concat(newGroup);
    group = [];
}

//Formats notes into an array
function formatNote(octave, character){
    note = "";
    if(character == "-"){
        note = " ";
    }else if(character == character.toUpperCase()){
        note = `${character}S${octave}`;
    }else if(character == character.toLowerCase()){
        note = `${character.toUpperCase()}${octave}`;
    }
    return note;
}

//Transforms song into array
//For every line of music
let group = [];
for(let i = 0; i < lines.length; i++){
    let line = []

    if(lines[i].length != 0){
        //For every note/silence
        for(let j = 2; j < lines[i].length - 1; j++){
            let octave = lines[i][0];
            let character = lines[i][j];
            line.push(formatNote(octave, character));
        }
        group.push(line);
    }else{
        combineGroup(group);
        group = [];
    }
}

//Outputs song into file
require("fs").writeFile("./output_song.txt", JSON.stringify(finalNotesArray),
    function(err){
        if(err){
            console.error("Crap happens");
        }
    }
);
