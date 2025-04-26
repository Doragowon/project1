import csv
import sys
import pandas as pd

def main():

    # TODO: Check for command-line usage
        if archive == csv arguments = 2
        print(name_match)


    # TODO: Read database file into a variable
df = pd.read_csv("small.csv")

   subsequence[] = {AGATC =0
             TTTTTTCT=0
             AATG=0
             TCTAG,=0
             GATA,=0
             TATC,=0
             GAAA,=0
             TCTG=0

   }
    subsequence = sub


    # TODO: Read DNA sequence file into a variable
seq = todict(txt)

    # TODO: Find longest match of each STR in DNA sequence
   longest_match(seq,subsequence[i]) += subsequence

    # TODO: Check database for matching profiles
    if df.columnn sequences == int(subsequence(i))
    printf(df.column = names)

    return names


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
