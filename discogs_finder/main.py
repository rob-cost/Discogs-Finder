# Notes
# If release has no video prints empty array

import discogs_client
import os

from dotenv import load_dotenv
from .data.countries import COUNTRIES
from .data.styles import ELECTRONIC_STYLES
from .input.prompts import (
    STYLE_PROMPT,
    COUNTRY_PROMPT,
    YEAR_PROMPT,
    WANTS_PROMPT,
    FILE_NAME_PROMPT,
)
from .input.validators import get_string, get_year, get_int
from .utils.helpers import filter_list


def main():

    load_dotenv()
    user_token = os.getenv("DISCOGS_API_TOKEN")

    # Initialize the Discogs client with a user token
    d = discogs_client.Client("ExampleApplication/0.1", user_token=user_token)

    # Get user inputs
    style = get_string(STYLE_PROMPT, allowed={s.lower() for s in ELECTRONIC_STYLES})
    country = get_string(COUNTRY_PROMPT, allowed={c.lower() for c in COUNTRIES})
    year = get_year(YEAR_PROMPT)
    want = get_int(WANTS_PROMPT)
    file_name = get_string(FILE_NAME_PROMPT)

    # Get releases based on user inputs
    releases = d.search(
        type="release",
        genre="electronic",
        format="vinyl",
        style=style,
        year=year,
        country=country,
    )

    # Extract release IDs from the fetched releases
    releases_ids = [release.id for release in releases.page(1)]

    # Create a desktop file path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, file_name + ".html")
    with open(file_path, "w") as f:
        f.write(
            f"Search for releases with style: {style}, country: {country}, year: {year}, want less than: {want}<br><br>\n"
        )
        f.close()

    # Filter list based on parameters annd write to file
    filter_list(d, releases_ids, want, style, file_path)


if __name__ == "__main__":
    main()
