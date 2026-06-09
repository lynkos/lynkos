from gifos import Terminal, utils
from datetime import datetime
from zoneinfo import ZoneInfo
from random import randint

USERNAME = "lynkos"
EXPERIENCE = [ "Oracle Cloud (OCI)", "Analytics for Cyber Defense (ACyD) Lab" ]
FOCUS = [ "Infrastructure", "Distributed Systems", "Backend", "Platform", "Cloud", "CI/CD" ]
ZONE = ZoneInfo("America/New_York")
WIDTH = 775
HEIGHT = 570
PADDING = 15
FONT_SIZE = 15
# FONT_FAMILY = "~/Library/Fonts/FiraCode-Retina.ttf" # FiraCode-Regular.ttf

def bright_red(text: str | int) -> str: # aka orange
    return f"\x1b[91m{text}\x1b[0m"

def bright_green(text: str | int) -> str:
    return f"\x1b[92m{text}\x1b[0m"

def bright_yellow(text: str | int) -> str:
    return f"\x1b[93m{text}\x1b[0m"

def bright_magenta(text: str | int) -> str:
    return f"\x1b[95m{text}\x1b[0m"

def bright_cyan(text: str | int) -> str:
    return f"\x1b[96m{text}\x1b[0m"

def login(t: Terminal):
    t.clear_frame()
    t.toggle_show_cursor(False)
    tty = f"tty00{randint(0, 9)}"
    t.gen_text(bright_yellow(f"LYNKOS v1.0.11 ({tty})"), 1, count = 5)
    t.gen_text("login: ", 3, count = 5)
    t.toggle_show_cursor(True)
    t.gen_typing_text(USERNAME, 3, contin = True, speed = 1)
    t.gen_text("", 4, count = 5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count = 5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("*********", 4, contin = True, speed = 1)
    t.toggle_show_cursor(False)
    time_now = datetime.now(ZONE).strftime("%a %b %d %Y %I:%M:%S %p")
    t.gen_text(f"Last login: {time_now} on {tty}", 6)

def fetch(t: Terminal):
    t.gen_prompt(7, count = 5)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text(bright_red("fetch.s"), 7, contin = True, speed = 1)
    t.delete_row(7, prompt_col)
    t.gen_text(bright_green("fetch.sh"), 7, count = 3, contin = True)
    t.gen_typing_text(f" -u {USERNAME}", 7, contin = True)

def get_gen_details():
    git_user_details = utils.fetch_github_stats(USERNAME, include_all_commits = True)
    top_languages = [bright_yellow("Jupyter") if lang[0] == "Jupyter Notebook" else bright_yellow(lang[0]) for lang in git_user_details.languages_sorted]
    return f"""
{bright_magenta(f"{USERNAME}@GitHub")}
--------------
{bright_cyan("Role")}:           {bright_yellow("Software Engineer")}
{bright_cyan("Experience")}:     {(' · ').join([bright_yellow(experience) for experience in EXPERIENCE])}
{bright_cyan("Focus")}:          {(' · ').join([bright_yellow(focus) for focus in FOCUS])}
{bright_cyan("University")}:     {bright_yellow("Florida International University (FIU)")}
{bright_cyan("Degree")}:         {bright_yellow("Computer Science, B.S.")}

{bright_magenta("GitHub Stats")}
--------------
{bright_cyan("User Rating")}:    {bright_yellow(git_user_details.user_rank.level)}
{bright_cyan("Followers")}:      {bright_yellow(git_user_details.total_followers)}
{bright_cyan("Total Stars")}:    {bright_yellow(git_user_details.total_stargazers)}
{bright_cyan("Commits")}:        {bright_yellow(git_user_details.total_commits_all_time)}
{bright_cyan("Pull Requests")}:  {bright_yellow(git_user_details.total_pull_requests_made)}
{bright_cyan("Contributions")}:  {bright_yellow(git_user_details.total_repo_contributions)}

{bright_magenta("Top Languages")}
--------------
{(' · ').join(top_languages[:10])}
    """

def exit(t: Terminal):
    t.toggle_show_cursor(True)
    t.gen_prompt(t.curr_row)
    t.gen_typing_text(bright_green("# Aspiring multidisciplinary"), t.curr_row, contin = True, speed = 1)
    t.gen_text("", t.curr_row, count = 400, contin = True)

def info(t: Terminal):
    details = get_gen_details()
    t.toggle_show_cursor(True)
    t.gen_text(details, 8, 1, count = 5, contin = True)

def main():
    t = Terminal(width = WIDTH,
                 height = HEIGHT,
                 xpad = PADDING,
                 ypad = PADDING,
                 font_size = FONT_SIZE)
                 #font_file = FONT_FAMILY)

    login(t)
    fetch(t)
    info(t)
    exit(t)
    
    t.gen_gif()

if __name__ == "__main__":
    main()