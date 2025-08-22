import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    try:
        logs = getattr(browser.driver, 'get_log', lambda _: [])(log_type='browser')
        if logs:
            allure.attach(
                '\n'.join(log['message'] for log in logs),
                name='browser_logs',
                attachment_type=allure.attachment_type.TEXT
            )
        else:
            allure.attach(
                str(browser.driver.capabilities),
                name='browser_capabilities',
                attachment_type=allure.attachment_type.JSON
            )
    except Exception as e:
        allure.attach(
            f'Error getting logs: {str(e)}',
            name='log_error',
            attachment_type=allure.attachment_type.TEXT
        )


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')