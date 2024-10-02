# Section 02 - Software Design and Specifications

## Coding Standards and Style

We use [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html) as our published, reviewed, and industry-accepted code style. For more details see page 93 of the [VVSG Volume 1.0](https://www.eac.gov/sites/default/files/eac_assets/1/28/VVSG.1.0_Volume_1.PDF) guide.

Code development and review processes are described in [**Section 13 - Quality Assurance Plan**](quality_assurance_plan.md).

### Java 17
The tabulator is written in Java because it meets the VVSG and California requirements for software language selection. It is widely supported and popular in both industry and the open-source community for a wide variety of applications. It offers a mature and robust collection of third-party libraries. The Java Runtime Environment is standard on our target platforms which means a simple installation process. Our specific version of Java is OpenJDK 17.0.2 and it can be downloaded [here](https://jdk.java.net/archive/).

### Open Source
We develop the tabulator as an open-source project for three main reasons:

1.  **Transparency**: published source code increases public confidence in the application by giving anyone the opportunity to review our work and the processes and methodology behind it.
2.  **Adoption**: open-source licensing encourages others to use the software to facilitate the spread of ranked choice voting.
3.  **Collaboration**: open-source licensing enables other software developers to contribute enhancements to the project and incorporate it into other related projects (RCV visualizers, policy research, etc.)

### Architecture
RCTab consists of one in-house java code module built from 27 source files. These are described in more detail under [**Tabulator Java Classes**](#tabulator-java-classes) below. The Tabulator relies on basic java platform libraries (file I/O, string processing, logging) and several 3rd-party modules listed below for reading and writing various file formats. These code modules are compiled and packaged with a minimal java runtime environment (17.0.2) which executes compiled object code when installed and run on the target system.

## Tabulator Java classes
The following Java classes comprise the entirety of all in-house developed software and implement all core functionality of the Tabulator.

-   `AuditableFile`: Create a file that, on close, is read-only and has its hash added to the audit log.
-   `CastVoteRecord`: The in-memory representation of each cast vote record read from a source file. When source files are first processed at the beginning of a tabulation, each `CastVoteRecord` object contains the data parsed from the source, including the candidate rankings, the precinct ID, and other relevant metadata. As the tabulation progresses, the object keeps track of the cast vote record’s fate, including which candidate(s) this ballot is counting toward and whether it has been exhausted.
-   `ClearBallotCvrReader`: Contains the logic for parsing a CVR source file in Clear Ballot’s comma-separated value format and populating a list of `CastVoteRecord` objects.
-   `CommonDataFormatReader`: Contains the logic for parsing a CVR source file in the Common Data Format and populating a list of `CastVoteRecord` objects. It supports both XML and JSON.
-   `ContestConfig`: A wrapper around `RawContestConfig`. It performs extensive validation to confirm that a config file contains parameters that are permitted by the software and consistent with one another. It also has logic for reading a config file from disk, preprocessing the candidate data from a config, and normalizing some of the config values for use during tabulation.
-   `ContestConfigMigration`: Provides support for identifying whether a config file’s version is compatible with the version of the application that is running. It also contains logic for automatically migrating a config from an older version to make it compatible with the current version.
-   `DominionCvrReader`: Contains the logic for parsing a set of CVR source files in Dominion’s JSON format and populating a list of `CastVoteRecord` objects.
-   `FileUtils`: A few simple utility functions for reading from and writing to directories on disk.
-   `GuiApplication`: The simple logic for launching the application’s graphical user interface, including loading the main layout markup stored in the `GuiConfigLayout.fxml` file.
-   `GuiConfigController`: Contains most of the logic for the interactive components of the graphical user interface, ensuring that the application responds appropriately when the user clicks a button, menu item, or other interactive element.
-   `GuiContext`: A singleton class that supports the graphical user interface in managing file chooser dialogs for opening and saving config files.
-   `GuiTiebreakerController`: Supports the interactive logic for selecting a tie-breaker winner or loser in the graphical user interface when the tie-break mode is set to one of the interactive options.
-   `HartCvrReader`: Contains the logic for parsing a CVR source file in the Hart XML format and populating a list of `CastVoteRecord` objects.
-   `JsonParser`: Generic logic for reading JSON files from disk and writing them to disk. It’s used by the JSON parsing code for parsing Common Data Format and Dominion CVR files, as well as for reading and writing tabulator config files.
-   `Logger`: Handles the formatting and saving to disk of audit and operator log files.
-   `Main`: The main entry point for the application. Depending on the arguments supplied, it either launches the graphical user interface or proceeds with a command-line-based tabulation.
-   `RawContestConfig`: A `RawContestConfig` object is a simple in-memory representation of a config file loaded from disk.
-   `ResultsWriter`: After a tabulation completes, a `ResultsWriter` generates all of the appropriate summary results files and saves them to disk. Results files can include a summary CSV spreadsheet file, a summary JSON file, a full Common Data Format JSON file, and corresponding .hash files. When “tabulate by precinct” is enabled, it also produces separate summary files for each precinct.
-   `SecurityConfig`: Configuration for the cryptographic signing of a Hart file.
-   `SecuritySignatureValidation`: A set of tools to verify signatures of Hart CVRs.
-   `SecurityTests`: Test the cryptographic signature validation functionality.
-   `SecurityXmlParsers`: In-memory representation of `.sig.xml` signature files.
-   `StreamingCvrReader`: Contains the logic for parsing a CVR source file and populating a list of `CastVoteRecord` objects. It also extracts a list of precinct IDs if tabulation by precinct is enabled.
-   `Tabulator`: The core logic for tabulating a contest given a list of `CastVoteRecord` objects and a `ContestConfig`, it runs the round-by-round tabulation, writing to the tabulation log file as it proceeds, and then calls `ResultsWriter` to generate results files when it completes.
-   `TabulatorSession`: Manages the process of running a single tabulation. Given the path to a config file, it loads and validates the config, loads and parses the cast vote record source files, and runs the tabulation, including generating the results files at the end. It also contains logic for converting a CVR file into a Common Data Format CVR file without actually running a tabulation.
-   `TabulatorTests`: Runs all of the regression tests. Each test involves loading a config file and, if it’s valid, running the tabulation and then comparing the output summary JSON file to an existing file containing the expected output. If the config file has `generateCdfJson` enabled, it also compares the generated CDF JSON file to an existing file containing the expected version of this output.
-   `TallyTransfers`: The `Tabulator` class maintains a `TallyTransfers` object (and one per precinct if tabulating by precinct is enabled) to keep track of the number of votes transferring from each source to each destination in each round as candidates are eliminated or elected. This data is included in the results summary JSON to enable Sankey plot visualizations.
-   `Tiebreak`: Contains the logic for breaking a tie when the tabulation needs to select a candidate for elimination or election and multiple candidates are tied with the same current vote total.
-   `Utils`: Miscellaneous utility functions for processing strings and identifying the user’s environment.

## 3rd-party Modules
RCTab incorporates several 3rd-party modules which are all open-source. These meet the VVSG and California requirements for third-party modules. They are mature and widely accepted and used.  None of them are modified in any way.

| Module Name            | Version | Purpose                                          | Link                                                                           |
|:-----------------------|:--------|:-------------------------------------------------|:-------------------------------------------------------------------------------|
| Apache Commons CSV     | 1.9     | CSV "Comma Separated Values" reader / writer.    | <https://commons.apache.org/proper/commons-csv/user-guide.html>                |
| Apache POI OOXML       | 5.2.2   | Excel spreadsheet reader / writer.               | <https://poi.apache.org/apidocs/dev/org/apache/poi/ooxml/package-summary.html> |
| Jackson Core           | 2.13.3  | XML / JSON streaming reader / writer core        | <https://github.com/FasterXML/jackson-core>                                    |
| Jackson Annotations    | 2.13.3  | XML / JSON deserialization annotations           | <https://github.com/FasterXML/jackson-annotations>                             |
| Jackson Databind       | 2.13.3  | XML / JSON deserialization                       | <https://github.com/FasterXML/jackson-databind>                                |
| Jackson Dataformat XML | 2.13.3  | XML reader / writer                              | <https://github.com/FasterXML/jackson-dataformat-xml>                          |
| Jupiter JUnit API      | 5.9.0   | Automated testing (used only during development) | <https://mvnrepository.com/artifact/org.junit.jupiter/junit-jupiter-api>       |
| Jupiter JUnit Engine   | 5.9.0   | Automated testing (used only during development) | <https://mvnrepository.com/artifact/org.junit.jupiter/junit-jupiter-engine>    |
| BouncyCastle FIPS API  | 1.0.2.4 | RSA Validation                                   | <https://mvnrepository.com/artifact/org.bouncycastle/bc-fips/1.0.2.4>          |

**Software Limits:**
Limitations of the Tabulation software i.e., how many CVRs can be tabulated are detailed in [**Section 03 - System Hardware Specification**](system_hardware_specification.md) document. 

## Contest Tabulation Logic

### Overview

When the user triggers a contest tabulation, the application creates a new `TabulatorSession` object to manage the process flow. The `TabulatorSession` loads, parses, and validates the contest config file. If those steps succeed, it reads the cast vote records into memory, runs the tabulation, and generates the results summary files. Throughout these processes logging output is written to two locations as detailed below under [**RCTab Logging**](#rctab-logging)

1. Read the config file  
2. Validate the config file  
3. Read cvr files  
4. Round by round tabulation of votes according to configuration  
5. Generate reports

For detailed user guides, see [**Section 18 - User Guide**](user_guide.md) and [**Section 25 - Configuration File Parameters**](configuration_file_parameters.md). Note that this document covers all tabulation logic in RCTab in order to fully describe the software design. All tabulation logic is described in the ‘Tabulation of CVRs’ section below, in conjunction with the draft VVSG 2.0 1500-107 Voting Methods and Tabulation Models document (for which RCTab acts as a reference implementation), as well as with reference to all RCV laws currently in use in the United States. Contact the manufacturer for a folder with all such RCV laws and/or a copy of that unpublished draft standard. 

#### Reading a config file

When a user selects an existing config file to open, the tabulator parses the JSON file and stores the information in a `RawContestConfig` object. This object is wrapped inside a `ContestConfig` object. The `ContestConfig` object serves as an interface between the config file and the rest of the application, providing extensive validation logic and a number of convenience methods for accessing normalized versions of the config settings.

A config file includes a `tabulatorVersion` string and a collection of parameters organized into four sections.

The `tabulatorVersion` is used to confirm that the version of the application that’s loading the config file is compatible (specifically: not older than) the version of the application that created the file.

The `outputSettings` section contains settings related to what forms of output should be generated and where it should be saved on disk.

The `cvrFileSources` section is a list of one or more source file paths containing cast vote records, along with the parameters necessary for the tabulator to parse the records successfully.

The candidates section lists all of the candidate names/codes that appear in any of the CVR source files.

The rules section contains all of the parameters that determine exactly how the application should tabulate the cast vote records and produce results.

#### Writing the config file

A user can create a new config file or open an existing one and edit it. The GUI allows the user to modify all of the parameters that populate a config file (except for `tabulatorVersion`, which is determined by the app), run a validation to confirm that all of the settings in the file are valid, and save the file. 

#### Validation

Config file validation checks each aspect of the file and attempts to verify that all of the individual settings are compatible with one another and should result in a successful tabulation. This includes confirming that the tabulation rules are consistent, that the candidate names are valid and don’t contain duplicates, and that each source cvr file exists on disk, and has the proper parameters set for that cvr provider. The GUI prevents the user from creating a config file that would fail many of these checks, but the validation assumes nothing and provides an additional layer of protection against user error.  Because a user can create or modify a config file simply using a text editor the tabulator can’t assume that a config file has only been modified by its own GUI.

#### Reading CVR Files

Reading the cast vote records into memory consists of parsing the source files and creating a `CastVoteRecord` object to represent each record. This object contains the candidate rankings for the CVR along with additional information parsed from the source file such as an ID and a precinct name. As the tabulation progresses, the `CastVoteRecord` object also stores information about the CVR’s fate in each round (which candidate(s) its vote is counting toward and what fraction of the vote belongs to each). The details of parsing each source file depend on that file’s provider.

#### Tabulation of CVRs 

Note: for all winning modes other than `MULTI_SEAT_SEQUENTIAL_WINNER_TAKES_ALL` (a.k.a. multi-pass IRV), the application performs a single tabulation when it processes a config file. For multi-pass IRV, it instead performs a sequence of single-seat tabulations in which each tabulation excludes the candidates who have won on prior iterations, continuing until it has run numWinners tabulations and identified numWinners winners.

For the tabulation itself, the application creates a `Tabulator` object. This object’s tabulation method runs a loop that iterates until it determines that the tabulation is complete. Each iteration of the loop is a new round. Each round starts by calling computeTalliesForRound, which iterates over all of the cast vote records and sums up the total number of current votes for each candidate. This involves a number of steps:

1. If the CVR has already been marked as exhausted, it is skipped.  
2. If the CVR was counted toward a candidate in the previous round and that candidate is still active, it’s counted toward that candidate again in this round.  
3. If the CVR has no rankings at all, it is marked as exhausted.  
4. The tabulator then begins iterating through the rankings in the CVR, starting with the most preferred rank found (i.e., the lowest rank number, which is typically 1) and proceeding in order. At each rank, it checks for a number of possible cases:  
    1. If the number of rankings skipped between the last ranking seen and this one exceeds the maxSkippedRanksAllowed value in the config, the CVR is marked as exhausted.  
    2. If one or more of the candidates at this rank already appeared at another rank and the config has enabled exhaustOnDuplicateCandidate, the CVR is marked as exhausted.  
    3. If the rankings at this rank constitute an overvote, the CVR is handled according to the overvote rule set in the config.  
    4. If a continuing candidate is found at this rank, the CVR is marked as counting toward the candidate.  
    5. Otherwise, the CVR is marked as exhausted.  
5. If the config has enabled tabulation by precinct, the method also updates the per-precinct tallies for this round.

Next, if the tabulation is in the first round and/or the contest is for a single seat or the mode is `MULTI_SEAT_SEQUENTIAL_WINNER_TAKES_ALL` (multi-pass IRV), the software sets/updates the winning threshold (the number of votes that a candidate must meet or exceed in order to be named a winner) based on the winning rules set in the config. 

1. The threshold in single-seat and `MULTI_SEAT_SEQUENTIAL_WINNER_TAKES_ALL` is calculated in each round as: 

    `winningThreshold` = floor(`V`/2) + 1

    Where `V` = the total number of votes counting for continuing candidates in the current round (and continuing refers to non-excluded candidates who have not yet been eliminated -- and, in the case of multi-pass IRV, who have not been elected in a previous pass).

2. The threshold in `MULTI_SEAT_ALLOW_ONLY_ONE_WINNER_PER_ROUND` and `MULTI_SEAT_ALLOW_MULTIPLE_WINNERS_PER_ROUND` is calculated as: 

    `winningThreshold` = (`V`/(`N`+`1`) + 10^(-1 * `decimalPlacesForVoteArithmetic`) if `nonIntegerWinningThreshold` is set to `true`

    `winningThreshold` = floor(`V`/(`N`+1)) + 1 if `nonIntegerWinningThreshold` is set to `false`

    `winningThreshold` = floor(`V`/`N`) if `hareQuota` is set to `true`

    Where `V` = the sum of the values in `currentRoundCandidateToTally` in the first round and `n` = `numWinners`

3. The election threshold in `MULTI_SEAT_BOTTOMS_UP_USING_PERCENTAGE_THRESHOLD` is calculated as:

    `winningThreshold` = `V`*`T`

    Where `V` = total number of votes counting for continuing candidates (candidates not eliminated) in the current round and `T` = `bottomsUpPercentageThreshold`

No threshold is calculated in `MULTI_SEAT_BOTTOMS_UP_UNTIL_N_WINNER`S mode because the tabulation simply eliminates candidates until exactly numWinners remain, then selects those candidates as the winners. 

The software then checks whether there are any continuing candidates with vote tallies in the current round that meet or exceed the winning threshold. Each of these candidates is marked as a winner and, if the winning rules in the config indicate that surplus votes should be redistributed (which is the case when the winning mode is either `MULTI_SEAT_ALLOW_ONLY_ONE_WINNER_PER_ROUND` and `MULTI_SEAT_ALLOW_MULTIPLE_WINNERS_PER_ROUND`), then the software calculates a surplus fraction. The surplus fraction for a winning candidate is calculated as: 

    `surplusFraction` = (`C` - `T`) / `C`

    Where `C` = the candidate’s vote tally in the current round and `T` = the winning threshold

Each `CastVoteRecord` object counting towards a winning candidate redistributes an amount equal to its current value multiplied by the surplusFraction according to step 4 in “Tabulation of CVRs” above, based on that `CastVoteRecord`’s rankings. Each of these `CastVoteRecord`s is also updated to record the portion of that vote that should remain allocated to the candidate in future rounds, which is its current value multiplied by (1 - `surplusFraction`).

Note that if a `CastVoteRecord` is involved in multiple surplus redistributions, the fraction of the vote allocated to earlier winners is not affected by subsequent redistributions; only the surplus portion is eligible for further redistribution.

Any decimal values in the above calculations are governed by the `decimalPlacesForVoteArithmetic` setting. 

More information about how surplus vote values are calculated is included in the fractional transfers discussion in [**Section 19 - Tabulation Options for RCV Tabulation**](tabulation_options_for_rcv_tabulation.md).

If the mode is `MULTI_SEAT_ALLOW_ONLY_ONE_WINNER_PER_ROUND` and more than one continuing candidate meets or exceeds the winning threshold in a round, only the candidate with the top tally is selected as the winner (and any other continuing candidates meeting the threshold will be selected in subsequent rounds). If multiple candidates are tied for this top tally value, the tie is broken according to the selected tiebreakMode. 

In `MULTI_SEAT_BOTTOMS_UP_USING_PERCENTAGE_THRESHOLD`, winners are selected in a given round only if every continuing candidate meets or exceeds the winning threshold.

Finally, if no winners have been identified in the current round, the software determines whether it should identify one or more candidates to eliminate. (_This is true if a) the number of identified winners is fewer than the number of seats for the contest, b) there are more than two candidates remaining and the winning rules specify a single-seat contest that should continue until only two candidates remain, or c) the winning mode is _`MULTI_SEAT_BOTTOMS_UP_USING_PERCENTAGE_THRESHOLD`_._) In this case, the candidate(s) to be eliminated are identified by trying the following methods in order until one of them returns one or more candidates:

1. If the cast vote records include undeclared write-ins and this set of candidates have not been eliminated yet, select them.  
2. If the config specifies a minimum vote threshold for a viable candidate and one or more continuing candidates has a tally below that threshold, select them.  
3. If the config enables batch elimination, attempt to identify two or more candidates who can be eliminated via this process.  
4. Otherwise, select the remaining candidate with the lowest tally. (If multiple candidates are tied for the lowest tally, select one according to the tie-breaking rule specified in the config.)

The tabulator then determines whether it should continue to the next round and repeat the process. It continues if one of the following conditions is true:

1. For a single-seat contest, one of these is true:  
    1. A winner has not been identified yet.  
    2. “Continue until two candidates remain” is enabled and one of these is true:  
        1. There are more than two candidates remaining.  
        2. The eliminations that reduced the number of remaining candidates to two happened in the current round. (This condition is included to ensure that the tabulator will generate an additional round showing the final vote tallies when only the last two candidates remain.)  
2. For a multi-seat contest, one of these is true:  
    1. The winning mode is `MULTI_SEAT_BOTTOMS_UP_USING_PERCENTAGE_THRESHOLD` and no winners have been identified yet.  
    2. The winning mode is not `MULTI_SEAT_BOTTOMS_UP_USING_PERCENTAGE_THRESHOLD` and the number of winners identified is fewer than the number of seats.  
    3. The winning mode is neither `MULTI_SEAT_BOTTOMS_UP_USING_PERCENTAGE_THRESHOLD` nor `MULTI_SEAT_BOTTOMS_UP_UNTIL_N_WINNER`S and the number of winners equals the number of seats, but the final winners were identified in the current round. (Similar to above, this condition ensures that the tabulator will generate an additional round showing the final surplus redistribution in `MULTI_SEAT_ALLOW_ONLY_ONE_WINNER_PER_ROUND` and `MULTI_SEAT_ALLOW_MULTIPLE_WINNERS_PER_ROUND`.)

When the tabulator determines that it should not continue tabulating, the tabulation is complete.

#### Reporting results

After the tabulation completes, the software generates results files and saves them to disk. These results are based on the following data that the tabulation process has produced and stored in memory:

- Which round each eliminated candidate was eliminated  
- Which round each winning candidate was identified as a winner  
- The winning threshold that was used to select the winner(s)  
- Each candidate’s vote tally in each round  
- If the config has enabled tabulating by precinct, each candidate’s vote tally in each precinct in each round  
- A record of the number of votes in each round that were transferred from each candidate to each other candidate (or were exhausted)  
- In a multi-seat contest involving surplus redistribution, the cumulative amount of residual surplus in each round  
- The number of exhausted ballots in each round, which are the number of ballots that cannot be counted for any continuing candidates - those candidates who are still active in the contest. This ranked choice voting specific category of ballots includes undervoted ballots and overvoted ballots. Exhausted ballots are referred to as inactive ballots in summary results files. 

Using this data, the tabulator creates a `ResultsWriter` object that writes the following files with corresponding hashes to disk:

1. A CSV spreadsheet that includes the round-by-round tally for each candidate, when each candidate won or was eliminated, and related information  
2. A JSON file that includes the same information found in the CSV spreadsheet, plus the number of votes transferred from each candidate to each other candidate (or exhaustion) in each round

Each of these files contains a corresponding `fileName.hash` file. These files can be used to verify the content of their corresponding result files.

If tabulating by precinct is enabled, the `ResultsWriter` also generates a CSV spreadsheet with round-by-round tallies for each precinct found in the cast vote records.

Finally, if the config file specifies that the tabulator should generate CDF (Common Data Format) output, it saves a CDF file in JSON format.

Note: if the winning mode is `MULTI_SEAT_SEQUENTIAL_WINNER_TAKES_ALL` (multi-pass IRV), the output files described in this section are generated after each pass, i.e., after each single-seat tabulation. The pass number is appended to each filename to allow the user to distinguish among them.

### RCTab Logging

In addition to results files, RCTab generates various log outputs which describe:  
- Program status  
- Operations in progress  
- Critical errors and warnings  
- Tabulation-specific data: e.g., config file contents and how each vote counted in each round  
- Additional system information

Log output is logically divided into two data streams:

#### Stream 1: Tabulator "Operator" Logging

This data stream captures the overall operation of the Tabulator which may include loading, editing, validating, and saving multiple config files, running cvr conversion functions, and tabulating multiple contests.

File Name: `rcv_0.log`  
File Rotation:  
 When `rcv_0.log` reaches 50MB size it will be renamed along with any other preceding log files.  For example:  
 `rcv_0.log` -> `rcv_1.log`  
 rcv_1.log -> `rcv_2.log`  
Then a new `rcv_0.log` file will be created, and logging will continue.  
This is a standard log rotation strategy that limits log file sizes for easier management.

File location: The Tabulator Operator Log will be created in the current working directory.  When launched using the rcv.bat file this is next to the rcv.bat file.  For example:   `C:\Users\MyUser\rcv\bin\rcv\_0.log`

Operator logging is duplicated in the black GUI console box at the bottom of the application window.  The console is provided as a convenience primarily for showing validation errors and providing feedback to the user. See screenshot below for example of this console box.

<div
    style="
        /* leave border in comment for debugging */
        /*border: 1px dotted deeppink;*/
        width: 100%;
        aspect-ratio: 6.27/2.09;
        overflow: hidden;
    "
>
    <img 
        src="../images/image62.png"
        alt="example of console box screenshot"
        style="
            /* leave border in comment for debugging */
            /*border: 1px solid red;*/
            display: block;
            width: 100%;
            height: auto;
            /* transform: translateX(X%) translateY(Y%) scale(S); */
            /* translateX(X%): Adjusts horizontal position. Negative moves left, positive moves right. */
            /* translateY(Y%): Adjusts vertical position. Negative moves up, positive moves down. */
            /* scale(S): Scales the image. Values >1 enlarge, <1 shrink. */
            /* tip: use binary search to find ideal values */
            transform: translateX(1.5%) translateY(-58%) scale(1.15);
        "
    >
</div>

#### Stream 2: Contest-Specific "Audit" Logging

This data stream captures information about a specific contest tabulation.  It includes all the same information written to the Execution Log (within the context of a single contest tabulation) and includes a listing of the config file being tabulated, and a record of how each cvr was counted in each round.

File Name: `[time_stamp]_audit_0.log` where timestamp is created when the tabulation is triggered and used on all output files for a given tabulation.  For example: `2021-04-24_22-49-49_audit_0.log`  
File Rotation uses the same strategy as the Execution Logging.  When an audit log reaches 50MB size it will be renamed along with any other preceding log files.  For example:  
`2021-04-24_22-49-49_audit_0.log` -> `2021-04-24_22-49-49_audit_1.log`  
`2021-04-24_22-49-49_audit_1.log` -> `2021-04-24_22-49-49_audit_2.log`  
Then a new `2021-04-24_22-49-49_audit_0.log` file will be created, and logging will continue.  
Each audit_*N*.log is created with a corresponding audit_*N*.log.hash file. This hash file can be used to validate the contents of its corresponding audit_N.log file with the directions in [**Section 23 - Trusted Build & Output Hash Verification - Windows OS**](trusted_build_and_output_hash_verification.md)

### User Interface

The tabulator was originally developed for a command-line interface. The GUI (graphical user interface) was introduced both to make the process of configuring and running a tabulation faster and more intuitive and to enable users with a less technical background to use the software. The command-line interface still exists as a way to support execution via script, e.g., for batch processing and test automation. The GUI prevents the user from creating a config file that would fail many of these checks. A brief user guide to the Command Line Interface is available in [**Section 24 - Tabulator Command Line Instructions**](tabulator_command_line_instructions.md). More information about error messages can be found in [**Section 29 - RCTab Operator Log Messages**](rctab_operator_log_messages.md).

### Supported File types

The Tabulator uses the JSON format for contest configuration files and one style of results summary output. JSON is simple, popular, and easy for humans and software to read and write.  The Tabulator uses CSV (comma-separated values) for the tabular version of its results summary output.  CSV is a non-proprietary format that all modern spreadsheet applications can recognize. Tabulation output log files are produced in plain-text with a .log extension for clarity.  RCTab reads `.xlsx` (Microsoft Excel) and `.xml` (Extensible Markup Language) cvr and elections metadata files supplied by various manufacturers (ES&S, Hart, CDF, Unisyn).

Additionally, the following documents were used to design the RCTab software:

[**Section 07 - System Security Specification Requirements**](system_security_specification_requirements.md)  
[**Section 19 - Tabulation Options for RCV Tabulation**](tabulation_options_for_rcv_tabulation.md)  
[**Section 20 - Process Ranked Choice Voting Contest**](process_ranked_choice_voting_contest.md)  
[**Section 21 - Ballot Limitations & Maximum Testing Range**](ballot_limitations_and_maximum_testing_range.md)  
[**Appendix III - Ranked Choice Voting Laws Appendix**](ranked-choice-voting-laws.md)   
[**Appendix II - Expected Outcome RCV Test Sets Single-Winner**](expected-outcome-rcv-test-sets-single-winner.md)  
[**Appendix I- Expected Outcome RCV Test Sets Multi-Winner**](expected-outcome-rcv-test-sets-multi-winner.md)

## 7.4.4 Software Distribution

b. The documentation shall designate all software files as static, semi-static or dynamic.

The `.json` config files used to configure RCTab are semi-static. These files are modified for contest-specific configuration options such as the candidate list, winning rules and output locations.

RCTab output files, if considered part of the “software files,” are also semi-static. The `summary.json`, `summary.csv`, `audit.log` and corresponding `.hash` files output for each tabulation are different depending on the configured contest. 

All other RCTab files, excluding the `.json` config files and output files, are static. All remaining files’ contents (specifically the source code files and 3rd party dependencies) are not modified based on the election being conducted or the equipment upon which it is installed. All executable code files are the same no matter what hardware it is installed on and no matter what voting equipment it is being used with.

## 9.5.2 Applicable Documents

The manufacturer shall list all documents controlling the development of the software and its specifications. Documents shall be listed in order of precedence.

* This is described in the [**Coding Standards and Style**](#coding-standards-and-style) paragraph of [**Section 02 - Software Design and Specifications**](#).

## 9.5.3 Software Overview {#9.5.3-software-overview}

The manufacturer shall provide an overview of the software that includes the following items:  

1. A description of the software system concept, including specific software design objectives, and the logic structure and algorithms used to accomplish these objectives. 

    - This is described in the [**Contest Tabulation Logic**](#contest-tabulation-logic) section of [**Section 02 - Software Design and Specifications**](#) and informed by the following documents:   
    - [**Section 07 - System Security Specification Requirements**](system_security_specification_requirements.md)  
    - [**Section 19 - Tabulation Options for RCV Tabulation**](tabulation_options_for_rcv_tabulation.md)  
    - [**Section 20 - Process Ranked Choice Voting Contest**](process_ranked_choice_voting_contest.md)  
    - [**Section 21 - Ballot Limitations & Maximum Testing Range**](ballot_limitations_and_maximum_testing_range.md)  
    - [**Appendix III - - Ranked Choice Voting Laws Appendix**](ranked-choice-voting-laws.md)   
    - [**Appendix II - Expected Outcome RCV Test Sets Single-Winner**](expected-outcome-rcv-test-sets-single-winner.md)  
    - [**Appendix I - Expected Outcome RCV Test Sets Multi-Winner**](expected-outcome-rcv-test-sets-multi-winner.md)

2. The general design, operational considerations, and constraints influencing the design of the software.

    - This is described in the [**Contest Tabulation Logic**](#contest-tabulation-logic) section of [**Section 02 - Software Design and Specifications**](#) and informed by the following documents:   
    - [**Section 07 - System Security Specification Requirements**](system_security_specification_requirements.md)  
    - [**Section 19 - Tabulation Options for RCV Tabulation**](tabulation_options_for_rcv_tabulation.md)  
    - [**Section 20 - Process Ranked Choice Voting Contest**](process_ranked_choice_voting_contest.md)  
    - [**Section 21 - Ballot Limitations & Maximum Testing Range**](ballot_limitations_and_maximum_testing_range.md)  
    - [**Appendix III - Ranked Choice Voting Laws Appendix**](ranked-choice-voting-laws.md)   
    - [**Appendix II - Expected Outcome RCV Test Sets Single-Winner**](expected-outcome-rcv-test-sets-single-winner.md)  
    - [**Appendix I - Expected Outcome RCV Test Sets Multi-Winner**](expected-outcome-rcv-test-sets-multi-winner.md)

3. Identification of all software items, indicating items that were:

    1. Written in-house.

        - All in-house items written in-house are described in this doc under [**Tabulator Java Classes**](#tabulator-java-classes) located in [**Section 02 - Software Design and Specifications.**](#)

    2. Procured and not modified; and

        - All third-party modules are not modified. They are described in [**Section 02 - Software Design and Specifications**](#) under [**Java 17, Architecture, 3rd-party Modules**](#3rd-party-modules)

    3. Procured and modified including descriptions of the modifications to the software and to the default configuration options. The manufacturer shall also include a certification that procured software items were obtained directly from the manufacturer or a licensed dealer or distributor.

        - No third-party modules have been modified. 

We affirm that all third-party modules were obtained from the manufacturer.  All of the third-party modules can be freely obtained and updated via the internet.  They are maintained by their respective authors and hosted in the Maven Central Repository. More information on verifying dependencies can be found in [**Section 14 - Tabulator Trusted Build Instructions**](tabulator_trusted_build_instructions.md)

## 9.5.4 Software Standards and Conventions

The manufacturer shall provide information that can be used by the SOS and S-ATA to support software analysis and test design. The information shall address standards and conventions developed internally by the manufacturer as well as published industry standards that have been applied by the manufacturer. The manufacturer shall provide information that addresses the following standards and conventions:

1. Software System development methodology.

    Our software development methodology is feature-driven:

    - New customer needs are identified and specified  
    - Features are designated for a particular release or deferred  
    - Design new or updated software to meet those needs  
    - Software is created or updated, reviewed and tested (see [**Section 13 - Quality Assurance Plan**](quality_assurance_plan.md))  
    - Software is submitted for VSTL testing  
    - Iterate with test lab  
    - Release

2. Software design standards, including internal manufacturer procedures.  
3. Software specification standards, including internal manufacturer procedures.  
4. Software coding standards, including internal manufacturer procedures.  
5. Testing and verification standards, including internal manufacturer procedures, that can assist in determining the program's correctness and ACCEPT/REJECT criteria; and  
6. Quality assurance standards or other documents that can be used by the ITA to examine and test the software. These documents include standards for program flow and control charts, program documentation, test planning, and for test data acquisition and reporting.

    - Our software design and coding standards are based on the VVSG 1.0 VOL 1: 5.2 Software Design and Coding Standards. Additionally, we use Google Checkstyle as described in this document under [**Coding Standards and Style.**](#coding-standards-and-style)  
    - Software specifications are described in our Github repo under the related issues. Our software specification standard is ad-hoc.    
    - Testing and verification standards are described in [**Section 13 - Quality Assurance Plan**](quality_assurance_plan.md) and [**Section 17 - System Test & Verification**](system_test_and_verification_specification.md).

## 9.5.5 Software Operating Environment

This section shall describe or make reference to all operating environment factors that influence the software design.

- RCTab is designed to run on unmodified COTS Windows, Mac, and Linux operating systems as they are very popular, robust, mature, trusted, and they all support Java 17.  For more information see the above section titled [**Java 17**](#java-17).    
- RCTab core processing and tabulation logic is entirely platform (i.e., operating system) agnostic.   
- All platform-specific functionality is encapsulated in the Java language implementation and Java platform libraries, including:  
    - Basic OS services for disk IO  
    - File path resolution  
    - Memory management  
    - System interrupt handling.

### 9.5.5.1 Hardware Environment and Constraints

The manufacturer shall identify and describe the hardware characteristics that  
influence the design of the software, such as:

1. The logic and arithmetic capability of the processor.  
2. Memory read-write characteristics.  
3. External memory device characteristics.  
4. Peripheral device interface hardware.  
5. Data input/output device protocols; and  
6. Operator controls, indicators, and displays.

    - RCTab is designed to be as efficient as possible with RAM and CPU usage in order to lower the hardware requirements needed to process an election and decrease costs for our users.  
    - Because the Tabulator creates an in-memory record for each CVR it processes, the maximum number of CVRs that can be processed in a single contest is limited by the amount of available RAM on the host system. See [**Section 03 - System Hardware Specification**](system_hardware_specification.md) for more details.

### 9.5.5.2 Software Environment

The manufacturer shall identify the compilers or assemblers used in the generation of executable code and describe the operating system or system monitor.

- We use the javac compiler javac 17.0.2 included with OpenJDK 17.0.2 (build 17.0.2+8).  
- See also [**Section 14 - Tabulator Trusted Build Instructions**](tabulator_trusted_build_instructions.md)

## 9.5.6 Software Functional Specification

The manufacturer shall provide a description of the operating modes of the system and of software capabilities to perform specific functions.

For more information about operating modes of the system and of system capabilities to perform specific functions, please see:

- [**Section 01 - System Overview**](system_overview.md)
- [**Section 18 - User Guide**](user_guide.md)  
- [**Section 19 - Tabulation Options for RCV Tabulation**](tabulation_options_for_rcv_tabulation.md)  
- [**Section 25 - Configuration File Parameters**](configuration_file_parameters.md)

### 9.5.6.1 Configurations and Operating Modes

The manufacturer shall describe all software configurations and operating modes of the system, such as ballot preparation, election programming, preparation for opening the polling place, recording votes and/or counting ballots, closing the polling place, and generating reports. For each software function or operating mode, the manufacturer shall provide:  
1. A definition of the inputs to the function or mode (with characteristics, tolerances or acceptable ranges, as applicable);  
2. An explanation of how the inputs are processed; and  
3. A definition of the outputs produced (again, with characteristics, tolerances, or acceptable ranges as applicable).

RCTab only processes ballot data once it has been exported from an election management system. It then produces a final report. For more information about the components of RCTab with regard to data input/counting and generating final count that are relevant here, please see:

- [**Section 01 - System Overview**](system_overview.md)  
- [**Section 18 - User Guide**](user_guide.md)  
- [**Section 19 - Tabulation Options for RCV Tabulation**](tabulation_options_for_rcv_tabulation.md)  
- [**Section 25 - Configuration File Parameters**](configuration_file_parameters.md)

### 9.5.6.2 Software Functions

The manufacturer shall describe the software's capabilities or methods for detecting  
or handling:  
1. Exception conditions.  
2. System failures.  
3. Data input/output errors.  
4. Error logging for audit record generation.

   - Exceptions are handled using Java language built-in exception handling.  
   - Exceptions are logged to the **Operator Log** and, if a contest is being tabulated, the **Audit Log**.   
   - Tabulator Exceptions are detailed in [**Section 29 - RCTab Operator Log Messages**](rctab_operator_log_messages.md).  
   - System failures such as out of memory, disk input/output errors, etc. will be logged in these locations as well.

5. Production of statistical ballot data.

   - Tabulator results are described in [**Section 18 - User Guide**](user_guide.md) under [**Running A Tabulation**](user_guide.md#running-a-tabulation).

6. Data quality assessment; and

   - For data quality assessment, we only operate upon CVR data formatted according to the standards the manufacturers have defined for their CVRs. See election system manufacturer documentation for more information regarding CVR formatting.   
   - Additionally, audit logs describe how all ballot data and configuration data in a contest tabulation was read/interpreted by RCTab. 

7. Security monitoring and control.

   - Jurisdiction practices and policies govern the security monitoring control when using the tabulator.  We recommend a minimum of 2 trained employees operate the system together at all times.   
   - For detailed information about security monitoring and control issues, please see [**Section 07 - System Security Specification Requirements**](system_security_specification_requirements.md).
   - If there are additional questions outside the scope of the jurisdiction practices and policies or the documentation provided with the software regarding security issues, we recommend consulting with an information technology security specialist. 

## 9.5.7 Programming Specifications

The manufacturer shall provide in this section an overview of the software design, its structure, and implementation algorithms and detailed specifications for individual software modules.

This is described in this document under [**Contest Tabulation Logic.**](#contest-tabulation-logic) Also see the below diagram located in [9.5.7.1](#9571-programming-specifications-overview).

### 9.5.7.1 Programming Specifications Overview

This overview shall include such items as flowcharts, HIPOs, data flow diagrams, and other graphical techniques that facilitate understanding of the programming specifications. This section shall be prepared to facilitate understanding of the internal functioning of the individual software modules. Implementation of the functions shall be described in terms of the software architecture, algorithms, and data structures.

This is described in the [**Contest Tabulation Logic**](#contest-tabulation-logic) section of [**Section 02 - Software Design and Specifications.**](#) Also see the below diagram: 

![Tabulator Session Processing Overview diagram](../images/image63.png)

### 9.5.7.2 Programming Specifications Details

The programming specifications shall describe individual software modules and their component units, if applicable. For each module and unit, the manufacturer shall provide the following information:  

1. Module and unit design decisions, if any, such as algorithms used.  
2. Any constraints, limitations, or unusual features in the design of the software module or unit.  
3. The programming language used and rationale for its use, if other than the specified module or unit language  
4. If the software module or unit consists of, or contains, procedural commands (such as menu selections in a database management system for defining forms and reports, on-line queries for database access and manipulation, input to a graphical user interface builder for automated code generation, commands to the operating system, or shell scripts), a list of the procedural commands and reference to user manuals or other documents that explain them  
5. If the software module or unit contains, receives, or outputs data, a description of its inputs, outputs, and other data elements as applicable.  
6. If the software module or unit contains logic, the logic to be used by the software unit, including, as applicable:  
    1. Conditions in effect within the software module or unit when its execution is initiated.  
    2. Conditions under which control is passed to other software modules or units.  
7. Exception and error handling

    - The programming specifications that describe individual software modules and their component units are described in the **[Tabulator Java Classes](#tabulator-java-classes)** and **[3rd Party Modules](#3rd-party-modules)** sections of this document.
    - For additional information, see the following documents:
        - **[Section 01 - System Overview](system_overview.md)**
        - **[Section 18 - User Guide](user_guide.md)**
        - **[Section 19 - Tabulation Options for RCV Tabulation](tabulation_options_for_rcv_tabulation.md)**
        - **[Section 25 - Configuration File Parameters](configuration_file_parameters.md)**

8. If the software module is a database, provide the information described below in [Subsection 9.5.8](#958-databases).
 

## 9.5.8 Databases

The RCTab software does not use any databases for its operation. This requirement does not apply to RCTab.

## 9.5.9 Interfaces

RCTab does not rely on any interfaces for its operation. This requirement does not apply to RCTab. 
