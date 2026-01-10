import logging

from assertpy import assert_that, soft_assertions
from playwright.sync_api import Page

import allure


@allure.epic("Test Playwright framework")
@allure.feature("Tests from Viola course")
@allure.story("Work with select element")
class TestSelectOption:
    @allure.title("Github repo search with filtering: handling <select>")
    @allure.description(
        """
        Github repo search with filtering: handling <select> element.

        Scenario:
        - Open page `https://github.com/search/advanced`.
        - Fill filters:
            - Select `Written in this language` filter, select value option.
            - Select `With this many stars` filter, fill some value.
            - Select `With this file name` filter, fill some value.
        - Click `Search` button.
        - Verify results match filter criteria.
        """
    )
    def test_sample_no_fixtures(self, page: Page):
        test_url = "https://github.com/search/advanced"
        language = "Python"
        stars = "123"
        file_name = "requirements.yml"
        with allure.step(f"Open url '{test_url}'"):
            page.goto(test_url)
        with allure.step(f"Select filter 'Written in this language' to '{language}'"):
            page.locator("#search_language").select_option(language)
        with allure.step(f"Fill filter 'With this many stars' with '{stars}'"):
            page.locator("#search_stars").fill(stars)
        with allure.step(f"Fill filter 'With this file name' with '{file_name}'"):
            page.locator("#search_filename").fill(file_name)
        with allure.step("Click 'Search' button"):
            page.locator("xpath=(//*[@class='btn flex-auto'])[2]").click()
        with allure.step("Wait for results list in results page"):
            page.locator("xpath=//div[@data-testid='results-list']").wait_for()
        with allure.step("Make screenshot and log current URL"):
            screenshot_bytes = page.screenshot(full_page=True)
            allure.attach(
                body=screenshot_bytes,
                name="page_screenshot.png",
                attachment_type=allure.attachment_type.PNG,
            )
            logging.info("Search results page url: %s", page.url)
            allure.attach(
                body=page.url,
                name="page_url.txt",
                attachment_type=allure.attachment_type.TEXT,
            )
        with soft_assertions():     # pyright: ignore[reportGeneralTypeIssues]
            with allure.step("Verify results match filter criteria"):
                with allure.step("Verify elements with stars rating"):
                    with allure.step("Find elements for each result on results page"):
                        stars_list = page.locator(
                            "xpath=//div[@data-testid='results-list']//ul//a",
                        ).all()
                    with allure.step("Check elements list is not empty"):
                        assert_that(stars_list, "Stars elements list should not be empty").is_not_empty()
                    with allure.step(f"Check {len(stars_list)} elements matches filter '{stars}'"):
                        for star in stars_list:
                            assert_that(star.get_attribute("aria-label"), "Repo stars value").contains(stars)
                with allure.step("Verify elements with repo language"):
                    with allure.step("Find elements for each result on results page"):
                        lang_list = page.query_selector_all(
                            # 'xpath=//ul[@class="Box-sc-62in7e-0 dmuROe"]//li[1]',
                            'xpath=//div[@data-testid="results-list"]/div/div/div[1]/ul/li[1]/span',
                        )
                    with allure.step("Check elements list is not empty"):
                        assert_that(lang_list, "Language elements list should not be empty").is_not_empty()
                    with allure.step(f"Check {len(lang_list)} elements matches filter '{language}'"):
                        for lang in lang_list:
                            assert_that(lang.inner_text(), "Repo language value").contains(language)
