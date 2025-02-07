class Inputs:
    jenkins_url = 'http://localhost:8080'
    username = 'lochu-55'
    password = 'Lovely@3455'  #password or API token of jenkins
    get_job_name = "GPIO"
    copy_destination_job = 'job3'
    copy_source_job = 'job2'
    build_job_name = 'job1'
    build_number = 2
    regex_pattern = 'job'
    upstream_job = "job0"
    view_name = "My View"


    artifact_url = "http://localhost:8080/job/job1/ws/Reports/report.xml"
    artifact_filename = 'job1_report1.xml'
    artifact_saving_path_to_dir = "/home/vlab/PycharmProjects/JenkinsAPI/saved_artifacts"
    Jenkins_folder_name = "Job_Folder"

    pipeline_name = "first_pipeline"
    pipeline_xml_path = "Inputs/XMLs/pipeline.xml"


    downstream_job = "job2"
    downstream_job_build_no = 30

    node_name = "jyo_gpio"
    launcher_params = {
        'host': '172.16.203.40',
        'port': '22',
        'username': 'vlab',  # The SSH username
        'credentialsId': 'jyo',  # Use the Jenkins credentials ID for SSH authentication
    }
