class Project:
    """Represent a project object."""
    DATE_FORMAT_STRING = "%d/%m/%Y"

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def is_complete(self):
        """Determine whether the project is complete."""
        return self.completion_percentage == 100

    def __lt__(self, other):
        """Determine if one project is less than the other based on priority."""
        return self.priority < other.priority

    def __repr__(self):
        return f"{self.name}, start: {self.start_date:{self.DATE_FORMAT_STRING}}, priority {self.priority}, estimate: ${self.cost_estimate:1,.2f}, completion: {self.completion_percentage}%"
