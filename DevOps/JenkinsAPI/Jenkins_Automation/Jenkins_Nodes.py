import jenkins
from jenkins import Jenkins
from Inputs.Inputs_to_jenkinsAPI import Inputs


class Nodes:
    def __init__(self):
        try:
            self.jenkins = Jenkins(Inputs.jenkins_url, username=Inputs.username, password=Inputs.password)
            print("Successfully connected to Jenkins.")
        except jenkins.JenkinsException as e:
            print(f"Failed to connect to Jenkins: {e}")

    def get_list_of_nodes_in_jenkins(self):
        try:
            nodes = self.jenkins.get_nodes()
            print(f"available nodes in jenkins are : {nodes} ")

        except jenkins.JenkinsException as e:
            print(f"Failed to get list of nodes: {e}")

    def get_node_information(self, node_name):
        try:
            node_info = self.jenkins.get_node_info(node_name)
            print(f"information of {node_name}: {node_info}\n ")

        except jenkins.JenkinsException as e:
            print(f"Failed to retrieve info of node {node_name}: {e}")

    def get_node_config_xml(self, node_name):
        try:
            node_xml = self.jenkins.get_node_config(node_name)
            print(f"configuration of {node_name}:\n {node_xml} ")

        except jenkins.JenkinsException as e:
            print(f"Failed to retrieve xml configuration of node {node_name}: {e}")

    def check_node_existence(self, node_name):
        try:
            check_node = self.jenkins.node_exists(node_name)
            if check_node:
                print(f"Node {node_name} exists... ")
            else:
                print("Node does not exist...")

        except jenkins.JenkinsException as e:
            print(f"Failed to retrieve xml configuration of node {node_name}: {e}")

    def create_a_node(self):
        try:
            node_created = self.jenkins.create_node(Inputs.node_name, numExecutors=1, nodeDescription="jyothsna Node",
                                                    remoteFS="/home/vlab/jenkins", labels="jyo",
                                                    launcher=jenkins.LAUNCHER_SSH,
                                                    launcher_params=Inputs.launcher_params)
            print(f"Created and launched node {node_created} successfully.... ")

        except jenkins.JenkinsException as e:
            print(f"Failed to create node:   {e}")

    def delete_a_node(self, node_name):
        try:
            self.jenkins.delete_node(node_name)
            print(f"Deleted the node {node_name} successfully....\n")

        except jenkins.JenkinsException as e:
            print(f"Failed to delete the node {node_name}: {e}")

    def disable_a_node(self, node_name):
        try:
            self.jenkins.disable_node(node_name)
            print(f"Disabled the node {node_name} successfully....\n")

        except jenkins.JenkinsException as e:
            print(f"Failed to disable the node {node_name}: {e}")

    def enable_a_node(self, node_name):
        try:
            self.jenkins.enable_node(node_name)
            print(f"Enabled the node {node_name} successfully....\n")

        except jenkins.JenkinsException as e:
            print(f"Failed to enable the node {node_name}: {e}")

    def reconfigure_a_node(self):
        try:
            node_xml = open('Inputs/XMLs/node.xml', mode='r', encoding='utf-8').read()
            self.jenkins.reconfig_node(Inputs.node_name,node_xml)
            print(f"Reconfigured the node {Inputs.node_name} successfully....\n")

        except jenkins.JenkinsException as e:
            print(f"Failed to reconfigure the node {Inputs.node_name}: {e}")

if __name__ == '__main__':
    node = Nodes()
    node.get_list_of_nodes_in_jenkins()
    node.get_node_information(Inputs.node_name)
    node.get_node_config_xml(Inputs.node_name)
    node.check_node_existence(Inputs.node_name)
    node.create_a_node()
    #node.delete_a_node(Inputs.node_name)
    #node.disable_a_node(Inputs.node_name)
    #node.enable_a_node(Inputs.node_name)
    node.reconfigure_a_node()
