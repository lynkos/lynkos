from gifos import Terminal
from gifos.utils import fetch_github_stats
from datetime import datetime
from zoneinfo import ZoneInfo
from random import randint

USERNAME = "lynkos"
"""GitHub username"""

EXPERIENCE = [ "Oracle Cloud (OCI)", "Analytics for Cyber Defense (ACyD) Lab" ]
"""Work experience"""

FOCUS = [ "Infrastructure", "Distributed Systems", "Backend", "Platform", "Cloud", "CI/CD" ]
"""Areas of focus"""

ZONE = ZoneInfo("America/New_York")
"""Timezone"""

INFO_DISPLAY_TIME = 400
"""How long the info section is displayed in the terminal animation"""

WIDTH = 750
"""Terminal width"""

HEIGHT = 490
"""Terminal height"""

PADDING = 15
"""Terminal padding"""

FONT_SIZE = 15
"""Terminal font size"""

SPEED = 1
"""Typing speed"""

COUNT = 5
"""Number of times to generate text"""

ROW = 1
"""Tracks current row in the terminal for text generation"""

USER_DETAILS = fetch_github_stats(USERNAME, include_all_commits = True)
"""User details fetched from GitHub, including stats like followers, stars, commits, languages, etc."""

# FONT_FAMILY = "~/Library/Fonts/FiraCode-Retina.ttf" # FiraCode-Regular.ttf
# """Terminal font family"""

def red(text: str | int) -> str:
    """
    Formats text in red using ANSI escape codes

    Args:
        text (str | int): Text to format

    Returns:
        str: Red input text formatted with ANSI escape code
    """
    return f"\x1b[31m{text}\x1b[0m"

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

def bright_green(text: str | int) -> str:
    """
    Formats text in bright green using ANSI escape codes

    Args:
        text (str | int): Text to format

    Returns:
        str: Bright green input text formatted with ANSI escape code
    """
    return f"\x1b[92m{text}\x1b[0m"

def bright_yellow(text: str | int) -> str:
    """
    Formats text in bright yellow using ANSI escape codes

    Args:
        text (str | int): Text to format

    Returns:
        str: Bright yellow input text formatted with ANSI escape code
    """
    return f"\x1b[93m{text}\x1b[0m"

def bright_magenta(text: str | int) -> str:
    """
    Formats text in bright magenta (aka purple) using ANSI escape codes

    Args:
        text (str | int): Text to format

    Returns:
        str: Bright magenta (aka purple) input text formatted with ANSI escape code
    """
    return f"\x1b[95m{text}\x1b[0m"

def bright_cyan(text: str | int) -> str:
    """
    Formats text in bright cyan using ANSI escape codes

    Args:
        text (str | int): Text to format

    Returns:
        str: Bright cyan input text formatted with ANSI escape code
    """
    return f"\x1b[96m{text}\x1b[0m"

def login(t: Terminal):
    """
    Simulates a login sequence with a username and password prompt,
    followed by a last login message with a random tty

    Args:
        t (Terminal): Terminal instance
    """
    global ROW

    t.clear_frame()
    t.toggle_show_cursor(False)
    t.gen_text(bright_green(f"LYNKOS v2.0.1"), ROW, count = COUNT)

    ROW += 2
    
    t.gen_text("Login: ", ROW, count = COUNT)
    t.toggle_show_cursor(True)
    t.gen_typing_text(USERNAME, ROW, contin = True, speed = SPEED)

    ROW += 1
    
    t.gen_text("", ROW, count = COUNT)
    t.toggle_show_cursor(False)
    t.gen_text("Password: ", ROW, count = COUNT)
    t.toggle_show_cursor(True)
    t.gen_typing_text("*******", ROW, contin = True, speed = SPEED)
    t.toggle_show_cursor(False)

    ROW += 2

    time_now = datetime.now(ZONE).strftime("%a %b %d %Y %H:%M:%S")
    t.gen_text(f"Last login: {time_now} on {f"tty00{randint(0, 9)}"}", ROW, count = 3)

    ROW += 1

