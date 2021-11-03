"""Extract the paragraphs and other textual content from the paragraphs of text."""

# TODO: Add the required imports at the top of the file


def extract_lines_including_blanks(input_lines: str) -> List[str]:
    """Extract all of the lines, including the blanks lines."""
    # TODO: extract all of the lines in the file, using splitlines
    # TODO: return all of the extracted lines


def extract_lines_not_including_blanks(input_lines: str) -> List[str]:
    """Extract all of the lines, not including the blanks lines."""
    # TODO: extract all of the lines in the file, using splitlines
    # TODO: filter out all of the blank lines that have a length of zero
    # TODO: return the list of non-blank lines


def extract_paragraphs(input_lines: str) -> List[str]:
    """Extract all of the paragraphs from the lines of textual input."""
    # TODO: implement a function that uses, for instance, regular expressions to
    # break up a provided text in a string as a list of strings, with each
    # string representing a paragraph
    # TODO: consult the following reference:
    # https://stackoverflow.com/questions/53240763/python-how-to-separate-paragraphs-from-text
    # TODO: you may use other online tutorials or responses in your implementation
    # of this function as long as you provide the needed references
    # remove leading and trailing newline characters


def extract_unique_words_paragraphs(paragraphs: List[str]) -> List[Set[str]]:
    """Extract all of the unique words in each one of the paragraphs."""
    # TODO: go through each of the strings inside of the list and
    # extract the unique words in each of the paragraphs
    # TODO: collect the unique words for each paragraph in a set of strings
    # TODO: store each set of unique words in a separate index of a list
    # TODO: return a list that contains at each index a set of strings
    # such that every one of the sets contains the unique words for a paragraph


def extract_unique_words(sets: List[Set[str]]) -> Set[str]:
    """Extract all of the unique words shared across the sets in a list."""
    # TODO: create a single set of strings that includes all of the words
    # that that are unique across all of the sets for each of the paragraphs


def extract_common_words(sets: List[Set[str]]) -> Set[str]:
    """Extract all of the unique words shared in common by sets in a list."""
    # TODO: create a single set of strings that includes all of the words
    # that are found in every one of the sets for each paragraph in the text
    return sets[0].intersection(*sets)
