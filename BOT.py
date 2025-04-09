import discord
import asyncio
import aiohttp
from discord.ext import commands, tasks
import os
import io
import random
from datetime import datetime, timezone
import time
from itertools import cycle

# Nhập prefix
PREFIX = input("Nhập prefix bot (mặc định là '.'): ").strip() or "."

# Nhập token thủ công
def input_tokens():
    tokens = []
    print("Nhập từng token (gõ 'done' khi xong):")
    while True:
        token = input(f"Token {len(tokens) + 1}: ").strip()
        if token.lower() == 'done':
            break
        if token:
            tokens.append(token)
    return tokens

TOKENS = input_tokens()

if not TOKENS:
    print("Không có token nào được nhập!")
    exit()

TOKEN = TOKENS[0]  # Dùng token đầu tiên làm token chính

# Nhập ID admin thủ công
def input_admins():
    admins = []
    print("Nhập từng ID admin (gõ 'done' khi xong):")
    while True:
        try:
            id_input = input(f"Admin ID {len(admins) + 1}: ").strip()
            if id_input.lower() == 'done':
                break
            admins.append(int(id_input))
        except ValueError:
            print("ID không hợp lệ, vui lòng nhập số.")
    return admins

ADMINS = input_admins()

if not ADMINS:
    print("Không có admin nào được nhập!")
    exit()

# Ghi nhận thời gian khởi động
START_TIME = datetime.now(timezone.utc)

# Cấu hình thông điệp
TIPS = ["Luôn kiểm tra lại token trước khi chạy!", "Sử dụng lệnh .st để dừng mọi hoạt động!"]
QUOTES = ["Hãy làm điều bạn thích, đừng để ai cản trở!", "Cuộc sống là một chuỗi những lựa chọn!"]

# Biến toàn cục
SPAM_TASKS = []
TOKENS = []
BOT_MESSAGES = []
AUTO_REPLY_MESSAGES = []
last_message_time = time.time()

def load_tokens():
    """Tải token từ file tokens.txt"""
    if os.path.exists("tokens.txt"):
        with open("tokens.txt", "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return []

def load_file(filename):
    """Tải nội dung từ file"""
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.readlines()
    return []

# Tải dữ liệu từ file
TOKENS = load_tokens()
BOT_MESSAGES = load_file("spam.txt")
AUTO_REPLY_MESSAGES = load_file("reply.txt")

class CustomBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=PREFIX,
            self_bot=True,
            intents=discord.Intents.all(),
            case_insensitive=True
        )
        self.session = None
        self.voice_clients_dict = {}

    async def setup_hook(self):
        self.session = aiohttp.ClientSession()

bot = CustomBot()

@bot.command()
async def menu(ctx):
    if ctx.author.id not in ADMINS:
        return

    user = ctx.author  
    uptime = datetime.now(timezone.utc) - START_TIME  
    tips = random.choice(TIPS).strip()  
    quote = random.choice(QUOTES).strip()  

    menu_text = f"""```css
════════════════════
🌟 [Self bot V5] 🌟
🎉 [Create by: 5544330 | Đăng Khoa] 🎉
════════════════════
🛠️ Người dùng: {user.name}
🎭 Nickname: {user.display_name}
🆔 ID: {user.id}
⏳ Uptime: {str(uptime).split('.')[0]}
💡 Tip: {tips}
💬 Quote: {quote}
════════════════════
📜 .sp » Spam file (1 token)
🚀 .spdt » Spam file đa token
🔥 .n <@tag> » Spam tag
🛑 .st » Dừng tất cả spam
⚔️.raid » Phá sever
😀.emoji [số lần] » Spam emoji ngẫu nhiên
════════════════════
📩 .nhaytin <@tag>  »  Nháy tin nhắn người được chọn
📩 .rep <@tag> » Auto reply theo user
════════════════════
🎙️ .vc <id> » Treo voice
🔊 .leave » Thoát voice
📺.streammode <nội dung> /.stopstream » Bật/tắt Stream
⌛.spvc <id> <số lần> »  Out ra vô lại voice chat liên tục
════════════════════
🆔 .id [@tag] » Lấy ID
📡 .ping » Kiểm tra độ trễ
════════════════════```"""

    # Lấy file ảnh GIF từ thư mục hiện tại của bot
    file = discord.File("banner.gif", filename="banner.gif")

    # Gửi menu kèm ảnh GIF
    await ctx.send(content=menu_text, file=file)

