def gather_credits(credits, *args):
    courses = set()
    all_credits = 0

    for course in args:
        course_name, course_credits = course

        if all_credits >= credits:
            break

        if course_name not in courses:
            courses.add(course_name)
            all_credits += course_credits

    if all_credits >= credits:
        enrolled_courses_sorted = sorted(courses)
        courses_str = ', '.join(enrolled_courses_sorted)
        return f"Enrollment finished! Maximum credits: {all_credits}.\nCourses: {courses_str}"

    credits_shortage = credits - all_credits
    return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."


print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

