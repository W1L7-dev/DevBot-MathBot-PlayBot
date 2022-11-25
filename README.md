# DevBot, PlayBot and MathBot

Hey! I'm W1L7, the developer of __DevBot__, __PlayBot__ and __MathBot__. Those discord bots will manage the Dev Community server. They will have many features, such as:
- Moderation
- Administration
- Mathematical Calculations
- Polls
- Music
- And more!

## Commands
### Administration
- `/addrole <user> <role>`: Adds a role to a user, permissions required: `MANAGE_ROLES`
- `/removerole <user> <role>`: Removes a role from a user, permissions required: `MANAGE_ROLES`
- `/createrole <role>`: Creates a role, permissions required: `MANAGE_ROLES`
- `/delrole <role>`: Deletes a role, permissions required: `MANAGE_ROLES`
- `/createcategory <category>`: Creates a category, permissions required: `MANAGE_CHANNELS`
- `/delcategory <category>`: Deletes a category, permissions required: `MANAGE_CHANNELS`
- `/addcategory <channel> <category>`: Adds a channel to a category, permissions required: `MANAGE_CHANNELS`
- `/removecategory <channel>`: Removes a channel from a category, permissions required: `MANAGE_CHANNELS`
- `/createchannel <channel>`: Creates a channel, permissions required: `MANAGE_CHANNELS`
- `/delchannel <channel>`: Deletes a channel, permissions required: `MANAGE_CHANNELS`
- `createvoicechannel <channel>`: Creates a voice channel, permissions required: `MANAGE_CHANNELS`
- `/delvoicechannel <channel>`: Deletes a voice channel, permissions required: `MANAGE_CHANNELS`
### Moderation
- `/kick <user> [reason]`: Kicks a user, permissions required: `KICK_MEMBERS`
- `/ban <user> [reason]`: Bans a user, permissions required: `BAN_MEMBERS`
- `/unban <user>`: Unbans a user, permissions required: `BAN_MEMBERS`
- `/tempban <user> <time> [reason]`: Temporarily bans a user, permissions required: `BAN_MEMBERS`
- `/lock [channel]`: Locks a channel, permissions required: `MANAGE_CHANNELS`
- `/unlock [channel]`: Unlocks a channel, permissions required: `MANAGE_CHANNELS`
- `/templock <time> [channel]`: Temporarily locks a channel, permissions required: `MANAGE_CHANNELS`
- `/slowmode <time> [channel]`: Sets the slowmode of a channel, permissions required: `MANAGE_CHANNELS`
- `/clear <amount> [channel]`: Clears a channel, permissions required: `MANAGE_MESSAGES`
- `/timeout <user> <time> [reason]`: Times out a user, permissions required: `MANAGE_MESSAGES`
- `/warn <user> [reason]`: Warns a user, permissions required: `MANAGE_MESSAGES`
- `/warnings <user>`: Shows a user's warnings, permissions required: `MANAGE_MESSAGES`
- `/clearwarns <user>`: Clears a user's warnings, permissions required: `MANAGE_MESSAGES`
- `/removewarn <user> <number>`: Removes a warning from a user, permissions required: `MANAGE_MESSAGES`
### Development
- `/eval <code>`: Evaluates code, permissions required: `ADMINISTRATOR`
- `/uptime`: Shows the bot's uptime permissions required: `ADMINISTRATOR`
- `/clearoutput`: Clears the output, permissions required: `ADMINISTRATOR`
- `/exec <code>`: Executes code, permissions required: `ADMINISTRATOR`
- `/print <message>`: Prints text, permissions required: `ADMINISTRATOR`
- `/restart`: Restarts the bot, permissions required: `ADMINISTRATOR`
- `/shutdown`: Shuts down the bot, permissions required: `ADMINISTRATOR`
- `/loadcog <cog> <type>`: Loads a cog, permissions required: `ADMINISTRATOR`
- `/unloadcog <cog> <type>`: Unloads a cog, permissions required: `ADMINISTRATOR`
- `/reloadcog <cog> <type>`: Reloads a cog, permissions required: `ADMINISTRATOR`
- `/activityplay <activity>`: Sets the bot's activity to "Playing", permissions required: `ADMINISTRATOR`
- `/activitywatch <activity>`: Sets the bot's activity to "Watching", permissions required: `ADMINISTRATOR`
- `/activitylisten <activity>`: Sets the bot's activity to "Listening to", permissions required: `ADMINISTRATOR`
- `/activitystream <activity>`: Sets the bot's activity to "Streaming", permissions required: `ADMINISTRATOR`
- `/activityclear`: Clears the bot's activity, permissions required: `ADMINISTRATOR`
- `/activitydefault`: Sets the bot's activity to the default, permissions required: `ADMINISTRATOR`
- `/statusonline`: Sets the bot's status to "Online", permissions required: `ADMINISTRATOR`
- `/statusidle`: Sets the bot's status to "Idle", permissions required: `ADMINISTRATOR`
- `/statusdnd`: Sets the bot's status to "Do Not Disturb", permissions required: `ADMINISTRATOR`
- `/statusoffline`: Sets the bot's status to "Invisible", permissions required: `ADMINISTRATOR`
- `/createfile <file>`: Creates a file, permissions required: `ADMINISTRATOR`
- `/delfile <file>`: Deletes a file, permissions required: `ADMINISTRATOR`
- `/writefile <file> <text>`: Writes text to a file, permissions required: `ADMINISTRATOR`
- `/readfile <file>`: Reads a file, permissions required: `ADMINISTRATOR`
- `/clearfile <file>`: Clears a file, permissions required: `ADMINISTRATOR`
- `/createfolder <folder>`: Creates a folder, permissions required: `ADMINISTRATOR`
- `/delfolder <folder>`: Deletes a folder, permissions required: `ADMINISTRATOR`
- `/clearfolder <folder>`: Clears a folder, permissions required: `ADMINISTRATOR`
- `/listfolder <folder>`: Lists a folder, permissions required: `ADMINISTRATOR`
- `/clearcache`: Clears the bot's cache, permissions required: `ADMINISTRATOR`

