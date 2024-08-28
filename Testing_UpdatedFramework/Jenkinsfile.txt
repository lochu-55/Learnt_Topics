pipeline {
agent any

stages {
    
    
    stage("clean up previous workspace") {
        steps {
            script {
                def prev_ws = "${env.WORKSPACE}@prev"
               deleteDir(path: prev_ws)
            }
        }
    }
    
    
    
    
    stage('checkout') {
        options{
            timestamps()
        }
        steps {
            script {
                checkout changelog: false, poll: false, scm: scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '2085b70a-cad7-4b05-b72b-52cf90f7f1c1', url: 'https://github.com/srijyothsna18/Testing_team_2024.git']])
            }
        }
        
    }
    
    
    
    
    stage("installing dependencies") {
        options{
            timestamps()
        }
        steps {
            bat "pip install -r requirements.txt"
        }
    }
    
    
    
    
    stage ("exceuting web") {
        steps {
                    bat "python -m pytest Tests/WEB_tests/test_web.py --html=Base/utils/Reports/web_report.html"
            }
    }
    
    
    
    
    stage('check node service status and executes gui tests') {
        steps {
            script {
                    def serv_stat=bat(script:'sc queryex "jenkins"',returnStatus:true)
                    try {
                        if (serv_stat == 0) {
                            throw new Exception("jenkins running as a service,skipping current stage,not possible to execute notepad test cases...")
                            
                        }
                        else {
                                bat "python -m pytest Tests/GUI_tests/test_notepad.py"
                        }
                    }
                    
                    catch(Exception e) {
                        echo "Exception:${e.message}"
                    }
                    
                    
                }

        }
    }
    
    
    
    stage("executing api"){
        options{
            timestamps()
        }
        steps {
            bat "dir"
            bat "python -m Base.Elements.Data.datagenerator"
            bat "python -m pytest Tests/API_tests/test_1_post_method.py --html=Base/utils/Reports/API_reports/api_post.html"
            bat "python -m pytest Tests/API_tests/test_2_get_method.py --html=Base/utils/Reports/API_reports/api_get.html"
            bat "python -m pytest Tests/API_tests/test_3_put_method.py --html=Base/utils/Reports/API_reports/api_put.html"
            bat "python -m pytest Tests/API_tests/test_4_delete_method.py --html=Base/utils/Reports/API_reports/api_delete.html"
         
            }
            
        }
    }
        
   

post {
    success {
        script {
            emailext subject: 'Pipeline execution status',
                      body: 'build executed successfully',
                      to: 'veenanjalitammina999@gmail.com anudeepch1818@gmail.com lochu5vilehya@gmail.com sripilla94@gmail.com abhishekweslee@gmail.com',
                      attachmentsPattern:'Base/utils/Logs/API_logs/API.log,Base/utils/Logs/WEB_logs/web.log,Base/utils/Reports/API_reports/*.html,Base/utils/Reports/web_report.html',
                      attachLog: true
                      
        }
    }
}
}
