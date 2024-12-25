import google.generativeai as palm
import asyncio
from pyppeteer import launch

import config

url = "https://www.google.com/maps/place/Za+Arlington/@42.4041201,-71.1507548,15z/data=!4m8!3m7!1s0x89e37701e73238bf:0x7ec798698b759a26!8m2!3d42.4041206!4d-71.1404765!9m1!1b1!16s%2Fg%2F1td2vxk3?entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D"

async def scrape_reviews(url):

    browser = await launch({"headless": False, "args": ["--window-size=800,3200"]})

    page = await browser.newPage()
    await page.setViewport({"width": 800, "height": 3200})
    await page.goto(url)