import argparse

from milto.etl import CoinGeckoETL


def run() -> None:
    parser = argparse.ArgumentParser(
        "ETL process for fetching top 100 coins by market cap into 'top_100_coins_by_market_cap' SQLite table"
    )

    parser.add_argument(
        "--db_name",
        type=str,
        required=True,
        help="""
            Name of SQLite database to which load (for example 'coins.db').
            If database doesn't exist, it will be created by pipeline in the same directory where command was executed.
        """
    )

    args = parser.parse_args()

    coin_etl = CoinGeckoETL(db_name=args.db_name)
    coin_etl.execute()
