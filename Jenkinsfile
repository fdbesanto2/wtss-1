def mensagemResult = ''
def tagName = 'brazildatacube/wtss:build-' + currentBuild.number

env.tagName = tagName

def checkoutProject() {
    stage('checkout') {
        checkout([
            $class: 'GitSCM',
            branches: [[name: 'origin-pull/pull/${GITHUB_PR_NUMBER}/merge']],
            doGenerateSubmoduleConfigurations: false,
            extensions: [],
            gitTool: 'Default',
            submoduleCfg: [],
            userRemoteConfigs: [[
                name: 'origin-pull',
                refspec: '+refs/pull/${GITHUB_PR_NUMBER}/merge:refs/remotes/origin-pull/pull/${GITHUB_PR_NUMBER}/merge',
                url: 'https://github.com/brazil-data-cube/wtss.git'
            ]]
        ])
    }
}

def prepareEnvironment() {
    stage('prepare-environment') {
        sh 'docker build --tag ${tagName} -f docker/Dockerfile .'
    }
}

def codeCheck() {
    stage('code check') {
        sh 'docker run --rm -i -v $(pwd):/data --name wtss_code_check ${tagName} pylint --exit-zero --output-format=parseable --reports=yes bdc_wtss/ > /data/pylint.log'

        recordIssues minimumSeverity: 'NORMAL',
            qualityGates: [
                [threshold: 1, type: 'DELTA_ERROR', unstable: false],
                [threshold: 1, type: 'DELTA_HIGH', unstable: true],
                [threshold: 1, type: 'DELTA_NORMAL', unstable: true],
                [threshold: 1, type: 'NEW_HIGH', unstable: false],
                [threshold: 1, type: 'TOTAL_HIGH', unstable: true],
                [threshold: 1, type: 'TOTAL_ERROR', unstable: false]
            ],
            tools: [pyLint(pattern: 'pylint.log')]
    }
}

def generateDocs() {
    stage('generate docs') {
        sh 'docker run --rm -i -v $(pwd):/bdc-wtss --name wtss_docs ${tagName} python3 manage.py docs'
    }
}

def unittest() {
    stage('unittest') {
        sh 'docker run --rm -i --name wtss_test ${tagName} python3 manage.py test'
    }
}

def deploy() {
    stage('deploy') {
        // TODO
        sh 'echo "Deploy development server"'
    }
}

def notifySlack(String buildStatus = 'STARTED', String mensagem = '') {
    buildStatus = buildStatus ?: 'SUCCESS'

    def color
    def state

    if (buildStatus == 'STARTED') {
        color = '#D4DADF'
        mensagem = mensagem ?: 'Build starting'
        state = 'PENDING'
    } else if (buildStatus == 'SUCCESS') {
        color = '#BDFFC3'
        mensagem = mensagem ?: 'Build successfully'
        state = 'SUCCESS'
    } else if (buildStatus == 'UNSTABLE') {
        color = '#FFFE89'
        mensagem = mensagem ?: 'Build unstable'
        state = 'SUCCESS'
    } else {
        color = '#FF9FA1'
        mensagem = mensagem ?: 'Build failed'
        state = 'FAILED'
    }

    setGitHubPullRequestStatus context: 'jenkins', message: mensagem, state: state

    def msg = "${buildStatus}: `${env.JOB_NAME}` #${env.BUILD_NUMBER}:\n${env.BUILD_URL}\n${mensagem}"

    echo "${env}"

    slackSend(color: color, message: msg)
}

def cleanEnvironment() {
    sh 'docker rmi ${tagName} || exit 0'
}

node("ubuntu-16.04"){
    try {
        checkoutProject()
        notifySlack()

        setGitHubPullRequestStatus context: 'jenkins', message: 'Starting pipeline', state: 'PENDING'

        prepareEnvironment()

        codeCheck()

        generateDocs()

        unittest()

        deploy()
    } catch (e) {
        currentBuild.result = 'FAILURE'
        mensagemResult = e.toString()
        throw e
    } finally {
        notifySlack(currentBuild.result, mensagemResult)
        cleanEnvironment()
    }
}