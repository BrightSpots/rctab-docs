# Section 15 - System Change Notes

## 9.12 System Change Notes

Manufacturers submitting modifications for a system that has been tested previously and received national certification shall submit system change notes. These will be used by the S-ATA to assist in developing and executing the test plan for the modified system. The system change notes shall include the following information:

1. Summary description of the nature and scope of the changes, and reasons for each change
1. A listing of the specific changes made, citing the specific system configuration items changed and providing detailed references to the documentation sections changed
1. The specific sections of the documentation that are changed (or completely revised documents, if more suitable to address a large number of changes)
1. Documentation of the test plan and procedures executed by the manufacturer for testing the individual changes and the system as a whole, and records of test results

## RCTab Version 1.3.2

RCTab version 1.3.1 was submitted with Hart InterCivic’s Verity Voting 3.2 to SLI  for initial testing to California Voting System Standards.  After an initial round of testing we received SLI’s report. Some of the report results identified recommendations for RCTab mostly related to access control and programmatically verifying RCTab input and output. Ranked Choice Voting Resource Center (RCVRC) submitted a new version, v1.3.2, to address each of the report results. v1.3.2 updates apply to Windows only. ***In 2.0**, Hart Cryptographic Signature verification is not enabled by default as it would only work in the state of California.

**New Features**

- Two Windows OS accounts. One Administrator level Windows account for installation and initial configuration. A separate ‘RCTab’ Windows standard account for running the tabulation with only necessary permissions and **will not have access to make administrative changes to the machine** that could be security issues
- Read-Only RCTab output files, each with a corresponding read-only .hash file that contains the hash of file contents to ensure they haven’t been edited
- Automatic, programmatic verification of the cryptographic signature of Hart input CVRs. This verification step ensures both the integrity (CVR contents have not been edited) and provenance (CVRs came from the Hart voting system) of the Hart CVRs. RCTab will throw a halting error and tabulation will not begin if cryptographic validation of Hart’s CVR signature is not successful.

**Hardware Setup Improvements**

- Explicit TDP directions for a secure, hardened OS install
- Password secured BIOS

**TDP Updates**

- [**Section 02 - Software Design and Specifications**](software_design_and_specifications.md)
    *  Includes .hash file descriptions in **Reporting Results** header, **RCTab Logging Stream 2: Contest-Specific "Audit" Logging** header, ResultsWriter Java class
    *  Removes paragraph in **RCTab Logging - Stream 2: Contest-Specific "Audit" Logging** header about config validation missing from audit log. That was fixed in 1.3.1
    *  9.5.3.c.3 updated with link to [Section 14 - Tabulator Trusted Build Instructions](tabulator_trusted_build_instructions.md)
    * 3rd Party Modules section updated with new version numbers and added BouncyCastle FIPS API module
    * Include new 1.3.2 Java classes: AuditableFile, SecurityConfig, SecuritySignatureValidation, SecurityXmlParsers, SecurityTests
- [**Section 07 - System Security Specification Requirements**](system_security_specification_requirements.md)
    * Add RCTab Windows standard user account, read-only outputs, .hash files for RCTab output and Hart CVR signature verification throughout CVSS security & access control requirements
        + 9.6.1.a, 9.6.1.b, 9.6.1.c, 9.6.1.d, 9.6.1.e, 9.6.1.1, 9.6.1.1.a, 9.6.2
    * 9.6.1.b updated to include Windows OS Account and BIOS Password access control mechanisms
    * 9.6.1.2 updated to include full description of two tier Windows OS accounts for access control
    * 9.6.1.1.e updated to include explicit overview of Operating System protection abilities
    * 9.6.3.f describes in detail the signature verification interaction with Hart Verity
    * 9.6.7 Cryptography header updated with explicit cryptographic signature verification details
- [**Section 07I - Design and Interface Specification**](design_and_interface_specification.md)
    * Includes all security enhancements for 1.3.2 and describes the threat that they protect against as well as the threats that still exist
    * Added explicit system security objectives and known vulnerabilities
- [**Section 07J - Security Architecture**](security_architecture.md)
    * Include 1.3.2 updates in Access Control and Integrity sections
