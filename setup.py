from typing import List

class FileReaderAndWriter:
    """
    Handles reading in and writing out of files.
    """

    def __init__(self, filepath: str) -> None:
        """
        Initializes the FileReaderAndWriter object
        """
        self.filepath = filepath
        self.lines = []

    def read_lines(self) -> List[str]:
        """
        Reads in the lines from the file
        """
        if not self.lines:
            try:
                with open(self.filepath) as f:
                    self.lines = [line.strip("\n") for line in f.readlines]
            except:
                raise IOError("Cannot open file")
        return self.lines

    def flush_lines(self, filepath_out) -> List[str]:
        """
        Flushes the lines to f_out, storing all the data on disk.
        """
        if not filepath_out:
            filepath_out = self.filepath
        with open(filepath_out, "w") as f:
            f.writelines(self.lines)
