
# Jenkins_Automation_using_Python

## Table of Contents
- [Installation](#installation)
- [Jenkins Object Creation](#jenkins-object-creation)
- [Jenkins Server Information APIs](#jenkins-server-information-apis)
- [Job Management APIs](#job-management-apis)
- [Build Management APIs](#build-management-apis)
- [View Management APIs](#view-management-apis)
- [Node Management APIs](#node-management-apis)

---

## Installation

Follow these steps to install Jenkins on Ubuntu/Debian:

```bash
sudo apt update
sudo apt install -y openjdk-17-jdk

wget -O /usr/share/keyrings/jenkins-keyring.asc \  
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key

echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \  
  https://pkg.jenkins.io/debian-stable binary/" | sudo tee \  
  /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt-get update
sudo apt-get install -y jenkins
```

Start and enable Jenkins service:

```bash
sudo systemctl start jenkins
sudo systemctl enable jenkins
```

Retrieve the initial admin password:

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

## Accessing Jenkins

Jenkins runs on port `8080` by default. Open a browser and visit:

```
http://<your-server-ip>:8080
```

Complete the setup by following the on-screen instructions.  
Jenkins is now ready for use! 🚀

---
# Jenkins Python Integration with python-jenkins

## Installation

To interact with Jenkins via Python, you can use the `python-jenkins` library. To install it, follow the steps below:

1. **Install python-jenkins** using pip:

   ```bash
   pip install python-jenkins
   ```

2. **Ensure you have access to your Jenkins server**:
   - You should have the Jenkins URL (e.g., `http://localhost:8080`).
   - You'll need a valid API token for authentication.

## Create a Jenkins Object in Python

After installing the `python-jenkins` library, you can create a Jenkins object to interact with your Jenkins server. Here's how:

1. **Import the `jenkins` module**:

   ```python
   import jenkins
   ```

2. **Create a Jenkins object** by specifying the Jenkins URL and authentication credentials (username and API token):

   ```python
   # Replace with your Jenkins server URL and your credentials
   jenkins_url = 'http://localhost:8080'
   username = 'your_username'
   password = 'your_password'

   # Create Jenkins object
   server = jenkins.Jenkins(jenkins_url, username=username, password=password)
   ```

3. **Verify the connection** by getting the Jenkins version:

   ```python
   version = server.get_version()
   print("Jenkins version:", version)
   ```

This will print the Jenkins version if the connection is successful. You are now ready to interact with Jenkins using the available API methods.

## Jenkins Server Information APIs

| API Method   | Description |
|--------------|-------------|
| `get_info()` | Retrieves information about the Jenkins master or a specific item. |
| `get_version()` | Get the Jenkins server version. |
| `get_whoami()` | Get information about the authenticated user. |
| `get_plugins()` | Retrieve the list of installed plugins. |
| `get_jobs()` | Get list of jobs. Each job is a dictionary with ‘name’, ‘url’, ‘color’ and ‘fullname’ keys. |
| `get_plugins_info()` | Retrieves information about all installed plugins (deprecated).|

---

## Job Management APIs

| API Method                       | Description                                         |
|----------------------------------|-----------------------------------------------------|
| `create_job(name, config_xml)`   | Create a new Jenkins job.                           |
|`create_job(name, jenkins.EMPTY_CONFIG_XML)` |Create a new Jenkins job with empty configuration.|
| `get_job_config(name)`           | Get configuration of an existing job.               |
| `reconfig_job(name, config_xml)` | Change the configuration of an existing job.        |
| `job_exists(name)`               | Check whether a job exists.                         |
| `jobs_count()`                   | Get the total number of jobs on the Jenkins server. |
| `copy_job(from_name, to_name)`   | Copy an existing Jenkins job.                       |
| `rename_job(from_name, to_name)` | Rename an existing Jenkins job.                     |
| `delete_job(name)`               | Permanently delete a Jenkins job.                   |
| `enable_job(name)`               | Enable a Jenkins job.                               |
| `disable_job(name)`              | Disable a Jenkins job.                              |
| `get_job_info(name)`             | Retrieves detailed information for a specific job.  |
| `get_job_info_regex(pattern)`    | Retrieves information about jobs whose names match the specified regex pattern.  |
| `get_job_name(name)`             | Returns the name of a Jenkins job, used for identity verification.  |
| `wipeout_job_workspace(name)`   | Wipes out the workspace for a given Jenkins job.    |

---

## Build Management APIs

| API Method                                     | Description                            |
|------------------------------------------------|----------------------------------------|
| `build_job(name, parameters=None)`             | Trigger a Jenkins job build.           |
| `get_build_info(name, build_number)`           | Get details of a specific job build.   |
| `get_build_console_output(name, build_number)` | Retrieve the console output of a build. |
| `stop_build(name, build_number)`               | Stop a running build.                  |
| `delete_build(name, number)`                   | Deletes a specific Jenkins build permanently. |
| `get_running_builds()`                         | Retrieves a list of all currently running builds.|
| `get_build_test_report(name, number)`          | Retrieves the test results report for a specific build.|
| `get_build_env_vars(name, number)`             | Get build environment variables.       |

---

## View Management APIs

| **API Method**               | **Description**                                           |
|------------------------------|-----------------------------------------------------------|
| `get_view_name(name)`         | Returns the name of a view using the API. Used to verify if a view exists. |
| `assert_view_exists(name, exception_message)` | Raises an exception if a view does not exist.            |
| `get_views()`                 | Retrieves a list of all views running in Jenkins.         |
| `delete_view(name)`           | Deletes a Jenkins view permanently.                       |
| `create_view(name, config_xml)` | Creates a new Jenkins view.                              |
| `reconfig_view(name, config_xml)` | Modifies the configuration of an existing view.         |
| `get_view_config(name)`       | Retrieves the configuration of an existing Jenkins view in XML format. |

## Node Management APIs

| **Method Name**              | **Description**                                           |
|------------------------------|-----------------------------------------------------------|
| `get_nodes(depth=0)`          | Get a list of nodes connected to the Master.              |
| `get_node_info(name, depth=0)`| Get detailed information about a specific node.           |
| `node_exists(name)`           | Check whether a node exists in Jenkins.                   |
| `assert_node_exists(name, exception_message)` | Raise an exception if a node does not exist. |
| `delete_node(name)`           | Permanently delete a Jenkins node.                        |
| `disable_node(name, msg='')`  | Disable a Jenkins node (take it offline).                 |
| `enable_node(name)`           | Enable a previously disabled node.                        |
| `create_node(name, numExecutors, nodeDescription, remoteFS, labels, exclusive, launcher, launcher_params)` | Create a new Jenkins node with the specified parameters. |
| `get_node_config(name)`       | Get the XML configuration of a Jenkins node.             |
| `reconfig_node(name, config_xml)` | Modify the existing configuration of a Jenkins node.    |

Now you can use the `python-jenkins` library to manage Jenkins views, jobs, nodes, and more through the API.

The extra APIs and information are provided in the document in the above repo.