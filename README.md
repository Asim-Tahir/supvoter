<h1 align="center">Supvoter Reddit Bot</h1>
<p align="center">
  <img src="https://external-preview.redd.it/1LSNsf-YaFwNyoyc87WTE1koBiJZVbmzODo0JBVZ0Fg.png?auto=webp&s=0ef9e07743513eb8b254477cfc840e2bc135fa5d" alt="snoo upvote" alt="snoo upvote"/>
  
  <p align="center">Supvote is crowd upvote bot</p>
</p>

## Installation

1. Rename `praw.example.ini` to `praw.ini` and add crowds upvote bots in `praw.ini`
2. Install dependencies

#### With Poetry
```bash
poetry install
```

#### With Pip
```bash
pip install -r requirements.txt
```

3. Run the bot
#### With Poetry

```bash
poetry run start <submission_url>
```

#### With regular Python

```bash
python main.py <submission_url>
```

### Example usage

#### With Poetry

```bash
poetry run start https://www.reddit.com/r/redditdev/comments/8dmv8z/is_there_no_distinguish_method_for_comments_in/
```

#### With regular Python

```bash
python main.py https://www.reddit.com/r/redditdev/comments/8dmv8z/is_there_no_distinguish_method_for_comments_in/
```
