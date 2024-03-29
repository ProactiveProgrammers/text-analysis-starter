# Text Analysis

TODO: Make sure that you delete all of the TODO markers in this file and either
rewrite or delete all of the prompts. Ultimately, this file should contained
polished writing that is free of mistakes in grammar, spelling, or Markdown
syntax. It should also be a polished article that is suitable for publication on
your professional web site.

TODO: Make sure that your GitHub repository contains the following text files:

- `generated_one.txt`: automatically generated text file
- `generated_two.txt`: automatically generated text file
- `input_one.txt`: human-written text provided as part of this project
- `input_two.txt`: human-written text provided as part of this project

TODO: Make sure that your GitHub repository contains the following graphics files:

- `set-visualization-generated.png`: visualization created by `textanalysis` for the file `generated_one.txt`
- `set-visualization-input.png`: visualization created by `textanalysis` for the file `input_one.txt`

TODO: You must use a command like `git add` to ensure that certain files exist in the repository.

## Add Your Name Here

## Program Input and Output

### What is the output from running the following command?

TODO: Use a fenced code block to provide the output for this command.

`poetry run textanalysis --input-file text/input_one.txt --analyze`

### What is the output from running the following command?

TODO: Use a fenced code block to provide the output for this command.

`poetry run textanalysis --input-file text/generated_one.txt --analyze`

### What is inside of the `generated_two.txt` file in the GitHub repository?

TODO: Use a fenced code block to provide the contents of the file.

### What is inside of the `input_two.txt` file in the GitHub repository?

TODO: Use a fenced code block to provide the contents of the file.
TODO: You should download and save a short text segment written by another person.
TODO: Alternatively, you can write your own text that you want to analyze.

## Source Code

### Describe in detail how the source code in the `textanalysis` works

#### Please explain each line of source code from the `extract` module

TODO: Write at least one paragraph to explain the following source code

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

#### Pick one snippet of Python source code that you wrote in the `extract.py` module and explain how it works

TODO: Write at least one paragraph to explain the source code code that you selected

## Analyzing the Text

NOTE: The analysis described in this reflection file only requires you to study
the output of `textanalysis` when run with the files called `input_one.txt` and
`input_two.txt`. With that said, you should make sure that the program also
works correctly when it is run with other input files! Please note that the
output of the `textanalysis` includes both the words that you see in the
terminal window and the `png` files stored in the `graphics/` directory.

### According to the output of your program, what words does `input_one.txt` have in common across all paragraphs? How did you know?

TODO: Provide response to this question, demonstrating your knowledge of the use and visualization of sets.

### Using the console output and visualization for the `input_one.txt`, what trends do you see? Interpret these trends.

TODO: Provide response to this question, demonstrating your knowledge of the use and visualization of sets.

### Using the console output and visualization for the `generated_one.txt`, what trends do you see? Interpret these trends.

TODO: Provide response to this question, demonstrating your knowledge of the use and visualization of sets.

## Professional Development

### What are the similarities and differences between `set`, `FrozenSet`, and `FiniteSet`?

TODO: Provide a response to this question, explaining these three implementations of the set discrete structure.
TODO: Please refer to your notes, the course text book, and online resources to answer this question.
TODO: If you refer to online resources, please make sure to cite them in your response.

### How is the `set` discrete structure similar to and different from the `list` and the `tuple` discrete structures?

TODO: Provide a response to this question, leveraging your course notes and the Proactive Programmers web site.

### At your own option, do you have any other insights to share about this assignment?

TODO: At your own option, provide further insights about this assignment!
