# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.annotation import Annotation  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_annotations import PageOfAnnotations  # noqa: E501
from openapi_server.test import BaseTestCase


class TestAnnotationController(BaseTestCase):
    """AnnotationController integration test stubs"""

    def test_create_annotation(self):
        """Test case for create_annotation

        Create an annotation
        """
        annotation = {
  "textDateAnnotations" : [ {
    "start" : 42,
    "length" : 10,
    "text" : "10/26/2020",
    "dateFormat" : "MM/DD/YYYY"
  }, {
    "start" : 42,
    "length" : 10,
    "text" : "10/26/2020",
    "dateFormat" : "MM/DD/YYYY"
  } ],
  "textPersonNameAnnotations" : [ {
    "start" : 42,
    "length" : 11,
    "text" : "Chloe Price"
  }, {
    "start" : 42,
    "length" : 11,
    "text" : "Chloe Price"
  } ],
  "textPhysicalAddressAnnotations" : [ {
    "start" : 42,
    "length" : 11,
    "text" : "Seattle",
    "addressType" : "city"
  }, {
    "start" : 42,
    "length" : 11,
    "text" : "Seattle",
    "addressType" : "city"
  } ],
  "annotationSource" : {
    "resourceSource" : {
      "name" : "name"
    }
  },
  "name" : "name"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStores/{annotation_store_id}/annotations'.format(dataset_id='dataset_id_example', annotation_store_id='annotation_store_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(annotation),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_annotation(self):
        """Test case for delete_annotation

        Delete an annotation
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStores/{annotation_store_id}/annotations/{annotation_id}'.format(dataset_id='dataset_id_example', annotation_store_id='annotation_store_id_example', annotation_id='annotation_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_annotation(self):
        """Test case for get_annotation

        Get an annotation
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStores/{annotation_store_id}/annotations/{annotation_id}'.format(dataset_id='dataset_id_example', annotation_store_id='annotation_store_id_example', annotation_id='annotation_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_annotations(self):
        """Test case for list_annotations

        List the annotations in an annotation store
        """
        query_string = [('limit', 10),
                        ('offset', 0),
                        ('annotationType', 'annotation_type_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}/annotationStores/{annotation_store_id}/annotations'.format(dataset_id='dataset_id_example', annotation_store_id='annotation_store_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
