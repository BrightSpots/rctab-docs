# Section 13 - Quality Assurance Plan
Content for Quality Assurance Plan.

# Section 13 - Quality Assurance Plan

## Scope

This document outlines the general Quality Assurance processes and procedures of the RCTab counting software.

The RCTab software is designed for use as a round-by-round counting software and installed on COTS equipment after centralization of the cast vote record data. Centralization of data occurs based on the policies, procedures, and laws of the jurisdiction using the counting software. This software is designed specifically for use in ranked choice voting elections.

The software is simple to install and utilize with proper training of election officials. From the earliest concept of this product, RCTab was designed to provide confidence and accuracy in the round-by-round count of any jurisdiction. The software is designed for election official input based on jurisdiction RCV rules. The software uses CVR data exports from election tabulation equipment.

### Items Covered in the Scope

- Requirements, design process, and definition of RCTab software.
- Determination of the specifications that a COTS device must meet in order to optimize RCTab installation and operation.
- The process recommendations for centralization of CVR data prior to round-by-round counting.
- The validation and verification of the performance of RCTab.
- Validation and verification of the process for installation of RCTab on COTS hardware along with the necessary steps to secure the system as would be required in a jurisdiction.

## Requirements, Design Process, and Definition of RCTab Software

### Requirements

###

RCTab is tabulation software that is designed to use voting system data (such as the Cast Vote Record (CVR) from a tabulation system) to run a round-by-round tabulation of a ranked choice voting contest. The software must be installed on a computer configured according to the specifications listed in [**Section 03 - System Hardware Specification**](system_hardware_specification.md).

The computer must be a standalone computer that is not connected to an internet connection or a network of any kind. Wireless connection must be disabled if available on the computer. All industry standard security configurations must be set up and any security policies must be followed, included but not limited to: computer hardening and installation of a recommended antivirus software. For additional information, see documentation listed below.

### Description of Parts and Materials Necessary for RCTab Use: (V.2: 2.12.2--Description)

Trusted build of RCTab to be acquired from the Ranked Choice Voting Resource Center or State Agency.

COTS computer that is not connected to the internet and is configured according to all

specifications laid out in the following documents:

- [**Section 03 - System Hardware Specification**](system_hardware_specification.md)
- [**Section 07 - System Security Specification Requirements**](system_security_specification_requirements.md)
- [**Section 12 - Configuration Management Plan**](configuration_management_plan.md)
- [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md)

- Battery backup is also recommended if the facility does not have a generator. This is not required to run the software.

### Ensuring Proper Functionality of the Parts and Materials

- The parts were chosen in the following manner in accordance with VVSG Volume 2: 2:12.1 as it refers to Volume 1:8.5 and Volume 1:8.6.
    * RCTab software--the voting tabulation product. (See below for all testing information regarding the product.)
    * COTS hardware was chosen as an industry standard for a Windows machine. All set up should refer to the documentation listed above. RCVRC does not design, manufacture, or resale any hardware.
- Test data storage process has been updated to meet the specifications outlined in the VVSG Volume 1:8.5c

## Design Process

The RCTab software is developed with the following tools, policies, and practices to ensure robust software quality and reliability. RCTab testing relates only to the function of the software and performs no parts and materials testing as we produce only software and do not design or manufacture hardware. Testing follows standards laid out in the VVSG Volume 2:2.12.1 with regard to V1:8.5.

[**Section 04 - System Functionality Description**](system_functionality_description.md) incorporates general functional requirements for the tabulation software system. Requirements for accuracy were taken into account when designing and performing all testing including stress tests. The VVSG 2.0 requirements with regard to accuracy were also utilized when designing and performing stress tests. V2:2.12.1 also refers to V1:8.5, V1:8.6 and V1:8.7 and were followed throughout the process. Regression testing is completed for each design change or addition, whether minor or major. For additional information about testing, refer to [**Section 17 - System Test and Verification Specification**](system_test_and_verification_specification.md).

### Design, Testing, and QA Process Responsibilities

The design process and QA assessments are performed by a joint team that includes the developers from Bright Spots and software team from EARC/RCVRC. Project managers may be used on a contract basis to manage QA responsibilities such as testing.

### Documentation of Quality Conformance Procedures

