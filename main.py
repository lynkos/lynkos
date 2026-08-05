"""
Generates a terminal animation sequence (.gif) for GitHub Profile using `github-readme-terminal`

1. Generate a fine-grained personal access token (https://github.com/settings/tokens):
    * Repository access: ALL
    * Permissions: Contents (read-only), Metadata (read-only)

2. Create `.env` file in the root directory with the following content:
    ```
    GITHUB_TOKEN=your_github_token_from_step_1
    ```

3. Go to your GitHub Profile's repository settings --> Secrets and variables --> Actions --> New repository secret:
    * Name: `READ_STATS_TOKEN`
    * Secret: your_github_token_from_step_1

4. Update the constants below as needed

5. Run the script:
    ```
    python main.py
    ```

6. If successful, the generated GIF will be saved in the root directory

7. Add generated GIF to your GitHub Profile README.md:
    ```markdown
    ![Profile statistics card](output.gif)
    ```
    OR
    ```html
    <img alt="Profile statistics card" src="output.gif">
    ```

8. For more info and customization options, refer to the documentation:
    https://github.com/x0rzavi/github-readme-terminal
"""
from gifos import Terminal
from gifos.utils import fetch_github_stats
from datetime import datetime
from zoneinfo import ZoneInfo
from random import randint

USERNAME = "lynkos"
"""GitHub username"""

EXPERIENCE = [ "Oracle Cloud (OCI)", "Analytics for Cyber Defense (ACyD) Lab" ]
"""Work experience"""

FOCUS = [ "Infrastructure", "Distributed Systems", "Backend", "Cloud", "Platform" ]
"""Areas of focus"""

INTERESTS = [ "Research", "Cybersecurity", "AI/ML", "Edge Computing", "Quantum Computing" ]
"""Areas of interest"""

ROLE = "Software Engineer"
"""Current role"""

UNIVERSITY = "Florida International University (FIU)"
"""University attended (or currently attending)"""

DEGREE = "Computer Science, B.S."
"""Degree obtained (or currently pursuing)"""

ZONE = ZoneInfo("America/New_York")
"""Timezone"""

INFO_DISPLAY_TIME = 500
"""How long the info section is displayed"""

WIDTH = 750
"""Terminal width"""

HEIGHT = 500
"""Terminal height"""

PADDING = 15
"""Terminal padding"""

FONT_SIZE = 16
"""Terminal font size"""

SPEED = 1
"""Typing speed"""

COUNT = 5
"""Number of times to generate text"""

VERSION = "2.1.0"
"""Version of the script"""

GIT_COMMIT_MESSAGE = "aspiring multidisciplinary"
"""Git commit message"""

USER_DETAILS = fetch_github_stats(USERNAME, include_all_commits = True)
"""User details fetched from GitHub, including stats like followers, stars, commits, languages, etc."""

def red(text: str | int) -> str:
    """
    Formats text in red using ANSI escape codes

    Args:
        text (str | int): Text to format

    Returns:
        str: Red input text formatted with ANSI escape code
    """
    return f"\x1b[31m{text}\x1b[0m"

def green(text: str | int) -> str:
    """
    Formats text in green using ANSI escape codes

    Args:
        text (str | int): Text to format

    Returns:
        str: Green input text formatted with ANSI escape code
    """
    return f"\x1b[32m{text}\x1b[0m"

def yellow(text: str | int) -> str:
    """
    Formats text in yellow using ANSI escape codes

    Args:
        text (str | int): Text to format

    Returns:
        str: Yellow input text formatted with ANSI escape code
    """
    return f"\x1b[33m{text}\x1b[0m"

def blue(text: str | int) -> str:
    """
    Formats text in blue using ANSI escape codes

    Args:
        text (str | int): Text to format

    Returns:
        str: Blue input text formatted with ANSI escape code
    """
    return f"\x1b[34m{text}\x1b[0m"

