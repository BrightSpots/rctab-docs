# Section 07K - Development Environment Specification

**Objective**: This document shall provide descriptions of the physical, personnel, procedural, and technical security of the development environment, including version control, tools used, coding standards used, software engineering model used, and description of developer and independent testing.

**Version Control**: We use Git version control software (<https://git-scm.com>) in conjunction with Github (<https://github.com/BrightSpots/rcv>) to coordinate the efforts of our developers and maintain a complete record of all software code changes to RCTab and the reasoning behind them.

**Coding Standards**: We use *Google Checkstyle for Java* as our published, reviewed, and industry-accepted code style. For details, see [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html) and page 93 of the [VVSG Volume 1.0](https://www.eac.gov/sites/default/files/eac_assets/1/28/VVSG.1.0_Volume_1.PDF) guide.

**Software Engineering Model**: RCTab development uses the Waterfall model.

**Description of Developer**: The Ranked Choice Voting Resource Center (RCVRC), a nonprofit organization, and Bright Spots, a software development team, have joined together to develop RCTab as an open-source software package that provides post-election tabulation to determine results in a ranked choice voting election.

**Independent Testing**: We have developed a suite of 68 Tabulation Regression Tests and continue to add more tests as new features and bug fixes are added. These are designed to verify that various aspects of Tabulator functionality behave as expected. They also verify that new code changes do not inadvertently alter Tabulator behavior. The entire test suite must be run, and all tests must pass before any new code changes can be merged into the main Tabulator repository. See [**Section 17 - System Test and Verification Specification**](system_test_and_verification_specification.md) for additional information.

The RCTab software is developed with the following tools, policies, and practices to ensure robust software quality and reliability. RCTab testing relates only to the function of the software and performs no parts and materials testing as we produce only software and do not design or manufacture hardware. Testing follows standards laid out in the VVSG Volume 2:2.12.1 with regard to V1:8.5.