The RCTab development team uses a ticketing system to identify bugs as well as design issues. All procedures below reflect this process and are managed through the Resource Center and Bright Spots using GitHub. See also [**Section 12 - Configuration Management Plan**](configuration_management_plan.md) to understand the process more fully.

### QA Processes and Procedures

*1. Version Control Software:*
We use Git version control software (git-scm.com) in conjunction with Github (github.com/BrightSpots/rcv) to coordinate the efforts of our developers and maintain a complete record of ALL software code changes to the RCTab and the reasoning behind them.

*2. Software Revision Control Branching Policy:*
To isolate code in development from production code (released), we use Git-Flow: a branching policy built on top of Git. The policy coordinates development, testing, review, and deployment of code throughout the development life-cycle. Details can be found here: (www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

*3. Code reviews:*
All code changes submitted for incorporation into the RCTab software must undergo a manual code review from at least one developer other than the original drafter/developer. Other stakeholders and experts are involved with code reviews as needed. Code reviews offer an additional opportunity to identify potential defects, improve code structure, clarity, performance, and robustness. Code merges are blocked until at least one developer explicitly approves the code submission, at which point the code is merged, and regression tests will be run. For code review examples, see: github.com/BrightSpots/rcv/pulls.

*4. Regression Tests:*

See [**Section 17 - System Test and Verification Specification**](system_test_and_verification_specification.md) for detailed information on the 68 RCTab regression tests.

### Quality Conformance Inspections and Documentation

*1. System Requirements Testing:*
Minimum system requirements were determined by repeated tabulation of elections with 100,000 CVRs, 1,000,000 CVRs, and 6,000,000 CVRs on each target platform. These tests were timed to ensure they complete in a reasonable amount of time successfully.

*2. Ad-hoc user testing:*
When developing new features, we try to recruit as much user feedback and user testing as possible. These testers are typically from the RCVRC staff, manufacturer partners, election administrators, and RCV activists.

*3. Process for Handling of deficiencies:*
Any defects discovered through testing or reported by users are recorded and tracked using Github issue tracking tools. We confirm the existence of the defect, evaluate its severity, and mark it accordingly. Depending on user impact, development resources, and release timelines, we schedule developers to address the defects in order of priority and then do the actual work. Typically, this involves:

1. reproducing the defect
1. making necessary code changes to fix the defect on an isolated git branch 3\) requesting a code review and implementing any changes arising from the code review 4\) verifying that regression tests pass
1. pushing the code change to the main branch and linking the issue in the commit message
1. closing the issue and linking to the commit in Github issue tracker

In this way, we are able to ensure that all known issues are tracked, and the most important ones are mitigated according to criticality. For more details, see:

https://github.com/BrightSpots/rcv/issues.

### Testing Documentation

The full suite of programmatic tests that are run with every update to RCTab are located in [**Section 17 - System Test and Verification Specification**](system_test_and_verification_specification.md).

### Product Documentation

All documentation in this submission is named according to the formula:
\[System Version\]\[Document/Section Number\] - \[Document Name\] \[Document version\]
System Version: RCTab v1.3.2

Document version: 1.0.0
Example: [Section 13 - Quality Assurance Plan](quality_assurance_plan.md)

RCTab provides documentation in order to meet the VVSG standards outlined in Volume 2, Section 2, Description of the Technical Data Package. Refer to this reference list of documentation for more information:

- [**Section 01 - System Overview**](system_overview.md)
- [**Section 02 - Software Design and Specifications**](software_design_and_specifications.md)
- **[Section 03 - System Hardware Specification**](system_hardware_specification.md)
- [**Section 04 - System Functionality Description**](system_functionality_description.md)
- [**Section 07 - System Security Specification Requirements**](system_security_specification_requirements.md)
- [**Section 09 - System Maintenance Manual** ](system_maintenance_manual.md)
- [**Section 10 - Personnel Deployment and Training**](personnel_deployment_and_training.md)
- [**Section 12 - Configuration Management Plan**](configuration_management_plan.md)
- [**Section 13 - Quality Assurance Plan**](quality_assurance_plan.md)
- [**Section 15 - System Change Notes**](system_change_notes.md)
- [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md)
- [**Section 17 - System Test and Verification Specification**](system_test_and_verification_specification.md)
- [**Section 18 - User Guide**](user_guide.md)
