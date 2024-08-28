# Section 07 - System Security Specification Requirements

## 9.6.1 Access Control

1. Manufacturers shall provide user and TDP documentation of access control capabilities of the voting system.

    * [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md) enumerates steps for creating a ‘RCTab’ Windows Standard user account on the RCTab machine. Installation instructions for RCTab in [**Section 22 - Installation Instructions for Windows OS**](installation_instructions_for_windows_os.md) describe how to set up and run the RCTab software using the ‘RCTab’ user account which has the absolute minimum permissions necessary. Following these instructions ensures the following:
        + RCTab users cannot edit or delete RCTab summary output files or audit logs.
        + RCTab users cannot edit or delete corresponding `.hash` files that can be used to verify the contents of all output files and audit logs.

2. Manufacturers shall provide descriptions and specifications of all access control mechanisms of the voting system including management capabilities of authentication, authorization, and passwords in the TDP.

    * Access to RCTab should be at minimum made by no less than two employees within the user jurisdiction. These employees should have received the suggested training time provided by the manufacturer before accessing the software. See [**Section 10 - Personnel Deployment and Training**](personnel_deployment_and_training.md) for more.
    * [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md) enumerates steps for creating two Windows OS Accounts. One Administrator level Windows account for installation and initial configuration. A separate ‘RCTab’ Windows Standard user account with only necessary permissions that will not have access to make administrative changes to the machine that could be security issues.
    
        Installation instructions for RCTab in [**Section 22 - Installation Instructions for Windows OS**](installation_instructions_for_windows_os.md) describe how to properly run RCTab with minimum permissions necessary - being logged into the Windows OS as the ‘RCTab’ Windows standard user while using Window’s ‘Run As’ capability to run the RCTab software **only** with Administrator privileges.
    
        This ensures that RCTab has the privileges necessary to ensure security (like setting output files to read-only) while simultaneously preventing the logged in human user from inheriting any of the same privileges or having any extra privileges not necessary for running a Tabulation.

    * [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md) describe setting a hardware BIOS password to protect the system BIOS settings from tampering. This locks down attempts to boot from unauthorized devices and prevents system configuration settings from being changed at a BIOS level.

3. Manufacturers shall provide descriptions and specifications of methods to prevent unauthorized access to the access control mechanisms of the voting system in the TDP.

    * Access to RCTab should be at minimum made by no less than two employees within the user jurisdiction. These employees should have received the suggested training time provided by the manufacturer before accessing the software. See [**Section 10 - Personnel Deployment and Training**](personnel_deployment_and_training.md) for more.
    * Access to the desktop or laptop should require password entry from the initial operating system for all users assigned to operate RCTab. Instructions in [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md)  and [**Section 22 - Installation Instructions for Windows OS**](installation_instructions_for_windows_os.md) provide all necessary steps so that RCTab users have the minimum permissions necessary to run and verify a contest tabulation.
    * Jurisdictions shall restrict access to Windows Admin account and BIOS password to the minimum number of users necessary for initial setup. Election officials running the tabulation shall not have access to the Windows Admin account.

4. Manufacturers shall provide descriptions and specifications of all other voting system mechanisms that are dependent upon, support, and interface with access controls in the TDP.

    * RCTab is hosted on a separate, standalone tabulation workstation. Users can bring flash drives holding cast vote record (CVR) data to and from the RCTab workstation to produce RCV results and bring RCV results back into the main voting system.

        The RCTab workstation does not directly interface, control, or support any other functions of the voting system.

5. Manufacturers shall provide a list of all of the operations possible on the voting system and list the default roles that have permission to perform each such operation as part of the TDP.

    * After installation and set up following the instructions in [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md) and [**Section 22 - Installation Instructions for Windows OS**](installation_instructions_for_windows_os.md) the only operations possible on an RCTab workstation are RCTab rules configuration, production of round-by-round RCV results, review of CVR data when setting up rules, review of audit logs and other event logs, and read-only review of round-by-round results after tabulation completes. All features are available to users once they have logged into the RCTab workstation.

