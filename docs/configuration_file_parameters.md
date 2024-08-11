# Section 25 - Configuration File Parameters

This document lists the parameters the user will configure within RCTab. The output is the JSON file used for tabulation.

The Config file must be a valid JSON format. Example config files can be found under the test folder. The values a user inputs into any of these fields depend upon the relevant laws and regulations in place in their jurisdiction, as well as the voting system vendor used to produce cast-vote records for their elections. Users must understand the requirements of their laws, regulations, and vendor CVR data in order to fill out these fields successfully.

This document lists the parameters that can be included in a config file suitable for input tabulation. Parameters are categorized by required and optional. If a user fails to fill out a required parameter when building a configuration file, RCTab will alert the user to the missing requirement and provide suggested resolution steps.

Config file must be valid JSON format. Examples can be found in the test_data folder.

- "tabulatorVersion" required
    * version of the application that created this file
    * used for migrating config data between different application versions
    * example: "1.0.1"
    * value: text string of length \[1..1000\]

  **"outputSettings"** required
A list of output settings and their associated parameters
The "outputSettings" section contains the following parameters:

1. "contestName" required
    1. The name of the contest
    1. Used for naming audit output files
    1. Example: "Portland Mayoral Race 2017"
    1. Value: text string of length \[1..255\]
1. The "outputDirectory" optional
    1. Directory for audit output files (absolute or relative path)
    1. Example: /Path/To/TabulatorResults
    1. Example: output data/contest1
    1. Value: string of length \[1..255\]
    1. If not supplied: files will be saved to the current working directory
1. The "contestDate" optional
    1. Date of the contest
    1. Example: "2015-11-03"
    1. Value: text string of length \[1..1000\]
    1. If not supplied: none
1. The "contestJurisdiction" optional
    1. Text description of the jurisdiction of this contest
    1. Example: "Portland, ME"
    1. Value: text string of length \[1..1000\]
    1. If not supplied: none
1. "contestOffice" optional
1. text description of the office being contested
1. Example: "Mayor"
1. Value: text string of length \[1..1000\]
1. If not supplied: none

**"cvrFileSources"** required
List of input CVR file paths and their associated parameters. Multiple CVRs can be input in a single configuration file.
Each "cvrFileSources" list item contains the following parameters:

1. "provider" required
    1. text description of the vendor / machine which generated this file
    1. value: "cdf" | "clearBallot" | "dominion" | "ess" | "hart"
1. "filePath" required
    1. location of the CVR file (in the case of CDF, Clear Ballot, and ES&S), or the CVR folder (in the case of Dominion and Hart)
    1. example: /Users/test_data/2015-portland-mayor-cvr.xlsx
    1. value: string of length \[1..255\]
1. "contestId" required when CVR source files are from a provider other than ES&S; must be blank for ES&S
    1. the ID of the contest to tabulate, as represented in the CVR file(s)
    1. example: "b651b997-417a-46d9-a676-a43d4df94ddc"
    1. value: text string of length \[1..1000\]
1. "firstVoteColumnIndex" required and used if and only if the provider is ES&S
    1. index of the column (starting from 1\) that contains the top-ranked candidate for each CVR
    1. example: 3
    1. value: \[1..1000\]
1. "firstVoteRowIndex" required and used if and only if the provider is ES&S
    1. index of the row (starting from 1\) that contains the rankings for the first CVR
    1. example: 2
    1. value: \[1..100000\]
1. "idColumnIndex" optional and can be used only if the provider is ES&S
    1. index of the column (starting from 1) that contains the unique ID for each CVR
    1. example: 1
    1. value: \[1..1000\]
1. "precinctColumnIndex" required and used if and only if "tabulateByPrecinct" is enabled and the provider is ES&S
    1. index of the column (starting from 1) that contains the precinct name for each CVR
    1. example: 2
    1. value: \[1..1000\]
1. "overvoteLabel" optional and can be used only if the provider is ES&S or CDF
    1. label used in the CVR to denote an overvote; if this parameter is present overvoteRule must be either "alwaysSkipToNextRank" or "exhaustImmediately" (because the other option, "exhaustIfMultipleContinuing", relies on knowing which specific candidates were involved in each overvote)
    1. example: "OVERVOTE"
    1. value: string of length \[1..1000\]
