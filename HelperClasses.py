import abc
import pathlib

import regex


class HeaderExtractor(abc.ABC):
    @abc.abstractmethod
    def __init__(self, file_path: pathlib.Path):
        pass

    @abc.abstractmethod
    def extract_header(self) -> str:
        raise NotImplementedError()


class SICFileName(HeaderExtractor):
    def __init__(self, file_path: pathlib.Path):
        super().__init__(file_path)
        self._file_name = file_path.stem
        self._file_name_elements = file_path.stem.split(sep='_')

    def matches_pattern(self) -> bool:
        if len(self._file_name_elements) != 3:
            return False

        if self._file_name_elements[0] != 'SIC':
            return False

        if not len(self._file_name_elements[1]) == 2:
            return False

        if not self._file_name_elements[1].isdigit():
            return False

        if not self._file_name_elements[2][:2].isupper():
            return False

        return True

        # return regex.fullmatch(
        #     pattern='SIC_0[1-4]_[[:upper:]]{2,}[[:lower:]]*',
        #     string=self._file_name
        # )

    def extract_header(self) -> str:
        if self.matches_pattern():
            return self.get_authors_name()
        else:
            return self.get_sanitized_file_name()

    def get_authors_name(self) -> str:
        authors_name = self._file_name_elements[-1]

        if not self.matches_pattern():
            return authors_name
        else:
            # Count the capital letters at the beginning of the name
            num_start_capitals = 0
            while authors_name[num_start_capitals].isupper():
                num_start_capitals += 1

            res_authors_name = ''
            for i in range(num_start_capitals - 1):
                res_authors_name += authors_name[i] + '. '

            res_authors_name += authors_name[(num_start_capitals - 1):]

            return res_authors_name

    def get_sanitized_file_name(self) -> str:
        elements_copy = self._file_name_elements.copy()

        for i, element in enumerate(elements_copy):
            if element == 'SIC' or element.isdigit():
                elements_copy.pop(i)

        if len(elements_copy) > 1:
            return ' '.join(elements_copy)
        else:
            return elements_copy[0]

    def print_mismatch_reasons_to_console(self):
        reasons = ''

        num_elements = len(self._file_name_elements)
        if num_elements != 3:
            reasons += ('Expected three elements separated by underscores but '
                        'found {0}.\n').format(num_elements)

        first_element = self._file_name_elements[0]
        if first_element != 'SIC':
            reasons += ('Expected the first element to have the content "SIC" '
                        'but it was "{0}" instead.\n').format(first_element)

        if num_elements >= 2:
            second_element = self._file_name_elements[1]
            if not len(second_element) == 2:
                reasons += ('Expected the second element to contain exactly '
                            'two characters but found {0}.\n'
                            ).format(len(second_element))
            if not second_element.isdigit():
                reasons += ('Expected the second element to consist only of '
                            'digits but found "{0}" instead.\n'
                            ).format(second_element)

        print(reasons)
