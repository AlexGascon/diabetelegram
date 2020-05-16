import pytest

from freezegun import freeze_time

from diabetelegram.actions.constants import Actions
from tests.fixtures.actions import MockActionFactory


@pytest.fixture
def put_file_command(mocker):
    return mocker.patch('diabetelegram.actions.dexcom_actions.PutFileInS3Command')

class TestDexcomAction:
    def build_action(self, message, state_manager):
        return MockActionFactory.build(Actions.Dexcom, message, state_manager=state_manager)

    def test_matches_if_message_is_a_csv_file(self, message_with_csv, state):
        action = self.build_action(message_with_csv, state)

        assert action.matches()

    def test_does_not_match_if_message_is_not_a_file(self, message, state):
        action = self.build_action(message, state)
        
        assert not action.matches()

    def test_does_not_match_if_message_is_not_a_csv(self, message_with_pdf, state):
        action = self.build_action(message_with_pdf, state)

        assert not action.matches()

    @freeze_time('2020-05-09 12:34:56.789')
    def test_handle_puts_the_file_in_s3(self, message_with_csv, state, put_file_command):
        action = self.build_action(message_with_csv, state)
        expected_filename = 'dexcom/cgm-data_2020-05-09T12:34:56.789000.csv'
        expected_content = 'header1,header2\nvalue1,value2'
        expected_bucket = 'alexgascon-api-files'
        action.telegram.get_file.return_value = expected_content

        action.handle()

        put_file_command.assert_called_with(expected_filename, expected_content, expected_bucket)
        put_file_command.return_value.execute.assert_called_once()

    def test_handle_sends_updates_in_telegram(self, message_with_csv, state, put_file_command):
        action = self.build_action(message_with_csv, state)

        action.handle()

        assert 2 == action.telegram.reply.call_count

    def test_handle_sets_the_state_to_initial(self, message_with_csv, state, put_file_command):
        action = self.build_action(message_with_csv, state)

        action.handle()

        action.state_manager.set.assert_called_with('initial')

