#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  // SPDX-License-Identifier: BSD
import logging
from unittest.mock import MagicMock

import pytest

from s3torchconnector._s3client import S3Client, MockS3Client

TEST_BUCKET = "test-bucket"
TEST_KEY = "test-key"
TEST_REGION = "us-east-1"
S3_URI = f"s3://{TEST_BUCKET}/{TEST_KEY}"


@pytest.fixture
def s3_client() -> S3Client:
    client = MockS3Client(TEST_REGION, TEST_BUCKET)
    client.add_object(TEST_KEY, b"data")
    return client


def test_get_object_log(s3_client: S3Client, caplog):
    with caplog.at_level(logging.DEBUG):
        s3_client.get_object(TEST_BUCKET, TEST_KEY)
    assert f"GetObject {S3_URI}, object_info is None=True" in caplog.messages


def test_get_object_log_with_info(s3_client: S3Client, caplog):
    with caplog.at_level(logging.DEBUG):
        s3_client.get_object(TEST_BUCKET, TEST_KEY, object_info=MagicMock())
    assert f"GetObject {S3_URI}, object_info is None=False" in caplog.messages


def test_head_object_log(s3_client: S3Client, caplog):
    with caplog.at_level(logging.DEBUG):
        s3_client.head_object(TEST_BUCKET, TEST_KEY)
    assert f"HeadObject {S3_URI}" in caplog.messages


def test_put_object_log(s3_client: S3Client, caplog):
    with caplog.at_level(logging.DEBUG):
        s3_client.put_object(TEST_BUCKET, TEST_KEY)
    assert f"PutObject {S3_URI}" in caplog.messages


def test_list_objects_log(s3_client: S3Client, caplog):
    with caplog.at_level(logging.DEBUG):
        s3_client.list_objects(TEST_BUCKET, TEST_KEY)
    assert f"ListObjects {S3_URI}" in caplog.messages