@bot.command()
async def st(ctx):
    """Dừng tất cả spam"""
    if ctx.author.id not in ADMINS:
        return

    global SPAM_TASKS
    for task in SPAM_TASKS:
        task.cancel()
    SPAM_TASKS = []
    await ctx.send("🛑 Đã dừng tất cả spam!")

@bot.command()
async def sp(ctx):
    """Spam đơn token (gửi toàn bộ nội dung file trong 1 tin nhắn, lặp lại vô hạn)"""
    if ctx.author.id not in ADMINS or not BOT_MESSAGES:
        return

    async def spam_task():
        while True:
            full_message = "\n".join(BOT_MESSAGES)  # Gộp toàn bộ nội dung file
            await ctx.send(full_message)
            await asyncio.sleep(1)  # Delay 1 giây trước khi gửi lại

    task = asyncio.create_task(spam_task())
    SPAM_TASKS.append(task)

@bot.command()
async def spdt(ctx):
    """Spam đa token (spam hết nội dung file, lặp lại từ đầu)"""
    if ctx.author.id not in ADMINS or not TOKENS:
        return

    channel_id = ctx.channel.id

    async def spam_task(token):
        """Spam từng token riêng lẻ"""
        while True:
            full_message = "\n".join(BOT_MESSAGES)  # Gộp toàn bộ nội dung file
            await send_message(token, channel_id, full_message)
            await asyncio.sleep(1.5)  # Delay giữa mỗi lần gửi

    # Khởi chạy spam trên từng token
    for token in TOKENS:
        task = asyncio.create_task(spam_task(token))
        SPAM_TASKS.append(task)

@bot.command()
async def n(ctx, member: discord.Member):
    """Spam tag vô hạn, hết file lặp lại từ đầu"""
    if ctx.author.id not in ADMINS or not BOT_MESSAGES:
        return

    async def spam_task():
        while True:
            try:
                for msg in BOT_MESSAGES:
                    await ctx.send(f"# {member.mention} {msg.strip()}")
                    await asyncio.sleep(1)  # Delay giữa mỗi tin nhắn
            except Exception as e:
                print(f"Lỗi spam: {e}")
                await asyncio.sleep(5)  # Tránh spam lỗi quá nhanh

    task = asyncio.create_task(spam_task())
    SPAM_TASKS.append(task)

@bot.command()
async def rep(ctx, member: discord.Member):
    """Bật/Tắt auto reply tin nhắn của user"""
    if ctx.author.id not in ADMINS:
        return await ctx.send("🚫 Bạn không có quyền dùng lệnh này!")

    if member.id in bot.auto_reply_users:
        bot.auto_reply_users.remove(member.id)
        await ctx.send(f"❌ Đã tắt auto reply cho {member.mention}")
    else:
        bot.auto_reply_users.add(member.id)
        await ctx.send(f"✅ Đã bật auto reply cho {member.mention}")

@bot.event
async def on_message(message):
    if message.author.id in bot.auto_reply_users and not message.author.bot:
        try:
            reply_text = next(AUTO_REPLY_CYCLE)  # Lấy tin nhắn tiếp theo từ file

            # Rep ở server
            await message.channel.send(f"{message.author.mention} {reply_text}")

            # Rep vào DM nếu là tin nhắn riêng
            if isinstance(message.channel, discord.DMChannel):
                await message.author.send(reply_text)

        except StopIteration:
            pass  # Không bao giờ xảy ra do `cycle()`

    await bot.process_commands(message)

# Khởi tạo danh sách auto reply nếu chưa có
if not hasattr(bot, "auto_reply_users"):
    bot.auto_reply_users = set()

# Load file reply.txt và tạo vòng lặp tin nhắn
AUTO_REPLY_MESSAGES = load_file("reply.txt")
AUTO_REPLY_CYCLE = cycle(AUTO_REPLY_MESSAGES) if AUTO_REPLY_MESSAGES else cycle(["Lỗi: Chưa có dữ liệu!"])

@bot.command()
async def vc(ctx, channel_id: int):
    """Treo voice"""
    if ctx.author.id not in ADMINS:
        return

    try:
        channel = bot.get_channel(channel_id)
        if not channel or not isinstance(channel, discord.VoiceChannel):
            return await ctx.send("❌ Không tìm thấy kênh voice!")
        voice_client = await channel.connect()
        bot.voice_clients_dict[channel.id] = voice_client
        await ctx.send(f"✅ Đã treo voice tại {channel.mention}!")
    except Exception as e:
        await ctx.send(f"❌ Lỗi khi treo voice: {str(e)}")

