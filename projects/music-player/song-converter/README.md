# Music player converter

1. Copy the full song from the website as is (do not remove blank lines or else the program will not work)
2. Paste the song in a text file named "song.txt" within the same directory
3. Run the following powershell command: `node songConverter.js` (or simply double click the `.js` file if you have node.js installed)

If you have connected more than 1 buzzer to your Raspberry Pi Pico, you're in luck! My code supports up to 3 buzzers at once to allow multiple different notes being played at once. This allows to play more complex sounds. It also prevents the program from crashing if the converted song contains 2 or more notes at once.

An example text file is provided for reference (Megalovania)