### Math (With MathBot)
- `/add <number> <number>`: Adds two numbers
- `/subtract <number> <number>`: Subtracts two numbers
- `/multiply <number> <number>`: Multiplies two numbers
- `/divide <number> <number>`: Divides two numbers
- `/power <number> <number>`: Raises a number to a power
- `/sqrt <number>`: Finds the square root of a number
- `/cbrt <number>`: Finds the cube root of a number
- `/root <number> <root>`: Finds the root of a number
- `/log <number>`: Finds the natural logarithm of a number
- `/log10 <number>`: Finds the base 10 logarithm of a number
- `/log2 <number>`: Finds the base 2 logarithm of a number
- `/logb <number> <base>`: Finds the logarithm of a number with a base
- `/sin <number>`: Finds the sine of a number
- `/cos <number>`: Finds the cosine of a number
- `/tan <number>`: Finds the tangent of a number
- `/asin <number>`: Finds the arcsine of a number
- `/acos <number>`: Finds the arccosine of a number
- `/atan <number>`: Finds the arctangent of a number
- `/atan2 <number> <number>`: Finds the arctangent of two numbers
- `/sinh <number>`: Finds the hyperbolic sine of a number
- `/cosh <number>`: Finds the hyperbolic cosine of a number
- `/tanh <number>`: Finds the hyperbolic tangent of a number
- `/asinh <number>`: Finds the hyperbolic arcsine of a number
- `/acosh <number>`: Finds the hyperbolic arccosine of a number
- `/atanh <number>`: Finds the hyperbolic arctangent of a number
- `/abs <number>`: Finds the absolute value of a number
- `/ceil <number>`: Finds the ceiling of a number
- `/floor <number>`: Finds the floor of a number
- `/round <number>`: Rounds a number
- `/trunc <number>`: Truncates a number
- `/sign <number>`: Finds the sign of a number
- `/max <number> <number>`: Finds the maximum of two numbers
- `/min <number> <number>`: Finds the minimum of two numbers
- `/factorial <number>`: Finds the factorial of a number
- `/hypot <number> <number>`: Finds the hypotenuse of two numbers
- `/gcd <number> <number>`: Finds the greatest common divisor of two numbers
- `/lcm <number> <number>`: Finds the least common multiple of two numbers
- `/pi`: Finds pi
- `/e`: Finds e
- `/tau`: Finds tau
- `/degrees <number>`: Converts radians to degrees
- `/radians <number>`: Converts degrees to radians
- `/isclose <number> <number>`: Checks if two numbers are close
- `/isfinite <number>`: Checks if a number is finite
- `/isinf <number>`: Checks if a number is infinite
- `/isnan <number>`: Checks if a number is not a number
- `/copysign <number> <number>`: Copies the sign of a number
- `/exp <number>`: Finds e to the power of a number
- `/expm1 <number>`: Finds e to the power of a number minus 1
- `/fmod <number> <number>`: Finds the remainder of two numbers
- `/frexp <number>`: Finds the mantissa and exponent of a number
- `/fsum <number> <number>`: Finds the sum of two numbers
- `/ldexp <number> <number>`: Finds the product of a number and 2 to the power of another number
- `/modf <number>`: Finds the integer and fractional parts of a number
- `/isqrt <number>`: Finds the integer square root of a number
- `/perm <number> <number>`: Finds the number of permutations of two numbers
- `/random <number> <number>`: Finds a random number between two numbers

