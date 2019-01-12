"""
SYSC 1005 A Fall 2017
Case study: iterative, incremental development of a function that uses
Python's str, list, and set types.
"""
import string

# For information about the string module, type help(string) at the shell 
# prompt, or browse the Library Reference, Section 6.1, in the Python 3.5.2 
# documentation (available @ python.org).


def build_word_list(filename):
    """ (str) -> list of str
    
    Return a list of all the distinct words in the specified file,
    sorted in ascending order.
    
    >>> word_list = build_word_list('sons_of_martha.txt')
    >>> word_list
    >>> len(word_list)  # How many different words are in the file?
    """
    
    infile = open(filename, "r")
    word_set = set()

    for line in infile:

        # Split each line into a list of words.
        # By default, the split method removes all whitespace; e.g.,
        # '  Hello,    world!   '.split() returns this list:
        #
        # ['Hello,', 'world!']
        #
        # and not:
        #
        # ['  Hello,', '    world!   ']
        #
        # Notice that the punctuation marks have not been removed.
        
        word_list = line.split()

        # For each word, first remove any leading or trailing punctuation,
        # then convert the the word to lower case.
        #
        # Examples: 
        #  'Hello,'.strip(string.punctuation) returns 'Hello'.
        #  'Hello'.lower() returns 'hello'.
        
        for word in word_list:
            word = word.strip(string.punctuation).lower()
            
            # This statement is equivalent to: 
            # word = word.strip(string.punctuation)
            # word = word.lower()

            # Don't save any empty strings that were created when the 
            # punctuation marks were removed.
            # For example, if word is bound to a hyphen, '-',
            # word.strip(string.punctuation) yields the empty string, ''.
            
            if word != '':
                # Storing the words in a set discards any duplicates.
                word_set.add(word)

    # Now build the list of distinct words.  
    word_list = list(word_set)
    
    # or,
    # word_list = []
    # for word in word_set:
    #    word_list.append(word)

    # Sort the list into ascending order.
    word_list.sort()
    
    return word_list
