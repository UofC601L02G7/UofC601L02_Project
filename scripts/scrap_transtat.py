import undetected_chromedriver as uc
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

class PDCrawler:
    def __init__(self):
        options = uc.ChromeOptions()
        options.add_argument("--start-minimized")
        self.driver = uc.Chrome(use_subprocess=True, options=options)
        self.driver.set_window_size(800, 600)

    def goto(self, url):
    	self.driver.get(url)

    def interact_select(self, ID, desired_year):
    	select_element = self.driver.find_element(By.ID, ID)
    	select = Select(select_element)
    	select.select_by_value(desired_year)

    def interact_checkbox(self, ID):
    	click_element = self.driver.find_element(By.ID, ID)
    	click_element.click()

    def interact_btn(self, ID):
    	click_element = self.driver.find_element(By.ID, ID)
    	click_element.click()

if __name__ == "__main__":
	crawler = PDCrawler()
	crawler.goto("https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=")

	year_month = [
		[2019, 9],
	]
	checkboxes = [
		"FL_DATE",
		"OP_UNIQUE_CARRIER",
		"OP_CARRIER",
		"TAIL_NUM",
		"ORIGIN",
		"ORIGIN_CITY_NAME",
		"DEST",
		"DEST_CITY_NAME",
		"DEP_TIME",
		"DEP_DELAY",
		"TAXI_OUT",
		"TAXI_IN",
		"ARR_TIME",
		"ARR_DELAY",
		"CANCELLED",
		"CANCELLATION_CODE",
		"CARRIER_DELAY",
		"WEATHER_DELAY",
		"NAS_DELAY",
		"SECURITY_DELAY",
		"LATE_AIRCRAFT_DELAY"
	]

	for year, month in year_month:
		crawler.goto("https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=")

		crawler.interact_select("cboYear", str(year))
		crawler.interact_select("cboPeriod", str(month))

		for checkbox in checkboxes:
			crawler.interact_checkbox(checkbox)

		crawler.interact_btn("btnDownload")
	#time.sleep(600)
	#crawler.driver.quit()