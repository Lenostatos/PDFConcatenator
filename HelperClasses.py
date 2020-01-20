import abc
import pathlib

import regex


class HeaderExtractor(abc.ABC):
    @abc.abstractmethod
    def extract_header(self) -> str:
        raise NotImplementedError()


class SICFileName(HeaderExtractor):
    def __init__(self, file_path: pathlib.Path):

        self._file_path = file_path

    def extract_header(self) -> str:

        author = self._try_to_identify_authors_name()

        if author is not None:
            return self._format_authors_name(author)
        else:
            return self._sanitize_file_name()

    def _try_to_identify_authors_name(self):

        file_name = self._file_path.stem
        file_name_elements = file_name.split(sep='_')

        if len(file_name_elements) != 3:
            self._print_warning_with_file(file_name)
            print(('Expected three elements separated by underscores but '
                   'found {0} elements.').format(len(file_name_elements)),
                  end='\n')
            return None

        if file_name_elements[0] != 'SIC':
            self._print_warning_with_file(file_name)
            print(('Expected the first element to have the content "SIC" but '
                  'it was "{0}" instead.\n').format(file_name_elements[0]),
                  end='\n')
            return None

        if not len(file_name_elements[1]) == 2:
            self._print_warning_with_file(file_name)
            print(('Expected the second element to contain exactly two '
                   'characters but found {0}.'
                   ).format(len(file_name_elements[1])),
                  end='\n')
            return None

        if not file_name_elements[1].isdigit():
            self._print_warning_with_file(file_name)
            print(('Expected the second element to consist only of digits but'
                   'found "{0}" instead.\n').format(file_name_elements[1]),
                  end='\n')
            return None

        if not file_name_elements[2].isalpha():
            self._print_warning_with_file(file_name)
            print(('Expected the third element to contain only letters but '
                   'found {0} instead.').format(file_name),
                  end='\n')

        if not file_name_elements[2][:2].isupper():
            self._print_warning_with_file(file_name)
            print(('Expected the third element\'s first two letters to be '
                   'upper case but found {0} instead.'
                   ).format(file_name_elements[2]),
                  end='\n')
            return None

        return file_name_elements[2]

    @staticmethod
    def _print_warning_with_file(file_name: str):
        print('Warning with file {0}:'.format(file_name), end='\n')

    @staticmethod
    def _format_authors_name(abbrev_name: str) -> str:

        # Count the capital letters at the beginning of the name
        num_start_capitals = 0
        while abbrev_name[num_start_capitals].isupper():
            num_start_capitals += 1

        # Concatenate each starting capital, except the last, with a dot and a
        # space.
        res_name = ''
        for i in range(num_start_capitals - 1):
            res_name += abbrev_name[i] + '. '

        remaining_name = abbrev_name[(num_start_capitals - 1):]

        in_between_capitals = regex.finditer(
            pattern='[[:lower:]]([[:upper:]])[[:lower:]]',
            string=remaining_name
        )

        for capital in in_between_capitals:
            remaining_name = remaining_name.replace(
                capital.group(0),  # the full match
                capital.group(0)[0] + ' ' + capital.group(0)[1:],
                1
            )

        # Append the rest of the name
        res_name += remaining_name

        return res_name

    def _sanitize_file_name(self) -> str:

        file_name_elements = self._file_path.stem.split(sep='_')

        retainable_elements = [e for e in file_name_elements if
                               not (e.casefold() == 'SIC'.casefold() or
                                    e.isdigit())]

        if len(retainable_elements) > 1:
            return ' '.join(retainable_elements)
        else:
            if retainable_elements[0].isalpha():
                return self._format_authors_name(retainable_elements[0])
            else:
                return retainable_elements[0]
