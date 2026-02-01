from scraper import WallapopScraper
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wallapop Market Sentinel Scraper")
    parser.add_argument("--search", type=str, default="nike", help="Key word to search ex: nike")
    parser.add_argument("--limit", type=int, default=10, help="Number of articles to extract ex: 200")

    args = parser.parse_args()
    scraper = WallapopScraper()

    base_url = "https://es.wallapop.com/search?keywords="
    params = "&order_by=most_relevance"
    search_query = args.search.replace(" ", "%20")
    url = f"{base_url}{search_query}{params}"
    scraper.fetch_page(url)
    
    scraper.get_page_articles(args.limit)
    #scraper.get_dataframe()
    scraper.close()