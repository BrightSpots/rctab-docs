# Section 17 - System Test and Verification Specification

## 9.7 System Test and Verification Specification

The manufacturer shall provide test and verification specifications for: Development test specifications.

### 9.7.1 Development Test Specifications

1. The manufacturer shall describe the plans, procedures, and data used during software development and system integration to verify system logic correctness, data quality, and security.
1. This description shall include: Test identification and design, including:
    1. Test structure
    1. Test sequence or progression; and
    1. Test conditions

#### Test Structure

Included below is the basic template used to define every setting for each test set used to test RCTab. This form is filled out with the settings for the relevant test. Testers can compare the information in this form to the information in the configuration file loaded from the relevant folder in test\_data to ensure that all settings are correct. Each setting selected in this form has been tested. RCTab has not yet created a Test Structure Form for every RCTab test but will set up a form for all RCTab regression tests based on this form. Questions about this form can be made to the Ranked Choice Voting Resource Center at info@rcvresources.org or by calling 1-833-868-3728. We also have included an example Test Structure Form filled out according to the requirements of the Portland 2015 Mayor test.

#### Regression Test Overview

We have developed a suite of 68 Tabulation Regression Tests and continue to add more tests as new features and bug fixes are added. These are designed to verify that various aspects of Tabulator functionality behave as expected. They also verify that new code changes do not inadvertently alter Tabulator behavior. The entire test suite must be run, and all tests must pass before any new code changes can be merged into the main Tabulator repository.

#### Design Overview

Each test contains a set of normal tabulation inputs (config file and cvr files) and a known valid "expected" results summary file. The test runs a tabulation with new code, and compares the results of that tabulation to previous, expected, correct results. In essence, we isolate and analyze the effects any new code changes may have on the tabulation output. This is a classic regression test design.

#### Test Execution Details


The test suite will run through all tests automatically as follows:

1. Tabulator is built from source code.
1. For each test:
    1. Run a tabulation using the test config file and cvr files.
    1. Compare tabulation output summary file to reference expected summary file.
    1. If the files match exactly (except for timestamps) the test passes.
    1. If the files do not match the test fails.
    1. Test execution and test results are written to a log file and console.

#### Test Conditions

Test conditions require the following files for input for each test case:  Configuration file (JSON), Cast Vote Record (typically CSV format). Confirm appropriate files are uploaded to proceed with appropriate testing conditions.

For more information on the development process as it relates to testing see [**Section 13 - Quality Assurance Plan**](quality_assurance_plan.md).

1. Standard test procedures, including any assumptions or constraints

#### Testing Procedures

When new code is ready for submission, a developer will follow these procedures to ensure the code is safe for incorporation:

1. Run test suite:  in a console, from the rcv root directory, enter:  *./gradlew.bat test*
1. Observe the test output. If *any* test fails the source of the failure must be identified and either:
    1. Fixed. Usually, a test failure is caused by a bug in logic or data which can be fixed.
    1. Update the reference test asset.  Sometimes bug fixes cause tests to fail because they are now operating correctly.  In these cases, test output must be manually verified and peer-reviewed (like any code change) before it can be updated.

Example test outputs are included in: TabulatorTests_example_console_output.txt and Test_Results_TabulatorTests.html