### 9.6.1.1 General Access Control Policy

The manufacturer shall specify the features and capabilities of the access control policy recommended to purchasing jurisdictions to provide effective voting system security. The access control policy shall address the general features and capabilities and individual access privileges.

- Access to RCTab should be at minimum made by no less than two employees within the user jurisdiction. These employees should have received the suggested training time provided by the manufacturer before accessing the software. See [**Section 10 - Personnel Deployment and Training**](personnel_deployment_and_training.md) for more.
- Access to the desktop or laptop must require password entry from the initial operating system for all users assigned to operate RCTab. See [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md) document for more information.
- Installation instructions for RCTab in [**Section 22 - Installation Instructions for Windows OS**](installation_instructions_for_windows_os.md) describe how to set up and run the RCTab software using the ‘RCTab’ Windows standard user account which has the absolute minimum permissions necessary to operate the software. Following these instructions ensures the following
    * RCTab users cannot edit or delete RCTab summary output files or audit logs.
    * RCTab users cannot edit or delete corresponding `.hash` files that can be used to verify the contents of all output files and audit logs.
- Employees accessing the software should be provided a paper log tracking for the purposes of establishing a recorded access record. The log should require the name of the personnel accessing the system, purpose of access, and the start and end times.  This log should be maintained as part of the official election record and for as long as the user jurisdiction is required to maintain records per their controlling records retention schedule.
- The RCTab software provides full capabilities and access upon start-up and the manufacturer recommends not less than two user employees access the system simultaneously to prevent incorrect, accidental or on purpose, use of the features to tabulate ranked choice voting results.

#### Suggested Software, Hardware, and Personnel Access Controls

1. Suggested software access controls

    * After successful completion of the steps to harden Windows OS and workstation hardware in [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md) and steps to install the RCTab software in [**Section 22 - Installation Instructions for Windows OS RCTab**](installation_instructions_for_windows_os.md) the following software access controls apply to RCTab
        + RCTab users cannot edit or delete RCTab summary output files or audit logs.
        + RCTab users cannot edit or delete corresponding `.hash` files that can be used to verify the contents of all output files and audit logs.
        + RCTab software will automatically, programmatically verify the cryptographic signature of the Hart CVRs used as input. If unable to verify, the software will not begin tabulation.
    
    * The RCTab software employs a single user level, and the user has access to the capabilities of the software described in the [**Section 25 - Configuration File Parameters**](configuration_file_parameters.md) document and described by [**Section 18 - User Guide**](user_guide.md). The manufacturer recommends that at least two users visually observe the software during use.
    * Access to RCTab should be at minimum no less than 2 employees within the user jurisdiction. These employees should have received the suggested training time provided by the manufacturer before accessing the software.  See [**Section 10 - Personnel Deployment and Training**](personnel_deployment_and_training.md).

2. Suggested hardware access controls
    * Maintaining proper physical security to all computers is absolutely essential. When the equipment is in use, no less than two properly trained and trusted election officials should be present in the room with the equipment at all times. When the equipment is not being used (for instance, between elections), the computer and any backup hardware should be kept in a locked room, and entry to that room should be restricted and logged.

3. Suggested communications controls
    * [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md) requires users to turn off all networking features on hardware. No RCTab installed computer should ever run with its Wi-Fi enabled. No RCTab computer should ever be connected to any public network. For software installation, files should be captured to a USB flash drive using only secure methods. See also [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md)

4. Suggestions for effective password management.
    * Access to the desktop or laptop should require password entry from the initial operating system for all users assigned to operate RCTab. Any additional user jurisdiction security requirements should also be maintained when accessing any user jurisdiction owned equipment.

5. Suggestions for protection abilities of a particular operating system
    * The user jurisdiction is fully responsible for maintaining owned hardware in keeping with universal maintenance and security standards including all updates and security patches for the operating system in use. See also [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md) and [**Section 09 - System Maintenance Manual**](system_maintenance_manual.md).
    * Following the instructions in [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md) and [**Section 22 - Installation Instructions for Windows OS RCTab**](installation_instructions_for_windows_os.md) enables the following protection abilities for the Windows Operating system
        + Sets up an RCTab Windows standard user account with minimum permissions required to run RCTab
        + Restricts OS folder permissions on the RCTab output folder to read only
        + Enables Windows OS drive encryption
        + Disables all OS-level network connections