def clear(t: Terminal):
    """
    Simulates clearing the terminal screen with `clear` command

    Args:
        t (Terminal): Terminal instance
    """
    t.gen_prompt(ROW, count = COUNT)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("clea", ROW, speed = SPEED, contin = True)
    t.delete_row(ROW, prompt_col)
    t.gen_text(blue("clear"), ROW, count = COUNT, contin = True)
    t.clear_frame()

def fetch(t: Terminal):
    """
    Simulates fetching data with `fetch.sh -u {USERNAME}` command,
    which is a custom script that fetches user's GitHub stats

    Args:
        t (Terminal): Terminal instance
    """
    global ROW
    
    ROW = 1
    
    t.gen_prompt(ROW, count = COUNT)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("fetch.s", ROW, contin = True, speed = SPEED)
    t.delete_row(ROW, prompt_col)
    t.gen_text(blue("fetch.sh"), ROW, count = 3, contin = True)

    prompt_col = t.curr_col
    t.gen_typing_text(" -", t.curr_row, contin = True, speed = SPEED)
    t.delete_row(t.curr_row, prompt_col)
    t.gen_text(red(" -u"), t.curr_row, count = 3, contin = True)

    t.gen_typing_text(f" {magenta(USERNAME)}", ROW, speed = SPEED, contin = True)

    ROW += 1

def get_gen_details() -> str:
    """
    Formats the user's details and GitHub stats into a readable string with ANSI color codes

    Returns:
        str: Formatted string containing the user's details and GitHub stats
    """
    top_languages = list_languages()

    return f"""
{bright_magenta(f"User Profile")}
--------------
{bright_cyan("Role")}:           {bright_yellow("Software Engineer")}
{bright_cyan("Experience")}:     {(' · ').join([bright_yellow(experience) for experience in EXPERIENCE])}
{bright_cyan("Focus")}:          {(' · ').join([bright_yellow(focus) for focus in FOCUS])}
{bright_cyan("University")}:     {bright_yellow("Florida International University (FIU)")}
{bright_cyan("Degree")}:         {bright_yellow("Computer Science, B.S.")}

{bright_magenta("GitHub Stats")}
--------------
{bright_cyan("User Rating")}:    {bright_yellow(USER_DETAILS.user_rank.level)}
{bright_cyan("Followers")}:      {bright_yellow(USER_DETAILS.total_followers)}
{bright_cyan("Total Stars")}:    {bright_yellow(USER_DETAILS.total_stargazers)}
{bright_cyan("Total Commits")}:  {bright_yellow(USER_DETAILS.total_commits_all_time)}
{bright_cyan("Pull Requests")}:  {bright_yellow(USER_DETAILS.total_pull_requests_made)}
{bright_cyan("Contributions")}:  {bright_yellow(USER_DETAILS.total_repo_contributions)}

{bright_magenta("Top Languages")}
--------------
{(' · ').join(top_languages[:5])}
{(' · ').join(top_languages[5:10])}
    """

def list_languages() -> list[str]:
    """
    Formats the user's top programming languages into a list of strings with ANSI color codes

    Returns:
        list[str]: Formatted list of top languages with their usage percentage, sorted by usage
    """
    languages = [ ]
    
    for language, percent in USER_DETAILS.languages_sorted:
        if language == "Jupyter Notebook": language = "Jupyter"

        lang = f"{bright_cyan(language)} ({bright_yellow(f'{percent}%')})"
        languages.append(lang)

    return languages

def exit(t: Terminal):
    """
    Prints a final message

    Args:
        t (Terminal): Terminal instance
    """
    t.gen_prompt(t.curr_row, count = COUNT)
    t.toggle_show_cursor(True)
    t.gen_typing_text(bright_green("# Aspiring multidisciplinary"), t.curr_row, contin = True, speed = SPEED)
    t.gen_text("", t.curr_row, count = INFO_DISPLAY_TIME, contin = True)

def info(t: Terminal):
    """
    Prints the user's GitHub stats

    Args:
        t (Terminal): Terminal instance
    """
    t.toggle_show_cursor(True)
    t.gen_text(get_gen_details(), ROW, contin = True)

def main():
    """
    Main function that generates a gif of terminal animation sequence:
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
                 #font_file = FONT_FAMILY)

    login(t)
    clear(t)
    fetch(t)
    info(t)
    exit(t)
    
    t.gen_gif()

if __name__ == "__main__":
    main()