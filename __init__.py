from airflow.plugins_manager import AirflowPlugin
from snowflake_plugin.hooks.snowflake_hook import SnowflakeHook
from snowflake_plugin.operators.s3_to_snowflake_operator import S3ToSnowflakeOperator
from snowflake_plugin.operators.snowflake_operator import SnowflakeOperator

class S3ToSnowflakePlugin(AirflowPlugin):
    name = 'snowflake_plugin'
    hooks = [SnowflakeHook]
    operators = [S3ToSnowflakeOperator, SnowflakeOperator]
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []
