import os
from typing import TYPE_CHECKING, Optional, Set

import pandas as pd

from exceptions import CustomException

if TYPE_CHECKING:
    from gui.new_main_widget import MainWidget


class CandidateProcess:
    MANDATORY_KEYS = {"email", "title"}

    def __init__(self, main_widget: "MainWidget"):
        self.main_widget = main_widget
        self.__file_path: Optional[str | os.PathLike] = None
        self.__candidate_df: Optional[pd.DataFrame] = None

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

    def load_dataframe(self) -> None:
        """Read the file as a Pandas dataframe.
        Check whether the columns of the dataframe matches the `place_holders` from the TemplateProcess instance.
        """
        file_extension = os.path.splitext(self.__file_path)[1]

        if file_extension == ".csv":
            self.__candidate_df = pd.read_csv(self.__file_path)
        else:
            self.__candidate_df = pd.read_excel(self.__file_path)

        if len(self.__candidate_df) == 0:
            raise CustomException("Candidate data is empty.")

        candidate_col_set = set(self.__candidate_df.columns)

        # Check columns
        check_mandatory_key_set = self.MANDATORY_KEYS - candidate_col_set
        if check_mandatory_key_set:
            raise CustomException(
                f"Candidate files must contain `{', '.join(check_mandatory_key_set)}` columns."
            )

        candidate_col_set -= self.MANDATORY_KEYS
        check_template_place_holders = (
                candidate_col_set - self.main_widget.template_process.place_holders
        )
        if check_template_place_holders:
            raise CustomException(
                f"Template file doesn't have place holders `{', '.join(check_template_place_holders)}`"
            )

        check_candidate_columns = (
                self.main_widget.template_process.place_holders - candidate_col_set
        )
        if check_candidate_columns:
            raise CustomException(
                f"Template file doesn't have place holder `{', '.join(check_candidate_columns)}`"
            )

    @property
    def candidate_df(self):
        """Return __candidate_df variable."""
        return self.__candidate_df
