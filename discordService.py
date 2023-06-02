from typing import Optional
import models
import firebaseService as fs
import discord
from discord.ext import commands
import discord.ui

fsManager = fs.FirebaseAction()
intents = discord.Intents.default()
intents.message_content = True
# intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


# 시작이벤트
# @bot.event
# async def on_ready():
#     print(bot.application_id)

#test용
@bot.command(name='ping')
async def ping(ctx:commands.Context):
    await ctx.send('Pong!')
    print(ctx.author.guild.id)

# 콘텐츠 선택
class SelectViewOfContents(discord.ui.View):
    def __init__(self, classes, ctx:commands.Context, timeout: float | None = 180):
        super().__init__(timeout=timeout)
        self.classes = classes
        self.ctx = ctx
    def createSelct():
        return [
            discord.SelectOption(
                label=models.Contents[i][1],
                value=models.Contents[i][0],
                description=models.Contents[i][2],
                )
            for i in range(len(models.Contents))
        ]
    @discord.ui.select(
        placeholder = '수행가능한 모든 컨텐츠를 선택해 주세요!',
        min_values=1,
        max_values=6,
        options=createSelct()
    )
    async def select_callback(self, interaction:discord.Interaction, select):
        s = sum([int(v) for v in select.values])
        await interaction.message.delete()
        data = {
            'class': self.classes,
            'code': s,
        }
        fsManager.createCharacter(
            guild_id=str(self.ctx.author.guild.id),
            user_id=str(self.ctx.author.id),
            data=data)
        embed = discord.Embed(title=self.ctx.author.name, description="님의 추가된 콘텐츠 목록입니다.", color=discord.Color.blue())
        for content in models.convertToList(s):
            embed.add_field(name=content, value="", inline=False)
        await interaction.channel.send(embed=embed)
@bot.command(name='add')
async def inputCharacter(ctx:commands.Context, classes=""): 
    if classes == "":
        await ctx.send("!직업명을 같이 입력해 주세요! \n**add [직업명]**",reference=ctx.message)
        return
    elif classes not in models.getClassesToList():
        embed = discord.Embed(title="입력 가능한 클래스", description="", color=discord.Color.dark_gold())
        for k, v in models.Classes_kor.items():
            t = "<|> "
            for i in v.keys():
                t += str(i) + " <|> "
            embed.add_field(name=k, value=t, inline=False)
        embed.add_field(name="", value="", inline=False)
        # embed.set_footer(text="하나의 직업명을 입력해 주세요. ex)디스트로이어")
        await ctx.send(f"**{classes}**는 없는 직업명 입니다. 아래의 직업명을 참고해주세요!" ,embed=embed, reference=ctx.message)
        return
    await ctx.send(view=SelectViewOfContents(classes=classes, ctx=ctx, timeout = 120))
class myMemberList(discord.ui.Select):
    def __init__(self, ctx:commands.Context):
        super().__init__(placeholder="이름",)
        self.ctx = ctx
    async def createSelctOptions(self):
        options = []
        for member in fsManager.getGuildMemberIdList(guild_id=str(self.ctx.guild.id)):
            try :
                m = await self.ctx.guild.fetch_member(member)
            except discord.NotFound:
                print("NotFound")
            except:
                print("err")
            else:
                self.append_option(discord.SelectOption(
                    label=m.name,
                    value=m.id
                    )) 
        return self
    async def callback(self, interaction:discord.Interaction):
        await interaction.message.delete()
        data = fsManager.getMemberData(guild_id=str(self.ctx.guild.id), user_id=self.values[0])
        for d in data:
            print(d)
        
        
@bot.command(name='s')
async def showContentsList(ctx:commands.Context):
    myView = discord.ui.View(timeout=120)
    item = await myMemberList(ctx=ctx).createSelctOptions()
    myView.add_item(item)
    await ctx.send("test", view=myView)

#bot.run("token")
