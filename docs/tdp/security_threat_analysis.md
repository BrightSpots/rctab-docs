# Section 07L - Security Threat Analysis

**Objective:** This document shall identify the threats the voting system protects against and the implemented security controls on voting system and system components.

## Identified Threats & Mitigation

- Equipment Failure - RCTab is used on COTS equipment.  While equipment failure is rare, it should be recognized as a possibility.  Jurisdiction backup and disaster plans should include strategies for handling equipment failures and replacements before they occur.
    * See [**Section 03 - System Hardware Specification**](system_hardware_specification.md) for minimum operating specifications and [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md) for procedures to ensure the hardware is adequately protected against unauthorized access, theft of data, and/or malicious attacks.

    * Following any maintenance or replacement of equipment used to operate RCTab, users should refer to [**Section 05 - Acceptance Test Procedures**](acceptance_test_procedures.md).

    * The manufacturer also recommends conducting a post-installation and post-election hashing as outlined in [**Section 23 - HashCode Instructions - Windows OS**](trusted_build_and_output_hash_verification.md).

    * If the user elects to use USB devices to move installation files and/or data to and from devices, the manufacturer recommends using instructions as outlined in  [**Section 32 - Secure USB Process**](secure_usb_process.md).
  
- Unauthorized Access - Software itself is vulnerable to attack if someone gains access to the tabulation computer/RCTab workstation without jurisdiction approval or knowledge because of violation of access controls
    * Users should only access the software per jurisdiction approved rules and after users have obtained the recommended training as outlined in [**Section 10 - Personnel Deployment and Training**](personnel_deployment_and_training.md). See also [**Section 07 - System Security Specification Requirements**](system_security_specification_requirements.md).

    * When used with Hart Verity, RCTab 1.3.2 includes the following programmatic security mechanisms
        + When tabulation begins, RCTab automatically, programmatically verifies the cryptographic signature of all Hart CVRs used as input for contest tabulation. This verification step ensures both the integrity (CVR contents have not been edited) and provenance (CVRs came from the Hart voting system) of the Hart CVRs. RCTab will throw a halting error and tabulation will not begin if cryptographic validation of Hart’s CVR signature is not successful. This is to protect against tampering of CVRs between Hart Verity export and RCTab import by malicious internal actors.

        + After successfully following installation instructions in [**Section 22 - Installation Instructions for Windows OS**](installation_instructions_for_windows_os.md) *only* the RCTab software is run with administrator privileges, the logged in Windows user does **not** have administrative privileges. All RCTab output files (audit logs, summary .csv and .json, corresponding .hash files) are programmatically set to Read-Only and cannot be edited by the RCTab Windows Standard user.

            This is to protect against any tampering with the content of the summary files or audit log by malicious internal actors. This also ensures that the tabulation user does not have admin-level OF privileges to make changes that could be security issues e.g. disabling read-only access or enabling network adaptors.

        + Additionally, RCTab automatically, programmatically creates a cryptographic hash of all output files - audit logs, summary .csv and .json - that can be used to validate that those files have not been edited. This is to protect against any tampering with the content of the summary files and audit log.

    * The objective of these programmatic and procedural security improvements is to make the execution of malicious tampering so onerous that it will not be a viable target. The combination of procedural and new programmatic controls require significantly more time and complexity for any malicious actor - this makes RCTab a less appealing target. Additionally, these procedural and programmatic controls make auditing a tabulation to ensure secure, successful execution easier and quicker.

    * Though perfect security is the goal of RCTab, threats still exist. Certain programmatic requirements continue to require procedural steps. Not following the procedural steps could make it easier for a malicious actor to tamper with an election. For example, [**Section 22 - Installation Instructions for Windows OS**](installation_instructions_for_windows_os.md) describes explicitly setting permissions for the RCTab output folder to ensure read only access. If this is not done - either by not setting permissions during installation, or by configuring RCTab during tabulation to use a different folder - RCTab users cannot edit RCTab output but they can delete RCTab output. Someone could

        + Copy the contents of the output
        + Create a new file
        + Edit the contents of that new file
        + Delete the original file
        + Then rename the edited file to the original

        But this is mitigated by the other security additions to v1.3.2. To successfully tamper with the `summary.csv` file for example, a malicious actor must also

        + Rehash the edited file, delete the corresponding `.hash` file and recreate it with the new hash
        + Delete the `summary.json` file, recreate it with the same edits to `summary.csv`, hash the `summary.json` file, delete it’s corresponding `.hash` file and recreate it with the edited hash
        + Find the `audit_X.log`, copy its contents to a new file, search through it to find and edit original hashes of the output files, rehash the `audit_X.log`, delete the corresponding `audit_X.log.hash`, and recreate it with the edited hash, delete the original `audit_X.log` and rename the edited one


        And all of these steps described above would be moot if installation instruction procedures are properly followed and permissions on the output folder set correctly. In that case, all RCTab output files are read only and cannot be edited, deleted, or recreated by the user running the tabulation.

- Incorrect assignment of RCV rules as set by the jurisdiction - Jurisdictions establish rules for interpreting and counting ranked choice voting results.  Failure to correctly set up the RCTab configuration file according to jurisdiction requirements could lead to incorrect results.
    * Pre-election testing should be performed as per jurisdiction policies and procedures.  Instructions for conducting those tests can be found at [**Section 11 - L&A Testing**](l_and_a_testing.md)
