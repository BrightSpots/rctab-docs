# Documentation Abstracts

**[Section 01 \- System Overview](system_overview.md)**

The System Overview provides a brief introduction to the RCTab software and its intended use cases.

**[Section 02 \- Software Design and Specifications](software_design_and_specifications.md)**

The Software Design and Specifications document describes RCTab coding standards, programming language, in-house software, third-party software, and software logic. It is designed to respond to CVSS 9.5. 

**[Section 03 \- System Hardware Specification](system_hardware_specification.md)**

The System Hardware Specification document describes potential hardware configurations on which the RCTab system can run. 

**[Section 04 \- System Functionality Description](system_functionality_description.md)**

The System Functionality Description describes suggested procedures for recovering from potential hardware or software failures when using an RCTab workstation. 

**[Section 05 \- Acceptance Test Procedures](acceptance_test_procedures.md)**

Acceptance Test Procedures verify that RCTab is correctly configured and operating properly on an RCTab workstation. Acceptance tests should always be conducted on a new install of RCTab prior to its use in an election. 

**[Section 06 \- System Design Specifications](system_design_specifications.md)**

System Design Specifications describe the configuration options available to users when installing the RCTab software and briefly describe voting and audit data retention requirements. 

**[Section 07 \- System Security Specification Requirements](system_security_specification_requirements.md)**

The System Security Specification Requirements describe processes and tools necessary to ensure access control, equipment and data security, software installation and security, air gap, event logging, physical security, setup inspection, cryptography, telecommunications, and other elements of an effective security program when deploying RCTab. 

**[Section 07I \- Design and Interface Specification](design_and_interface_specification.md)**

This document provides a high-level design of RCTab, discusses external interfaces, and identifies threats RCTab protects against.

**[Section 07J \- Security Architecture](security_architecture.md)**

This document provides an architecture level description of how the security requirements are met, and includes various authentication, access control, audit, confidentiality, integrity, and availability requirements.

**[Section 07K \- Development Environment Specification](development_environment_specification.md)**

This document describes the physical, personnel, procedural, and technical security of the development environment including version control, tools used, coding standards used, software engineering model used, and a description of developer and independent testing

**[Section 07L \- Security Threat Analysis](security_threat_analysis.md)**

This document identifies the threats the voting system protects against and the implemented security controls on voting system and system components.

**[Section 07M \- Security Testing and Vulnerability Analysis Documentation](security_testing_and_vulnerability_analysis.md)**

This document describes security tests performed to identify vulnerabilities and the results of the testing. This also includes testing performed as part of software development, such as unit, module, and subsystem testing.

**[Section 09 \- System Maintenance Manual](system_maintenance_manual.md)**

This section discusses the support needed to adjust or repair components of RCTab. RCTab leverages content from the jurisdictions voting system, all maintenance on equipment should be referred to your voting system vendor. All RCTab hardware is COTS and software other than RCTab are also COTS. 

**[Section 10 \- Personnel Deployment and Training](personnel_deployment_and_training.md)**

It is recommended that RCTab is used by at least two people in compliance with the jurisdictions’ guidelines for partisan participation. Personnel should generally have a basic knowledge of desktop applications with some additional skills required for testing. Training requirements vary between two to eight hours depending on the task. 

**[Section 11 \- L\&A Testing](l_and_a_testing.md)**

The Logic \& Accuracy Test document lays out an L\&A for RCTab that will allow jurisdictions to verify that RCTab is correctly configured and operating properly. 

**[Section 12 \- Configuration Management Plan](configuration_management_plan.md)**

The Configuration Management Plan describes RCTab’s development processes, how different versions of the software are managed, how to identify specific versions of the software, and provides details for functional and physical configuration audits of RCTab. 

**[Section 13 \- Quality Assurance Plan](quality_assurance_plan.md)**

This section describes the quality assurance plan used in RCTab development. It covers requirements, design process, and definition of RCTab software; determination of the specifications that a COTS device must meet in order to optimize RCTab installation and operation; process recommendations for centralization of CVR data prior to round-by-round counting; the validation and verification of the performance of RCTab; and validation and verification of the process for installation of RCTab on COTS hardware along with the necessary steps to secure the system as would be required in a jurisdiction.

**[Section 14 \- Tabulator Trusted Build Instructions](tabulator_trusted_build_instructions.md)**

This section explains how to create a trusted build of RCTab. It also provides a method for verifying whether the trusted build was successful.

**[Section 15 \- System Change Notes](system_change_notes.md)**

This section details the changes for each version of RCTab resulting from previous testing and certification. RCTab is currently used to produce official RCV results, as a testing tool, or as an auditing tool. The State of New York certified RCTab for use in single-winner RCV elections in the State, the State of Utah certified the RCTab for use in local RCV elections, and the State of Michigan certified RCTab for use in Eastpointe, Michigan’s RCV elections.