6. Suggested general characteristics of supervisory access privileges

    * Access to RCTab should be at minimum no less than 2 employees within the user jurisdiction. These employees should have received the suggested training time provided by the manufacturer before accessing the software.  See [**Section 10 - Personnel Deployment and Training**](personnel_deployment_and_training.md)
    * The user jurisdiction is fully responsible for assigning access to the software and procuring the suggested training (see [**Section 10 - Personnel Deployment and Training**](personnel_deployment_and_training.md)) for those employees.
    * The user jurisdiction is also responsible for creating and maintaining a segregation of duties plan and a backup plan where there will be no less than two employees identified in the event that assigned personnel are unable to fulfill their assigned roles.

7. Suggested policies for segregation of duties
    * Access to RCTab should be at minimum no less than 2 employees within the user jurisdiction. These employees should have received the suggested training time provided by the manufacturer before accessing the software.  See [**Section 10 - Personnel Deployment and Training**](personnel_deployment_and_training.md).
    * The user jurisdiction is fully responsible for assigning access to the software and procuring the suggested training (see [**Section 10 - Personnel Deployment and Training**](personnel_deployment_and_training.md)) for those employees.
    * The user jurisdiction is also responsible for creating and maintaining a segregation of duties plan and a backup plan where there will be no less than two employees identified in the event that assigned personnel are unable to fulfill their assigned roles.

8. Suggestions for any additional relevant characteristics
    * There are no additional relevant characteristics associated with RCTab.

### 9.6.1.2 Access Control Measures

The manufacturer shall provide a detailed description of all system access control measures and mandatory procedures designed to permit access to system states in accordance with the access policy, and to prevent all other types of access to meet the specific requirements.

- RCTab uses two Windows OS accounts. The first is a Windows Administrator level account. Steps for its creation are described in [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md). RCTab shall be installed and initial configuration done by an election administrator with access to this account. [**Section 22 - Installation Instructions for Windows OS**](installation_instructions_for_windows_os.md) describes steps for the creation of a ‘RCTab’ Windows standard account. This new account does not have OS administrative privileges. Running a tabulation will be done only with the ‘RCTab’ standard user account. This ensures that once installation and initial configuration is complete, RCTab users will have minimum OS privileges necessary to run a tabulation and will not have access to make administrative changes to the machine that could be security issues. Election officials running the tabulation shall not have access to the Windows Admin account. The Windows Admin account credentials should be shared with the fewest number of users necessary to complete installation and initial configuration.
- Access to RCTab should be a minimum of two employees within the user jurisdiction. These employees should have received the suggested training time provided by the manufacturer before accessing the software. See [**Section 10 - Personnel Deployment and Training**](personnel_deployment_and_training.md).

#### Additional Suggested Access Control Measures

1. Suggested measures for use of data and user authorization
    * Access to RCTab should be limited to no less than 2 employees within the user jurisdiction.
    * Upon startup, the software provides capabilities as described in [**Section 25 - Configuration File Parameters**](configuration_file_parameters.md) and [**Section 18 - User Guide**](user_guide.md). The manufacturer recommends that at least two users visually observe the software during use simultaneously to prevent incorrect, accidental or on purpose, use of the features to tabulate ranked choice voting results.
    * Access to RCTab should only be permitted during pre-election logic & accuracy testing and post-election tabulation of ranked choice voting results from the voting system generated cast vote records (CVR).

2. Suggested measures for program unit ownership and other regional boundaries
    * The user jurisdiction is fully responsible for assigning access to the software and procuring the suggested training (see [**Section 10 - Personnel Deployment and Training**](personnel_deployment_and_training.md)) for those employees.
    * The user jurisdiction is also responsible for creating and maintaining a backup plan in the event that assigned personnel are unable to fulfill their assigned roles.

