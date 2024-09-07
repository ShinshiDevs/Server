from os import getenv

from aurum.client import Client
from dotenv import load_dotenv
from hikari.impl import GatewayBot


def main() -> None:
    load_dotenv(override=True, verbose=True)

    bot: GatewayBot = GatewayBot(getenv("SERVER_DISCORD_TOKEN"), banner=None)
    client: Client = Client(bot, ignore_l10n=True)

    bot.run(check_for_updates=False)


if __name__ == "__main__":
    main()
