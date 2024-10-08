# Section 06 - System Design Specifications

5.1.1 - Configuration of software, both operating systems and applications, is critical to proper system functioning. Correct test design and sufficient test execution must account for the intended and proper configuration of all system components. Therefore, the vendors shall submit a record of all user selections made during software installation as part of the Technical Data Package. The vendor shall also submit a record of all configuration changes made to the software following its installation. The accredited test lab shall confirm the propriety and correctness of these user selections and configuration changes.

- RCTab software does not permit installation configuration changes by the user at any time during or after the installation process.
- RCTab software installation must be conducted according to [**Section 22 - Installation Instructions for Windows OS**](installation_instructions_for_windows_os.md).
- See [**Section 18 - User Guide**](user_guide.md) and [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md) document for more information about RCTab operation and other software requirements on hardware used for RCTab software.

5.3.a - Maintain the integrity of voting and audit data during an election, and for at least 22 months thereafter, a time sufficient in which to resolve most contested elections and support other activities related to the reconstruction and investigation of a contested election.

- The user jurisdiction should follow all record retention policy requirements set by the jurisdiction itself and all other higher governing authorities with respect to the appropriate retention and storage of any materials generated by the software.
- The manufacturer recommends that in the absence of any user controlling records retention schedule, all materials generated by the software for a particular election be securely stored for a minimum period of 22 months.
- User must save all results files created for each contest in an election, including all configuration files used for those contests. This should also include testing data. User must export files to a hard drive secured and stored according to jurisdiction policies. For every contest processed through RCTab at least four files must be exported:
    * Contest `configuration.json` file
    * Contest summary `.csv` file
    * Contest summary `.json` file
    * Contest audit `.log` file(s)
        + Depending on the size of the contest multiple `.log` files may be created. `.log` files have a maximum size of 50MB. Large contests frequently have many `.log` files.
    * The [**Section 18 - User Guide**](user_guide.md) suggests users create a folder for each contest where all relevant files for the contest are saved. If these procedures are followed, users will be able to copy whole sets of contest files over, folder by folder, on the external hard drive to be used for records retention.
    * At the close of an election, users must also export any operator `.log` files, located in the bin folder of the RCTab installation folder. These `.log` files will be named `rcv_0.log`, `rcv_1.log`, and so on, depending upon how many `.log` files were produced during use of RCTab. These files must also be placed on the secured hard drive.
    * After successfully copying over all relevant files to a secured hard drive, the hard drive should be stored in a temperature and humidity controlled area that meets the criteria for such media.