3. Suggested measures for one-end or two-end port protection devices
    * RCTab software does not use any one-end or two-end port encryption devices.

4. Suggested measures for security kernels
    * RCTab software does not use security kernels.

5. Suggested measures for Computer-generated password keys
    * RCTab software does not use computer-generated password keys.

6. Suggested measures for special protocols
    * RCTab software does not require special protocols as data does not transmit in or out via a web-based system.
    * The manufacturer does recommend a dedicated USB flash drive and backup be secured with the hardware and used for no other purpose than software use.

7. Suggested measures for message encryption
    * RCTab does not require message encryption as data does not transmit in or out via a web-based system.

8. Suggested measures for controlled access security
    * RCTab access takes place at a single central-count location. The software and hardware resides at this location. All election personnel are present at this location.
    * Physical access to the site is controlled by policy and procedures under control of the jurisdiction.
    * Physical access to the system hardware is controlled by policy and procedures under control of the jurisdiction.
    * At no time should the hardware with installed software be connected to the internet via WiFi or ethernet.
    * The user jurisdiction is fully responsible for assigning access to the software and procuring the suggested training (see [**Section 10 - Personnel Deployment and Training**](personnel_deployment_and_training.md)) for those employees.
    * The user jurisdiction is also responsible for creating and maintaining a backup plan in the event that assigned personnel are unable to fulfill their assigned roles.

## 9.6.2 Equipment and Data Security

The manufacturer shall provide a detailed description of system capabilities and mandatory procedures for purchasing jurisdictions to prevent disruption of the voting process and corruption of voting data to meet the specific requirements. This information shall address measures for polling place security and central count location security.

- Access to RCTab should only be permitted during pre-election logic & accuracy testing and post-election tabulation of ranked choice voting results from the voting system generated cast vote records (CVR). RCTab should not be deployed in polling places. If the RCTab workstation is deployed and in use in a central count location, no less than two properly trained and trusted election officials should be present in the room with the equipment at all times. When the equipment is not being used (for instance, between elections), the computer and any backup hardware should be kept in a locked room, and entry to that room should be restricted and logged.
- Transportation of CVR data from the voting system to the RCTab workstation should follow jurisdiction procedures for handling election data. Any results data produced by RCTab should be secured following jurisdiction procedures.
- After successful completion of the steps in [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md) and [**Section 22 - Installation Instructions for Windows OS RCTab**](installation_instructions_for_windows_os.md) RCTab contains the following capabilities to prevent corruption of voting data
    * RCTab users cannot edit or delete RCTab summary output files or audit logs.
    * RCTab users cannot edit or delete corresponding `.hash` files that can be used to verify the contents of all output files and audit logs.
    * RCTab software will automatically, programmatically verify the cryptographic signature of the Hart CVRs used as input. If unable to verify, the software will not begin tabulation.

## 9.6.3 Software Installation and Security

1. The manufacturer shall provide a detailed description of the system capabilities and mandatory procedures for purchasing jurisdictions to ensure secure software (including firmware) installation to meet specific requirements. This information shall address software installation for all system components.
    * User jurisdictions should install RCTab on a workstation configured according to the requirements laid out in [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md).
    * RCTab installation should follow the steps laid out in [**Section 22 - Installation Instructions for Windows OS**](installation_instructions_for_windows_os.md) and [**Section 05 - Acceptance Test Procedures**](acceptance_test_procedures.md).

2. Manufacturers shall provide a list of all software related to the voting system in the technical data package (TDP).
    * Software that must be installed on RCTab system:
        + Windows 10 Pro, or above
        + RCTab v1.3.2
        + LibreOffice
        + XML Notepad
        + Users must also retain access to:
            - Command Prompt
            - Notepad
        + Optional UPS
        + See also [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md).
    * No other software is necessary for user operation of RCTab.

