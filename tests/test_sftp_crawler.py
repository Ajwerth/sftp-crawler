import pytest
import paramiko
import mock
from unittest.mock import MagicMock, patch
from Crawler.crawler import Crawler


class TestCrawler:

    # Test paramikos transport.connect called with correct args
    @patch('Crawler.crawler.paramiko.Transport', autospec=True)
    @patch('Crawler.crawler.paramiko.SFTPClient')
    def test_connect(self, mock_sftp, mock_transport):


        mock_creds = {
            'host': 'host',
            'user': 'user',
            'password': 'password',
            'port': '22'
        }

        crawl = Crawler(mock_creds)
        crawl.transport.connect.assert_called_with(username='user', password='password')
    
    #Test something....
    def test_file_crawl(self):
