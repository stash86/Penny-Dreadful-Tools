from typing import Optional

from discord import FFmpegPCMAudio
from discord.ext import commands

from discordbot.command import MtgContext
from shared import redis


@commands.command()
async def modofail(ctx: MtgContext, args: Optional[str]) -> None:
    """Ding!"""
    if args is not None and args.lower() == 'reset':
        redis.clear(f'modofail:{ctx.guild}')
    if hasattr(ctx.author, 'voice') and ctx.author.voice is not None and ctx.author.voice.channel is not None:
        voice_channel = ctx.author.voice.channel
        voice = ctx.channel.guild.voice_client
        if voice is None:
            voice = await voice_channel.connect()
        elif voice.channel != voice_channel:
            voice.move_to(voice_channel)
        voice.play(FFmpegPCMAudio('ding.ogg'))
    n = redis.increment(f'modofail:{ctx.guild}')
    redis.expire(f'modofail:{ctx.guild}', 3600)
    await ctx.send(f':bellhop: **MODO fail** {n}')
