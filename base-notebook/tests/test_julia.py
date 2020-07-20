# Souced from:
# https://github.com/jupyter/docker-stacks/blob/d3ef6d89b2f8b9062a57f9c7856b2b91fc9298f0/datascience-notebook/test/test_julia.py
import logging


LOGGER = logging.getLogger(__name__)


def test_julia(container):
    """Basic julia test"""
    LOGGER.info("Test that julia is correctly installed ...")
    running_container = container.run(
        tty=True, command=["start.sh", "bash", "-c", "sleep infinity"]
    )
    command = "julia --version"
    cmd = running_container.exec_run(command)
    output = cmd.output.decode("utf-8")
    assert cmd.exit_code == 0, f"Command {command} failed {output}"
    LOGGER.debug(output)
