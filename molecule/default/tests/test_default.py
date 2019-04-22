import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["logrotate"])
def test_packages(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize(
    "file,content",
    [
        ("/etc/logrotate.conf", r"^# rotate log files daily"),
        ("/etc/logrotate.conf", r"^daily"),
        ("/etc/logrotate.conf", r"^# keep 30 days worth of backlogs"),
        ("/etc/logrotate.conf", r"^rotate 30"),
        ("/etc/logrotate.conf", r"^compress"),
    ],
)
def test_files(host, file, content):
    f = host.file(file)

    assert f.exists
    assert f.contains(content)


@pytest.mark.parametrize(
    "file,content",
    [
        ("/etc/logrotate.d/rsyslog", r"^\s*daily"),
        ("/etc/logrotate.d/rsyslog", r"^\s*rotate 7"),
    ],
)
def test_rsyslog_file(host, file, content):
    f = host.file(file)

    # The file only exists on Debian systems
    if f.exists:
        assert f.contains(content)
