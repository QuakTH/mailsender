import json
import os
import re
from typing import TYPE_CHECKING, Optional, Set

if TYPE_CHECKING:
    from gui.new_main_widget import MainWidget


class TemplateProcess:
    def __init__(self, main_widget: "MainWidget"):
        self.main_widget = main_widget
        self.__file_path: Optional[str | os.PathLike] = None
        self.__place_holders: Set[str] = set()

    def set_file_path(self, file_path: str | os.PathLike):
        """Set the `__file_path` variable.

        :param str | os.PathLike file_path: Path to file. (must be a .txt file)
        """
        self.__file_path = file_path

    @property
    def file_path_set(self) -> bool:
        """Check if the `__file_path` variable is set.

        :return: Whether the __file_path variable is set.
        """
        return self.__file_path is not None

    def extract_place_holders(self):
        """Search the file in `file_path` and add place holder elements.
        Place holders must look like this:
        - ${{<name>}}

        """
        if self.__file_path:
            with open(self.__file_path, "rt") as f:
                self.__place_holders = set(re.findall(r"\${{(\w+)}}", f.read()))

    @property
    def place_holders(self):
        """Return the private __place_holder variable."""
        return self.__place_holders

    def set_email_example(self):
        """Set the email_example output.
        1. If the candidate files are not loaded, only show the raw text.
        2. If the candidate files are set. And there are candidate rows, the placeholders will be
           changed to the matching candidate value.
        """
        if self.__file_path:
            with open(self.__file_path, "rt") as f:
                text = f.read()

            if self.main_widget.candidate_process.candidate_df is not None:
                json_format = self.main_widget.candidate_process.candidate_df.iloc[0].to_json(force_ascii=False)

                for key, value in json.loads(json_format).items():
                    if key not in self.main_widget.candidate_process.MANDATORY_KEYS:
                        text = text.replace(f'${{{{{key}}}}}', value)

            self.main_widget.email_example.setText(text)

    @property
    def template(self) -> str:
        """Return the template string.

        :return: Template string.
        """
        with open(self.__file_path, "rt") as f:
            return f.read()
