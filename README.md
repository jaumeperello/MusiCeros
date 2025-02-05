# MusiCeros — Open-source PyTgCalls based project forked from Calls Music
<img src="https://github.com/jaumeperello/MusiCeros/blob/main/etc/repo.png?raw=true" width="620"/>

## Screenshoots
<img src="https://github.com/jaumeperello/MusiCeros/blob/main/screenshots/cover.jpg?raw=true" width="200"/>   <img src="https://github.com/jaumeperello/MusiCeros/blob/main/screenshots/search.jpg?raw=true" width="200"/>   <img src="https://github.com/jaumeperello/MusiCeros/blob/main/screenshots/playlist.jpg?raw=true" width="200"/>


## Requirements

- FFmpeg
- Mysql
- Python 3.7+

## Deployment

### Config

Copy `example.env` to `.env` and fill it with your credentials.

### Without Docker

1. Install Python requirements:
   ```bash
   pip install -U -r requirements.txt
   ```
2. Create Database as ```MusiCeros.sql``` shows
3. copy ```example.env``` to ```.env``` and edit it with your data
4. Run:
   ```bash
   python MusiCeros_bot.py
   ```

### Using Docker

1. Build:
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```

## Commads
### Users Commands
| Command | Description                                          |
| ------- | ---------------------------------------------------- |
| /play   | play the replied audio file or YouTube video         |
| /pause  | pause the audio stream                               |
| /resume | resume the audio stream                              |
| /skip   | skip the current audio stream                        |
| /mute   | mute the userbot                                     |
| /unmute | unmute the userbot                                   |
| /stop   | clear the queue and remove the userbot from the call |
| /list   | shows playlist queue                                 |
### Administrators Commands
| Command       | Description                                   |
| ------------- | --------------------------------------------- |
| /allow_all    | all users can use user commands in the group  |
| /allow_admin | telegram group admins can use user commands   |
| /disallow     | only bot admins can use user command          |
### Global Administrators Commands
| Command                | Description                             |
| ---------------------- | --------------------------------------- |
| /admin @usertag        | user is added as bot admin on the group |
| /remove_admin @usertag | remove the user from the bot group admin|
| /ban @usertag          | Ban the user from the bot in this group |
| /unban @usertag        | unBan the user from  in this group      |

### SuperUser Commads
| Command                        | Description                      |
| ------------------------------ | -------------------------------- |
| /global_admin @usertag         | user is added as bot global admin|
| /remove_global_admin @usertag  | remove the user as global admin  |
| /global_ban @usertag                  | Ban the user from the bot        |
| /global_unban @usertag                | unBan the user from the bot      |

## License

### GNU Affero General Public License v3.0
[Read more](http://www.gnu.org/licenses/#AGPL)

Thanks for asking and make this bot possible
