const fs = require("fs");
const { format } = require("path");

//Gets song and splits it by lines
let song = fs.readFileSync("./song.txt").toString('utf-8'); //the whole song
let lines = song.split("\r\n") //the song separated by lines (which sometimes includes multiples lines of different octaves)
let finalNotesArray = []; //final output array

//Combines "groups" of "sentences" into a single line (extremely messy code but stfu, no one cares)
function combineGroup(i){
    if(lines[i].length == 0){
        newGroup = [];
        if(group.length == 52){
            for(let j = 0; j < 26; j++){
                newGroup.push((group[j] + group[j + 26]).trim());
            }
        }else if(group.length == 78){
            for(let j = 0; j < 26; j++){
                newGroup.push((group[j] + group[j + 26] + group[j + 52]).trim());
            }
        }
        
        for(let j = 0; j < 26; j++){
            if(newGroup[j] == ""){
                newGroup[j] = " ";
            }
        }
        finalNotesArray = finalNotesArray.concat(newGroup);
        group = [];
    }
}

//Formats notes into an array
function formatNote(octave, character){
    if(character == "-"){
        group.push(" ");
    }else if(character == character.toUpperCase()){
        group.push(`${character}S${octave}`);
    }else if(character == character.toLowerCase()){
        group.push(`${character.toUpperCase()}${octave}`);
    }
}

//Transforms song into array
//For every line of music
let group = [];
for(let i = 0; i < lines.length; i++){
    combineGroup(i);

    //For every note/silence
    for(let j = 2; j < lines[i].length - 1; j++){
        let octave = lines[i][0];
        let character = lines[i][j];
        formatNote(octave, character);
    }
}

//Outputs song into file
require('fs').writeFile('./output_song.txt', JSON.stringify(finalNotesArray),
    function(err){
        if(err){
            console.error('Crap happens');
        }
    }
);
