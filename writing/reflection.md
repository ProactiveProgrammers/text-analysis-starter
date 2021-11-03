# Text Analysis

## Add Your Name Here

## Program Input and Output

### What is the output from running the following command?

TODO: Use a fenced code block to provide the output for this command.

`poetry run textanalysis --output-file text/generated_two.txt --generate`

### What is the output from running the following command?

TODO: Use a fenced code block to provide the output for this command.

`poetry run textanalysis --input-file text/input_one.txt --analyze`

### What is the output from running the following command?

TODO: Use a fenced code block to provide the output for this command.

`poetry run textanalysis --input-file text/generated_one.txt --analyze`

### What is inside of the `generated_two.txt` file that your tool created?

TODO: Use a fenced code block to provide the contents of the file.

### What is inside of the `input_two.txt` file that you downloaded and saved?

TODO: Use a fenced code block to provide the contents of the file.
TODO: You should download and save a short text segment written by another person

## Source Code

### Describe in detail how your provided source code works

#### Please explain each line of source code from the `extract` module

TODO: Write at least one paragraph to explain the requested source code

```python
def extract_paragraphs(input_lines: str) -> List[str]:
    """Extract all of the paragraphs from the lines of textual input."""
    # Reference:
    # https://stackoverflow.com/questions/53240763/python-how-to-separate-paragraphs-from-text
    no_newlines = input_lines.strip("\n")
    split_text = NEWLINES_RE.split(no_newlines)
    paragraphs = [p + "\n" for p in split_text if p.strip()]
    return paragraphs
```

## Analyzing the Text

### According to the output of your program, what words does `input_one.txt` have in common across all paragraphs? How did you know?

TODO: Provide response to this question, demonstrating your knowledge of the use and visualization of sets.

### Using the console output and visualization for the `input_one.txt`, what trends do you see? Interpret these trends.

TODO: Provide response to this question, demonstrating your knowledge of the use and visualization of sets.

### Using the console output and visualization for the `generated_one.txt`, what trends do you see? Interpret these trends.

TODO: Provide response to this question, demonstrating your knowledge of the use and visualization of sets.

## Professional Development

### What are the similarities and differences between `set`, `FrozenSet`, and `FiniteSet`?

TODO: Provide a response to this question, explaining these three implementations of the set discrete structure.

### At an intuitive and informal level what is the `aitextgen` package and how does it work?

TODO: Provide a response to this question, leveraging the documentation for this tool on sites like GitHub.

### At your own option, do you have any other insights to share about this assignment?

TODO: At your own option, provide further insights about this assignment!
