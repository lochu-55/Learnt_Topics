from jenkinsapi.jenkins import Jenkins
from Inputs.Inputs_to_jenkinsAPI import Inputs

class JenkinsAPI_Build:
    def __init__(self):
        self.jenkins = Jenkins(Inputs.jenkins_url, username=Inputs.username, password=Inputs.password)
        self.job = self.jenkins.get_job(Inputs.downstream_job)
        self.build = self.job.get_build(32)

    def get_downstream_jobs_info(self):
        downstream_jobs = self.job.get_downstream_jobs()
        print(f"Downstream jobs of {self.job.name}:")

        for downstream_job in downstream_jobs:
            print(f"Job Name: {downstream_job.name}")

            # Fetch and display builds
            try:
                last_build = downstream_job.get_last_build()  # Get the latest build
                print(f"Last Build Number: {last_build.get_number()}")
                print(f"Last Build URL: {last_build.get_url()}")  # Use get_url() instead of url
                print(f"Last Build Status: {last_build.get_status()}")

                # Optionally, list all builds
                builds = downstream_job.get_build_dict()  # Returns {build_number: build_url}
                print(f"All Builds: {list(builds.keys())}")
            except Exception as e:
                print(f"Could not fetch builds for job {downstream_job.name}. Error: {e}")


if __name__ == '__main__':
    JB = JenkinsAPI_Build()
    JB.get_downstream_jobs_info()