3. Manufacturers shall provide at a minimum in the TDP the following information for each piece of software related to the voting system: software product name, software version number, software manufacturer name, software manufacturer contact information, type of software (application logic, border logic, third party logic, COTS software, or installation software), list of software documentation, component identifier(s) (such as filename(s)) of the software, type of software component (executable code, source code, or data).
    * Documentation, manufacturer name, product name, version, certification application number of voting system, and file names and paths are all referred to with unique labels in documentation and in the system itself. See also [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md) and [**Section 13 - Quality Assurance Plan**](quality_assurance_plan.md) document for information about version numbers and documentation numbers.

4. As part of the TDP, manufacturers shall provide the location (such as full path name or memory address) and storage device (such as type and part number of storage device) where each piece of software is installed on the voting system.
    * RCTab does not require election specific programming to be created or installed. See also [**Section 22 - Installation Instructions for Windows OS**](installation_instructions_for_windows_os.md) and [**Section 18 - User Guide**](user_guide.md).

5. As part of the TDP, manufacturers shall document the functionality provided to the voting system by the installed software.
    * All RCTab functionality is described in [**Section 02 - Software Design and Specifications**](software_design_and_specifications.md), and [**Section 18 - User Guide**](user_guide.md).

6. As part of the TDP, manufacturers shall map the dependencies and interactions between software installed on the voting system.
    * RCTab is designed to operate as a standalone piece of software on a tabulation workstation. RCTab is dependent upon the CVRs from the configured voting systems as input. RCTab does not depend on or interface with any other software installed on a voting system.
    * Depending on the needs of user jurisdictions, users may use LibreOffice or NotePad to inspect CVRs when generating RCTab configuration files and may depend on Windows PowerShell or the Command Line to produce hash codes using the procedures in [**Section 23 - HashCode Instructions - Windows OS**](trusted_build_and_output_hash_verification.md).
    * There are no interactions between software installed on the system.

7. The manufacturer shall provide a detailed description of the system capabilities and mandatory procedures for purchasing jurisdictions used to provide protection against threats to third party products and services.
    * Third party products and services installed on RCTab workstations should be configured according to the steps laid out in [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md).


### 9.6.3.1 Air Gap

The TDP for the voting system shall provide full procedures and instructions, to be incorporated into the Official Use Procedures for the voting system, to implement the segregated dual-installation architecture. Those procedures and instructions shall:

1. Require elections officials to use the permanent installation to lay out the ballot, define the election, and program all of the memory cards, including any DRE, ballot marking device, optical scan unit, etc.
    * RCTab is not used to lay out ballots, define elections, or program memory cards.

2. Require elections officials to write a backup of the election database from the permanent installation onto write-once media (e. g., CD-R or DVD-R), carry the media by hand to the sacrificial installation, and install that database onto the sacrificial installation. After this point, the permanent installation shall not be used for the remainder of the election.
    * RCTab is not used to set up election databases.

3. Require that, after the close of the polls, memory cards or other equipment containing votes returned from polling locations are uploaded to the sacrificial installation (not the permanent installation).
    * RCTab does not interface directly with memory cards or other equipment after its return from polling locations.

4. Require that the sacrificial installation, not the permanent installation, is used to accumulate and tabulate election results, produce reports, and calculate the official election results.
    * RCTab only interacts with cast vote records from sacrificial installations. It should therefore be used as part of any sacrificial installation.

5. Require that the "sacrificial" installation is treated as presumed-to-be-infected, so any machine or equipment that is ever connected to the sacrificial installation must never again be connected to the permanent installation.
    * Results created by RCTab shall never be connected back to any permanent installation.

6. Ensure that any media that has been connected to the sacrificial installation is securely erased or reformatted before being used with the permanent installation.
    * Any media connected to RCTab shall be erased or reformatted if it will be used with a permanent installation.

## 9.6.4 System Event Logging

1. Manufacturers shall provide TDP documentation of event logging capabilities of the voting devices.

    * RCTab produces audit logs and tabulator operator logs. Logging capabilities are described in the RCTab Logging section of [**Section 02 - Software Design and Specifications**](software_design_and_specifications.md) and [**Section 29 - RCTab Operator Log Messages**](rctab_operator_log_messages.md)
    * Windows OS also logs all events on the OS. Those event logs are available via the Windows Event Log application.