### Fun
- `/8ball <question>`: Answers a question
- `/coinflip`: Flips a coin
- `/dice`: Rolls a dice
- `/choose <option> <option>`: Chooses between two options
- `russianroulette`: Plays Russian Roulette
- `/slots`: Plays slots
- `/rockpaperscissors <choice>`: Plays rock, paper, scissors
- `/ruin <text>`: Ruins a text
- `/reverse <text>`: Reverses a text

### Infos
- `/rules`: Shows the rules
- `/userinfo [user]`: Shows information about a user
- `/serverinfo`: Shows information about the server
- `/botinfo`: Shows information about the bot
- `/roleinfo <role>`: Shows information about a role
- `/channelinfo <channel>`: Shows information about a channel
- `/emojiinfo <emoji>`: Shows information about an emoji

### Polls
- `/poll <question> <options>`: Creates a poll
- `/pollresult <message>`: Shows the results of a poll
- `/yesno <question>`: Creates a yes/no poll

### Utils
- `/ping`: Pings the bot
- `/say <text>`: Makes the bot say something
- `/embed <title> <color> <message>`: Makes the bot say something in an embed
- `/nick <nickname>`: change the author's nickname
- `/resetnick`: reset the author's nickname
- `/avatar [user]`: Shows the avatar of a user

### Music (with PlayBot)
- `/play <song>`: Plays a song
- `/skip`: Skips the current song
- `/stop`: Stops the music
- `/volume <volume>`: Changes the volume
- `/queue`: Shows the queue
- `/join`: Makes the bot join the voice channel
- `/leave`: Makes the bot leave the voice channel
- `/pause`: Pauses the music
- `/resume`: Resumes the music
- `/lyrics <song>`: Shows the lyrics of a song
- `/nowplaying`: Shows the current song
- `/shuffle`: Shuffles the queue
- `/loop`: Loops the queue
- `/add <song>`: Adds a song to the queue
- `/remove <song>`: Removes a song from the queue
- `/clear`: Clears the queue

## JOIN The Dev Community Discord Server: https://discord.gg/X3VMD2KjTY