# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
# from six import BytesIO

# from openapi_server.models.note import Note  # noqa: E501
from openapi_server.test import BaseTestCase


class TestNoteController(BaseTestCase):
    """NoteController integration test stubs"""

    def test_notes_read(self):
        """Test case for notes_read

        Get a clinical note by ID
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/notes/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_notes_read_all(self):
        """Test case for notes_read_all

        Get all clinical notes
        """
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/notes',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_notes_update(self):
        """Test case for notes_update

        Update a clinical note by ID
        """
        note = {
            "fileName": "260-01.xml",
            "text": "October 3, Ms Chloe Price met with...",
            "type": "pathology"
        }
        headers = {
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/notes/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(note),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
