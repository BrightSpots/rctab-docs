# Section 02 - Software Design and Specifications

**⚠️ Warning: Make sure that this text is up-to-date and accurate!**

**Section 02 - Software Design and Specifications** document is solely for use in the State of California. This document can be expanded or updated as is necessary or required. Where relevant, this document refers to specific sections and requirements of the California Voting System Standards. Any recommendations listed in this document should not supersede user jurisdiction procedures or other controlling governance entities.

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
-   `HartCvrReader`: Contains the logic for parsing a CVR source file in the Hart XML format and populating a list of CastVoteRecord objects.
-   `JsonParser`: Generic logic for reading JSON files from disk and writing them to disk. It’s used by the JSON parsing code for parsing Common Data Format and Dominion CVR files, as well as for reading and writing tabulator config files.
-   `Logger`: Handles the formatting and saving to disk of audit and operator log files.
-   `Main`: The main entry point for the application. Depending on the arguments supplied, it either launches the graphical user interface or proceeds with a command-line-based tabulation.
-   `RawContestConfig`: A `RawContestConfig` object is a simple in-memory representation of a config file loaded from disk.
-   `ResultsWriter`: After a tabulation completes, a ResultsWriter generates all of the appropriate summary results files and saves them to disk. Results files can include a summary CSV spreadsheet file, a summary JSON file, a full Common Data Format JSON file, and corresponding .hash files. When “tabulate by precinct” is enabled, it also produces separate summary files for each precinct.
-   `SecurityConfig`: Configuration for the cryptographic signing of a Hart file.
-   `SecuritySignatureValidation`: A set of tools to verify signatures of Hart CVRs.
-   `SecurityTests`: Test the cryptographic signature validation functionality.
-   `SecurityXmlParsers`: In-memory representation of `.sig.xml` signature files.
-   `StreamingCvrReader`: Contains the logic for parsing a CVR source file and populating a list of `CastVoteRecord` objects. It also extracts a list of precinct IDs if tabulation by precinct is enabled.
-   `Tabulator`: The core logic for tabulating a contest given a list of `CastVoteRecord` objects and a `ContestConfig`, it runs the round-by-round tabulation, writing to the tabulation log file as it proceeds, and then calls `ResultsWriter` to generate results files when it completes.
-   `TabulatorSession`: Manages the process of running a single tabulation. Given the path to a config file, it loads and validates the config, loads and parses the cast vote record source files, and runs the tabulation, including generating the results files at the end. It also contains logic for converting a CVR file into a Common Data Format CVR file without actually running a tabulation.
-   `TabulatorTests`: Runs all of the regression tests. Each test involves loading a config file and, if it’s valid, running the tabulation and then comparing the output summary JSON file to an existing file containing the expected output. If the config file has `generateCdfJson` enabled, it also compares the generated CDF JSON file to an existing file containing the expected version of this output.
-   `TallyTransfers`: The Tabulator class maintains a `TallyTransfers` object (and one per precinct if tabulating by precinct is enabled) to keep track of the number of votes transferring from each source to each destination in each round as candidates are eliminated or elected. This data is included in the results summary JSON to enable Sankey plot visualizations.
-   `Tiebreak`: Contains the logic for breaking a tie when the tabulation needs to select a candidate for elimination or election and multiple candidates are tied with the same current vote total.
-   `Utils`: Miscellaneous utility functions for processing strings and identifying the user’s environment.

## 3rd-party Modules
RCTab incorporates several 3rd-party modules which are all open-source. These meet the VVSG and California requirements for third-party modules. They are mature and widely accepted and used.  None of them are modified in any way.

| Module Name            | Version  | Purpose                                          | Link                                                                                                                                                         |
|:-----------------------|:---------|:-------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Apache Commons CSV     | 1.9      | CSV "Comma Separated Values" reader / writer.    | [https://commons.apache.org/proper/commons-csv/user-guide.html](https://commons.apache.org/proper/commons-csv/user-guide.html)                               |
| Apache POI OOXML       | 5.2.2    | Excel spreadsheet reader / writer.               | [https://poi.apache.org/apidocs/dev/org/apache/poi/ooxml/package-summary.html](https://poi.apache.org/apidocs/dev/org/apache/poi/ooxml/package-summary.html) |
| Jackson Core           | 2.13.3   | XML / JSON streaming reader / writer core        | [https://github.com/FasterXML/jackson-core](https://github.com/FasterXML/jackson-core)                                                                       |
| Jackson Annotations    | 2.13.3   | XML / JSON deserialization annotations           | [https://github.com/FasterXML/jackson-annotations](https://github.com/FasterXML/jackson-annotations)                                                         |
| Jackson Databind       | 2.13.3   | XML / JSON deserialization                       | [https://github.com/FasterXML/jackson-databind](https://github.com/FasterXML/jackson-databind)                                                               |
| Jackson Dataformat XML | 2.13.3   | XML reader / writer                              | [https://github.com/FasterXML/jackson-dataformat-xml](https://github.com/FasterXML/jackson-databind)                                                         |
| Jupiter JUnit API      | 5.9.0    | Automated testing (used only during development) | [https://mvnrepository.com/artifact/org.junit.jupiter/junit-jupiter-api](https://github.com/FasterXML/jackson-databind)                                      |
| Jupiter JUnit Engine   | 5.9.0    | Automated testing (used only during development) | [https://mvnrepository.com/artifact/org.junit.jupiter/junit-jupiter-engine](https://github.com/FasterXML/jackson-databind)                                   |
| BouncyCastle FIPS API  | 1.0.2.4  | RSA Validation                                   | [https://mvnrepository.com/artifact/org.bouncycastle/bc-fips/1.0.2.4](https://github.com/FasterXML/jackson-databind)                                         |

**Software Limits:**
Limitations of the Tabulation software i.e., how many CVRs can be tabulated are detailed in [**Section 03 - System Hardware Specification**](system_hardware_specification.md) document. 
