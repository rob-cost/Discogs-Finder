# Notes
# If release has no video prints empty array

import discogs_client
import os

from dotenv import load_dotenv
from .data.countries import COUNTRIES
from .data.styles import ELECTRONIC_STYLES
from .input.prompts import (
    STYLE_PROMPT,
    INCLUDE_MORE_STYLES,
    COUNTRY_PROMPT,
    YEAR_PROMPT,
    WANTS_PROMPT,
    HAVE_PROMPT,
    FILE_NAME_PROMPT,
)
from .input.validators import get_string, get_year, get_int, get_bool
from .utils.helpers import filter_list


def main():

    load_dotenv()
    user_token = os.getenv("DISCOGS_API_TOKEN")

    # Initialize the Discogs client with a user token
    d = discogs_client.Client("ExampleApplication/0.1", user_token=user_token)

    # Get user inputs
    style = get_string(STYLE_PROMPT, allowed={s.lower() for s in ELECTRONIC_STYLES})
    include_style = get_bool(INCLUDE_MORE_STYLES)
    country = get_string(COUNTRY_PROMPT, allowed={c.lower() for c in COUNTRIES})
    year = get_year(YEAR_PROMPT)
    have = get_int(HAVE_PROMPT)
    want = get_int(WANTS_PROMPT)
    file_name = get_string(FILE_NAME_PROMPT)

    # Create arguments for the search
    search_params = {
        "type": "release",
        "genre": "electronic",
        "format": "vinyl",
        "year": year,
        "style": style,
    }

    if country:
        search_params["country"] = country

    # Fetch releases
    try:
        releases = d.search(
            **search_params
        )  # ** turn each key/value into named argument
    except Exception as e:
        print(f"Error fetching releases: {e}")
        return

    # Extract release IDs from the fetched releases
    try:
        releases_ids = [release.id for release in releases]
        print(f"Total releases found: {len(releases_ids)}")
    except Exception as e:
        print(f"Error extracting release IDs: {e}")
        return

    # Create a desktop file path
    try:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, file_name + ".html")
        with open(file_path, "w") as f:
            f.write(
                f"Search for releases with style: {style}, country: {country}, year: {year}, want less than: {want}, have less than: {have}<br><br>\n"
            )
            f.close()
    except Exception as e:
        print(f"Error creating file path: {e}")
        return

    # Filter list based on parameters annd write to file
    filter_list(d, releases_ids, want, have, style, include_style, file_path)


if __name__ == "__main__":
    main()