- [**Section 07L - Security Threat Analysis**](security_threat_analysis.md)
    * Include all 1.3.2 updates and describe the threats that they protect against
- [**Section 07M - Security Testing and Vulnerability Analysis**](security_testing_and_vulnerability_analysis.md)
    * Include all 1.3.2 updates to describe how initial testing report results have all been addressed
- [**Section 09 - System Maintenance Manual**](system_maintenance_manual.md)
    * Includes read-only output and .hash file verification in 9.9.1.f
- [**Section 11 - L&A Testing**](l_and_a_testing.md)
    * Update hash verification of output with .hash files
- [**Section 12 - Configuration Management Plan**](configuration_management_plan.md)
    * Update RCTab Workstation model, hash value of v1.3.2, required software
- [**Section 13 - Quality Assurance Plan**](quality_assurance_plan.md)
    * Adds security tests for v1.3.2
- [**Section 14 - Tabulator Trusted Build Instructions**](tabulator_trusted_build_instructions.md)
    * Clarify Java install check
    * Add step to confirm gradle install
    * Clarify jlinkZip should be done in the cmd prompt
    * v5 - Add steps for offline build
        + Third party dependencies cache
        + Gradle
    * v5 - Fix --branch instead of -branch in git clone command
    * v5 - Clarify git instructions to use specific version
    * v5 - Clarify instructions for JAVA_HOME variable, hash.bat
    * Added explicit instructions for setting JAVA_HOME variable
    * Updated Comparing Two Builds section to explain more clearly how we get a single hash, remove ‘Individual Files’ section
- [**Section 15 - System Change Notes**](system_change_notes.md)
    * Include code updates, TDP updates
- [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md)
    * Clarify and clean up Windows OS install steps
    * Remove UPS step
    * Included BIOS password, Windows OS Installation
    * Make clear the distinction between online prep and offline updates
    * Explicit steps for enabling Bitlocker device encryption
    * Edit ‘Operating System Hardening’ header to disable screensaver and correctly disable Remote Desktop
    * Remove additional optional antivirus, Windows Update
    * Replace Excel with LibreOffice
    * Remove manual driver installation
- [**Section 17 - System Test and Verification Specification**](system_test_and_verification_specification.md)
    * Adds security tests for v1.3.2
- [**Section 18 - User Guide**](user_guide.md)
    * Include automatic signature verification of Hart signed CVRs, .hash output files and read-only output.
    * Output Directory instructions detail explicit steps to ensure read-only permissions are set
    * Include directions to configure Verity Count to sign CVR exports
    * Remove manual hash steps in ‘Generating Results Files’ header
    * Include automatic signature verification of Hart signed CVRs, .hash output files and read-only output.
    * Output Directory instructions detail explicit steps to ensure read-only permissions are set
    * Include directions to configure Verity Count to sign CVR exports
    * Remove manual hash steps in ‘Generating Results Files’ header
    * Programmatic CVR signature verification in Hart CVR Files Options header and Prepping CVRs For Use header
    * Instructions for Read-Only output in Generating Results Files - Output Tab header
    * Running A Tabulation header output files updated to include .hash files
    * Remove CVR .csv from list of output files as it doesn’t apply to Hart
- [**Section 22 - Installation Instructions for Windows OS**](installation_instructions_for_windows_os.md)
    * Include instructions for creating ‘RCTab’ Windows Standard User
    * Explicit instructions for RCTab Windows Standard user vs. Windows Administrator user
    * Include directions for enforcing read-only permissions on output folder
    * Include directions for creating desktop shortcut
- [**Section 23 - Trusted Build & Output Hash Verification - Windows OS**](trusted_build_and_output_hash_verification.md)
    * Use .hash files for output summary file verification. Use different example path that doesn’t use user folders
- [**Section 24 - Tabulator Command Line Instructions**](tabulator_command_line_instructions.md)
    * Use different example path outside of user paths
- [**Section 26 - RCTab CVR Files**](rctab_cvr_files.md)
    * Include .sig.xml file description for required Hart CVR archive cryptographic signature
