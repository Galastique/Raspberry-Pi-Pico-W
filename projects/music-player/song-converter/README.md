# Music player converter

1. Copy the full song from the website as is (do not remove blank lines or else the program will not work)
2. Paste the song in a text file named "song.txt" within the same directory
3. Run the following powershell command: `node songConverter.js` (or simply double click the `.js` file if you have node.js installed)

DISPLAIMER: This will not work if multiple notes are played at once. My code for the music player only uses a single XHD buzzer, not multiple. At some point in the future it will support more, but for now you will have to deal with this.

An example text file is provided for reference (Megalovania)