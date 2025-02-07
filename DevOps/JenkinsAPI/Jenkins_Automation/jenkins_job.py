import jenkins
from jenkins import Jenkins
from Inputs.Inputs_to_jenkinsAPI import Inputs

class Job:
    def __init__(self):
        self.job_count = None
        try:
            self.jenkins = Jenkins(Inputs.jenkins_url, username=Inputs.username, password=Inputs.password)
            print("Successfully connected to Jenkins.")
        except jenkins.JenkinsException as e:
            print(f"Failed to connect to Jenkins: {e}")


    def create_empty_job(self,job_name):
        try:
            self.jenkins.create_job(job_name, jenkins.EMPTY_CONFIG_XML)
            print("Job 'job1' created successfully...")
        except jenkins.JenkinsException as e:
            if 'already exists' in str(e):
                print("Job 'job1' already exists.")
            else:
                print(f"Failed to create job: {e}")
        
    def create_job_using_xml(self,job_name):
        try:
            job2_xml = open("Inputs/XMLs/sample_job_config.xml", mode='r',encoding='utf-8').read()
            self.jenkins.create_job(job_name,job2_xml)
            print("job2 created successfully....")
        except jenkins.JenkinsException as e:
            if 'already exists' in str(e):
                print("Job 'job2' already exists.")
            else:
                print(f"Failed to create job: {e}")


    def get_all_available_jobs(self):
        jobs = self.jenkins.get_jobs()
        print("Jobs on Jenkins server:")
        #print(jobs)
        for job in jobs:
            print(f" - {job['name']}")
        return jobs


    def get_job_details_in_xml(self):
        try:
            # Fetch and print configuration of the specific job
            if any(job['name'] == Inputs.get_job_name for job in self.get_all_available_jobs()):
                config = self.jenkins.get_job_config(Inputs.get_job_name)
                print(f"Configuration for job '{Inputs.get_job_name}':\n{config}\n")
            else:
                print(f"Job '{Inputs.get_job_name}' does not exist.")
        except jenkins.JenkinsException as e:
            print(f"Failed to retrieve job xml file: {e}")

    
    def Delete_the_job(self, job_name):
        try:
            self.jenkins.delete_job(job_name)
        except jenkins.JenkinsException as e:
            print(f"Failed to delete job '{job_name}': {e}")
    
    
    
    def copy_the_job(self):
        try:
            if any(job['name'] == Inputs.copy_destination_job for job in self.get_all_available_jobs()):
                print(f"Destination job '{Inputs.copy_destination_job}' already exists. Deleting it first...")
                self.Delete_the_job(Inputs.copy_destination_job)
                print(f"Job '{Inputs.copy_destination_job}' deleted successfully.")

            self.jenkins.copy_job(Inputs.copy_source_job, Inputs.copy_destination_job)
            print(f"Copied '{Inputs.copy_source_job}' to '{Inputs.copy_destination_job}' successfully.")

        except jenkins.JenkinsException as e:
            print(f"Failed to copy job : {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")




    def update_job(self):
        try:
            updated_job1 = open('Inputs/XMLs/updated_job1.xml',mode='r',encoding='utf-8').read()
            self.jenkins.reconfig_job('job1',updated_job1)
            print("updated job1 successfully......")
        except jenkins.JenkinsException as e:
            print("failed to copy job contents to other job...")

    def disable_the_job(self):
        try:
            self.jenkins.disable_job('job1')
            print("disabled job1 successfully......")
        except jenkins.JenkinsException as e:
            print(f"failed to disable the job :{e}")


    def enable_the_job(self):
        try:
            self.jenkins.enable_job(Inputs.get_job_name)
            print("enabled job1 successfully......")
        except jenkins.JenkinsException as e:
            print(f"failed to enable the job :{e}")

    def rename_a_job(self,existing_job_name,new_job_name):
        try:
            self.jenkins.rename_job(existing_job_name,new_job_name)
            print(f"renamed {existing_job_name} to {new_job_name} successfully......")
        except jenkins.JenkinsException as e:
            print(f"failed to rename the job {existing_job_name} :{e}")

    def get_job_information(self):
        try:
            job_info = self.jenkins.get_job_info(Inputs.get_job_name,fetch_all_builds=True)
            print("job information: ")
            print(job_info,"\n")
            print("job info in detailed format...")
            self.jenkins.debug_job_info(Inputs.get_job_name)

        except jenkins.JenkinsException as e:
            print(f"failed to get info about {Inputs.get_job_name} :{e}")


    def get_job_info_using_regex(self):
        try:
            job_info_regex = self.jenkins.get_job_info_regex(Inputs.regex_pattern)
            print("all job builds information with matching regular exepression 'job': ")
            for job in job_info_regex:
                print(job,"\n")
        except jenkins.JenkinsException as e:
            print(f"failed to get info about jobs with regex {Inputs.regex_pattern} :{e}")


    def check_job_existence_in_jenkins(self):
        try:
            check_job = self.jenkins.job_exists(Inputs.get_job_name)
            if check_job:
                print(f"{Inputs.get_job_name} exists in jenkins server")
            else:
                print(f"{Inputs.get_job_name} does not exists in jenkins server")
        except jenkins.JenkinsException as e:
            print(f"failed to check the existence of {Inputs.get_job_name} :{e}")

    def get_job_count_from_jenkins(self):
        try:
            self.job_count = self.jenkins.jobs_count()
            print("Total number of jobs in jenkins server: ",self.job_count)
        except jenkins.JenkinsException as e:
            print(f"failed to fetch the count of jobs :{e}")


    def create_a_job_within_separate_folder(self):
        try:
            folder = open('Inputs/XMLs/folder.xml', mode='r', encoding='utf-8').read()
            self.jenkins.create_job(Inputs.Jenkins_folder_name, folder)
            print(f"************Created folder : {Inputs.Jenkins_folder_name}**************")
            job_xml = open("Inputs/XMLs/updated_job1.xml", mode='r', encoding='utf-8').read()
            self.jenkins.create_job(f"{Inputs.Jenkins_folder_name}/{Inputs.get_job_name}",job_xml)
            print(f"Created the job {Inputs.get_job_name} inside {Inputs.Jenkins_folder_name}")
        except jenkins.JenkinsException as e:
            print(f"failed to create folder:{e}")


    def create_a_upstream_job(self):
        try:
            upstream_xml = open('Inputs/XMLs/job_set_upstream_trigger_when_success.xml', mode='r', encoding='utf-8').read()
            self.jenkins.create_job(Inputs.upstream_job, upstream_xml)
            print(f"Created the upstream job for {Inputs.upstream_job}")
        except jenkins.JenkinsException as e:
            print(f"failed to create upstream job:{e}")


    def delete_job_workspace(self,job_name):
        self.jenkins.wipeout_job_workspace(job_name)
        print("clearing all contents of the jenkins workspace...")


if __name__ == '__main__':
    job = Job()
    #job.create_empty_job("job2")
    #job.create_job_using_xml("job4")
    job.get_job_details_in_xml()

    #job.copy_the_job()
    #job.update_job()
    job.rename_a_job("gpio_job","job2")
    #job.enable_the_job()
    #job.disable_the_job()
    #     job.Delete_the_job("job4")

    job.get_job_information()
    job.get_job_info_using_regex()
    job.check_job_existence_in_jenkins()
    job.get_job_count_from_jenkins()
    #job.create_a_job_within_separate_folder()

    #job.create_a_upstream_job()
    #job.delete_job_workspace()
