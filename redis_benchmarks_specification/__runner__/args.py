import argparse

from redis_benchmarks_specification.__common__.env import (
    SPECS_PATH_TEST_SUITES,
    DATASINK_RTS_HOST,
    DATASINK_RTS_PORT,
    DATASINK_RTS_AUTH,
    DATASINK_RTS_USER,
    DATASINK_RTS_PUSH,
    MACHINE_NAME,
)


def create_client_runner_args(project_name):
    parser = argparse.ArgumentParser(
        description=project_name,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--platform-name",
        type=str,
        default=MACHINE_NAME,
        help="Specify the running platform name. By default it will use the machine name.",
    )
    parser.add_argument("--triggering_env", type=str, default="ci")
    parser.add_argument("--setup_type", type=str, default="oss-standalone")
    parser.add_argument("--github_repo", type=str, required=True)
    parser.add_argument("--github_org", type=str, required=True)
    parser.add_argument("--github_version", type=str, default="NA")
    parser.add_argument(
        "--logname", type=str, default=None, help="logname to write the logs to"
    )
    parser.add_argument(
        "--test-suites-folder",
        type=str,
        default=SPECS_PATH_TEST_SUITES,
        help="Test suites folder, containing the different test variations",
    )
    parser.add_argument(
        "--test",
        type=str,
        default="",
        help="specify a test to run. By default will run all the tests"
        + " present in the folder specified in --test-suites-folder.",
    )
    parser.add_argument("--db_server_host", type=str, default="localhost")
    parser.add_argument("--db_server_port", type=int, default=6379)
    parser.add_argument("--cpuset_start_pos", type=int, default=0)
    parser.add_argument(
        "--datasink_redistimeseries_host", type=str, default=DATASINK_RTS_HOST
    )
    parser.add_argument(
        "--datasink_redistimeseries_port", type=int, default=DATASINK_RTS_PORT
    )
    parser.add_argument(
        "--datasink_redistimeseries_pass", type=str, default=DATASINK_RTS_AUTH
    )
    parser.add_argument(
        "--datasink_redistimeseries_user", type=str, default=DATASINK_RTS_USER
    )
    parser.add_argument(
        "--datasink_push_results_redistimeseries",
        default=DATASINK_RTS_PUSH,
        action="store_true",
        help="uploads the results to RedisTimeSeries. Proper credentials are required",
    )
    parser.add_argument(
        "--flushall_on_every_test_start",
        default=False,
        action="store_true",
        help="At the start of every test send a FLUSHALL",
    )
    parser.add_argument(
        "--flushall_on_every_test_end",
        default=False,
        action="store_true",
        help="At the end of every test send a FLUSHALL",
    )
    return parser
