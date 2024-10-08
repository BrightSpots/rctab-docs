# Section 30 - RCTab System Tab Hints

These hints are displayed in the user interface of RCTab to help users navigate through each option available in RCTab.

## Hints for Contest Info Tab

> The tabulator calculates results for one contest at a time, rather than the results of several contests for an election all at once. The information on this tab is for the particular contest you will be tabulating.
> 
> These fields do not influence the computations. They are shown in the final output file(s) to help connect the data (results) with the contest the results belong to.
> 
> * Think long term, e.g. from the perspective of looking at the results files 6 months after the election and wanting to be clear what contest the results belong to.
> * You may find it helpful to revisit this tab once you have done a few test runs and see what the output looks like.
> 
> Contest Name (required): Enter a name to identify it.  
> Examples: City Council 2018, Board of Election Ward 13 2017, Mayor, Referendum 289b
> 
> Contest Date (optional): The date on which the election for this contest was run.
> 
> Contest Jurisdiction (optional): E.g.: Minneapolis, Eastpointe  
> Whether this is helpful may depend on what you put into the Contest Name field
> 
> Contest Office (optional): E.g.: Mayor, County Clerk  
> Whether this is helpful may depend on what you put into the Contest Name field
> 
> Rules Description (optional): What short description of this configuration would help you remember in, say, six months what election this specific rule configuration is for?

## Hints for Candidates Tab

> Fill in the fields and click the Add button:
> 
> Name (required): E.g.: Dave Harris.
> 
> Code (optional): Some CVR files use codes in lieu of full candidate name. E.g.: "JCD" or "14".
> 
> Excluded (optional): When checked, the candidate will be ignored during tabulation. An example of when this might be used: a candidate dropped out after the ballots were printed.

## Hints for CVR Files Tab

> The tabulator needs to know where each of your CVR files is and how to interpret each of them. As you add files, it will build up a list of files to use when it tabulates the results of this contest.
> 
> For each of your CVR files, provide the necessary information and then use the Add button to add it to the list.
> 
> Provider (required): The vendor/machine that generated (produced) the file. After you select the field, the tabulator will fill in as many of the other fields as it can based on what it knows about that provider. You can adjust those values as necessary.
> 
> Path (required): Location of the CVR file.
> 
> * Example: /Users/test data/2015-portland-mayor-cvr.xlsx
> 
> Contest ID (required for non-ES&S): Some CVRs assign an ID label to each contest in the CVR. The tabulator needs to know which contest is being tabulated when multiple contests are included in one CVR. Enter the ID of the contest being tabulated in this field.
> 
> First Vote Column (required for ES&S): the column where the first vote record is.
> 
> First Vote Row (required for ES&S): the row where the first vote record is.
> 
> ID Column (optional): The column the IDs are in. Not all CVR files contain an ID column.
> 
> Precinct Column (required for ES&S if you want to tabulate by precinct): The column that contains the precinct.
> 
> Overvote Delimiter (optional, but must be blank if "Overvote Label" is provided): If using a CVR in ES&S style, overvotes can be reflected in a CVR by displaying all candidates marked at a ranking. Those candidate names will be differentiated from each other by a delimiter, something like a vertical bar | or a slash /. If your overvotes are delimited like this, enter the delimiter used in this field. Note that ES&S files may include only the label "overvote" and no additional information, in which case the "Overvote Label" field should be used instead.
> 
> Overvote Label (optional): Some CDF and ES&S CVRs use a particular word/phrase to indicate an overvote.
> 
> Undervote Label (optional): Some ES&S CVRs use a particular word/phrase to indicate an undervote. Undeclared Write-in Label (optional): Some CVRs use a particular word/phrase to indicate a write-in.
> 
> Treat Blank as Undeclared Write-in (optional): When checked, the tabulator will interpret blank cells in this ES&S CVR as votes for undeclared write-ins.

## Hints for Winning Rules Tab