For actual test data, including configuration files and expected results, see: [github.com/BrightSpots/rcv/tree/master/src/test/resources/network/brightspots/rcv/test\_data](https://github.com/BrightSpots/rcv/tree/master/src/test/resources/network/brightspots/rcv/test\_data). To download the data, go to this page: [https://github.com/BrightSpots/rcv/tree/v1.3.2](https://github.com/BrightSpots/rcv/tree/hotfix/1.3.2). This is the location on GitHub where version 1.3.2 of the RCTab source code is hosted. Click on “Code” and select “Download ZIP.” Once the ZIP is downloaded, extract it. Navigate to the unzipped folder and navigate to src/test/resources/network/brightspots/rcv/test_data. All test data files will be included in this folder.

Users can also manually run each test. The steps required to run tests manually are as follows:

1. Open RCTab
1. Click “File”
1. Click “Load”
1. Navigate to the configuration file for the test you wish to run
1. Select the configuration file and load it into RCTab
1. Confirm that the configuration file properly loaded into RCTab by checking that the relevant fields are filled in
1. Click “Tabulation”
1. Click “Tabulate”
1. Wait for RCTab to finish tabulating
1. Navigate to the output location for your results
1. Compare your results .json summary file to the .json summary file included with the data. If this matches exactly, the test passes.

#### Additional Testing Procedures

In addition to regression testing of all changes, new features are tested by developers and RCVRC staff to ensure that they work as expected. If any features did not work as expected, a ticket was filed on GitHub with the test data and an explanation of how the achieved results differed from the expected results.

The RCVRC and Bright Spots also conduct scale tests of the RCTab. Tests include a contest with 100 CVR files composed of 100,000 individual cast vote records each, a contest with 1,000 CVR files composed of 1,000,000 individual cast vote records each, a contest with 6,000 CVR files composed of 6,000,000 individual cast vote records each, and a set of 11 CVRs composed of 9,200,000 individual cast vote records each. Volume tests with these records were conducted throughout March and April 2021.

1. Special purpose test procedures including any assumptions or constraints;

No special-purpose test procedures are followed.

1. Test data, test data source, whether it is real or simulated, and how test data are controlled;

#### Test Data

The data for 2017 Minneapolis Mayor, 2013 Minneapolis Mayor, 2013 Minneapolis Park, 2018 Maine Governor Democratic Primary are all from real-world elections and were procured directly from the websites of the jurisdictions listed in the name of the data. All other data was manufactured by Bright Spots developers, RCVRC staff, voting system vendors, or election jurisdictions. Any data with vendor names included (Unisyn, Clear Ballot, Dominion, Hart, CDF) was procured from vendors directly or from jurisdictions working with those vendors. Any data not falling in those categories was manufactured by RCTab developers according to the CVR requirements of the software to test specific functionalities of the RCTab software.

Regression test data are controlled by hosting them on GitHub and updating tests as new features are added to RCTab. Other test data, for tests run by RCVRC staff, Bright Spots developers, or others, did not previously have clear controls on data. Data was procured from trusted sources, such as actual election jurisdictions and voting system vendors, as much as possible or generated according to the specifications of previously used CVR data from vendors. However, no formal controls were in place for test data or for tracking results. Results were communicated via the relevant issue(s) on GitHub. We are implementing formal control methods for tests and test data going forward.

1. Expected test results;

Expected results for regression tests are included in the test folders available in the test_data.zip that includes all test data and was submitted with documentation.

1. Criteria for evaluating test results.

The names of the tests are mostly self-explanatory. For example, *test\_set\_1\_exhaust\_at\_overvote* tests whether the tabulator correctly interprets the overvoteRule \= "exhaust immediately" setting.  Some of the tests aren't testing specific features but instead are testing a known data set, e.g., *2018\_maine\_governor\_primary*.  The complete list is included below.

Results from any tests run on regression test data should 100% match the expected results in each individual test’s folder on GitHub. Note that test folders include only .json summary result files, while tests run by users will produce .json summary results, .csv summary results, and .log audit log files. The .json summary results should therefore be compared when evaluating test results.

In tests run by RCVRC staff and Bright Spots developers when incorporating new features, any features were tested according to requirements as laid out in RCV laws or regulations being incorporated into RCTab.

### 9.7.2 Test Specifications

The manufacturer shall provide specifications for verification and validation of overall software performance. These specifications shall cover:

1. Control and data input/output;

- Data input:  Data used in RCTab should come directly from the user jurisdiction certified voting system.  When exporting the data from the certified voting system the users should adhere to all export procedures as outlined by the voting system vendor.
- Data output:  Data created via RCTab should be created using the guidelines and procedures outlined in [**Section 18 - User Guide**](user_guide.md).


1. Acceptance criteria;

- Tests in the set of regression tests are designed to test one or more functionalities of RCTab. When each test is performed, the results of the test will reveal whether RCTab meets the functionality described in the TDP. Information about how each functionality of RCTab is intended to function is provided in [**Section 02 - Software Design and Specifications**](software_design_and_specifications.md) and [**Section 18 - User Guide**](user_guide.md).


1. Processing accuracy;

- All functions tested must produce a result that matches the expected results. Matching results means a test passed this requirement. Processing accuracy procedures are outlined in [**Section 18 - User Guide**](user_guide.md).

1. These specifications shall cover: Data quality assessment and maintenance;

- Data quality is tested by ensuring that data used in RCTab comes directly from the user jurisdiction certified voting system and by producing expected results for a test before running a test itself. Once a test is run, results should be inspected to confirm that they match the expected outcome. Data should be maintained on secure drives or secured computers/networks, as required by the user jurisdiction.


1. Ballot interpretation logic;

- Regression tests can be used to test ballot interpretation logic. All CVR data will include discrete and clearly defined values for how each ranking on an RCV ballot was used. Ballot interpretation via RCTab relies upon the candidate names, winning election rules, and voter error rules a user specifies in a configuration file. If the produced results match the expected results, then a test passed the ballot interpretation logic requirement.

1.  Exception handling;

- The invalid\_params\_test and invalid\_sources\_test can be used to test exception handling in RCTab. When run through RCTab these tests will cause RCTab to produce errors in the operator log box at the bottom of the user interface. If those errors shown match those in the below screenshot, the test was successful.

![][image19]

1. Security;

- RCTab has no tests specifically designed to test security. RCTab relies on a jurisdiction’s security policies, as laid out in [**Section 06 - System Design Specifications**](system_design_specifications.md). Security can be maintained by ensuring that all security procedures follow the requirements set out in [**Section 06 - System Design Specifications**](system_design_specifications.md).


1. Production of audit trails and statistical data.

- Regression tests will produce .log audit files and will log general information about the contest tabulation to the operator .log file. Production of these files can be tested using any regression test files, so long as the user activates the “Tabulate” function. All tests that produce a successful tabulation will also create .csv summary results files and .json summary results files. If these .log files are generated and updated, and .csv and .json summary files are produced when RCTab successfully completes a tabulation, then this requirement passes.

The specifications shall identify procedures for assessing and demonstrating the suitability of the software for election use.

- For additional user jurisdiction testing specifications, please see [**Section 05 - Acceptance Test Procedures**](acceptance_test_procedures.md) and [**Section 11 - L&A Testing**](l_and_a_testing.md) to review manufacturer procedures to ensure the user jurisdiction has received and is using the correct trusted build for the state of California.
- [**Section 18 - User Guide**](user_guide.md) also includes a detailed guide to expected user operation of RCTab, which can be used to create tests of the user interface, tabulation functionalities, and other functionalities of RCTab software. The manufacturer is available to support development of additional tests.

## RCTab Test Structure Form

| RCTab Test Structure Form |  |  |  |  |  |  |  |
| ----- | :---- | :---- | :---- | :---- | :---- | ----- | :---- |
| This form is the basic template used to define every test setting for each test set used to test RCTab. This form is filled out with the settings for the \[TEST NAME\]. Testers can compare the information in this form to the information in the configuration file loaded from the relevant folder in test\_data to ensure that all settings are correct. Each setting selected in this form is a setting tested by this test. RCTab has not yet created a Test Structure Form for every RCTab test, but will set up a form for all RCTab regression tests based on this form. Questions about this form can be made to the Ranked Choice Voting Resource Center at info@rcvresources.org or by calling 1-833-868-3728. |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Contest Info** |  |  |  |  |  |  |  |
| Contest Name\*: |  |  |  |  |  | Contest Date: |  |
| Contest Jurisdiction: |  |  |  |  |  | Contest Office: |  |
| Rules Description: |  |  |  |  |  |  |  |
| **CVR Files** |  |  |  |  |  |  |  |
| Provider\*: |  |  |  |  | *Enter Vendor (ES\&S, Hart, etc.)* |  |  |
| File Path\*: |  |  |  |  | *Location of the cvr export file.* |  |  |
| First Vote Column Index\*: |  |  |  |  | *Enter the Column where the First Vote is in the CVR export file.* |  |  |
| First Vote Row Index\*: |  |  |  |  | *Enter the Row where the First Vote is in the CVR export file.* |  |  |
| ID Column Index: |  |  |  |  | *Enter the ID Column (if being used)* |  |  |
| Precinct Column Index: |  |  |  |  | *Enter the Precinct Column in the CVR export file.* |  |  |
| Overvote Label |  |  |  |  |  |  |  |
| Undervote Label |  |  |  |  |  |  |  |
| Undeclared Write-In Label |  |  |  |  | *User will define.  Must match case and spelling with CVR*  |  |  |
| Treat Blank as Undeclared WI |  |  |  |  | *Circle One* |  |  |
| **Candidates** |  |  |  |  |  |  |  |
| Name\*: |  |  | *Obtain a list of candidates from the EMS System (Attach the list of candidates to this form)* |  |  |  |  |
| Code: |  |  | *Enter the Code for each candidate (if being used) example: DDE*  |  |  |  |  |
| Excluded: |  |  | *Check box if a candidate is not being counted in this tabulation* |  |  |  |  |
| **Winning Rules** |  |  |  |  |  |  |  |
| Winner Election Mode\* |  |  |  |  |  | Any user jurisdiction guidelines which identify the specific rules for ranked choice voting elections should be attached to this form for easy reference. Please see the RCTab User Guide for more information about the available selections that can be made. |  |
| Maximum \# of Ranked Candidates\* |  |  |  |  |  |  |  |
| Minimum Vote Threshold |  |  |  |  |  |  |  |
| Use Batch Elimination |  |  |  |   Y   N (Circle One) |  |  |  |
| Continue until Two Candidates Remain |  |  |  |   Y   N (Circle One) |  |  |  |
| Tiebreak Mode\* |  |  |  |  |  |  |  |
| Random Seed\* |  |  |  |  |  | Any user jurisdiction guidelines which identify the specific rules for ranked choice voting elections should be attached to this form for easy reference. Please see the RCTab User Guide for more information about the available selections that can be made. |  |
| Number of Winners\* |  |  |  |  |  |  |  |
| Percentage Threshold\* |  |  |  |  |  |  |  |
| Threshold Calculation Method\* |  |  |  |  |  |  |  |
| Most Common Threshold |  |  |  |  |  |  |  |
| HB Quota |  |  |  |  |  |  |  |
| Hare Quota‡ |  |  |  |  |  |  |  |
| Decimal Places for Vote Arith (MW ONLY)\* |  |  |  |  |  |  |  |
| **Voter Error Rules** |  |  |  |  |  |  |  |
| Overvote Rule\* |  |  |  |  |  | Choose one of the three available options. |  |
| Skip to next rank |  |  |  |  |  |  |  |
| Exhaust Immediately |  |  |  |  |  |  |  |
| Exhaust if mult. cont. |  |  |  |  |  |  |  |
| Consecutive Skip Ranks Allowed |  |  |  |  |  | Enter the number of consecutive skipped rankings or check Unlimited if permitted. |  |
| Exhaust on multi ranks for same candidate |  |  |  |   Y N (Circle One) |  | Check if multiple ranks for the same candidate are not permitted. |  |
| **Output** |  |  |  |  |  |  |  |
| Output Directory (where should results file go on PC?): |  |  |  |  |  |  |  |
| Tabulate by Precinct: |  |  |  |   Y      N     (Circle One) |  | Generate CDF JSON: |   Y N (Circle One) |
| Configuration File Name: |  |  |  |  |  |  |  |
| Date of Test: |  |  |  |  | Passed?:   YES   NO |  |  |
| Name of tester(s) |  |  |  |  |  |  |  |
| Name 1 |  |  |  |  | Name 2 |  |  |
|  |  |  |  |  |  |  |  |
| ‡Disclaimer: The Hare Quota tabulation option in the RCTab software has not been thoroughly tested in a controlled testing lab environment. Do not attempt to implement this option without first testing in a non-operational environment. Please contact the Ranked Choice Voting Resource Center for additional information. |  |  |  |  |  |  |  |

## RCTab Test Structure Form Example:

| RCTab Test Structure Form |  |  |  |  |  |  |  |
| ----- | :---- | ----- | :---- | ----- | :---- | ----- | ----- |
| This form is the basic template used to define every test setting for each test set used to test the RCTab. This form is filled out with the settings for the 2015 Portland Mayor test. Testers can compare the information in this form to the information in the configuration file loaded from the relevant folder in test\_data to ensure that all settings are correct. Each setting selected in this form is a setting tested by this test. RCTab has not yet created a Test Structure Form for every RCTab test, but will set up a form for all RCTab regression tests based on this form. Questions about this form can be made to the Ranked Choice Voting Resource Center at info@rcvresources.org or by calling 1-833-868-3728. |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Contest Info** |  |  |  |  |  |  |  |
| Contest Name\*: |  |  |  | Portland 2015 Mayoral Race |  | Contest Date: | 2015-11-03 |
| Contest Jurisdiction: |  |  |  | Portland, ME |  | Contest Office: | Portland, ME |
| Rules Description: |  |  |  |  |  |  |  |
| **CVR Files** |  |  |  |  |  |  |  |
| Provider\*: |  | ES\&S |  |  | *Enter Vendor (ES\&S, etc.)* |  |  |
| File Path\*: |  | 2015\_portland\_mayor\_cvr.xlsx |  |  | *Location of the cvr export file.* |  |  |
| First Vote Column Index\*: |  | 4 |  |  | *Enter the Column where the First Vote is in the CVR export file.* |  |  |
| First Vote Row Index\*: |  | 2 |  |  | *Enter the Row where the First Vote is in the CVR export file.* |  |  |
| ID Column Index: |  | Leave blank |  |  | *Enter the ID Column (if being used)* |  |  |
| Precinct Column Index: |  | 2 |  |  | *Enter the Precinct Column in the CVR export file.* |  |  |
| Overvote Label |  | overvote |  |  | *ES\&S will default to “overvote”* |  |  |
| Undervote Label |  | undervote |  |  | *ES\&S will default to “undervote”* |  |  |
| Undeclared Write-In Label |  | UWI |  |  | *User will define.  Must match case and spelling with CVR*  |  |  |
| Treat Blank as Undeclared WI |  | FALSE |  |  | *Circle One* |  |  |
| **Candidates** |  |  |  |  |  |  |  |
| Name\*: | See below for a list of candidates. |  | *Obtain a list of candidates from the EMS System (Attach the list of candidates to this form)* |  |  |  |  |
| Code: |  |  | *Enter the Code for each candidate (if being used) example: DDE*  |  |  |  |  |
| Excluded: |  |  | *Check box if a candidate is not being counted in this tabulation* |  |  |  |  |
| **Winning Rules** |  |  |  |  |  |  |  |
| Winner Election Mode\* |  |  |  | singleWinnerMajority |  | Any user jurisdiction guidelines which identify the specific rules for ranked choice voting elections should be attached to this form for easy reference. Please see the RCTab User Guide for more information about the available selections that can be made. |  |
| Maximum \# of Ranked Candidates\* |  |  |  | 15 |  |  |  |
| Minimum Vote Threshold |  |  |  | 0 |  |  |  |
| Use Batch Elimination |  |  |  |   **Y**      N     (Circle One) |  |  |  |
| Continue until Two Candidates Remain |  |  |  |   Y      **N**     (Circle One) |  |  |  |
| Tiebreak Mode\* |  |  |  | useCandidateOrder |  |  |  |
| Random Seed\* |  |  |  | N/A |  | Any user jurisdiction guidelines which identify the specific rules for ranked choice voting elections should be attached to this form for easy reference. Please see the RCTab User Guide for more information about the available selections that can be made. |  |
| Number of Winners\* |  |  |  | 1 |  |  |  |
| Percentage Threshold\* |  |  |  | N/A |  |  |  |
| Threshold Calculation Method\* |  |  |  | N/A |  |  |  |
| Most Common Threshold |  |  |  | N/A |  |  |  |
| HB Quota |  |  |  | N/A |  |  |  |
| Hare Quota‡ |  |  |  | N/A |  |  |  |
| Decimal Places for Vote Arith (MW ONLY)\* |  |  |  | N/A |  |  |  |
| **Voter Error Rules** |  |  |  |  |  |  |  |
| Overvote Rule\* |  |  |  | Exhaust Immediately |  | Choose one of the three available options. |  |
| Skip to next rank |  |  |  | - |  |  |  |
| Exhaust Immediately |  |  |  | X |  |  |  |
| Exhaust if mult. cont. |  |  |  | - |  |  |  |
| Consecutive Skip Ranks Allowed |  |  |  | 1 |  | Enter the number of consecutive skipped rankings or check Unlimited if permitted. |  |
| Exhaust on multi ranks for same candidate |  |  |  |   Y      **N**     (Circle One) |  | Check if multiple ranks for the same candidate are not permitted. |  |
| **Output** |  |  |  |  |  |  |  |
| Output Directory (where should results file go on PC?): output |  |  |  |  |  |  |  |
| Tabulate by Precinct: |  |  |  |   Y      **N**     (Circle One) |  | Generate CDF JSON: |   Y      **N**     (Circle One) |
| Configuration File Name: 2015\_portland\_mayor\_config.json |  |  |  |  |  |  |  |
| Date of Test: |  |  |  |  | Passed?:   YES   NO |  |  |
| Name of tester(s) |  |  |  |  |  |  |  |
| Name 1 |  |  |  |  | Name 2 |  |  |
| ‡Disclaimer: The Hare Quota tabulation option in the RCTab software has not been thoroughly tested in a controlled testing lab environment. Do not attempt to implement this option without first testing in a non-operational environment. Please contact the Ranked Choice Voting Resource Center for additional information. |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| Candidates | Brennan, Michael F. |  |  |  |  |  |  |
|  | Bragdon, Charles E. |  |  |  |  |  |  |
|  | Bryant, Peter G. |  |  |  |  |  |  |
|  | Carmona, Ralph C. |  |  |  |  |  |  |
|  | Dodge, Richard A. |  |  |  |  |  |  |
|  | Duson, Jill C. |  |  |  |  |  |  |
|  | Eder, John M. |  |  |  |  |  |  |
|  | Haadoow, Hamza A. |  |  |  |  |  |  |
|  | Lapchick, Jodie L. |  |  |  |  |  |  |
|  | Marshall, David A. |  |  |  |  |  |  |
|  | Mavodones, Nicholas M. Jr. |  |  |  |  |  |  |
|  | Miller, Markos S. |  |  |  |  |  |  |
|  | Rathband, Jed |  |  |  |  |  |  |
|  | Strimling, Ethan K. |  |  |  |  |  |  |
|  | Vail, Christopher L. |  |  |  |  |  |  |

## List of Tabulator Tests

| Name of Test | Name of Test Folder | Description of test | Purpose of Test |
| :---- | :---- | :---- | :---- |
| RCVRC & Bright Spots name for regression test | [Test folder name in:](https://github.com/BrightSpots/rcv/tree/master/src/test/resources/network/brightspots/rcv/test\_data) Refer to test\_data.zip that includes all test data and was submitted with documentation.   | Brief description of test and identification of RCTab functionalities tested by test files. | Unless otherwise noted, each regression test can be used to test control and data input/output, acceptance criteria, processing accuracy, ballot interpretation logic, and production of audit trails and statistical data. Processes for exporting and handling data, under control and data input, should also follow CVR handling procedures in a jurisdiction. Security processes should be tested according to the requirements in 06 - System Security Specifications. Exception handling tests are directly identified below. |
| 2013 Minneapolis Mayor | 2013\_minneapolis\_mayor | Test the ability of RCTab to read and process ES\&S CVR files and CVR settings usable with ES\&S CVR files. Test RCTab's ability to properly count real-life RCV elections. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| 2013 Minneapolis Mayor Scale | 2013\_minneapolis\_mayor\_scale | Tests the ability of RCTab to process a contest with 1,000,000 records. Test the ability of RCTab to read and process ES\&S CVR files and CVR settings usable with ES\&S CVR files. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| 2013 Minneapolis Park | 2013\_minneapolis\_park | Test the ability of RCTab to read and process ES\&S CVR files and CVR settings usable with ES\&S CVR files. Test the functionality of the "multi-winner allow multiple winners per round" functionality. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| test bottoms-up multi-seat logic | 2013\_minneapolis\_park\_bottoms\_up | Test the functionality of the bottoms-up winner election mode setting. Test the ability of RCTab to read and process ES\&S CVR files and CVR settings usable with ES\&S CVR files. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| 2017 Minneapolis Park | 2017\_minneapolis\_park | Test the ability of RCTab to read and process ES\&S CVR files and CVR settings usable with ES\&S CVR files. Test the functionality of the "multi-winner allow multiple winners per round" functionality. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| test Hare quota | 2013\_minneapolis\_park\_hare | Test the functionality of the Hare Quota Threshold Calculation Mode setting. Note that while RCTab passes this test the Hare Quota functionality has been updated but requires additional testing. Test the functionality of the "multi-winner allow multiple winners per round" functionality. Test the ability of RCTab to read and process ES\&S CVR files and CVR settings usable with ES\&S CVR files. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| test sequential multi-seat logic | 2013\_minneapolis\_park\_sequential | Test the functionality of the multi-pass IRV winner election mode setting. Test the ability of RCTab to read and process ES\&S CVR files and CVR settings usable with ES\&S CVR files. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| 2015 Portland Mayor | 2015\_portland\_mayor | Test the ability of RCTab to read and process ES\&S CVR files and CVR settings usable with ES\&S CVR files. Test ability to process a single-winner RCV contest. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| 2015 Portland Mayor Candidate Codes | 2015\_portland\_mayor\_codes | Test the ability of RCTab to read and process ES\&S CVR files and CVR settings usable with ES\&S CVR files; ability to process a single-winner RCV contest; ability to process a CVR using Candidate Codes instead of Candidate Names | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| 2017 Minneapolis Mayor | 2017\_minneapolis\_mayor | Test the ability of RCTab to read and process ES\&S CVR files and CVR settings usable with ES\&S CVR files, as well as RCTab's ability to properly count real-life RCV elections. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| 2018 Maine Governor Democratic Primary | 2018\_maine\_governor\_primary | Test the ability of RCTab to read and process ES\&S CVR files and CVR settings usable with ES\&S CVR files, as well as RCTab's ability to properly count real-life RCV elections. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| Clear Ballot - Kansas Primary | clear\_ballot\_kansas\_primary | Tests the ability of RCTab to read and process Clear Ballot CVR data | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| Continue Until Two Candidates Remain | continue\_tabulation\_test | Tests the ability of RCTab to properly count a single-winner contest down to two final candidates | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| Continue Until Two Candidates Remain with Batch Elimination | continue\_until\_two\_with\_batch\_elimination\_test | Tests the ability of RCTab to count a single-winner contest using both batch elimination and continue until two candidates remain settings simultaneously. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| Dominion test - Alaska test data | dominion\_alaska | Tests the ability of RCTab to read and process Dominion CVR data and to run an RCV count on that data. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| Dominion test - Kansas test data | dominion\_kansas | Tests the ability of RCTab to read and process Dominion CVR data and to run an RCV count on that data. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| Dominion - Multi-File | dominion\_multi\_file | Tests the ability of RCTab to read and process Dominion CVR data spread across multiple CVR files and to run an RCV count on that data.  | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| Dominion - No Precinct Data | dominion\_no\_precinct\_data | Tests the ability of RCTab to read and process Dominion CVR data and to run an RCV count on that data. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| Dominion test - Wyoming test data | dominion\_wyoming | Tests the ability of RCTab to read and process Dominion CVR data and to run an RCV count on that data. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| test inactivating ballot after encountering duplicate ranking of same candidate | duplicate\_test | Tests the ability of RCTab to properly detect and inactivate a ballot due to the same candidate being ranked multiple times on that ballot.  | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| test excluding candidates in config file | excluded\_test | Test the "Exclude" function in the Candidate settings of RCTab. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| Hart - Cedar Park School Board | hart\_cedar\_park\_school\_board | Tests the ability of RCTab to read and process Hart CVR data | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| Hart - Travis County Officers | hart\_travis\_county\_officers | Tests the ability of RCTab to read and process Hart CVR data | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| test invalid params in config file | invalid\_params\_test | Tests the ability of RCTab show errors if a configuration file is incomplete or improperly filled out. | Exception handling |
| test invalid source files | invalid\_sources\_test | Tests the ability of RCTab to show errors if CVR files are incompatible | Exception handling |
| test minimum vote threshold setting | minimum\_threshold\_test | Test the "minimum vote threshold" setting in winner election mode. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| testMinneapolisMultiSeatThreshold | minneapolis\_multi\_seat\_threshold | Test the ability of RCTab to determine winning candidates according to the default Threshold Calculation method in multi-winner elections. Test the functionality of the "multi-winner allow multiple winners per round" functionality. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| missing precinct example | missing\_precinct\_example | Test the ability of RCTab to continue tabulating if "Precinct Column ID" is supplied but precinct information is missing in part of a CVR file. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| test bottoms-up multi-seat with threshold logic | multi\_seat\_bottoms\_up\_with\_threshold | Test the functionality of the bottoms-up using percentage threshold winner election mode setting. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| multi-seat UWI test | multi\_seat\_uwi\_test | Undeclared write-ins should not win elections. This test ensures that RCTab properly handles this exception by not awarding a win to an undeclared write-in candidate in a multi-winner contest. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| NIST XML CDF 2 | nist\_xml\_cdf\_2 | Tests the ability of RCTab to read and process CDF data in XML format | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| No candidates meet minimum vote threshold | no\_candidates\_meet\_minimum | Tests the ability of RCTab to provide an accurate error message if all candidates fall below the value set in the Minimum Vote Threshold field.  | Exception handling.  |
| precinct example | precinct\_example | Test the ability of RCTab to detect precinct information based on CVR file data and the ability to produce precinct results using the Tabulate by Precinct functionality. Note that Tabulate by Precinct function produces precinct-level results of the RCV contest but does not identify precinct-level winners. This functionality needs updating to identify in-precinct winners. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| sample interactive tiebreak | sample\_interactive\_tiebreak | Test the functionality of the interactive tiebreak function available in "Stop counting and ask," or "Previous round counts (then stop counting and ask)" tiebreaking modes. This is not a regression test as it requires user input. It is included in the "sample\_input" folder of RCTab installation folder as an additional test of RCTab. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| Sequential with batch | sequential\_with\_batch | Tests the ability of RCTab to properly batch eliminate candidates in a multi-pass IRV tabulation scenario.  |  |
| Sequential with continue until two | sequential\_with\_continue\_until\_two | Tests the ability of RCTab to eliminate down to the final two candidates in a multi-pass IRV tabulation scenario.  |  |
| test skipping to next candidate after overvote | skip\_to\_next\_test | Test the functionality of the "Always skip to next rank" overvote setting. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| skipped first choice | test\_set\_0\_skipped\_first\_choice | Test the ability of RCTab to properly process CVR data with a skipped first ranking. Test the ability of RCTab to export CVR data in the CDF. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| exhaust at overvote rule | test\_set\_1\_exhaust\_at\_overvote | Test the functionality of the "Exhaust immediately" overvote setting. Test the ability of RCTab to export CVR data in the CDF. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| overvote skips to next rank | test\_set\_2\_overvote\_skip\_to\_next | Test the functionality of the "Always skip to next rank" overvote setting. Test the ability of RCTab to export CVR data in the CDF. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| skipped choice exhausts option | test\_set\_3\_skipped\_choice\_exhaust | Test the functionality of the "how many consecutive skipped ranks are allowed" setting when ballots exhaust after a single skipped ranking. Test the ability of RCTab to export CVR data in the CDF. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| skipped choice next option | test\_set\_4\_skipped\_choice\_next | Test the functionality of the "how many consecutive skipped ranks are allowed" setting when ballots don't exhaust after skipped rankings. Test the ability of RCTab to export CVR data in the CDF. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| two skipped ranks exhausts option | test\_set\_5\_two\_skipped\_choice\_exhaust | Test the functionality of the "how many consecutive skipped ranks are allowed" setting when ballots exhaust after multiple skipped rankings. Test the ability of RCTab to export CVR data in the CDF. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| duplicate rank exhausts | test\_set\_6\_duplicate\_exhaust | Test the functionality of the "Exhaust on multiple ranks for the same candidate" function, if function is turned on - ballots should exhaust when a duplicate ranking is encountered. Test the ability of RCTab to export CVR data in the CDF. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| duplicate rank skips to next option | test\_set\_7\_duplicate\_skip\_to\_next | Test the functionality of the "Exhaust on multiple ranks for the same candidate" function, if function is turned off - RCTab will ignore duplicate candidate rankings. Test the ability of RCTab to export CVR data in the CDF. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| multi-cdf tabulation | test\_set\_8\_multi\_cdf | Tests the ability of RCTab to read and process multiple CDF data files in XML format. Test the ability of RCTab to export CVR data in the CDF. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| test allow only one winner per round logic | test\_set\_allow\_only\_one\_winner\_per\_round | Test the functionality of the multi-winner allow only one winner per round logic. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| multi-seat fractional number threshold | test\_set\_multi\_winner\_fractional\_threshold | Test the functionality of the HB Quota Threshold Calculation Mode setting. Test the ability of RCTab to export CVR data in the CDF. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| multi-seat whole number threshold | test\_set\_multi\_winner\_whole\_threshold | Test the functionality of the default Threshold Calculation Mode setting. Test the ability of RCTab to export CVR data in the CDF. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| overvote delimiter test | test\_set\_overvote\_delimiter | Test the functionality of the "overvote delimiter" setting.  | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| treat blank as undeclared write-in | test\_set\_treat\_blank\_as\_undeclared\_write\_in | Test the functionality of the "Treat Blank as Undeclared Write-In" setting for CVRs. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| tiebreak using generated permutation | tiebreak\_generate\_permutation\_test | Test the functionality of the "Generate permutation" tiebreak setting. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| tiebreak using previousRoundCountsThenRandom | tiebreak\_previous\_round\_counts\_then\_random\_test | Test the functionality of the "Previous Round Counts then Random" tiebreak setting. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| test tiebreak seed | tiebreak\_seed\_test | Test the functionality of the "random seed" setting required for any of the Random Tiebreak modes ("Random" "Previous Round Counts then Random" and "Generate Permutation") | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| tiebreak using permutation in config | tiebreak\_use\_permutation\_in\_config | Test the functionality of the "Use candidate order in config file" tiebreak setting. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| unisyn\_xml\_cdf\_city\_chief\_of\_police | unisyn\_xml\_cdf\_city\_chief\_of\_police | Tests the ability of RCTab to read and process CDF data in XML format | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| unisyn\_xml\_cdf\_city\_coroner | unisyn\_xml\_cdf\_city\_coroner | Tests the ability of RCTab to read and process CDF data in XML format | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| unisyn\_xml\_cdf\_city\_council\_member | unisyn\_xml\_cdf\_city\_council\_member | Tests the ability of RCTab to read and process CDF data in XML format | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| unisyn\_xml\_cdf\_city\_mayor | unisyn\_xml\_cdf\_city\_mayor | Tests the ability of RCTab to read and process CDF data in XML format | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| unisyn\_xml\_cdf\_city\_tax\_collector | unisyn\_xml\_cdf\_city\_tax\_collector | Tests the ability of RCTab to read and process CDF data in XML format | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| unisyn\_xml\_cdf\_county\_coroner | unisyn\_xml\_cdf\_county\_coroner | Tests the ability of RCTab to read and process CDF data in XML format | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| unisyn\_xml\_cdf\_county\_sheriff | unisyn\_xml\_cdf\_county\_sheriff | Tests the ability of RCTab to read and process CDF data in XML format | Control and data input/output; Processing accuracy; Ballot interpretation logic; |
| undeclared write-in (UWI) cannot win test | uwi\_cannot\_win\_test | Undeclared write-ins (UWIs) cannot win elections in RCTab tabulation. This test ensures that RCTab properly handles this exception by not awarding a win to an undeclared write-in candidate in a single-winner contest. | Control and data input/output; Processing accuracy; Ballot interpretation logic; |

## List of Security Tests

| Name of Test | Description of test | Purpose of Test |
| :---- | :---- | :---- |
| RCVRC & Bright Spots name for regression test | Brief description of test and identification of RCTab functionalities tested by test files. | Unless otherwise noted, each regression test can be used to test control and data input/output, acceptance criteria, processing accuracy, ballot interpretation logic, and production of audit trails and statistical data. Processes for exporting and handling data, under control and data input, should also follow CVR handling procedures in a jurisdiction. Security processes should be tested according to the requirements in 06 - System Security Specifications. Exception handling tests are directly identified below. |
| Succeeds using the default, valid files | Tests that properly signed Hart CVRs succeed cryptographic validation | Ensuring cryptographic validation of signed Hart CVRs is implemented correctly |
| Verification fails when the signature is incorrect | When the cryptographic signature of the Hart CVR is incorrect, confirm that it successfully throws an exception | Ensuring cryptographic validation of signed Hart CVRs is implemented correctly  |
| Exception is thrown when the data file is modified | Confirms that if the signed Hart CVR file itself is modified that signature validation should fail | Ensuring cryptographic validation of signed Hart CVRs is implemented correctly  |
| Succeeds when data file is in a different folder (but has the right filename) | Hart includes a path in the data that is signed. Since CVRs will be moved from their original location to the RCTab machine, we make sure that this doesn’t affect signature verification. | Ensuring cryptographic validation of signed Hart CVRs is implemented correctly |
| Exception is thrown when the filenames differ | Though files can move, we require that file names stay the same. | Ensuring cryptographic validation of signed Hart CVRs is implemented correctly |
| Exception is thrown when the file is signed with an unsupported key | When the public key is not a valid public key, ensure that signature verification fails | Ensuring cryptographic validation of signed Hart CVRs is implemented correctly |
| Ensure FIPS Compliance check is run | Tests that Java Security Providers are properly setup to ensure FIPS compliance | Ensuring cryptographic validation of signed Hart CVRs is implemented correctly |
