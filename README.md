# lewdWaifu.im
Simple python script to supply you lewd anime pictures directly to your discord every given time >< <br> 
It uses [Waifu.im](https://waifu.im/) API to fetch lewd images.

## Get Started 
### Create Discord Bot Application
Go do [discord developer portal](https://discord.com/developers) and create a discord bot application.
Refer to [this blog](https://www.makeuseof.com/how-to-make-discord-bot/) (Only follow the part till application creation)
### Replace Token in the code
Uncomment the following code in the script and create a file `cred.txt`. Add your bot token in that txt file. 
```
# with open('cred.txt', 'r') as f:
#     global token 
#     token = f.read()
```
Remove or Comment `token = os.environ['TOKEN']`. Now your bot is ready to function on discord. 
### Add member id
Replace the ids in `member` list with your id. (You can add multiple discord ids and the bot will supply lewd to every member in `member` list)
```
members = [your_id, your_friends_id, your_familys_id_lol]
```
### Change the time duration
By default, the script will supply lewds every 12 hours i.e. 43200 seconds. You can set the timing according to your liking. Just replace the number and add your time in `seconds`.
```
await asyncio.sleep(time_in_sec)
```
### Remove Spoiler tag
Just remove `||` and you should be good. I dont recommend tho 
```
await mem.send(f"|| {res['images'][0]['url']} ||")
to
await mem.send(f"{res['images'][0]['url']}")
```
<hr>

### Preview 

<img src="https://cdn.discordapp.com/attachments/990523749721833532/1006240726868316272/Screenshot_2022-08-08_at_10.10.59_PM.png" width="40%"><h6>(No I wont reveal the image, go away)</h6>