> Winner Election Mode (required): What process to use for selecting winner(s) for this contest.
> 
> * Single-winner majority determines winner: Elects one winner. Eliminate candidates one-by-one or using batch elimination until a candidate emerges with a majority. Candidate with the most votes at the end wins.
> * Multi-winner allows only one winner per round: Elects multiple winners. Elect and transfer the surplus vote of only the candidate with the most votes if multiple candidates exceed the winning threshold in a round of counting.
> * Multi-winner allows multiple winners per round: Elects multiple winners. Elect and transfer the surplus vote of all candidates crossing the winning threshold if multiple candidates exceed the winning threshold in a round of counting.
> * Bottoms-up: Eliminate candidates until the desired number of winners is reached, then stop. Bottoms up does not transfer surplus votes.
> * Bottoms-up using percentage threshold: Elects multiple winners. Eliminate candidates until the remaining candidates have a vote share equal to or greater than a specified percentage of the vote.
> * Multi-pass IRV: Elects multiple winners. Eliminate candidates one-by-one or using batch elimination until only two candidates remain. Candidate with the most votes at the end wins. Run a new set of rounds with any winning candidates ignored.
> 
> Maximum Number of Candidates That Can Be Ranked: How many rankings each voter has in this contest.
> 
> Minimum Vote Threshold: The number of first-choice votes a candidate must receive in order to remain in the race. Most jurisdictions do not set a minimum vote threshold.
> 
> Use Batch Elimination: Batch elimination, or simultaneous elimination of all candidates for whom it is mathematically impossible to be elected, eliminates all candidates who cannot receive enough votes to surpass the candidate with the next highest number of votes. Example: in a six candidate contest with 200 votes, Candidate A has 80 votes, Candidate B has 70, and the other four combined have 50. Because those four candidates can never combine their votes to surpass Candidate B, they can be batch eliminated. Available only when Winner Election Mode is "Single-winner majority determines winner".
> 
> Continue until Two Candidates Remain: Single-winner ranked-choice voting elections can stop as soon as a candidate receives a majority of votes, even though 3 or more candidates may still be in the race. Selecting this option will run the round-by-round count until only two candidates remain, regardless of when a candidate wins a majority of votes.
> 
> Tiebreak Mode (required): Ties in ranked-choice voting contests can occur when eliminating candidates or when electing candidates. Multi-winner contests can have ties between candidates who have both crossed the threshold of election; in that case ties are broken to determine whose surplus vote valuetransfers first. Tiebreak procedures are set in law, either in the ranked-choice voting law used in your jurisdiction or in the elections code more generally. Select the option from this list that complies with law and procedure in your jurisdiction.
> 
> * Random: Randomly select a tied candidate to eliminate or, in multi-winner contests only, elect. Requires a random seed.
> * Stop counting and ask: Pause count when a tie is reached. User is prompted to select any tied candidate to eliminate or, in multi-winner contests only, elect.
> * Previous round counts (then random): The tied candidate with the least votes in the previous round loses the tie. If there is a tie in the previous round, the tie is broken randomly. Requires a random seed.
> * Previous round counts (then stop counting and ask): The tied candidate with the least votes in the previous round loses the tie. If there is a tie in the previous round, user is prompted to select any tied candidate to eliminate or, in multi-winner contests only, elect.
> * Use candidate order in the config file: Use the order of candidates in the config file to determine tiebreak results. Candidates lower in the list lose the tiebreaker.
> * Generate permutation: Generate a randomly ordered list of candidates in the contest. Candidates lower in the permutation lose the tiebreaker. Requires a random seed.
> 
> Random Seed (required if Tiebreak Mode is "Random", "Previous round counts (then random)", or "Generate permutation"): Enter a positive or negative integer to generate random orders.
> 
> Number of Winners: The number of seats to be filled in the contest.
> 
> Percentage Threshold: The share of votes a candidate must have in order to win. Candidates falling below this threshold are eliminated one-by-one beginning with the candidate with the fewest votes. Available only when Winner Election Mode is "Bottoms-up using percentage threshold".
> 
> Threshold Calculation Method: The threshold of election is the number of votes a candidate must receive in order to win election. There are three primary ways to calculate the threshold of election in multi-winner RCV contests. This will be set in law (either by statute or regulation) in your jurisdiction. Available only when Winner Election Mode is "Multi-winner allow only one winner per round" or "Multi-winner allow multiple winners per round".
> 
> * Compute using most common threshold formula: The most common threshold formula is calculated by dividing the number of votes by the number of seats plus one, then adding one to that number. Fractions are disregarded. This is also known as the Droop quota. Candidates must receive this number of votes (or more) to win.
> * Compute using HB Quota: The HB, or Hagenbach-Bischoff, Quota divides the number of votes by the number of seats plus one, leaving fractions. Candidates must receive more than this number of votes to win.
> * Compute using Hare Quota: The Hare quota divides the number of votes by the number of seats. It requires candidates to receive that number of votes (or more) to win.
> 
> Decimal Places for Vote Arithmetic (Multi-Winner Only): Sets how many decimal places after the decimal point are used in surplus transfers and in calculating the threshold.

## Hints for Voter Error Rules Tab

> The tabulator needs to know how to handle voter errors in your jurisdiction. These requirements are typically included in statute or regulation.
> 
> Overvote Rule (required): How to handle a ballot where a voter has marked multiple candidates at the same ranking when that ballot is encountered in the round-by-round count.
> 
> * Always skip to next rank: Skips over an overvote and goes to the next validly-marked ranking on a ballot.
> * Exhaust immediately: A ballot with an overvote exhausts when that overvote is encountered in the rounds of counting.
> * Exhaust if multiple continuing: If a voter has an overvote but only one candidate at that overvote is still in the race when that overvote is encountered, the ballot counts for that candidate. If multiple candidates at the overvote are still in the race, the ballot exhausts.
> 
> How Many Consecutive Skipped Ranks Are Allowed (required): How many rankings in a row can a voter skip and still have later rankings count? 0 allows no skipped rankings. 1 allows voters to skip rankings one at a time, but not more than 1 in a row, and so on.
> 
> Example: A voter could rank in 1, 3, 5 and not exhaust under this rule, for example.
> 
> Exhaust on Multiple Ranks for the Same Candidate: When checked, the tabulator will exhaust a ballot that includes multiple rankings for the same candidate when that repeat ranking is reached.
> 
> Example: A voter ranks the same candidate 1st and 3rd, a different candidate 2nd, and another candidate 4th. If their original first choice and their second choice are eliminated, the ballot exhausts when it reaches the repeat ranking in rank 3. The ranking in the 4th rank does not count.

## Hints for Output Tab

> Tell the tabulator where results files go and what additional results files you want.
> 
> Output directory: The location where results files will go. If no value (or a relative path, like "output") is supplied, the location where the config file is saved will be used as the base directory. Absolute paths, like "C:\output" work too.
> 
> Tabulate by Precinct: Produce round-by-round results at the precinct level. Results are how ballots at the precinct level transferred in the contest as a whole, not a simulated round-by-round count in the precinct. Requires precinct information in CVR Files tab.
> 
> Generate a CDF JSON: Produce a VVSG common data format JSON file of the CVR.
