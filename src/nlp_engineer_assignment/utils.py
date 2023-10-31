import numpy as np


def count_letters(text: str) -> np.array:
    """
    Count the number of times each letter appears in the text up to that point

    Parameters
    ----------
    text : str
        The text to count the letters in

    Returns
    -------
    np.array
        A vector of counts, one for each letter in the text
    """
    output = np.zeros(len(text), dtype=np.int32)
    for i in range(0, len(text)):
        output[i] = min(2, len([c for c in text[0:i] if c == text[i]]))

    return output


def print_line():
    """
    Print a line of dashes
    """
    print("-" * 80)


def read_inputs(path: str) -> list:
    """
    Read the inputs from a file

    Parameters
    ----------
    path : str
        Path to the file

    Returns
    -------
    list
        A list of strings, one for each line in the file
    """
    lines = [line[:-1] for line in open(path, mode="r")]
    print(f"{len(lines)} lines read")
    print_line()
    return lines


def score(
    golds: np.array,
    predictions: np.array
) -> float:
    """
    Compute the accuracy of the predictions

    Parameters
    ----------
    golds : np.array
        Ground truth labels
    predictions : np.array
        Predicted labels

    Returns
    -------
    float
        Accuracy of the predictions
    """
    return float(np.sum(golds == predictions)) / len(golds.flatten())
