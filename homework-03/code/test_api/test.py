import pytest

from test_api.base import ApiBase


class TestApi(ApiBase):
    @pytest.mark.API("API")
    def test_valid_login(self, credentials):
        self.api_client.post_login(*credentials)

    @pytest.mark.API("API")
    def test_campaign(self):
        campaign_data = self.api_client.post_campaign_create()
        campaign_id = campaign_data['id']
        self.api_client.delete_campaign(campaign_id)

    @pytest.mark.API("API")
    def test_create_segment(self):
        segment_data = self.api_client.post_segment_create()
        segment_id = segment_data['id']
        self.api_client.check_segment(segment_id, is_exist=True)
        self.api_client.post_segment_delete(segment_id)

    @pytest.mark.API("API")
    def test_delete_segment(self):
        segment_data = self.api_client.post_segment_create()
        segment_id = segment_data['id']
        self.api_client.post_segment_delete(segment_id)
        self.api_client.check_segment(segment_id, is_exist=False)