2. Manufacturers shall provide a technical data package that describes system event logging design and implementation.
    * RCTab produces audit logs and tabulator operator logs. Log design and implementation are described in the RCTab Logging section of [**Section 02 - Software Design and Specifications**](software_design_and_specifications.md). Detailed documentation describing how to read and make use of these logs is provided in [**Section 28 - Post-Election Audit & Clearing RCTab from System**](post-election_audit_and_clearing_rctab_from_system.md).

3. The technical data package shall provide the location (i.e. full path name or memory address) where each log is saved.
    * RCTab saves event logs according to user settings as described in the RCTab logging section of [**Section 02 - Software Design and Specifications**](software_design_and_specifications.md) and the Generating Results Files section of [**Section 18 - User Guide**](user_guide.md).

## 9.6.5 Physical Security

1. Manufacturers shall provide a list of all voting system components to which access must be restricted and a description of the function of each said component.
    - Maintaining proper physical security to all computers is absolutely essential. All RCTab workstations should have restricted physical access. When the RCTab workstation is in use, no less than two properly trained and trusted election officials should be present in the room with the equipment at all times. When the equipment is not being used (for instance, between elections), the computer and any backup hardware should be kept in a locked room, and entry to that room should be restricted and logged.

2. As part of the TDP, manufacturers shall provide a listing of all ports and access points of the voting system.
    - Any RCTab workstation will have a varying set of ports depending upon the laptop or desktop on which RCTab is installed. Users must physically seal all external ports on hardware where RCTab is installed, except ports used for power supply, necessary external displays, and one (1) USB port. The user jurisdiction should employ a policy where the use of tamper evident and tamper resistant seals are used to identify ports that should never be accessed, unlikely to be accessed, and can be accessed if necessary.

3. For each physical lock used on a voting system, manufacturers shall document whether the lock was installed to secure an access point.
    - Any RCTab workstation will have a varying set of ports depending upon the laptop or desktop on which RCTab is installed. Users must physically seal all external ports on hardware where RCTab is installed, except ports used for power supply, necessary external displays, and one (1) USB port. The user jurisdiction should employ a policy where the use of tamper evident and tamper resistant seals are used to identify ports that should never be accessed, unlikely to be accessed, and can be accessed if necessary.

4. Manufacturers shall provide a list of all physical security countermeasures that require power supplies.
    - No RCTab physical security countermeasures require power supplies.

5. Manufacturers shall provide a technical data package that documents the design and implementation of all physical security controls for the voting system.
    - Physical security controls and design are discussed in this section.

## 9.6.6 Setup Inspection

1. Manufacturers shall provide the technical specifications of how voting systems identify installed software in the TDP.
    - RCTab relies on hash codes to verify that the correct version of the software has been installed. See [**Section 05 - Acceptance Test Procedures**](acceptance_test_procedures.md), [**Section 22 - Installation Instructions for Windows OS**](installation_instructions_for_windows_os.md) and [**Section 23 - HashCode Instructions - Windows OS**](trusted_build_and_output_hash_verification.md) for details.

2. Manufacturers shall provide a technical specification of how the integrity of software installed on the voting system is verified as part of the TDP. Software integrity verification techniques used to support the integrity verification of software installed on voting systems need to be able to detect the modification of software.
    - RCTab relies on hash codes to verify that the correct version of the software has been installed. See [**Section 05 - Acceptance Test Procedures**](acceptance_test_procedures.md), [**Section 22 - Installation Instructions for Windows OS**](installation_instructions_for_windows_os.md), and [**Section 23 - HashCode Instructions - Windows OS**](trusted_build_and_output_hash_verification.md) for details.

3. Manufacturers shall provide a technical specification of how the inspection of all the voting system registers and variables is implemented by the voting device in the TDP.
    - RCTab does not have a voting device.

## 9.6.7 Cryptography

1. Manufacturers shall provide a list of all cryptographic algorithms and key sizes supported by the voting system.

    * RSA Cipher with a 2048-bit key size

