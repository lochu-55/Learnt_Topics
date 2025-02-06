from jenkinsapi.artifact import Artifact
from jenkinsapi.jenkins import Jenkins
from Inputs.Inputs_to_jenkinsAPI import Inputs

class Artifacts :
    def __init__(self):
        self.artifacts = None
        self.job = None
        self.build = None
        self.jenkins = Jenkins(Inputs.jenkins_url,username=Inputs.username,password=Inputs.password)


    def get_build_artifacts_info(self):

        self.job = self.jenkins.get_job(Inputs.build_job_name)
        self.build = self.job.get_build(Inputs.build_number)
        print("Job_name #build_number : ",self.build)



        print("********artifacts**********")
        artifacts = self.build.get_artifact_dict()
        print(f"artifacts of {Inputs.build_job_name} with build no {Inputs.build_number}")
        print(artifacts)

        # self.get_artifact = Artifact(Inputs.artifact_filename, Inputs.artifact_url, build)
        # print("the jenkins object : ",self.get_artifact.get_jenkins_obj())
        # print("the data of the artifact : ",self.get_artifact.get_data())

    def save_artifacts_in_directory(self):
        self.artifacts = self.build.get_artifacts()
        for artifact in self.artifacts:
            artifact.save_to_dir(Inputs.artifact_saving_path_to_dir, strict_validation=False)
        print(f"Successfully saved to a directory in path : {Inputs.artifact_saving_path_to_dir}")


    def save_artifacts_by_changing_its_name(self):
        for job in self.build.get_artifacts():
            job.save(Inputs.artifact_saving_path_to_dir+"/report_1.xml",True)
        print(f"Successfully saved the artifact to path : {Inputs.artifact_saving_path_to_dir}")



if __name__ == '__main__':
    arti = Artifacts()
    arti.get_build_artifacts_info()
    arti.save_artifacts_in_directory()
    arti.save_artifacts_by_changing_its_name()
