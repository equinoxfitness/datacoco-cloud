import unittest
from unittest.mock import MagicMock

from datacoco_cloud import CWLInteraction


class TestCWLInteraction(unittest.TestCase):
    def test_parse_and_print_events(self):
        testCls = CWLInteraction(region="", aws_secret_key="", aws_access_key="")

        testCls.client = MagicMock()
        testCls.parse_and_print_events(events="")
        self.assertTrue(True)  # Assert that this line is reached without error

    # FIXME this can have more tests
    def test_get_log_events(self):
        testCls = CWLInteraction(region="", aws_secret_key="", aws_access_key="")

        testCls.client = MagicMock()
        testCls.client.get_log_events.return_value = {
            "ResponseMetadata": {"HTTPStatusCode": 200},
            "events": [],
        }
        testCls.get_log_events(log_group="", log_stream="")
        self.assertTrue(True)  # Assert that this line is reached without error


if __name__ == "__main__":
    unittest.main()