import os

from notion.client import NotionClient

login_token = os.getenv('NOTION_TOKEN_V2')
page_url = os.getenv('NOTION_PAGE_URL')

def main():
    client = NotionClient(token_v2=login_token)
    page = client.get_block(page_url)

    last_block = page.children[-1]
    all_but_last = page.children[:-1]
    for child in all_but_last:
        child.move_to(last_block, 'after')

if __name__ == '__main__':
    main()