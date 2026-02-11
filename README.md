# Discogs Finder

**Discogs Finder** is a Python CLI application that enhances the Discogs search experience for electronic music collectors.

The official Discogs search is powerful, but it becomes difficult when you want precise control over things like rarity, popularity, or strict style combinations.

This tool adds an extra layer of filtering on top of the Discogs API, allowing users to define advanced rules and automatically receive direct URLs to matching releases.

---

## Features

- Filter releases by:
  - **Style** (single or multiple)

  - **Country** of release

  - **Year or range of years**

  - **Community want count** (how many users want it)

  - **Community have count** (how many users have it)

- Only returns releases that match the exact styles you choose

- Works entirely in the terminal — no web interface required

- Uses your Discogs API token for authenticated requests

- Automatically saves results to an HTML file with clickable links

---

## Tech-Stack

- Python 3.11+

- python3-discogs-client

- python-dotenv

- CLI / terminal interface

---

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd discogs-finder
```

2. Create and activate venv

```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

3. Create a .env file with your Discogs API Token

```bash
DISCOGS_API_TOKEN=your_token_here
```

4. Run

```bash
discogs-finder
```

---

## Example Use Case

User wants:

- Techno

- Germany

- 1995

- max 50 people want

- max 200 people have

The program prints matching release URLs and stores them in a result file.
