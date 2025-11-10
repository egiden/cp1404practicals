"""
Project Management Program
Estimate: 50 minutes
Actual:   5 hours
"""
import datetime
from operator import attrgetter
from project import Project

DEFAULT_FILE_NAME = 'projects.txt'
WELCOME_MESSAGE = "Welcome to Pythonic Project Management"
GOODBYE_MESSAGE = "Thank you for using custom-built project management software."
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    print(WELCOME_MESSAGE)
    projects = load_projects(DEFAULT_FILE_NAME)
    print(MENU)

    choice = input(">>> ")
    while choice.upper() != "Q":
        if choice.upper() == "L":  # Load projects from file name if file exists
            file_name = get_valid_file_name()
            if file_name:
                projects += load_projects(file_name)
        elif choice.upper() == "S":
            file_name = input("File name: ")
            save_projects(projects, file_name)
        elif choice.upper() == "D":
            # Group projects according to whether they are completed
            completed_projects, incomplete_projects = group_projects(projects)
            # Sort each group by priority
            completed_projects.sort()
            incomplete_projects.sort()
            # Display each group
            print("Incomplete projects:")
            display_projects(incomplete_projects, False, True)
            print("Completed projects:")
            display_projects(completed_projects, False, True)
        elif choice.upper() == "F":
            date = get_date("Show projects that start after date (dd/mm/yy): ")
            projects_after_date = [project for project in projects if project.start_date >= date]
            projects_after_date.sort(key=attrgetter("start_date"))
            display_projects(projects_after_date, False)
        elif choice.upper() == "A":
            project = get_project()
            projects.append(project)
        elif choice.upper() == "U":
            display_projects(projects, True)
            project_index = get_non_negative_number("Project choice")
            while project_index >= len(projects):
                print(f"Input for Project choice must be less than {len(projects)}")
                project_index = get_non_negative_number("Project choice")
            print(projects[project_index])
            new_percentage = get_non_negative_number("New Percentage", True)
            new_priority = get_non_negative_number("New Priority", True)
            update_project(projects, project_index, new_percentage, new_priority)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ")
    save_projects_to_file = input(f"Would you like to save to {DEFAULT_FILE_NAME}? ").upper() in ["Y", "YES"]
    if save_projects_to_file:
        save_projects(projects)
    print(GOODBYE_MESSAGE)


def get_valid_file_name() -> str | None:
    """Get the name of a file from the user and return it if the file exists. Return None otherwise."""
    file_name = input("File name: ")
    try:
        file_obj = open(file_name)
    except FileNotFoundError:
        print("File not found")
    else:
        file_obj.close()
        return file_name


def load_projects(file_name: str) -> list[Project]:
    """Read file of project details and save as Project objects."""
    projects = []
    in_file = open(file_name, 'r')
    # File format is like: Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage
    # 'Consume' the first line (header)
    in_file.readline()
    # All other lines are project data
    for line in in_file:
        parts = line.split('\t')
        name = parts[0]
        start_date = datetime.datetime.strptime(parts[1], Project.DATE_FORMAT_STRING).date()
        priority = int(parts[2])
        cost_estimate = float(parts[3])
        completion_percentage = int(parts[4])
        project = Project(name, start_date, priority, cost_estimate, completion_percentage)
        projects.append(project)
    in_file.close()
    print(f"Loaded {len(projects)} projects from {file_name}")
    return projects


def save_projects(projects: list[Project], file_name=DEFAULT_FILE_NAME):
    """Write project details from list of Project objects to file."""
    # Save projects
    out_file = open(file_name, 'w')
    print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)  # Write heading first
    for project in projects:
        print(
            f"{project.name}\t{project.start_date:{Project.DATE_FORMAT_STRING}}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
            file=out_file)
    out_file.close()

    # Display completion message
    print(f"Saved {len(projects)} projects to {file_name}")


def display_projects(projects: list[Project], include_list_numbering: bool, indent_list_items=False):
    """Display projects from a list of Project objects."""
    for i, project in enumerate(projects):
        list_number = f"{i:2} " if include_list_numbering else ''
        indent = '  ' if indent_list_items else ''
        print(f"{indent}{list_number}{project}")


def group_projects(projects: list[Project]) -> tuple[list[Project], list[Project]]:
    """Group a list of Project objects into two lists according to whether they are completed."""
    completed_projects = []
    incomplete_projects = []
    for project in projects:
        if project.is_complete():
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)
    return completed_projects, incomplete_projects


def update_project(projects: list[Project], project_index: int, new_percentage=None, new_priority=None):
    """Update a project from a list of Project objects with a new completion percentage and priority if they are provided."""
    project = projects.pop(project_index)
    if new_percentage:
        project.completion_percentage = new_percentage
    if new_priority:
        project.priority = new_priority
    projects.append(project)


def get_project() -> Project:
    """Prompt user for project details and create Project object."""
    print("Let's add a new project")
    name = get_project_name()
    start_date = get_date("Start date (dd/mm/yy): ")
    priority = get_non_negative_number("Priority")
    cost_estimate = get_non_negative_number("Cost Estimate")
    completion_percentage = get_non_negative_number("Completion Percentage")
    return Project(name, start_date, priority, cost_estimate, completion_percentage)


def get_project_name() -> str:
    """Prompt user for valid project name."""
    name = input("Name: ")
    while name == "":
        print("Project name cannot be empty")
        name = input("Name: ")
    return name


def get_date(prompt_text: str) -> datetime.date:
    """Prompt user for date formatted as dd/mm/yy."""
    start_date = convert_string_to_datetime(input(prompt_text))
    while not start_date:
        print("Invalid date")
        start_date = convert_string_to_datetime(input(prompt_text))
    return start_date


def get_non_negative_number(name: str, allow_blank_input=False) -> int | float | None:
    """Prompt user for non-negative number. If blank input is allowed, return None if user leaves input blank.

    Parameters:
        name: Name of the quantity or object which the number represents.
        allow_blank_input: Indicated whether blank input into prompt should be accepted.
    """
    prompt_text = f"{name}: "
    number = input(prompt_text)
    if number == '' and allow_blank_input:
        number = None
    else:
        number = convert_string_to_non_negative_number(number)
        while not is_non_negative_number(number):
            print(f"Input for {name} must be non-negative number")
            number = convert_string_to_non_negative_number(input(prompt_text))
    return number


def is_non_negative_number(number):
    """Determine if an object is a non-negative integer or float."""
    try:
        return number >= 0
    except TypeError:
        return False


def convert_string_to_non_negative_number(string) -> int | float | None:
    """Convert a number string to a non-negative number. Return None if it is not a number string."""
    try:
        return int(string)
    except ValueError:
        try:
            return float(string)
        except ValueError:
            pass


def convert_string_to_datetime(string) -> datetime.date | None:
    """Convert a date string to a datetime.date object."""
    try:
        return datetime.datetime.strptime(string, Project.DATE_FORMAT_STRING).date()
    except ValueError:
        pass


main()
