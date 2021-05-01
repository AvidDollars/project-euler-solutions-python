"""
used for automatic injection of problem description
straight into the working file
"""

import requests
from numbers import Integral
import re


class problem:
    # regex for extraction description from Euler site
    PROBLEM_DESCRIPTION_REGEX = re.compile(r'(?:<div class="problem_content".*?<p>)(.*?)(?:</div>)', flags=re.DOTALL)
    BASE_URL = "https://projecteuler.net"

    def __init__(self, problem_number):
        assert isinstance(problem_number, Integral), "must be an integer"
        assert problem_number > 0, "must be a positive number"
        self.num = problem_number
        self.page = self._problem_exists(problem_number)
        self._extracted_description = None

    def __repr__(self):
        url = f"{self.BASE_URL}/problem={self.num}"
        if self._extracted_description is None:
            self._extract_problem_description()
        description = "\n".join(self._extracted_description)
        return "\n".join([url, description])

    def inject(self):
        #TODO: implement injection mechanism
        return NotImplemented

    def _additional_cleanup(self):
        #TODO: for getting rid of html tags inside parsed text (eg. problem number 5)
        return NotImplemented

    def _problem_exists(self, num):
        url_to_go = f"{self.BASE_URL}/problem={num}"
        if not requests.get(url_to_go).url == url_to_go:
            raise ValueError("problem does not exists")
        return requests.get(url_to_go)

    def _extract_problem_description(self):
        if self._extracted_description is None:
            extracted_text = self.PROBLEM_DESCRIPTION_REGEX.search(self.page.content.decode("utf8")).group(1)
            extracted_and_splitted = extracted_text.split("\n")

            self._extracted_description = [
                string.lstrip("<p>").rstrip("</p>")
                for string in extracted_and_splitted
                if string != ""]
        return
