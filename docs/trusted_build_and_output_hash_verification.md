# Section 23 - Trusted Build & Output Hash Verification - Windows OS

## Validating the hash of a trusted RCTab build .zip

To validate that the provided zip folder contains the certified version of RCTab v1.3.2, follow these instructions:

- Open the Start Menu
- Type in Command Prompt
- Press "enter" to launch the Command Prompt
- Type in `C:\Windows\System32\certutil.exe -hashfile [filename]`
    * To insert the file name: locate the `rctab_v1.3.2_windows.zip` in File Explorer
    * Left-click on the file and while continuing to hold the mouse down, drag the file to the Command Prompt window and place after `-hashfile`.
    * Example: `C:\Windows\System32\certutil.exe -hashfile C:\RCTab\rctab_v1.3.2_windows.zip`
- Add `SHA512` to the end of the line
    * Example: `C:\Windows\Systems32\certutil.exe -hashfile c:\RCTab\rctab_v1.3.2_windows.zip SHA512`
- Press "enter". The command prompt will show the text of the hash in the following format `SHA512 hash of [filePath]: [SHA512 hash text]`
- Compare the `SHA512` hash code produced on your system to the SHA512 hash code supplied with the trusted build.
- If the `SHA512` hash codes match 100%, you are using an approved download and can proceed. Return to the [**Section 22 - Installation Instructions for Windows OS**](installation_instructions_for_windows_os.md) document to complete installation.

## Validating the hash of RCTab contest summary files

RCTab automatically creates corresponding `.hash` files for the `summary.csv` and `summary.json` output files. Follow these instructions for using the \[fileName\].hash files to verify their corresponding summary file. For this example we will verify a `summary.csv` file and we will assume that it is located in `c:\RCTab\output\`

- Create a new empty text file. We’ll call this the ‘comparison text file’
- Copy the RCTab programmatically generated hash to the comparison text file
    * Open `summary.csv.hash` in text editor. This file contains the following format: `[hash] [hashAlgorithm]`
        + `[hash]` is the text of the hash itself
        + `[hashAlgorithm]` is the algorithm used to get the hash e..g SHA512
    * Copy the `[hash]` to the comparison text file on a single line
- Use cmd prompt to generate hash of summary.csv
    * Open the Start Menu
    * Type in Command Prompt
    * Press "enter" to launch the Command Prompt
    * Create the command to hash the summary.csv with the following template `C:\Windows\System32\certutil.exe -hashfile [filePath] SHA512`
        + Replace `[filePath]` with the location of your summary.csv. You can drag the file into the cmd prompt window to have it automatically fill it in for you or you can type it manually if you know the path
    * Press enter. The command prompt will show the text of the hash in the following format `SHA512 hash of [filePath]: [SHA512 hash text]`
- Copy and paste `[SHA512 hash text]` to the next line of the comparison text file
- Compare the text of the two `SHA512` hashes. Pulling the width of the text editor wide enough so that the hashes each are one line each will help line them up for comparison.
