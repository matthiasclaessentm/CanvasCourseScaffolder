class Quiz:
    def __init__(self, assignment_group, name, due_at, available_at, available_until, points, published):
        self.id = None
        self.assignment_group = assignment_group
        self.name = name
        self.due_at = due_at
        self.available_at = available_at
        self.available_until = available_until
        self.points = points
        self.published = published