**[Section 16 \- System Hardening Procedures \- Windows OS](system_hardening_procedures_-_windows_os.md)**

The system hardening procedures describe the steps that should be taken to secure an RCTab workstation against various potential attacks on the system. It describes how to harden the OS, how to retrieve verifiable versions of software for use on the RCTab workstation, and procedures for locking down external ports on an RCTab workstation. 

**[Section 17 \- System Test and Verification Specification](system_test_and_verification_specification.md)**

The System Test and Verification Specification lays out all tests regularly conducted on the RCTab software and describes how to determine if a test of RCTab succeeds or fails. It also provides detailed information about each individual test condition used to test the software. 

**[Section 18 \- User Guide](user_guide.md)**

The User Guide provides a step-by-step guide for using RCTab. It walks users through launching the software, creating an RCTab configuration file, generating results files, and securing any results files.  

**[Section 19 \- Tabulation Options for RCV Tabulation](tabulation_options_for_rcv_tabulation.md)**

The Tabulation Options section is an enumeration and discussion of the various tabulation options that exist for Ranked Choice Voting (RCV) elections and how those options are or are not incorporated into RCTab. It also includes a glossary of ranked choice voting terms.

**[Section 20 \- Process Ranked Choice Voting Contest](process_ranked_choice_voting_contest.md)**

This section consists of an introduction, a flowchart, and a description of the flowchart laying out how RCV contests should be processed according to various rules in place in jurisdictions in the United States. 

**[Section 21 \- Ballot Limitations & Maximum Testing Range](ballot_limitations_and_maximum_testing_range.md)**

This document describes RCVRC’s understanding of the maximum ballot ranges possible when creating RCV data from different voting system vendors. 

**[Section 22 \- Installation Instructions for Windows OS](installation_instructions_for_windows_os.md)**

This document describes the Windows OS installation process for RCTab. 

**[Section 23 \- Trusted Build & HashCode Verification \- Windows OS](trusted_build_and_output_hash_verification.md)**

This document describes how to generate HashCodes when working on a Windows-based RCTab workstation. 

**[Section 24 \- Tabulator Command Line Instructions](tabulator_command_line_instructions.md)**

This document describes how to launch and operate RCTab from the command line. 

**[Section 25 \- Configuration File Parameters](configuration_file_parameters.md)**

This document describes all parameters included in configuration files in the RCTab software. 

**[Section 26 \- RCTab CVR Files](rctab_cvr_files.md)**

This document describes the different CVR files RCTab is compatible with. It documents how they are laid out and describes relevant file structures that inform how RCTab parses CVR data. 

**[Section 27 \- RCTab Config Files](rctab_config_files.md)**

This document provides an example of an RCTab configuration file. 

**[Section 28 \- Post-Election Audit & Clearing RCTab from System](post-election_audit_and_clearing_rctab_from_system.md)**

This document describes how to run a post-election tabulation audit and software audit of an RCTab installation. It also describes how to clear RCTab from a workstation if a fresh installation of RCTab is required. 

**[Section 29 \- RCTab Operator Log Messages](rctab_operator_log_messages.md)**

This section lays out all potential messages a user may receive through the RCTab operator log. It also suggests resolutions for any SEVERE errors that cause tabulation to fail. 

**[Section 30 \- RCTab System Tab Hints](rctab_system_tab_hints.md)**

This section recreates the Hints tab displayed to users in the RCTab UI. 

**[Section 31 \- Coding and Header Comment Standards for RCTab](coding_and_header_comment_standards_for_rctab.md)**

This section lays out the coding and header comment standards used in developing RCTab.

**[Section 32 \- Secure USB Process](secure_usb_process.md)**


This section outlines the details of how the RCVRC selects and secures a USB for use and transport to the requestee.


## Appendices

**[Appendix I \- Expected Outcome RCV Test Sets Multi-Winner](expected-outcome-rcv-test-sets-multi-winner.md)**

These tables lay out various tabulation conditions and expected outcomes in multi-winner RCV contests. They were used when developing the RCTab software to ensure different conditions were correctly handled by the software. 

**[Appendix II \- Expected Outcome RCV Test Sets Single-Winner](expected-outcome-rcv-test-sets-single-winner.md)**

These tables lay out various tabulation conditions and expected outcomes in single-winner RCV contests. They were used when developing the RCTab software to ensure different conditions were correctly handled by the software.

**[Appendix III \- Ranked Choice Voting Laws](ranked-choice-voting-laws.md)**

This spreadsheet lays out the RCV statutes and regulations that governed development of the RCTab software.

**[Appendix IV \- 22-Month Archiving Procedure](22-month-archiving-procedure.md)**

This document provides a procedure for archiving RCTab and any election results data from its use in elections. 
