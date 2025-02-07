import jenkins
from jenkins import Jenkins
from Inputs.Inputs_to_jenkinsAPI import Inputs

class View:
    def __init__(self):
        try:
            self.jenkins = Jenkins(Inputs.jenkins_url, username=Inputs.username, password=Inputs.password)
            print("Successfully connected to Jenkins.")
        except jenkins.JenkinsException as e:
            print(f"Failed to connect to Jenkins: {e}")


    def create_the_view(self,view_name):
        try:
            view_config = open('Inputs/XMLs/sample_view.xml', mode='r', encoding='utf-8').read()
            self.jenkins.create_view(view_name,view_config)
            print("Created a new view in jenkins...")
        except jenkins.JenkinsException as e:
            print(f"failed to create a view : {e}")

    def get_all_view_names(self):
        try:
            views = self.jenkins.get_views()
            print(f"Available views in jenkins are :")
            for view in views:
                print(f" - {view['name']}")
        except jenkins.JenkinsException as e:
            print(f"failed to fetch views : {e}")

    def get_config_xml_of_view(self,view_name):
        try:
            view_xml = self.jenkins.get_view_config(view_name)
            print(f"retrieved the {view_name} config xml :")
            print(view_xml)
        except jenkins.JenkinsException as e:
            print(f"failed to retrieve {view_name} config xml : {e}")


    def update_the_view(self,update_view_name):
        try:
            updated_view_config = open('Inputs/XMLs/updated_job_view.xml', mode='r', encoding='utf-8').read()
            self.jenkins.reconfig_view(update_view_name,updated_view_config)
            print(f"updated the {update_view_name} successfully")
        except jenkins.JenkinsException as e:
            print(f"failed to update {update_view_name} : {e}")


    def delete_the_view(self,delete_view_name):
        try:
            self.jenkins.delete_view(delete_view_name)
            print(f"deleted the {delete_view_name} successfully")
        except jenkins.JenkinsException as e:
            print(f"failed to delete {delete_view_name} : {e}")

    def check_view_existence(self,view_name):
        try:
            self.jenkins.view_exists(view_name)
            print(f"found {view_name} in jenkins server successfully")
        except jenkins.JenkinsException as e:
            print(f"{view_name} not found : {e}")


if __name__ == '__main__':
    view = View()
    view.create_the_view(Inputs.view_name)
    #view.create_the_view('My new View')
    view.get_config_xml_of_view(Inputs.view_name)
    view.get_all_view_names()
    view.update_the_view(Inputs.view_name)
    view.delete_the_view('My new View')
    view.get_all_view_names()
    view.check_view_existence(Inputs.view_name)



