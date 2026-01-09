# pylint: disable = unused-import

from time import sleep

import logging

from assertpy import assert_that, soft_assertions
from icecream import ic
from playwright.sync_api import Page, expect

import allure


@allure.epic("Test Playwright framework")
@allure.feature("Sample Feature")
@allure.story("Sample Story")
class TestSample:
    @allure.title("Sample Test")
    @allure.description(
        """
        Sample test description.

        Scenario:
        - sample step 1.
        - sample step 2.
        """
    )
    def test_sample_no_fixtures(self):
        with allure.step("Sample step 1"):
            logging.info("Sample step 1")
            assert_that(True).is_true()
        with allure.step("Sample step 2"):
            logging.info("Sample step 2")
            assert_that(False).is_false()
