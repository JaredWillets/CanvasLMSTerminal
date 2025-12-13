from canvasapi import Canvas
import json
from canvasapi.paginated_list import PaginatedList
from canvasapi.course import Course
import time

config = json.load(open("config.json"))

API_URL = config['url']
API_KEY = config['token']

class ClientWrapper:
    def __init__(self, url = API_URL, key = API_KEY):
        self.url = url
        self.key = key
        self.canvas = Canvas(self.url, self.key)
        self.user = self.canvas.get_current_user()

    def getCourses(self):
        return self.user.get_courses()
    
    def getCurrentCourses(self):
        return self.user.get_courses(enrollment_state = "active")



if __name__ == "__main__":
    wrapper = ClientWrapper()

    courses = wrapper.getCourses()
    for course in courses:
        try:course.name
        except:continue
        print(course.name)
        print(course.workflow_state)
        tabs = course.get_tabs()
        for tab in tabs:
            print(tab.__dict__)
        break
            # print(tab.label)
        # print(course.get_tabs())
        # course = course.__dict__
        # print(course)