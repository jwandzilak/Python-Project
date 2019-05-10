def test_possible_kmers:
    example_seq = "ATTTGGATT"
    expected_output = [4,8,7,6,5,4,3,2,1]
    assert expected_output == possible_kmers_function(example_seq)

def test_possible_k_empty():
    """empty list should return empty df

    """
    example_list = []
    expected_df = pd.DataFrame({'possible_k':[]}, index = [])
    assert expected_df.equals(text_list_to_df(example_list))

def test_total_kmers():
    """tests total_kmers function

    """
    example_sequence = 'ATTTGGATT'
    expected_df = pd.DataFrame(
        {'k':[1,2,3,4,5,6,7,8,9], 'observed_kmers':[3,5,6,6,5,4,3,2,1], 'possible_kmers':[4,8,7,6,5,4,3,2,1]},\
        index = [0,1,2,3,4,5,6,7,8]
        )
    assert expected_df.equals(kmers_df(example_sequence))


def test_linguistic_complexity():
    """tests linguistic_complexity function with example sequence

    """
    example_sequence = 'ATTTGGATT'
    expected_output = 0.875
    assert expected_output == linguistic_complexity(example_sequence)