@bot.command()
async def nhaytin(ctx, member: discord.Member):
    """Bật/Tắt spam tin nhắn vô hạn khi user chat"""
    if ctx.author.id not in ADMINS:
        return await ctx.send("🚫 Bạn không có quyền dùng lệnh này!")

    if member.id in bot.nhaytin_users:
        bot.nhaytin_users.remove(member.id)
        await ctx.send(f"❌ Đã tắt spam tin nhắn của {member.mention}")
    else:
        bot.nhaytin_users.add(member.id)
        await ctx.send(f"✅ Đã bật spam tin nhắn của {member.mention}")

@bot.event
async def on_message(message):
    if message.author.id in bot.nhaytin_users and not message.author.bot:
        try:
            await message.channel.send(message.content)  # Nháy 1 lần duy nhất
        except:
            pass

    await bot.process_commands(message)

# Khởi tạo danh sách nháy tin nếu chưa có
if not hasattr(bot, "nhaytin_users"):
    bot.nhaytin_users = set()

@bot.command()
async def leave(ctx):
    """Thoát voice"""
    if ctx.author.voice and ctx.author.voice.channel.id in bot.voice_clients_dict:
        await bot.voice_clients_dict[ctx.author.voice.channel.id].disconnect()
        del bot.voice_clients_dict[ctx.author.voice.channel.id]
        await ctx.send("✅ Đã thoát khỏi voice!")
    else:
        await ctx.send("❌ Bạn không ở trong voice channel!")

@bot.command()
async def ping(ctx):
    """Kiểm tra độ trễ"""
    await ctx.send(f"🏓 Ping: {round(bot.latency * 1000)}ms")

@bot.command()
async def id(ctx, member: discord.Member = None):
    """Lấy ID user"""
    member = member or ctx.author
    await ctx.send(f"🆔 ID của {member.mention}: {member.id}")

@bot.command()
async def raid(ctx):
    """Phá sever"""
    if ctx.author.id not in ADMINS:
        return await ctx.send("❌ Bạn không có quyền sử dụng lệnh này!")

    guild = ctx.guild

    # Đổi tên server
    try:
        await guild.edit(name="SERVER RAIDED BY ĐĂNG KHOA")
    except:
        pass

    # Xóa kênh
    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass

    # Xóa vai trò
    for role in guild.roles:
        try:
            await role.delete()
        except:
            pass

    # Xóa emoji
    for emoji in guild.emojis:
        try:
            await emoji.delete()
        except:
            pass

    # Tạo kênh spam
    for _ in range(10):
        try:
            await guild.create_text_channel("RAIDED-BY-ĐĂNG-KHOA")
        except:
            pass

    # Tạo vai trò troll
    for _ in range(10):
        try:
            await guild.create_role(name="RAIDED-BY-ĐĂNG-KHOA", colour=discord.Colour.random())
        except:
            pass

    # Đổi tên thành viên
    for member in guild.members:
        try:
            await member.edit(nick="RAIDED BY ĐĂNG KHOA")
        except:
            pass

    # Gửi tin nhắn riêng
    for member in guild.members:
        try:
            await member.send("SERVER ĐÃ BỊ RAID! 🚀🔥")
        except:
            pass

    # Ban/kick thành viên
    for member in guild.members:
        try:
            await member.ban(reason="RAIDED BY ĐĂNG KHOA")
        except:
            try:
                await member.kick(reason="RAIDED BY ĐĂNG KHOA")
            except:
                pass

    # Spam tin nhắn
    spam_count = 0
    for _ in range(20):
        for channel in guild.text_channels:
            try:
                await channel.send("@everyone RAIDED BY ĐĂNG KHOA! 🚀🔥")
            except:
                pass
            spam_count += 1
        await asyncio.sleep(1)

    await ctx.send("✅ RAID hoàn tất! Đã spam 20 lần, dừng hoạt động.")

