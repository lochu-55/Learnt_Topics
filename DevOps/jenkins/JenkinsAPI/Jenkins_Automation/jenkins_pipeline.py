import jenkins
from jenkins import Jenkins
import xml.etree.ElementTree as ET
from Inputs.Inputs_to_jenkinsAPI import Inputs

class Pipeline:
    def __init__(self):
        self.script_content = None
        try:
            self.jenkins = Jenkins(Inputs.jenkins_url, username=Inputs.username, password=Inputs.password)
            print("Successfully connected to Jenkins.")
        except jenkins.JenkinsException as e:
            print(f"Failed to connect to Jenkins: {e}")

    def extract_groovy_script_of_pipeline_from_xml(self,file_path):
        with open(file_path, 'r') as file:
            xml_content = file.read()

        # Parse the XML content and extract the Jenkinsfile script from the <script> tag
        tree = ET.ElementTree(ET.fromstring(xml_content))
        root = tree.getroot()
        self.script_content = root.find(".//script").text

        print("Extracted groovy scripr: ")
        print(self.script_content)
        return self.script_content

    def check_pipeline_script_syntax(self,file_path):
        script_content = self.extract_groovy_script_of_pipeline_from_xml(file_path)

        # Now check the syntax of the Jenkinsfile
        errors = self.jenkins.check_jenkinsfile_syntax(script_content)

        if errors:
            print("Jenkinsfile has syntax errors:")
            for error in errors:
                print(error)
        else:
            print("Jenkinsfile syntax is valid.")

    def create_pipeline(self):
        try:
            pipeline_xml = open('Inputs/XMLs/pipeline.xml', mode='r', encoding='utf-8').read()
            self.jenkins.create_job(Inputs.pipeline_name, pipeline_xml)
            print(f"Created the pipeline named:  {Inputs.pipeline_name}")
        except jenkins.JenkinsException as e:
            print(f"failed to create pipeline:{e}")

    def build_the_pipeline(self):
        try:
            self.jenkins.build_job(Inputs.pipeline_name)
            print("Qqqqqqqqqqqqqqqqqqqqqqqqq")
            q = self.jenkins.get_queue_info()
            print(q)
            print(f"built the pipeline : {Inputs.pipeline_name} successfully....")

        except jenkins.JenkinsException as e:
            print(f"Failed to build the pipeline: {e}")


    def get_last_build_number(self):
        try:
            last_build_no = self.jenkins.get_job_info(Inputs.pipeline_name)['lastCompletedBuild']['number']
            print(f"last build number of the job: {Inputs.pipeline_name} is {last_build_no}")
            return last_build_no
        except Exception as e:
            print(f"failed to retrieve the last build number : {e}")




if __name__ == '__main__':
    pipe = Pipeline()
    pipe.check_pipeline_script_syntax(Inputs.pipeline_xml_path)
    pipe.create_pipeline()
    pipe.build_the_pipeline()
