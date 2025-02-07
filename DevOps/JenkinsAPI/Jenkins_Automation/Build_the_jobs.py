import jenkins
from jenkins import Jenkins
from Inputs.Inputs_to_jenkinsAPI import Inputs



class Build:
    def __init__(self):
        try:
            self.jenkins = Jenkins(Inputs.jenkins_url, username=Inputs.username, password=Inputs.password)
            print("Successfully connected to Jenkins.")
        except jenkins.JenkinsException as e:
            print(f"Failed to connect to Jenkins: {e}")

    def start_build(self):
        try:
            self.jenkins.build_job(Inputs.build_job_name)
            print(f"built the job : {Inputs.build_job_name} successfully....")
        except jenkins.JenkinsException as e:
            print(f"Failed to build the job: {e}")


    def get_last_build_number(self):
        try:
            last_build_no = self.jenkins.get_job_info(Inputs.build_job_name)['lastCompletedBuild']['number']
            print(f"last build number of the job: {Inputs.build_job_name} is {last_build_no}")
            return last_build_no
        except Exception as e:
            print(f"failed to retrieve the last build number : {e}")



    def get_any_build_number_info_of_job(self):
        try:
            build_info = self.jenkins.get_build_info(Inputs.build_job_name,1)
            print(f"the build num {Inputs.build_number} info of the job: {Inputs.build_job_name} is {build_info}")
        except Exception as e:
            print(f"failed to retrieve the last build number : {e}")


    def get_last_build_information_of_job(self):
        try:
            last_build_info = self.jenkins.get_build_info(Inputs.build_job_name,self.get_last_build_number())
            print(f"last build info of the job: {Inputs.build_job_name} is {last_build_info}")
        except Exception as e:
            print(f"failed to retrieve the last build number : {e}")

    def get_build_test_report_of_job(self):
        try:
            build_report = self.jenkins.get_build_test_report(Inputs.build_job_name, Inputs.build_number)
            print("*****************Test Report******************")
            print(f"last build report of the job: {Inputs.build_job_name} is {build_report}")
        except Exception as e:
            print(f"failed to retrieve the build report of job {Inputs.build_job_name} : {e}")

    def delete_the_build(self):
        try:
            self.jenkins.delete_build(name=Inputs.build_job_name,number=Inputs.build_number)
            print(f"deleted the build number {Inputs.build_number} of {Inputs.build_job_name}")
        except Exception as e:
            print(f"failed to delete the build : {e}")


    def get_running_builds_info(self):
        try:
            builds = self.jenkins.get_running_builds()
            print(f"The running builds in jenkins are : {builds}")
        except Exception as e:
            print(f"failed to retrieve info of running builds : {e}")


    def get_console_output_of_build(self,job_name,build_no):
        try:
            op = self.jenkins.get_build_console_output(job_name,build_no)
            print(f"The console output of {job_name} is {op}")
        except Exception as e:
            print(f"failed to retrieve console output of build : {e}")


    def get_env_var_of_build(self,job_name,build_no):
        try:
            op = self.jenkins.get_build_env_vars(job_name,build_no)
            print(f"The env variables of {job_name} is {op}")
        except Exception as e:
            print(f"failed to retrieve env variables of build : {e}")


if __name__ == '__main__':
    build = Build()
    #build.start_build()
    build.get_any_build_number_info_of_job()
    build.get_last_build_information_of_job()
    build.get_build_test_report_of_job()
    #build.delete_the_build()
    build.get_running_builds_info()
    build.get_env_var_of_build(Inputs.build_job_name,Inputs.build_number)
    build.get_console_output_of_build(Inputs.build_job_name,Inputs.build_number)