@bot.command()
async def emoji(ctx, amount: int = 10):
    """Spam emoji ngẫu nhiên"""
    if ctx.author.id not in ADMINS:
        return

    EMOJI_LIST = [
        "😂", "🤣", "🔥", "💀", "👀", "🤡", "🚀", "🎉", "🤔", "🥵", "🤯", "😈", "💩", "🍆", "🥶",
        "😎", "👌", "💪", "✨", "🌟", "💖", "🍑", "🎃", "👑", "🤑", "🥳", "🤩", "🤬", "🙃", "🤮",
        "🕶️", "🎭", "🧨", "🔮", "🎲", "💰", "🎵", "⚡", "💣", "🕹️", "🔊", "🗿", "🌀", "🍷", "🔑",
        "🥂", "🎯", "💔", "🖤", "🎀", "💤", "🦄", "🐉", "🍀", "🎈", "🥶", "🤖", "🐵", "🐧", "🐺"
    ]

    for _ in range(min(amount, 100)):  # Giới hạn spam tối đa 100 lần
        await ctx.send(random.choice(EMOJI_LIST))
        await asyncio.sleep(0.5)

    await ctx.send("✅ Đã spam emoji xong!")
    
@bot.command()
async def copy(ctx, source_guild_id: int):
    """Sao chép server"""
    source_guild = bot.get_guild(source_guild_id)
    target_guild = ctx.guild

    if not source_guild:
        await ctx.send("❌ Không tìm thấy server nguồn!")
        return

    await ctx.send(f"🔄 Đang sao chép từ {source_guild.name} sang {target_guild.name}...")

    # Xóa dữ liệu cũ
    for channel in target_guild.channels:
        await channel.delete()
    for role in target_guild.roles:
        if role != target_guild.default_role:
            await role.delete()
    for emoji in target_guild.emojis:
        await emoji.delete()

    # Sao chép vai trò
    role_map = {}
    for role in reversed(source_guild.roles):
        if role != source_guild.default_role:
            new_role = await target_guild.create_role(
                name=role.name,
                permissions=role.permissions,
                color=role.color,
                hoist=role.hoist
            )
            role_map[role.id] = new_role

    # Sao chép kênh
    category_map = {}
    for category in source_guild.categories:
        new_category = await target_guild.create_category(category.name)
        category_map[category.id] = new_category

    for channel in source_guild.channels:
        if isinstance(channel, discord.TextChannel):
            await target_guild.create_text_channel(
                channel.name,
                category=category_map.get(channel.category_id)
            )
        elif isinstance(channel, discord.VoiceChannel):
            await target_guild.create_voice_channel(
                channel.name,
                category=category_map.get(channel.category_id)
            )

    await ctx.send("✅ Sao chép hoàn tất!")

@bot.command()
async def streammode(ctx, *, title="Đang live trên Twitch!"):
    """Bật trạng thái stream giả trên Discord."""
    stream_url = "https://www.twitch.tv/fakestream"
    activity = discord.Streaming(name=title, url=stream_url)
    await bot.change_presence(activity=activity)
    await ctx.send(f"✅ Đã bật chế độ stream với tiêu đề: `{title}`")

@bot.command()
async def stopstream(ctx):
    """Tắt trạng thái stream giả."""
    await bot.change_presence(activity=None)
    await ctx.send("⏹️ Đã tắt chế độ stream!")

@bot.command()
async def spvc(ctx, channel_id: int, times: int = 5):
    """Spam vào/ra voice channel theo ID đã chọn"""
    if ctx.author.id not in ADMINS:
        return

    # Lấy guild từ context
    guild = ctx.guild
    if guild is None:
        return await ctx.send("❌ Không thể lấy thông tin guild!")

    channel = bot.get_channel(channel_id)
    if not channel or not isinstance(channel, discord.VoiceChannel):
        return await ctx.send("❌ Không tìm thấy kênh voice!")

    for i in range(times):
        try:
            # Kiểm tra bot có đang ở voice không, nếu có thì thoát trước
            if guild.voice_client:
                await guild.voice_client.disconnect()
                await asyncio.sleep(1)  # Chờ bot hoàn toàn thoát khỏi voice

            # Kết nối vào voice channel
            voice_client = await channel.connect()
            await asyncio.sleep(1)  # Giữ bot trong voice 1 giây
            await voice_client.disconnect()
            await asyncio.sleep(1)  # Chờ trước khi vòng lặp tiếp tục
        except Exception as e:
            await ctx.send(f"❌ Lỗi lần {i+1}: {str(e)}")
            break

    await ctx.send(f"✅ Đã spam voice `{times}` lần vào kênh <#{channel_id}>!")

@bot.event
async def on_ready():
    print(f"✅ Bot đăng nhập thành công: {bot.user}")

bot.run(TOKEN, bot=False)