def magenta(text: str | int) -> str:
    """
    Formats text in magenta using ANSI escape codes

    Args:
        text (str | int): Text to format

    Returns:
        str: Magenta input text formatted with ANSI escape code
    """
    return f"\x1b[35m{text}\x1b[0m"

def cyan(text: str | int) -> str:
    """
    Formats text in cyan using ANSI escape codes

    Args:
        text (str | int): Text to format

    Returns:
        str: Cyan input text formatted with ANSI escape code
    """
    return f"\x1b[36m{text}\x1b[0m"

def bright_red(text: str | int) -> str:
    """
    Formats text in bright red (aka orange) using ANSI escape codes

    Args:
        text (str | int): Text to format

    Returns:
        str: Bright red (aka orange) input text formatted with ANSI escape code
    """
    return f"\x1b[91m{text}\x1b[0m"

def bright_magenta(text: str | int) -> str:
    """
    Formats text in bright magenta (aka purple) using ANSI escape codes

    Args:
        text (str | int): Text to format

    Returns:
        str: Bright magenta (aka purple) input text formatted with ANSI escape code
    """
    return f"\x1b[95m{text}\x1b[0m"

def format_list(items: list[str]) -> str:
    """
    Formats list of strings as string delimited by " · "

    Args:
        items (list[str]): List of strings to format

    Returns:
        str: Formatted string
    """
    return (" · ").join(items)

def list_languages() -> list[str]:
    """
    Formats top programming languages as color-coded list of strings

    Returns:
        list[str]: Color-coded list of top languages with usage percentage
    """
    languages = [ ]
    
    for language, percent in USER_DETAILS.languages_sorted:
        if language == "Jupyter Notebook": language = "Jupyter"

        lang = f"{bright_magenta(language)} ({yellow(f'{percent}%')})"
        languages.append(lang)

    return languages

def profile_details() -> str:
    """
    Formats profile details as color-coded string:
    1. User information
        * Role
        * Experience
        * Focus areas
        * University
        * Degree
    2. GitHub stats
        * User rating
        * Followers count
        * Total stars
        * Total commits
        * Pull requests
        * Contributions count
    3. Top languages

    Returns:
        str: Formatted string containing profile details
    """
    top_languages = list_languages()

    return f"""
{magenta(f"User Profile")}
--------------
{bright_magenta("Role")}:           {yellow(ROLE)}
{bright_magenta("Experience")}:     {format_list([yellow(experience) for experience in EXPERIENCE])}
{bright_magenta("Focus")}:          {format_list([yellow(focus) for focus in FOCUS])}
{bright_magenta("Interests")}:      {format_list([yellow(interest) for interest in INTERESTS])}
{bright_magenta("University")}:     {yellow(UNIVERSITY)}
{bright_magenta("Degree")}:         {yellow(DEGREE)}

{magenta("GitHub Stats")}
--------------
{bright_magenta("User Rating")}:    {yellow(USER_DETAILS.user_rank.level)}
{bright_magenta("Followers")}:      {yellow(USER_DETAILS.total_followers)}
{bright_magenta("Total Stars")}:    {yellow(USER_DETAILS.total_stargazers)}
{bright_magenta("Total Commits")}:  {yellow(USER_DETAILS.total_commits_all_time)}
{bright_magenta("Pull Requests")}:  {yellow(USER_DETAILS.total_pull_requests_made)}
{bright_magenta("Contributions")}:  {yellow(USER_DETAILS.total_repo_contributions)}

{magenta("Top Languages")}
--------------
{format_list(top_languages[:5])}
{format_list(top_languages[5:10])}
    """

