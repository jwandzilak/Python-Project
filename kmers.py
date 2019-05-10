import sys
import pandas as pd
import plotnine as p9

example_seq = "ATTTGGATT"

 def open_seq_file(seq_file):
    with open(seq_file,'r') as current_file:
        seq = current_file.read()

def possible_kmers_function(seq):
"""
Will return a list of possible kmers for a given sequence
"""
    seq_length = len(seq)

    possible_kmers = []
    for k in range(1,(seq_length+1)):
        if k == 1:
            kmers = 4
        else:
            kmers = (seq_length - k)+1
        possible_kmers.append(kmers)

    return(possible_kmers)

def observed_kmers_function(seq, k):
    """Count kmer occurrences in a given read with a specified k value


    """

    observed_k = {}

    observed = len(seq) - k + 1

    for i in range(observed):

        kmer = seq[i:i+k]

        if kmer not in observed_k:
            observed_k[kmer] = 0

        observed_k[kmer] += 1

    return observed_k

def total_kmers(seq):
"""This function will produce a pandas dataframe with the k values, observerd kmers, and possible kmers_df
for a given sequence 

"""
    seq_length = len(seq)

    possible_k = []
    for k in range(1,(seq_length+1)):
        if k == 1:
            kmers = 4
        else:
            kmers = (seq_length - k)+1

        possible_k.append(kmers)


    observed_kmers = []
    for x in range(1,(seq_length+1)):
        observed_k = {}

        observed = len(seq) - x + 1

        for i in range(observed):

            kmer = seq[i:i+x]

            if kmer not in observed_k:
                observed_k[kmer] = 1
            else:
                observed_k[kmer] += 1

        observed_kmers.append(len(observed_k))


    print(observed_kmers)



    kmers_df = pd.DataFrame(
 {'k':range(1,seq_length+1),
   'possible_kmers':possible_k,
   'observed_kmers':observed_kmers
 }
)

    return kmers_df


def linguistic_complexity(kmers_df):
"""This function will determine the linguistic complexity of a seqeuence using the dataframe

"""
    total_possible= plot_example['possible_kmers'].sum()
    total_observed = plot_example['observed_kmers'].sum()
    linguistic_complexity = (total_observed/total_possible)
    return linguistic_complexity

print(linguistic_complexity(kmers_df))

def make_plot(kmers_df,filename):


    plot = p9.ggplot(data = kmers_df,
             mapping = p9.aes(x = 'k',
                         y = 'observed_kmers/possible_kmers')) + \
    p9.geom_point()

    plot.save(filename+"kmers_plot.pdf")

if __name__ == '__main__':
    seq = sys.argv[1]
    jw_kmers_df = kmers_df(seq)
    jw_linguistic_complexity = linguistic_complexity(seq)
    print(jw_kmers_df.iloc[0:5])
    print('The linguistic complexity is', jw_linguistic_complexity)
    make_plot(kmers_df,filename)
