"""Given a list of projects and their dependencies, determine the order in which the projects could be installed."""

# Input
projects = ["a", "b", "c", "d", "e", "f"]
dependencies = [
    # (project, dependency)
    ("d", "a"),
    ("b", "f"),
    ("d", "b"),
    ("a", "f"),
    ("c", "d"),
]

# Sample output: f, e, a, b, d, c

# Solution
installed = list()
while projects:
    progress = False

    for project in projects:
        needs_dependency = False

        for p, d in dependencies:
            if p == project and d not in installed:
                needs_dependency = True
                break

        if not needs_dependency:
            projects.remove(project)
            installed.append(project)
            progress = True

    if not progress:
        # Unable to install all dependencies... should we rollback?
        installed.append(None)
        break

print(installed)  # Actual output: ['e', 'f', 'a', 'b', 'd', 'c']
