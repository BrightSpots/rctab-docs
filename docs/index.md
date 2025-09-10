# RCTab v2.0 Docs

RCTab is an open source tabulator for running ranked choice voting elections.

## User Guide
Start with the **[Quick Start](user_guide/user_guide.md)** if you are a new user. It will help you get RCTab configured and running tabulations.
It can be followed in sequential order: from installing RCTab on your computer, configuring it with your contest details and hardware, to getting results.

The **[User Guide Extended](user_guide/user_guide_extended.md)** contains more detailed information about RCTab for users who are looking to dig in to exactly how certain parts work. Sections here are roughly in order, but users can jump around to find exactly what they need.  

## Technical Documentation Package
The Technical Documentation Package or TDP contains detailed documentation to satisfy state and federal certification requirements. The RCTab v2.0 TDP is still being written.

## Use Principles

The Ranked Choice Voting Resource Center (RCVRC) offers the following principles and best practices for using RCTab, our RCV tabulation software. These principles and best practices can serve as a guide for jurisdictions to orient and augment their local procedures when using RCTab to generate RCV contest results. At no point should any of the following recommendations supersede the applicable laws, policies, or procedures of the jurisdiction.

These principles are applicable at all times -- before, during, and after Election Day. For the sake of clarity, they are organized chronologically here.


### Principle 1 \- Before the Election

Treat RCTab like any other sensitive election technology by using pre-existing jurisdiction procedures for user authorization and authentication, accessing the RCTab workstation, working in bipartisan teams, administering a test election from start to finish, etc.

#### Best Practices

1. Approve RCTab for use in RCV elections in accordance with state requirements.  
2. RCTab should be set up on an air-gapped, non-internet connected computer. The RCTab workstation should be configured using system hardening instructions in the RCTab TDP.  
3. If the jurisdiction is responsible for local installation, install from a trusted source only; e.g., from RCVRC or the state department of elections, and follow workstation hardening instructions in the RCTab TDP.  
4. Train multiple staff members on RCTab use and procedures for redundancy so employee absences or availability issues do not impact the jurisdiction’s ability to conduct RCV tabulation.  
5. Conduct thorough acceptance testing of RCTab after receiving or setting up an RCTab workstation.    
6. Ensure that statute requirements are properly translated into RCTab configuration, e.g. round-by-round tabulation and voter error rules.  
7. Conduct thorough pre-election testing to ensure RCTab will accurately tabulate all aspects of the RCV round-by-round count as laid out in law in the jurisdiction.  
8. Develop, document, and test steps for securely transporting CVR data for use in RCTab from the EMS export to the RCTab workstation.  
9. Develop, document, and test steps for securely transporting RCTab output files to secure storage.  
10. Develop, document, and test steps for translating RCTab output to public election results, using a recommended tool such as [RCVis](https://www.rcvis.com/).  
    

    

### Principle 2 \- During the Election

The use of RCTab should be transparent and auditable with a documented chain of custody.

#### Best Practices

1. Tabulate contests using RCTab with, at minimum, two-person and/or bipartisan teams.  
2. CVR data configured for use in RCTab should come straight from the EMS export with no stops in between, using secure file transfer methods.  
3. Chain of custody should be maintained at all times and documented as part of the election record.  
4. Conduct RCTab tabulation for final results of a contest on live stream following livestream best practices.   
5. Transfer all RCTab output files to secure storage, following the plan developed before Election Day.  
6. Once RCTab produces results, reconcile RCV results at each round of tabulation by comparing the total ballots in each round to the total ballots cast in the contest as reported by the EMS to ensure no inconsistencies.  
7. Execute the plan developed before Election Day for public display of RCTab results.

### Principle 3 \- After the Election

Secure and store RCTab workstation and related materials following jurisdiction requirements.

#### Best Practices

1. Store RCTab under lock and key when not in use. Jurisdiction laws and policies for accessing voting technology should be maintained even when not in use.  
2. All documentation of RCTab use during an election cycle should be archived and maintained using the record and retention policies adopted by the jurisdiction.  
3. Evaluate the current version of RCTab offered and determine if the jurisdiction should upgrade.  