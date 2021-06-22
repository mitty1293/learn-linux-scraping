import scraping, post_to_slack

def main():
    TARGET_URL = 'http://www.usupi.org/sysad/backno.html'
    SPLASH_API = 'http://splash:8050/render.html'
    err_cnt = 0
    while (rended_text := scraping.return_rended_page(TARGET_URL, SPLASH_API)) == "err":
        if (err_cnt := err_cnt + 1) > 4:
            failed_dict = {"title":"Scraping failed. Link to main page.", "url":TARGET_URL}
            topic_dict = {"todays":failed_dict, "previous":failed_dict, "next":failed_dict}
            break
    if err_cnt <= 4:
        topic_dict = scraping.extract_urls(rended_text, TARGET_URL)
    post_to_slack.post_to_slack(**topic_dict)

if __name__ == '__main__':
    main()