1. "undervoteLabel" optional and can be used only if the provider is ES&S
    1. the special label used in the cast vote records to denote an undervote
    1. example: "UNDERVOTE"
    1. value: string of length \[1..1000\]
1. "undeclaredWriteInLabel" optional
    1. the special label used in the cast vote records to denote a vote for an undeclared write-in
    1. example: "UWI"
    1. value: string of length \[1..1000\]
1. "treatBlankAsUndeclaredWriteIn" optional and can be used only if the provider is ES&S



    1. tabulator will interpret a blank cell in a CVR as a vote for an undeclared write-in
    1. value: true | false
    1. if not supplied: false

**"candidates"** required
List of registered candidate names and associated candidate code (note: leave empty when CVR is in Common Data Format)
Each "candidates" list item has the following parameters:

1. "name" required
    1. Full name of the registered candidate
        1. Example: "Duson, Jill C."
            1. Value: string of length \[1..1000\]
1. "code" optional
    1. Candidate code which may appear in CVRs in lieu of full candidate name
        1. Example: "JCD"
            1. Value: string of length \[1..1000\]
            1. If not supplied: none
1. "excluded" optional
    1. Candidate should be ignored during tabulation
        1. Value: true | false
            1. If not supplied: false

**"rules"** required
Set of configuration parameters that specify the tabulation rules
The "rules" section contains the following parameters:

