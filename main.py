import discord
from discord.ext import commands
from discord import ui
import yt_dlp as youtube_dl

#Permissões
permissoes = discord.Intents.default()
permissoes.message_content = True

#Prefixo para chamar acionar comandos no BOT
bot = commands.Bot(command_prefix="!", intents=permissoes)

# Link padrão do YouTube para tocar lo-fi
DEFAULT_URL = "https://www.youtube.com/watch?v=jfKfPfyJRdk"

# Configurações do youtube_dl
ytdl_config = {
    'format': 'bestaudio/best', 
    'quiet': True,
    'noplaylist': True 
}
ytdl = youtube_dl.YoutubeDL(ytdl_config)

# Comando para tocar lo-fi
@bot.command()
async def lofi(ctx):
    # vc = voice client
    vc = ctx.voice_client
    
    # Verificação para conectar se não estiver conectado
    if not vc:
        if ctx.author.voice:
            vc = await ctx.author.voice.channel.connect()
        else:
            return await ctx.send("Você precisa estar em um canal de voz!")
    
    # Busca o áudio pela URL
    audio_info = ytdl.extract_info(DEFAULT_URL, download=False)
    audio_url = audio_info['url']
    
    # Toca com volume em 40%
    volume = discord.FFmpegPCMAudio(audio_url, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5")
    player = discord.PCMVolumeTransformer(volume, volume=0.4)
    vc.play(player)
    
    # Cria o painel de controle
    caixa_estilo = discord.Embed(
        title="🎵 Tocando Agora",
        description="**Lo-fi Radio**",
        color=discord.Color.purple()
    )
    #Recebe a thumb e coloca em miniatura na exibição da caixa
    caixa_estilo.set_thumbnail(url=audio_info.get('thumbnail', ''))

    #Envia a caixa para a mensagem de texto do canal
    await ctx.send(embed=caixa_estilo)

#Evento para confirmação da conexão do BOT
@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')

#Insira a KEY do seu BOT 
bot.run("--------")