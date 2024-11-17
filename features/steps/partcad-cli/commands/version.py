from behave import given, when, then
import subprocess
import time


@given("I am in the command line interface")
def step_impl(context):

    pass


@when('I run the command "{command}"')
def step_impl(context, command):
    start_time = time.time()
    context.result = subprocess.run(
        ["pc", command],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    end_time = time.time()
    context.duration = end_time - start_time


@then('command takes less than "{max_duration}" seconds')
def step_impl(context, max_duration):
    assert context.duration < float(max_duration)


@then('the output should contain "{substring}"')
def step_impl(context, substring):
    import logging

    logging.critical("STDERR: " + context.result.stderr)
    logging.critical("STDOUT: " + context.result.stdout)
    assert substring in context.result.stdout


@then("the command should exit with a status code of {exit_code}")
def step_impl(context, exit_code):
    assert context.result.returncode == int(exit_code)