2. Manufacturers shall provide the technical specification of all cryptographic protocols supported by the voting system.
    * We support validation of files encrypted using a detached Signature File, created by Hart Verity with .NET Framework 4.8.1. We do not sign any files, but only validate the signature of files signed by Hart Verity. Below, we outline exactly what that library does, and how we validate the files it produces.
    
        .NET Framework 4.8.1 creates a “Signature File” with the file extension .sig.xml. This Signature File includes data about both the signature itself, and about the file it is signing (the “Signed File”). The Signature File file includes the public key used to sign the file, the signature value, the file path to where the Signed File was originally signed, and the SHA-256 digest of the Signed File.
    
        From the Signature File, .NET Framework 4.8.1 constructs the following XML snippet, hashes it using SHA-256, then signs the hash of this snippet:
    
        ```
        <SignedInfo xmlns="http://www.w3.org/2000/09/xmldsig#"><CanonicalizationMethod Algorithm="{CANONICALIZATION_URL}"></CanonicalizationMethod><SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"></SignatureMethod><Reference URI="file:///{FILE}"><DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"></DigestMethod><DigestValue>{SHA256_HASH}</DigestValue></Reference></SignedInfo>
        ```
    
    * The following variables, above surrounded by curly brackets, are replaced with values specific to each signed file
        + The value `{SHA256_HASH}` is the SHA-256 hash of the Signed File
        + The value `{FILE}` is the filename and filepath of the Signed File
        + The value `{CANONICALIZATION_URL}` is the URL used to uniquely identify the canonicalization algorithm
    * To validate the signature, we require three files:
        + The Public Key, which we store in a String in the source code to prevent runtime tampering, for which only one is valid for each release of RCTab.
        + The Signed File
        + The Signature File (`.sig.xml`) generated by .NET Framework 4.8.1
    * We validate that the signature is valid using the following procedure:
        + We verify that the Signed File matches the SHA-256 hash `{SHA256_HASH}` provided in the Signature File
        + We verify that the Signed File’s filename matches the expected filename `{FILE}` found in the Signature File
        + We verify that the public key found in the Signature File matches the expected Public Key that we have included in our source code
        + We verify the cryptographic signature of the XML snippet above using a 2048-bit RSA with a 256-bit SHA hash.
    * Additional notes:
        + The original path of the signed file at the time of signature is included in the signed message. The path at the time of signature verification may be different - the files will have been moved from the Verity machine they were signed on to the RCTab machine for tabulation. The filename and a hash of the file contents, both of which are included in the signature itself, verify the contents of the signed file.
        + We allow the `Algorithm` attribute of `CanonicalizationMethod` to vary, and support all CanonicalizationMethods supported by the `Java.Security` library in JDK 17.
        + If the Signed File is an XML, it is not canonicalized before being hashed.
        + The signature file IS canonicalized before being hashed.