def login(t: Terminal):
    """
    Simulates login sequence:
    1. Username
    2. Password
    3. "Last login" message with random tty

    Args:
        t (Terminal): Terminal instance
    """
    t.toggle_show_cursor(False)
    t.gen_text(bright_red(f"{USERNAME.upper()} v{VERSION}"), t.curr_row, count = COUNT)

    t.curr_row += 2
    
    t.gen_text("login: ", t.curr_row, count = COUNT)
    t.toggle_show_cursor(True)
    t.gen_typing_text(USERNAME, t.curr_row, speed = SPEED, contin = True)
    t.toggle_show_cursor(False)

    t.curr_row += 1
    
    t.gen_text("password: ", t.curr_row, count = COUNT)
    t.toggle_show_cursor(True)
    t.gen_typing_text("*******", t.curr_row, speed = SPEED, contin = True)
    t.toggle_show_cursor(False)

    t.curr_row += 2

    time_now = datetime.now(ZONE).strftime("%a %b %d %H:%M:%S")
    t.gen_text(f"Last login: {time_now} on {f"tty00{randint(0, 9)}"}", t.curr_row)

def clear(t: Terminal):
    """
    Simulates clearing terminal screen with `clear` command

    Args:
        t (Terminal): Terminal instance
    """
    t.curr_row += 1
    
    t.set_prompt(f"{cyan(USERNAME)}@{green('localhost:')}{red('~')}$ ")
    t.gen_prompt(t.curr_row, count = COUNT)
    
    t.toggle_show_cursor(True)
    t.gen_typing_text(blue("clear"), t.curr_row, speed = SPEED, contin = True)
    
    t.clear_frame()

def fetch(t: Terminal):
    """
    Simulates fetching data with `fetch.sh -u {USERNAME}` command
    (i.e. script that fetches user's GitHub stats)

    Args:
        t (Terminal): Terminal instance
    """
    t.gen_prompt(t.curr_row, count = COUNT)
    
    t.gen_typing_text(blue("fetch.sh"), t.curr_row, contin = True, speed = SPEED)

    prompt_col = t.curr_col
    t.gen_typing_text(cyan(" -"), t.curr_row, contin = True, speed = SPEED)
    t.delete_row(t.curr_row, prompt_col)
    t.gen_text(bright_red(" -u"), t.curr_row, count = 3, contin = True)

    t.gen_typing_text(f" {cyan(USERNAME)}", t.curr_row, speed = SPEED, contin = True)

def info(t: Terminal):
    """
    Prints GitHub stats

    Args:
        t (Terminal): Terminal instance
    """
    t.curr_row += 1
    t.gen_text(profile_details(), t.curr_row)

def final(t: Terminal):
    """
    Prints final message

    Args:
        t (Terminal): Terminal instance
    """
    t.gen_prompt(t.curr_row, count = COUNT)

    t.gen_typing_text(blue("git"), t.curr_row, contin = True, speed = SPEED)
    t.gen_typing_text(cyan(" commit"), t.curr_row, contin = True, speed = SPEED)

    prompt_col = t.curr_col
    t.gen_typing_text(cyan(" -"), t.curr_row, contin = True, speed = SPEED)
    t.delete_row(t.curr_row, prompt_col)
    t.gen_text(bright_red(" -a"), t.curr_row, contin = True)
    t.gen_typing_text(bright_red("m"), t.curr_row, speed = SPEED, contin = True)
    
    t.gen_typing_text(cyan(f" \"{GIT_COMMIT_MESSAGE}\""), t.curr_row, contin = True, speed = SPEED)
    t.gen_text("", t.curr_row, count = INFO_DISPLAY_TIME, contin = True)

def main():
    """
    Generate terminal animation sequence (.gif):
    1. Login
    2. Clear screen
    3. Fetch data
    4. Display data
    5. Final message
    """
    t = Terminal(width = WIDTH,
                 height = HEIGHT,
                 xpad = PADDING,
                 ypad = PADDING,
                 font_size = FONT_SIZE)

    login(t)
    clear(t)
    fetch(t)
    info(t)
    final(t)
    
    t.gen_gif()

if __name__ == "__main__":
    main()