- [**Section 28 - Post-Election Audit & Clearing RCTab from System**](post-election_audit_and_clearing_rctab_from_system.md)
    * Include comparing the text of output file .hash files to the hash text in the audit log as another auditable check
- [**Section 29 - RCTab Operator Log Messages**](rctab_operator_log_messages.md)
    * Added additional v1.3.2 Severe messages

## RCTab Version

**Bug fixes:**

- Fixed XML parsing failing when running built version ([\#625](https://github.com/BrightSpots/rcv/issues/625))

**Backend updates:**

- Releases for all platforms are now automatically built by GitHub when published ([\#282](https://github.com/BrightSpots/rcv/issues/282))

## RCTab Version

**New features:**

- Added support for multi-file Dominion format ([\#569](https://github.com/BrightSpots/rcv/pull/569))
- Allows batch elimination and "continue until two candidates remain" to be enabled in multi-pass IRV mode ([\#611](https://github.com/BrightSpots/rcv/pull/611))
- Allows users to specify multiple CVR files at once in the GUI ([\#617](https://github.com/BrightSpots/rcv/pull/617))
- Adds validation highlighting to the GUI when clicking the "add" buttons for candidates and CVRs ([\#618](https://github.com/BrightSpots/rcv/pull/618))

- Changed audit logs to include validation outcome ([\#616](https://github.com/BrightSpots/rcv/pull/616))

###

**Bug fixes:**

- Fixed Hare Quota ([\#562](https://github.com/BrightSpots/rcv/pull/562))
- Fixed build for M1 Macbooks ([\#586](https://github.com/BrightSpots/rcv/pull/586))
- Fixed crashes when % was in file paths ([\#601](https://github.com/BrightSpots/rcv/pull/601))
- Fixed inaccurate overvoteRule error message ([\#609](https://github.com/BrightSpots/rcv/pull/609))
- Fixed bug in logic for exhaustIfMultipleContinuing overvote rule ([\#610](https://github.com/BrightSpots/rcv/pull/610))

- Fixed bug where treatBlankAsUndeclaredWriteIn validation failure for certain providers wouldn't actually fail validation ([\#618](https://github.com/BrightSpots/rcv/pull/618))

###

**Other improvements**

- Rebranded "Universal RCV Tabulator" as "RCTab" ([\#603](https://github.com/BrightSpots/rcv/pull/603))
- Updated license from AGPL to MPL 2.0 ([\#604](https://github.com/BrightSpots/rcv/pull/604))
- Exits gracefully if all declared candidates fall beneath minimum vote threshold ([\#608](https://github.com/BrightSpots/rcv/pull/608))
- Moved validation of provided overvote delimiter and overvote label into performBasicCvrSourceValidation so user is alerted when clicking the "add" button in the CVR tab ([\#618](https://github.com/BrightSpots/rcv/pull/618))
- Updated documentation and help text ([\#547](https://github.com/BrightSpots/rcv/pull/547), [\#614](https://github.com/BrightSpots/rcv/pull/614), [\#617](https://github.com/BrightSpots/rcv/pull/617))

**Backend updates:**

- Enabled CI, which runs tests, Checkstyle, and Spotbugs ([\#576](https://github.com/BrightSpots/rcv/pull/576))
- Addressed all outstanding Checkstyle and Spotbugs warnings ([\#587](https://github.com/BrightSpots/rcv/pull/587))
- Internal clean-up to conform to VVSG coding requirements ([\#600](https://github.com/BrightSpots/rcv/pull/600), [\#602](https://github.com/BrightSpots/rcv/pull/602), [\#606](https://github.com/BrightSpots/rcv/pull/606))
- Changed ContestConfig.validate() and associated methods to return a set of validation errors instead of an isValid boolean ([\#618](https://github.com/BrightSpots/rcv/pull/618))
- checkstyle-suppressions.xml location is now handled in build.gradle to avoid needing to manually modify google\_checks.xml in the future ([\#544](https://github.com/BrightSpots/rcv/pull/544))
- Updated dependencies to latest versions:
    * JDK 17.0.2
    * JavaFX 18
    * Gradle 7.5.1
    * Checkstyle google\_checks.xml 10.3.2
    * Checkstyle plugin 10.3.2
    * spotbugs 4.7.1
    * spotbugs-gradle-plugin 5.0.9
    * org.openjfx.javafxplugin 0.0.11
    * org.beryx.jlink 2.25.0
    * com.fasterxml.jackson.core:jackson-\* 2.13.3
    * org.junit.jupiter.junit-jupiter-\* 5.9.0
    * org.apache.commons:commons-csv 1.9.0
    * org.apache.poi:poi-ooxml 5.2.2

## Universal RCV Tabulator (RCTab) Version

**Certification:**
Based on the testing performed by Pro V&V, a certified Voting System Testing Laboratory, and  the results obtained, the modified RCV-Tabulator solution identified in this test report  meets the requirements set forth by the VVSG 1.0.

**New features:**
• Added support for new manufacturer formats:
    * Clear Ballot (\#400)
    * Dominion (\#119, \#438, \#533)
    * Hart (\#401, \#457, \#460)
    * Unisyn (\#402)
• Redesigned GUI to be more user-friendly (\#461, \#123, \#128, \#152) (see "GUI redesign"  section below for more details)

• Added support for "Overvote Delimiter" field (\#482)
• "Minimum Vote Threshold" field is now optional (\#483)
• "Undeclared Write-In Label", "Overvote Label", "Undervote Label", and "Treat Blank as  Undeclared Write-in" fields are now defined on a per-CVR level (\#508)

**GUI redesign:**
• Added hint panels for each tab (\#499)
• Added help menu option for the config documentation (\#497, \#528)
• Changed "Continue until Two Candidates Remain" to a boolean config setting (\#481)
• Combo text box / check box input for "How Many Consecutive Skipped Ranks Are  Allowed" and "Maximum Number of Candidates That Can Be Ranked" (\#498)
• Disabled "Decimal Places for Vote Arithmetic" in non-multi-seat modes (\#500)
• Redesigned nonIntegerWinningThreshold and hareQuota as a three-way radio button  and added new validation rules (\#501)

• Disabled editing existing candidates and CVR sources after adding to prevent confusing  UX (\#502)

• Added support for multiple contests via implementation of "Contest ID" field  (\#456, \#472, \#478)

**Additional GUI changes:**
• Split Output tab into new Contest Info and Output tabs
• Redesigned GUI CVR Files tab, adding Clear button, and changing Add button so it only
enter multiple sources that share fields clears the file path to make it easier to manually • Improved visual presentation of Candidate tab; added Clear button and adds checkBoxCandidateExcluded when adding a candidate

• Reorganized presentation of rules in "Winning Rules" and "Voter Error Rules" tabs

• Winner Election Mode and Tiebreak Mode now start undefined with all relevant fields  disabled; choosing specific modes enables applicable fields

• Changed Winner Election Modes and Tiebreak Modes to be more user-friendly,  including necessary migration logic to update older config files

• Expanded footprint of GUI window to 1200x1000
• Implemented bordered boxes
• Converted overvoteRule from a ChoiceBox to an array of RadioButtons;  changed overvoteRule string display in config files and adds migration logic
• Disabled decimalPlacesForVoteArithmetic and nonIntegerWinningThreshold except  when winnerElectionMode is "Multi-winner allow only one winner per round" or "Multi winner allow multiple winners per round" (fixes \#500)

• Added suggested values for overvoteLabel, undervoteLabel, and ES&S column and row  indices

• Replaced checkBoxNonIntegerWinningThreshold and checkBoxHareQuota with a radio  button array, and added new validation rules for those settings (fixing \#501)

• GUI now disables numberOfWinners field and sets it to 1 only

when winnerElectionMode is "Single-winner majority determines winner"
• GUI now disables numberOfWinners field and sets it to 0 when winnerElectionMode is  "Bottoms-up using percentage threshold"

• Fixed bugs in validation error messages when numberOfWinners is 0 **Bug fixes:**

• Fixes CDF JSON reading and writing (\#505)
• Fixed being unable to tabulate multiple CDF sources (\#536)
• Fixed user and computer name logging (\#521)
• Fixed config referencing nonexistent CDF source leading to uncaught exception (\#347) • Fixed incorrect overvote label in CDF leading to NPE (\#453)

• Fixed config file with bad provider value failing with NPE (\#531)
**Other improvements:**
• Removed "Convert Dominion to Generic Format..." functionality since direct Dominion  tabulation is now possible (\#476)

• Registers explicit overvote as valid candidate / contest selection in CDF output when  needed (\#451)

• Handles bad path to CDF CVR source gracefully (\#452)
• Handles empty rows at end of CVR (\#455)
• Made sure all providers work with the CLI (\#471)
• Raises error if we encounter an unrecognized candidate while loading Dominion CVRs  during direct tabulation (\#473)

• Reports error if config specifies any column indexes for a CDF source (\#276) **Backend updates:**

• Created separate MigrationHelper class (\#507)
• Addressed warnings during Gradle build (\#280)
• Upgrading to a more recent version of Gradle no longer causes test failures (\#283) • Addressed all relevant Checkstyle warnings and disabled all invalid ones (\#490, \#489) • Enum parameters now use camel case for backend and user-friendly strings for frontend  (\#494)

• Fixed noinspection unchecked for excluded CheckBox in GuiConfigController (\#304) • Now

use UnrecognizedCandidatesException in ClearBallotCvrReader and HartCvrReader (\#4 91)

• Updated dependencies to latest version:
    * JDK 14.0.1
    * JavaFX 14.0.1
    * Gradle 6.5.1
    * Checkstyle google\_checks.xml 8.36.2
    * Checkstyle plugin 8.36.2
    * org.openjfx.javafxplugin 0.0.9
    * org.beryx.jlink 2.20.0
    * com.fasterxml.jackson.core:jackson-\* 2.11.1
    * org.junit.jupiter.junit-jupiter-\* 5.6.2

## Universal RCV Tabulator (RCTab) Version

**Certification:**
Based on the testing performed by Pro V&V, a certified Voting System Testing Laboratory, and  the results obtained, the Universal RCV Tabulator v1.1.0 solution is believed to meet the  applicable requirements set forth by the EAC-approved VVSG 1.0.

**New features:**
• Added support for converting Dominion JSON CVRs to generic .csv format (including  precinct portions) (\#404, \#406, \#407, \#408, \#415, \#439)

• Added multiSeatBottomsUpPercentageThreshold option (\#403)
• Added CLI option to convert Dominion CVR to generic .csv (\#408)
• New GUI menu and conversion options (can now convert to CDF and convert Dominion  to generic via the GUI) (\#408, \#421)

• Added Dominion Alaska CVR to sample\_input folder
**Bug fixes:**
• Batch elimination now works properly with
singleSeatContinueUntilTwoCandidatesRemain (\#396)
• In a multi-seat contest, if someone wins in the first round, we now automatically  eliminate undeclared write-ins before we eliminate any other candidates; previously, we  treated UWIs like a normal candidate, which meant we potentially eliminated other  candidates with lower tallies first (\#397)

• If UWI exceeds the winning threshold in the initial count, we no longer mistakenly elect  this candidate (\#398)

**Backend updates:**
• Updated dependencies to latest version: JDK, JavaFX, Checkstyle google\_checks.xml,  Checkstyle plugin, org.openjfx.javafxplugin, org.beryx.jlink,

org.apache.commons:commons-csv, org.apache.poi:poi-ooxml,
com.fasterxml.jackson.core:jackson-\*
• Added special code to test configs to obviate the need to update the version with each  increment (\#426)

• Updated tests and improved test coverage
• Copyright update (\#414)
• Code cleanup

## Universal RCV Tabulator (RCTab) Version

Based on the testing performed by Pro V&V, a certified Voting System Testing Laboratory, and  the results obtained, the Universal RCV Tabulator solution meets the requirements set forth by  the EAC-approved VVSG 1.0 to be used with the ES&S EVS 5.0.0.0 through 6.0.4.0 software. Changelog:

• Added Checkstyle plugin to Gradle and set it up for Google format
• Minor refactoring to address Checkstyle issues
