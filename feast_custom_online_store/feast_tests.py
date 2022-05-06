from tests.integration.feature_repos.integration_test_repo_config import (
    IntegrationTestRepoConfig,
)

MYSQL_CONFIG = {
    "type": "feast_custom_online_store.mysql_online_store.MySQLOnlineStore",
    "password": "jpassword",
    "host": "172.17.0.2",
    "user": "john",
    "database": "feastdb",
}

FULL_REPO_CONFIGS = [
    IntegrationTestRepoConfig(online_store=MYSQL_CONFIG),
]