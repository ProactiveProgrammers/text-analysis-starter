"""Define the command-line interface for the textanalysis program."""

from rich.console import Console

from aitextgen import aitextgen  # type: ignore

from pathlib import Path

from textanalysis import extract
from textanalysis import visualize

import typer

cli = typer.Typer()

console = Console()


@cli.command()
def main(
    input_file: Path = typer.Option(None),
    output_file: Path = typer.Option(None),
    analyze: bool = typer.Option(False, "--analyze"),
    generate: bool = typer.Option(False, "--generate"),
):
    """Automatically generate text and then analyze the words inside of it with sets."""
    # the analyze flag was specified
    if analyze:
        # the file was not specified so we cannot continue using program
        if input_file is None:
            console.print("No output file specified!")
            raise typer.Abort()
        # the file was specified and it is valid so we should analyze it
        if input_file.is_file():
            # break up the text into lines and count the lines, including blank lines
            input_text = input_file.read_text()
            input_line_count = len(extract.extract_lines_including_blanks(input_text))
            console.print(":sparkles: Let's characterize the file and its words!")
            console.print()
            console.print(
                f"\tThe input file contains {input_line_count} lines, including blank lines!"
            )
            # break up the text into lines, exclude blanks, and count the lines
            input_line_count_no_blanks = len(
                extract.extract_lines_not_including_blanks(input_text)
            )
            console.print(
                f"\tThe input file contains {input_line_count_no_blanks} lines, not including blank lines!"
            )
            # break up the text into paragraphs and count the paragraphs
            input_paragraphs = extract.extract_paragraphs(input_text)
            input_paragraphs_count = len(input_paragraphs)
            console.print(
                f"\tThe input file contains {input_paragraphs_count} paragraphs!"
            )
            # create a set of words for each paragraph
            list_of_paragraph_sets = extract.extract_unique_words_paragraphs(
                input_paragraphs
            )
            # extract and display the count of the number of unique words across all of the paragraphs
            unique_words_set = extract.extract_unique_words(list_of_paragraph_sets)
            unique_words_set_count = len(unique_words_set)
            console.print(
                f"\tThe input file contains {unique_words_set_count} unique words across all sets!"
            )
            # extract and display the words that are in common for all of the sets
            common_words_set = extract.extract_common_words(list_of_paragraph_sets)
            console.print(
                f"\tThe words that are found across all sets are: {common_words_set}"
            )
            console.print()
            # visualize the sets and then show all of the computed subsets
            console.print(
                ":paintbrush:  Saving the visualization in graphics/set-visualization.png"
            )
            console.print()
            console.print(":microscope: Get ready, here is the analysis of the sets!")
            console.print()
            set_chunks = visualize.visualize_sets(list_of_paragraph_sets)
            console.print(set_chunks)
    # if the generate flag was specified
    if generate:
        if output_file is None:
            console.print("No output file specified!")
            raise typer.Abort()
        # the file was specified and it is not None so we should write to it
        console.print(":sparkles: Generating text for subsequent analysis!")
        # create a new text generator
        text_generator = aitextgen()
        # generate one segment of text containing multiple paragraphs
        generated_text = text_generator.generate_one()
        # display the text in the terminal window
        console.print()
        console.print(":paintbrush:  Here is the automatically generated text:")
        console.print()
        console.print(generated_text)
        # save the text to the file system in the specified output file
        output_file.write_text(generated_text)
