import discord
import asyncio
import re


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        channels = self.get_all_channels()

        for channel in channels:
            if channel.category:
                print(channel)
                messages = await channel.history(limit=10).flatten()
                for message in messages:
                    reactions = [reaction for reaction in message.reactions if isinstance(reaction.emoji, discord.Emoji)]
                    for reaction in reactions:
                        print(reaction.emoji)

                    custom_emojis = re.findall(r'<:\w*:\d*>', message.content)
                    custom_emojis = [int(e.split(':')[2].replace('>', '')) for e in custom_emojis]
                    custom_emojis = [self.get_emoji(e) for e in custom_emojis]
                    print(custom_emojis)

        await self.close()


def main():
    import os
    from dotenv import load_dotenv
    load_dotenv()
    discord_token = os.getenv('TOKEN')

    client = MyClient()
    client.run(discord_token)


if __name__ == "__main__":
    main()