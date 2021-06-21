import scraping, post_to_slack

def main():
    TARGET_URL = 'http://www.usupi.org/sysad/backno.html'
    SPLASH_API = 'http://splash:8050/render.html'
    scraping.return_rended_page(TARGET_URL, SPLASH_API)
    scraping.extract_urls()
    post_to_slack.post_to_slack()

if __name__ == '__main__':
    main()