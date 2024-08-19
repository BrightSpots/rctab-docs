# Section 03 - System Hardware Specification

Hardware requirements vary depending on the size (number of CVRs) of the contest you wish to tabulate. In general, the more RAM a system has the larger the elections it can run. The more powerful a computer’s CPU is, the faster it will be able to process election results. Please note when tabulating large contests (more than 1 million CVRs) RCTab must be launched from the command line using the launch steps detailed below. In all cases, after running a tabulation, you must exit the tabulator to clear the memory. Launch RCTab again to tabulate another contest. No other applications should be running at the same time, as they may compete with the tabulator for resources (RAM and CPU) and cause it to run more slowly.

For a jurisdiction with a large number of registered voters, RCTab will need to configure a desktop computer that meets or exceeds the following specifications:

- Windows 10 operating system or above
- 3.0 GHz processor
- 32GB RAM
- 10GB disk space

The PC/Laptop is required to be set up according to the hardening procedures detailed in [**Section 16 - System Hardening Procedures - Windows OS**](system_hardening_procedures_-_windows_os.md)

**Please note when tabulating large contests (more than 1 million CVRs) RCTab must be launched from the command line using the launch steps detailed below.**

## Large Configuration:
- Goal: handle up to 6,000,000 CVRs containing up to 40 columns of rankings data each:
    * 3.0 GHz processor
    * 32GB RAM
    * 10GB disk space \+ room for whatever log files your tabulations generate
- Produces ~6GB of audit log output per contest  
- Runtime: less than 40 minutes  
- Launch steps for a large election:
    - Contest with more than 1,000,000 votes
        1. Open a Command Prompt by navigating to the start menu and typing in Command Prompt.
        2. Press enter to launch Command Prompt.
        3. Change the current directory to the rcv folder created when you unzipped the Tabulator.
        4. First, type in cd (note there should be a space after cd).
        5. Using File Explorer navigate to the folder where RCTab is installed.
        6. Double-click on the `rctab_v1.3.0_windows` folder
        7. Click and drag the rcv folder over to the command prompt window
        8. Your command prompt will now read something like:
            1. `cd C:\Users\user\rctab_v1.3.0_windows\rctab_v1.3.0_windows\rcv`
        9. Press enter
        10. Launch the tabulator by entering the following command:
             1. `.\bin\java -mx30G -p .\app -m network.brightspots.rcv/network.brightspots.rcv.Main`.
    - This configuration will run a 6,000,000 record contest in about 30 minutes.

Additional smaller configurations are possible for smaller contests ([see below](#small-configuration))

## Small configuration:
- Goal: handle up to 100,000 CVRs, up to 40 columns of rankings data each:
    - 1 GHz processor
    - 4GB of RAM
    - 1GB of disk space + room for whatever log files your tabulations generate
- Produces ~100MB of audit log output per contest  
- Runtime: less than 2 minutes  
- To Launch: double-click the `rcv.bat` file  
- Contests will be run in as long as one minute with this configuration. Smaller contests will run faster.

## Medium Configuration:
- Goal: handle up to 1,000,000 CVRs, up to 40 columns of rankings data each:
    - 3.0 GHz processor
    - 16GB RAM
    - 2GB disk space + room for whatever log files your tabulations generate
- Produces \~1GB of audit log output per contest
- Runtime: less than 5 minutes
- To Launch: double-click the `rcv.bat` file

- Contests will run in as long as 5 minutes with this configuration. Smaller contests will run faster.

> Both small and medium contests can be run by using the same launch steps on the recommended computer. Contests of small and medium size can be run on the hardware defined in this document and in [**Section 18 - User Guide**](user_guide.md) using the launch steps under the small and medium configurations.

## Hardware Physical, Reliability, Maintainability, and Environmental Characteristics

Any machine used to run RCTab does not have any required physical characteristics beyond those expected of commercial off the shelf (COTS) computing equipment.

The RCTab software itself can be maintained by following [**Section 09 - System Maintenance Manual**](system_maintenance_manual.md) and following [**Section 29 - RCTab Operator Log Messages**](rctab_operator_log_messages.md). These documents are written in a manner to be understood by non-technical election workers with sufficient training in the RCTab software. Any COTS hardware or software used to run RCTab should be maintained with reference to the Maintenance Procedures and to any relevant user guides and maintenance manuals included with that COTS equipment.

Any machine used to run RCTab should follow basic environmental conditions required of any COTS computing equipment.
