import requests
from datetime import datetime

def get_courses(base_url, request_header):
    # Get list of courses
    courses_url = base_url + "/api/v1/courses?enrollment_state=active"
    courses = requests.get(courses_url, headers=request_header).json()
    courses = list(courses)
    courses_url = base_url + "/api/v1/courses?enrollment_state=completed"
    courses.extend(requests.get(courses_url, headers=request_header).json())
    courses_url = base_url + "/api/v1/courses?enrollment_state=invited_or_pending"
    courses.extend(requests.get(courses_url, headers=request_header).json())
    return courses

def get_assignments(base_url, request_header, course_id: int):
    assignments_url = base_url + "/api/v1/courses/" + str(course_id) + "/assignments"
    assignments = requests.get(assignments_url, headers=request_header).json()
    return assignments

def get_announcements(base_url, request_header, course):
    course_id = course['id']
    start_date = course['created_at']
    end_date = str(datetime.now().isoformat())
    announcements_url = base_url + "/api/v1/announcements?context_codes[]=course_" + str(course_id) + "&start_date=" + start_date + "&end_date=" + end_date
    announcements = requests.get(announcements_url, headers=request_header).json()
    return announcements

def get_quizzes(base_url, request_header, course_id):
    quiz_url = base_url + "/api/v1/courses/" + str(course_id) + "/quizzes"
    quizzes = requests.get(quiz_url, headers=request_header).json()
    return quizzes