1. "tiebreakMode" required
    1. how the program should decide which candidate to eliminate when multiple candidates are tied for last place
    1. or which candidate to elect first when:
        1. electionWinnerMode is set to multiWinnerAllowOnlyOneWinnerPerRound, and
        1. multiple candidates exceed the winning threshold in the same round, and
        1. at least two of those candidates are tied for the highest vote total in that round
    1. value: "random" | "stopCountingAndAsk" | "previousRoundCountsThenRandom" | "previousRoundCountsThenAsk" | "useCandidateOrder" | "generatePermutation"
        1. we use java.util.random for randomness in our tiebreak implementations
            1. see: [https://docs.oracle.com/en/java/javase/12/docs/api/java.base/java/util/Random.html](https://docs.oracle.com/en/java/javase/12/docs/api/java.base/java/util/Random.html)
            1. compatible methods exist for other languages, e.g. [https://pypi.org/project/java-random/](https://pypi.org/project/java-random/)
        1. on tabulation start a java.util.Random object is created if required using the randomSeed value specified in the input config file:
            1. Random random = new Random(config.getRandomSeed());
    1. "Random"
        1. during tabulation, in the event of a tie at the end of a round:
            1. the list of tied candidates is sorted alphabetically
            1. a randomDouble is generated using the random object:
            1. double randomDouble = random.nextDouble();
            1. the randomDouble is mapped to one of the tied candidates in the list:
            1. int randomCandidateIndex = (int) Math.floor(randomDouble * (double) tiedCandidates.size());
            1. the selected candidate will be the winner or loser for that round
    1. "stopCountingAndAsk":
        1. the user is presented with a list of tied candidates
        1. the user will input their selection manually
    1. "previousRoundCountsThenRandom"
        1. the tied candidate with the highest vote total in the previous round is selected
        1. if there is a tie for the vote count in the previous round as well, a candidate is selected from the still tying candidates as described under tiebreakMode "Random"
    1. "previousRoundCountsThenAsk"
        1. the tied candidate with the highest vote total in the previous round is selected
        1. if there is a tie for the vote count in the previous round as well, a candidate is selected from the still tying candidates as described under tiebreakMode "Stop counting and ask"
    1. "useCandidateOrder"
        1. during tabulation, in the event of a tie at the end of a round the list of candidates from the config file is consulted
        1. if selecting a winner the tied candidate in this round who appears earliest is selected as a winner
        1. if selecting a loser the tied candidate who appears latest is selected as the loser.
    1. "generatePermutation"
        1. on config load candidate names are sorted alphabetically by candidate code, or if code is not present, candidate name
        1. a randomly ordered candidate permutation is created using Collections.shuffle() with the randomSeed specified in the input config file
        1. during tabulation, in the event of a tie at the end of a round, this permutation is consulted
        1. if selecting a winner: the tied candidate in this round who appears earliest is selected
        1. if selecting a loser: the tied candidate who appears latest is selected
1. "overvoteRule" required
    1. how the program should handle an overvote when it encounters one
    1. value: "alwaysSkipToNextRank" | "exhaustImmediately" | "exhaustIfMultipleContinuing"
    1. “exhaustImmediately”
        1. "exhaustImmediately": exhaust a ballot as soon as we encounter an overvote
1. "winnerElectionMode" required
    1. which process the program should apply for selecting the winner(s)
    1. value: "singleWinnerMajority" | "multiWinnerAllowOnlyOneWinnerPerRound" | "multiWinnerAllowMultipleWinnersPerRound" | "bottomsUp" | "bottomsUpUsingPercentageThreshold" | "multiPassIrv"
    1. If only “singleWinnerMajority” is in use.
        1. "singleWinnerMajority": no special process (only valid when numberOfWinners = 1).
            1. Election threshold = floor(V/(S+1)) + 1
            1. where V = total number of votes (in the current round); and S = numberOfWinners
1. "numberOfWinners" required
    1. the number of seats to be won in this contest



    1. Uneditable if using “single-winner majority determines winner,” automatically set to 1. Uneditable if using “Bottoms-up using percentage threshold,” automatically set to 0.
    1. note: we use fractional vote transfer to redistribute votes in “multiWinnerAllowOnlyOneWinnerPerRound” and “multiWinnerAllowMultipleWinnersPerRound” contests.
    1. note: 0 is valid only when winnerElectionMode is set to "bottomsUpUsingPercentageThreshold"
    1. value: \[0..number of declared candidates\]
1. "minimumVoteThreshold" optional
    1. if a candidate receives fewer than this number of votes in the first round, they are automatically eliminated
    1. example: 150
    1. value: \[0..1000000\]
    1. if not supplied: no automatic elimination occurs (equivalent to setting it to 0)
    1. Note: If no candidate exceeds the minimum vote threshold, tabulation silently fails. If you are using the minimum vote threshold setting and are having issues getting results, check that you have not set the minimum vote threshold too high.
1. "maxSkippedRanksAllowed" required
    1. maximum number of skipped ranks (undervotes) on a ballot before the ballot should be considered exhausted; if "unlimited" is entered, a ballot will never be considered exhausted due to skipped ranks
    1. example: 1
    1. value: \[unlimited, 0..1000000\]
1. "maxRankingsAllowed" required
    1. maximum number of candidates that a ballot is allowed to rank; if "max" is entered, this will default to the total number of declared candidates as entered on the candidates tab
    1. example: 15
    1. values: \[max, 1..1000000\]
1. "rulesDescription" optional
    1. text description of this rules configuration for organizing your config files -- not used by the tabulator
    1. Example "Maine Rules"
    1. value: string of length \[1..1000\]
1. "batchElimination" optional
    1. Tabulator will use batch elimination (only valid for single-winner contests)
    1. Value: true | false
    1. If not supplied: false
1. "continueUntilTwoCandidatesRemain" optional
    1. tabulator will keep tabulating (beyond winning round) until only two candidates remain (only valid for single-winner contests)
    1. Value: true | false
    1. If not supplied: false
1. "overvoteDelimiter" optional and can be used only if provider is ES&S; must be blank when overvoteLabel is provided
    1. string that will be used to split a cell into multiple candidate strings in the case of an overvote
    1. example: //
    1. value: any string that contains no backslashes and at least one character that is not a letter, number, hyphen, period, comma, apostrophe, quote, or space
1. "tabulateByPrecinct" optional
    1. Tabulator will generate a results spreadsheet for each precinct
    1. Value: true | false
    1. If not supplied: false
1. "generateCdfJson" optional
    1. Tabulator will generate a JSON of cast vote records in the Common Data Format
    1. Value: true | false
    1. If not supplied: false
    1. "exhaustOnDuplicateCandidate" optional
        1. Tabulator will exhaust a ballot when it encounters a duplicate candidate (instead of just skipping the duplicate)
        1. Value: true | false
        1. If not supplied: false
1. "nonIntegerWinningThreshold" optional

    1. the vote threshold used to determine winners can be a non-integer
    1. if true, threshold = V/(S+1) + 10^-d
    1. if false, threshold = floor(V/(S+1)) + 1
    1. where V = total number of votes (in the current round or in the first round, depending on the winnerElectionMode); S = numberOfWinners; and d = decimalPlacesForVoteArithmetic
    1. (note that S+1 in the formulas above becomes just S if hareQuota is set to true.)
    1. Only valid for “multiWinnerAllowOnlyOneWinnerPerRound” and “multiWinnerAllowMultipleWinnersPerRound” contests
    1. value: true | false
    1. if not supplied: false
1. "hareQuota**\***" optional
    1. the winning threshold should be computed using the Hare quota**\*** (floor(votes divided by seats)) instead of the preferred Droop quota (votes divided by (seats+1))
    1. Only valid for “multiWinnerAllowOnlyOneWinnerPerRound” and “multiWinnerAllowMultipleWinnersPerRound” contests
    1. Value: true | false
    1. If not supplied: false
1. "randomSeed" required if tiebreakMode is "random", "previousRoundCountsThenRandom", or "generatePermutation"
    1. the integer seed for the application's pseudorandom number generator
    1. value: \[-140737488355328..140737488355327\]
1. "multiSeatBottomsUpPercentageThreshold" required if winnerElectionMode is "bottomsUpUsingPercentageThreshold" and numberOfWinners is 0
    1. the percentage threshold used to determine when to stop the tabulation and declare winners
    1. note: only valid when winnerElectionMode is "bottomsUpUsingPercentageThreshold" and numberOfWinners is 0
    1. value: \[1..100\]
1. "decimalPlacesForVoteArithmetic" required
    1. number of rounding decimal places when computing winning thresholds and fractional vote transfers
    1. note: only editable when winnerElectionMode is "multiWinnerAllowOnlyOneWinnerPerRound" or "multiWinnerAllowMultipleWinnersPerRound"
    1. value: \[1..20\]
1. "winnerElectionMode" required
    1. which process the program should apply for selecting the winner(s)
    1. value: "singleWinnerMajority" | "multiWinnerAllowOnlyOneWinnerPerRound" | "multiWinnerAllowMultipleWinnersPerRound" | "bottomsUp" | "bottomsUpUsingPercentageThreshold" | "multiPassIrv"
    1. "multiWinnerAllowOnlyOneWinnerPerRound": elect no more than one winner per round, even when there are multiple candidates exceeding the winning threshold (only valid when numberOfWinners is > 1)
        1. Election threshold = floor(V/(S+1)) + 1
        1. where V = total number of votes (in the first round); and S = numberOfWinners
    1. "multiWinnerAllowMultipleWinnersPerRound": may elect more than one winner per round when there are multiple candidates exceeding the winning threshold (only valid when numberOfWinners is > 1)
        1. Election threshold = floor(V/(S+1)) + 1
        1. where V = total number of votes (in the first round); and S = numberOfWinners
    1. "bottomsUp": instead of running a standard multi-seat contest with single transferable votes, just eliminate candidates until there are numberOfWinners remaining (only valid when numberOfWinners is > 1)
        1. Election threshold = floor(V/(S+1)) + 1
        1. where V = total number of votes (in the first round); and S = numberOfWinners
        1. bottomsUp does not rely on election threshold for any vote processing
    1. "bottomsUpUsingPercentageThreshold": instead of running a standard multi-seat contest with single transferable votes, just eliminate candidates until all remaining candidates have vote shares that meet or exceed multiSeatBottomsUpPercentageThreshold (only valid when numberOfWinners is 0)
        1. Election threshold = V•T
        1. where V = total number of votes (in the current round); and T = multiSeatBottomsUpPercentageThreshold
    1. "multiPassIrv": instead of running a true multi-seat contest, run a series of single-seat contests and progressively exclude candidates as they win seats (only valid when numberOfWinners is > 1).
        1. Election threshold = floor(V/(2)) + 1
        1. where V = total number of votes (in the current round)
1. “overvoteRule" required
    1. how the program should handle an overvote when it encounters one
    1. value: "alwaysSkipToNextRank" | "exhaustImmediately" | "exhaustIfMultipleContinuing"
    1. "alwaysSkipToNextRank": when we encounter an overvote, ignore this rank and look at the next rank in the cast vote record
    1. "exhaustIfMultipleContinuing": if more than one candidate in an overvote are continuing, exhaust the ballot; if only one, assign the vote to them; if none, continue to the next rank (not valid with an ES&S source unless overvoteDelimiter is supplied)
