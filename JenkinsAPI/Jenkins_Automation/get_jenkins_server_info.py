from jenkins import Jenkins
from Inputs.Inputs_to_jenkinsAPI import Inputs


class Jenkins_server:

    def __init__(self):
        self.jenkins_info = None
        self.server = Jenkins(Inputs.jenkins_url, username=Inputs.username, password=Inputs.password)


    def get_server_instance(self):
        self.jenkins_info = self.server.get_info()
        print("the info of the jenkins server : ",self.jenkins_info)
        user = self.server.get_whoami()
        print("User of the jenkins server : ",user,"\n")
        version = self.server.get_version()
        print('Hello %s from Jenkins %s' % (user['fullName'],version),"\n")

    def get_the_jobs_info_from_server(self):
        jobs_list = self.jenkins_info['jobs']
        print ("the jobs present in jenkins server : ",jobs_list)
        print("the first job in jenkins is : ",jobs_list[0])

    def get_plugins_info_from_jenkins(self):
        plugins_list = self.server.get_plugins()
        print("installed plugins in jenkins: ",plugins_list)

    def get_particular_plugin_info(self):
        plugin = self.server.get_plugin_info('Docker plugin',depth=1)
        print("Particular plugin info in jenkins: ",plugin)

    def delete_workspace(self,job_name):
        self.server.wipeout_job_workspace(job_name)
        print(f"wiped out the workspace of {job_name}")

if __name__ == '__main__':
    server = Jenkins_server()
    server.get_server_instance()
    server.get_the_jobs_info_from_server()
    #server.get_plugins_info_from_jenkins()
    server.get_particular_plugin_info()
    #server.delete_workspace("job4")
