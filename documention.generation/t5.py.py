"""Store and manage simple course information.

Courses are stored in the ``courses`` dictionary using the course ID as the
key. Each value contains the course name and number of credits.
"""


courses = {}


def add_course(course_id, name, credits):
    """Add a course to the course dictionary.

    Args:
        course_id (str): The unique ID of the course.
        name (str): The name of the course.
        credits (int): The number of credits for the course.

    Returns:
        None: The course is added to the ``courses`` dictionary.
    """
    courses[course_id] = {
        "name": name,
        "credits": credits,
    }


def remove_course(course_id):
    """Remove a course from the course dictionary.

    Args:
        course_id (str): The ID of the course to remove.

    Returns:
        dict or None: The removed course information, or ``None`` if the
        course ID does not exist.
    """
    return courses.pop(course_id, None)


def get_course(course_id):
    """Return course information for a given course ID.

    Args:
        course_id (str): The ID of the course to find.

    Returns:
        dict or None: The course information, or ``None`` if the course ID
        does not exist.
    """
    return courses.get(course_id)
