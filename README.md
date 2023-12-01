## Overview
The program is designed to teach the user the capitals of the 50 (so far) states via a flashcard setup.
This program allows a user to create new cards (states and capitals). They can set up a training session, pick the number of cards they'd like to answer  and then see that many cards. For each card, the score is presented after each question is answered.

# Programs needed
peewee, psql sql are all needed.

## Seeding
  There is a seed file that mustbe run from a virtual environment (pipenv). After seeding, thie program is a py file run by python3.
### Schema
The dictionary consists of the 50 states and capitals. Database is called capital. Each entry is a tuple of name and capital.


