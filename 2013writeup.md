# Cicada 2013 puzzle

Date: 8-10-2021 | Author: @SH4D0WS99

## 1. 2013.jpg
1. Ran outguess revealed ```2013.out```.
2. Message revealed a book cipher.
3. Researching riddle revealed Liber AL vel Legis (The Book of the Law).

## 2. Liber AL vel Legis book cipher
1. Book cipher revealed: ```https:--www.dropbox.com-s-r7sgeb5dtmzj14s-3301```.
2. In hyperlink replace ```-``` with ```/```.
3. Complete hyperlink: ```https://www.dropbox.com/s/r7sgeb5dtmzj14s/3301```.
4. Downloading file revealed an .ISO file.

## 3. 3301.iso file
1. Downloaded ```3301.iso``` file.
2. Used 7zip to extract files from the ```3301.iso``` file.
3. Made a virtual machine using VirtualBox to boot up ```3301.iso``` file.
4. User tc is active and needs no password to interact with the OS.
5. Inside the folder ```/usr/local/bin``` there is a file called ```message.txt```.
6. The message contains the twitter username for the account ```@1231507051321```.
7. The twitter account contains a large amount of tweets resulting in a hexdump of a file.
8. Making a binary file using the command: ```xxd -c 65 -r twitter > twitter.bin```.
9. XORing the files ```560.13``` & ```761.mp3``` from the 3301.iso file and outputting this in a binary file called ```560761.bin```.
10. XORing the binary files ```twitter.bin``` & ```560761.bin``` revealed a PNG file.
11. XORing the binary file ```twitter.bin``` & the audio file ```761.mp3``` revealed the Gematria Primus rune translation JPG.

## 4. gematria-primus.jpg
1. Ran outguess revealed ```gematria-primus.out```.
2. The file ```gematria-primus.out``` has lines with spaces and tabs.
3. Replace the tabs with a 1 and the spaces with a 0.
4. Convert the binary to readable ASCII text.
5. Output of the conversion revealed the text: ```Come to emiwp4muu2ktwknf.onion We shall await you there. Good luck. 3301```

## 5. Onion deep web link
1. Website revealed that web browsers are useless.
2. Telnet into the website gives an interactive shell.
3. Typing ```hello``` into the shell outputs a hexdump.
4. Translating the hexdump to readable ASCII text revealed a second onion URL: ```xsxnaksict6egxkq.onion```.

## 6. 2nd Onion deep web link
1. Website revealed that patience is a virtue.
2. HTML comment revealed that we have to come back later.
3. Website revealed that we had to knock on the sky and listen to the sound.
4. Pinging the website and capturing the ping reply revealed a message.
5. Reading the message revealed a third onion URL: ```pklmx2eeh6fjt7zf.onion```.

## 7. 3rd Onion deep web link
1. Website revealed GPS coordinates.
2. GPS coordinates revealed cell phone numbers and access codes.
3. Calling the cell phone number prompted for a access code.
4. Convert the access code runes to a number with the Gematria Primus.
5. Calling the cell phone number and inputting the number access code revealed a SSSS code.
6. Each phone number had a different SSSS code.

## 8. SSSS code
1. Making use of ```Shamir's Secret Sharing Scheme``` revealed a fourth onion URL: ```p7amjopgric7dfdi.onion```.

## 9. 4th Onion deep web link
1. This webpage requires the person to make a test.