3. Manufacturers shall provide the cryptographic module name, identification information (such as hardware/firmware/software name, model name, and revision/version number) and NIST FIPS 140-2 validation certificate number for all cryptographic modules that implement the cryptographic algorithms of the voting systems.

    * RCTab uses [#4616](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4616) BC-FJA (Bouncy Castle FIPS Java API), a Level 1 FIPS 140-2 Validated Cryptographic Module to verify the cryptographic signature of Hart Verity Signed CVRs.

        Note: We have BouncyCastle implemented as a provider, but we still use a non-FIPS-certified Sun implementation of a random number generator. The random number generator is only used to validate that the chosen public key is valid -- it's used as part of a primality-checking algorithm. Since we know that the public key we're given is already valid (as it is created by Hart Verity using their FIPS 140-2 certified implementation), this check is superfluous.

        We ensure that only FIPS 140-2 certified modules are used for the RSA algorithm by programmatically removing the non-certified providers before and re-adding them after.

4. Manufacturers shall map the cryptographic modules to the voting system functions the modules support. This requirement documents the actions of the voting system that invoke the cryptographic module.

    | RCTab Function                           | Module                                                              |
    |:-----------------------------------------|:--------------------------------------------------------------------|
    | Verify Hart CVR cryptographic signatures | Java.Security (JDK 17) <br> BouncyCastle Provider (bc-fips) 1.0.2.3 |

5. When public key information is stored in a digital certificate (such as an X.509 certificate), manufacturers shall provide a description of all the certificate fields (such as names, algorithm, expiration date, etc.) including the default values for the voting system. If they exist, manufacturers shall provide any certificate policies associated with the digital certificate.

    * The public key is stored in the Java source code. It has only two fields, the Exponent and the Modulus, which refer to the values in an RSA 2048-bit public key.

6. Manufacturers shall provide documentation describing how cryptographic keys are created, stored, imported/exported, and deleted by the voting system.
    * Cryptographic public keys are provided via secure file transfer, and then included as part of the source code. As they are loaded, we use the Sun implementation of a random number generator to conduct a Miller-Rabin Test to ensure primality.
    
        We ensure that only FIPS 140-2 certified modules are used for the RSA algorithm by programmatically removing the non-certified providers before and re-adding them after.

## 9.6.8 Telecommunications and Data Transmission Security

The manufacturer shall provide a detailed description of the system capabilities and mandatory procedures for purchasing jurisdictions to ensure secure data transmission to meet specific requirements:

1. For all systems, this information shall address access control, and prevention of data interception

    * Jurisdictions should follow their election data handling procedures to ensure prevention of data interception. See also [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md), the Access Control section of this document, and the Physical Security section of this document.

## 9.6.9 Other Elements of an Effective Security Program

The manufacturer shall provide a detailed description of the following additional procedures required for use by the purchasing jurisdiction:

1. Administrative and management controls for the voting system and election management, including access controls
    * See sections [9.6.1](#961-access-control) and [9.6.1.2](#9612-access-control-measures) detailed description of access control in RCTab
    * The user jurisdiction should assign and train employees as per [**Section 10 - Personnel Deployment and Training**](personnel_deployment_and_training.md) documentation. These employees should work in pairs whenever accessing the hardware where the software is installed and during actual use of the software itself.

2. Internal security procedures, including operating procedures for maintaining the security of the software for each system function and operating mode;
    * The user jurisdiction should assign and train employees as per [**Section 10 - Personnel Deployment and Training**](personnel_deployment_and_training.md) documentation. These employees should work in pairs whenever accessing the hardware where the software is installed and during actual use of the software itself.
    * The hardware containing installed software should be secured in a reasonably climate controlled area with access being permitted and monitored through the use of signed access logs and in compliance with any of the user jurisdiction’s own facility security policies.

3. Adherence to, and enforcement of, operational procedures (e.g., effective password management);
    * The user jurisdiction should assign and train employees as per [**Section 10 - Personnel Deployment and Training**](personnel_deployment_and_training.md) documentation. These employees should work in pairs whenever accessing the hardware where the software is installed and during actual use of the software itself.
    * The user jurisdiction should only install the software on hardware that is not ever connected to the internet via WiFi or ethernet connections. See also [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md).
    * The hardware containing installed software should be secured in a reasonably climate controlled area with access being permitted and monitored through the use of signed access logs and in compliance with any of the user jurisdiction’s own facility security policies.

4. Physical facilities and arrangements; and
    * The hardware containing installed software should be secured in a reasonably climate controlled area with access being permitted and monitored through the use of signed access logs and in compliance with any of the user jurisdiction’s own facility security policies.

5. Organizational responsibilities and personnel screening.
    * The user jurisdiction should assign and train employees as per [**Section 10 - Personnel Deployment and Training**](personnel_deployment_and_training.md) documentation.  These employees should work in pairs whenever accessing the hardware where the software is installed and during actual use of the software itself.
    * The user jurisdiction is responsible for contacting the manufacturer to procure the recommended number of hours of training as per [**Section 10 - Personnel Deployment and Training**](personnel_deployment_and_training.md) documentation.  This training may be done virtually or in person.
