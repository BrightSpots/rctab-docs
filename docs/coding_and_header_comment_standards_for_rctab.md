# Section 31 - Coding and Header Comment Standards for RCTab

The BrightSpots programmers that do the coding of the RCTab following the Google Java Style Guide. They do not have revision histories on individual files because comprehensive file revision histories between versions are easily viewable on GitHub.

The CVVS includes the following Header Comments requirements:

*5.2.6 Header Comments*

*Header comments and other commenting standards should be specified by the selected coding standard in a manner consistent with the idiom of the programming language chosen. If the coding standard specifies a coding style and commenting standard that make header comments redundant, then they may be omitted. Otherwise, in the event that the coding standard fails to specify the content of header comments, application logic modules should include header comments that provide at least the following information for each callable unit (function, method, operation, subroutine, procedure,*

*etc.):*
*a. The purpose of the unit and how it works (if not obvious);*
*b. A description of input parameters, outputs and return values, exceptions thrown, and side-effects;*
*c. Any protocols that must be observed (e.g., unit calling sequences);*
*d. File references by name and method of access (read, write, modify, append, etc.);*
*e. Global variables used (if applicable);*
*f. Audit event generation;*
*g. Date of creation; and*
*h. Change log (revision record). Change logs need not cover the nascent period, but they must go back as far as the first baseline or release that is submitted for testing, and should go back as far as the first baseline or release that is deemed reasonably coherent.*

The coding style and commenting standard used in developing RCTab, the Google Java Style Guide, makes header comments redundant. Per the statement in 5.2.6 that if a “coding standard specifies a coding style and commenting standard that make\[s\] header comments redundant,” we exclude extensive header comments in source code. One of the benefits of writing high-quality code is that there's less need to add extraneous comments since the code speaks for itself.

The Google Java Style Guide is attached as an addendum to this document.
