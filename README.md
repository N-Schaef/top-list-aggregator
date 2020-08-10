# Top List Aggregator
This small script scrapes and aggregates top-X/best lists.
As result all entries are returned, together with how often they occurred together.

## Installation
To use this script you have to install the python dependencies with

```
pip install BeautifulSoup4 argparse requests
```

## Usage
The program supports two command line arguments

 - `--list` (`-l`): Add a URL to a Top-X list
 - `--selector` (`-s`): Add a selector for the list. (See BeautifulSoup selector reference for syntax)

For each list there has to be a selector.

### Examples

For example, if you want to get the best keyboards you could use the following lists:

```
./top-list-aggregator.py \
-l https://www.tomsguide.com/best-picks/best-gaming-keyboard -s ".buying-guide-block h3"  \
-l "https://www.rtings.com/keyboard/reviews/best/by-usage/gaming" -s ".recommendations_block-name" \
-l https://www.pcgamer.com/best-gaming-keyboard/ -s ".buying-guide-block h3" \
-l https://www.techradar.com/news/gaming/10-best-gaming-keyboards-1295703 -s ".buying-guide-block h3" \
-l https://uk.pcmag.com/keyboards/84334/the-best-mechanical-keyboards -s ".review-title" \
-l https://www.rtings.com/keyboard/reviews/best/mechanical -s ".recommendations_block-name" \
-l https://www.eurogamer.net/articles/digitalfoundry-best-mechanical-keyboard-for-gaming-typing-coding-7008 -s "h2" \
-l "https://www.pcgamer.com/best-mechanical-keyboard/" -s ".buying-guide-block > h3"  \
-l "https://www.omnicoreagency.com/best-mechanical-keyboards/" -s "h3 > a"
```
